"""
Report Generator
Reads mart_api_sla_summary from SQLite and writes a fresh report.md.
Run after dbt to update the README table.

Usage:
    python reports/generate_report.py
"""

import sqlite3
from datetime import datetime, timezone
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DB_PATH  = BASE_DIR / "data" / "monitor.db"
OUT_PATH = BASE_DIR / "report.md"


HEALTH_ICON = {
    "healthy":   "✅",
    "degraded":  "⚠️",
    "unhealthy": "❌",
}


def fetch_summary(conn: sqlite3.Connection) -> list[dict]:
    cur = conn.execute("""
        select
            api_name,
            uptime_pct,
            sla_compliance_pct,
            avg_response_ms,
            max_response_ms,
            sla_threshold_ms,
            sla_breaches,
            total_pings,
            health_status,
            last_seen
        from mart_api_sla_summary
        order by uptime_pct asc, avg_response_ms desc
    """)
    cols = [d[0] for d in cur.description]
    return [dict(zip(cols, r)) for r in cur.fetchall()]


def fetch_slow_hours(conn: sqlite3.Connection) -> list[dict]:
    cur = conn.execute("""
        select api_name, hour_label, avg_response_ms, sla_breach_pct
        from mart_hourly_trends
        where is_slow_hour = 1
        order by avg_response_ms desc
        limit 10
    """)
    cols = [d[0] for d in cur.description]
    return [dict(zip(cols, r)) for r in cur.fetchall()]


def build_report(summary: list[dict], slow_hours: list[dict]) -> str:
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    total   = len(summary)
    healthy = sum(1 for r in summary if r["health_status"] == "healthy")
    avg_uptime = sum(r["uptime_pct"] for r in summary) / total if total else 0

    lines = []
    lines.append("# API Reliability Monitor — SLA Report")
    lines.append(f"\n> Last updated: **{now}** &nbsp;|&nbsp; "
                 f"APIs monitored: **{total}** &nbsp;|&nbsp; "
                 f"Healthy: **{healthy}/{total}** &nbsp;|&nbsp; "
                 f"Avg uptime: **{avg_uptime:.1f}%**\n")

    lines.append("## SLA summary\n")
    lines.append("| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |")
    lines.append("|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|")

    for r in summary:
        icon = HEALTH_ICON.get(r["health_status"], "❓")
        lines.append(
            f"| {icon} | `{r['api_name']}` "
            f"| {r['uptime_pct']}% "
            f"| {r['sla_compliance_pct']}% "
            f"| {r['avg_response_ms']} "
            f"| {r['max_response_ms']} "
            f"| {int(r['sla_threshold_ms'])}ms "
            f"| {r['sla_breaches']}/{r['total_pings']} |"
        )

    if slow_hours:
        lines.append("\n## Consistently slow windows\n")
        lines.append("These APIs exceeded their SLA threshold on average during these hours:\n")
        lines.append("| API | Hour (UTC) | Avg (ms) | SLA breach rate |")
        lines.append("|-----|-----------|----------:|----------------:|")
        for r in slow_hours:
            lines.append(
                f"| `{r['api_name']}` "
                f"| {r['hour_label']} "
                f"| {r['avg_response_ms']} "
                f"| {r['sla_breach_pct']}% |"
            )
    else:
        lines.append("\n## Consistently slow windows\n")
        lines.append("_No APIs are consistently slow at any particular hour. All good!_")

    lines.append("\n---")
    lines.append("_Generated automatically by "
                 "[api-monitor](https://github.com/your-username/api-monitor) "
                 "via GitHub Actions + dbt._")

    return "\n".join(lines) + "\n"


def main() -> None:
    if not DB_PATH.exists():
        print(f"Database not found at {DB_PATH}. Run the poller first.")
        return

    conn = sqlite3.connect(DB_PATH)

    try:
        summary    = fetch_summary(conn)
        slow_hours = fetch_slow_hours(conn)
    except sqlite3.OperationalError as e:
        print(f"Error reading mart tables: {e}")
        print("Make sure you have run: dbt run")
        conn.close()
        return

    report = build_report(summary, slow_hours)
    OUT_PATH.write_text(report, encoding="utf-8")

    print(f"Report written to {OUT_PATH}")
    print(f"  {len(summary)} APIs | {sum(r['total_pings'] for r in summary)} total pings")


if __name__ == "__main__":
    main()