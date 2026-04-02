"""
API Reliability Monitor — Poller
Reads apis.yaml, pings each endpoint, writes results to SQLite raw_pings table.

Usage:
    # Run once (for GitHub Actions / cron):
    python poller.py

    # Run on a loop locally (every 30 min):
    python poller.py --loop
"""

import argparse
import sqlite3
import time
import uuid
from datetime import datetime, timezone
from pathlib import Path

import httpx
import yaml

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------
BASE_DIR = Path(__file__).resolve().parent.parent
DB_PATH  = BASE_DIR / "data" / "monitor.db"
CFG_PATH = Path(__file__).resolve().parent / "apis.yaml"

POLL_INTERVAL_SECONDS = 30 * 60   # 30 minutes for --loop mode
REQUEST_TIMEOUT       = 10        # seconds per request


# ---------------------------------------------------------------------------
# Database
# ---------------------------------------------------------------------------

def get_connection() -> sqlite3.Connection:
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def ensure_table(conn: sqlite3.Connection) -> None:
    conn.execute("""
        CREATE TABLE IF NOT EXISTS raw_pings (
            id            TEXT PRIMARY KEY,
            api_name      TEXT    NOT NULL,
            url           TEXT    NOT NULL,
            checked_at    TEXT    NOT NULL,   -- ISO-8601 UTC
            status_code   INTEGER,            -- NULL on network error
            response_ms   REAL    NOT NULL,
            is_success    INTEGER NOT NULL,   -- 1 / 0
            sla_ms        REAL    NOT NULL,
            error_message TEXT                -- NULL on success
        )
    """)
    conn.commit()


# ---------------------------------------------------------------------------
# Config
# ---------------------------------------------------------------------------

def load_apis(path: Path) -> list[dict]:
    with open(path) as f:
        cfg = yaml.safe_load(f)
    return cfg["apis"]


# ---------------------------------------------------------------------------
# Pinging
# ---------------------------------------------------------------------------

def ping(api: dict) -> dict:
    """Hit one API endpoint and return a result row dict."""
    name     = api["name"]
    url      = api["url"]
    sla_ms   = api["sla_ms"]
    expected = api.get("expected_status", 200)

    start = time.perf_counter()
    status_code   = None
    error_message = None
    is_success    = 0

    try:
        response    = httpx.get(url, timeout=REQUEST_TIMEOUT, follow_redirects=True)
        elapsed_ms  = (time.perf_counter() - start) * 1000
        status_code = response.status_code
        is_success  = 1 if status_code == expected else 0

    except httpx.TimeoutException:
        elapsed_ms    = (time.perf_counter() - start) * 1000
        error_message = "timeout"

    except httpx.RequestError as exc:
        elapsed_ms    = (time.perf_counter() - start) * 1000
        error_message = f"request_error: {type(exc).__name__}"

    return {
        "id":            str(uuid.uuid4()),
        "api_name":      name,
        "url":           url,
        "checked_at":    datetime.now(timezone.utc).isoformat(),
        "status_code":   status_code,
        "response_ms":   round(elapsed_ms, 2),
        "is_success":    is_success,
        "sla_ms":        sla_ms,
        "error_message": error_message,
    }


def ping_all(apis: list[dict]) -> list[dict]:
    results = []
    for api in apis:
        row = ping(api)
        status  = row["status_code"] or "ERR"
        sla_ok  = "OK " if row["response_ms"] <= row["sla_ms"] else "SLA"
        success = "✓" if row["is_success"] else "✗"
        print(
            f"  {success} [{sla_ok}] {api['name']:<30} "
            f"{str(status):<5}  {row['response_ms']:>7.1f}ms"
            + (f"  — {row['error_message']}" if row["error_message"] else "")
        )
        results.append(row)
    return results


def write_results(conn: sqlite3.Connection, rows: list[dict]) -> None:
    conn.executemany("""
        INSERT INTO raw_pings
            (id, api_name, url, checked_at, status_code,
             response_ms, is_success, sla_ms, error_message)
        VALUES
            (:id, :api_name, :url, :checked_at, :status_code,
             :response_ms, :is_success, :sla_ms, :error_message)
    """, rows)
    conn.commit()


# ---------------------------------------------------------------------------
# Summary print (optional, useful in CI logs)
# ---------------------------------------------------------------------------

def print_summary(rows: list[dict]) -> None:
    total      = len(rows)
    successful = sum(r["is_success"] for r in rows)
    sla_ok     = sum(1 for r in rows if r["response_ms"] <= r["sla_ms"])
    avg_ms     = sum(r["response_ms"] for r in rows) / total if total else 0

    print(f"\n  {'─'*50}")
    print(f"  Polled : {total} APIs")
    print(f"  Up     : {successful}/{total}  ({100*successful//total}%)")
    print(f"  SLA ok : {sla_ok}/{total}  ({100*sla_ok//total}%)")
    print(f"  Avg ms : {avg_ms:.1f}ms")
    print(f"  DB     : {DB_PATH}")
    print(f"  {'─'*50}\n")


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

def run_once() -> None:
    apis = load_apis(CFG_PATH)
    conn = get_connection()
    ensure_table(conn)

    ts = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    print(f"\n  Polling {len(apis)} APIs at {ts}\n")

    rows = ping_all(apis)
    write_results(conn, rows)
    print_summary(rows)
    conn.close()


def run_loop() -> None:
    print(f"  Loop mode — polling every {POLL_INTERVAL_SECONDS // 60} minutes. Ctrl+C to stop.\n")
    while True:
        run_once()
        print(f"  Sleeping {POLL_INTERVAL_SECONDS // 60} min...\n")
        time.sleep(POLL_INTERVAL_SECONDS)


def main() -> None:
    parser = argparse.ArgumentParser(description="API Reliability Poller")
    parser.add_argument(
        "--loop", action="store_true",
        help="Run continuously every 30 minutes (for local dev)"
    )
    args = parser.parse_args()

    if args.loop:
        run_loop()
    else:
        run_once()


if __name__ == "__main__":
    main()