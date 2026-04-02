# API Reliability Monitor

A fully automated data pipeline that monitors the uptime and response time of public APIs, transforms raw ping data using dbt, and publishes a live SLA report — updated every 30 minutes via GitHub Actions.

---

## Live SLA report

> See [report.md](./report.md) for the latest auto-generated SLA report.

The report updates automatically every 30 minutes without any manual intervention.

---

## What it does

Every 30 minutes, a GitHub Actions workflow:

1. **Polls 12 public APIs** — measures response time and HTTP status for each
2. **Writes raw results to SQLite** — one row per ping in the `raw_pings` table
3. **Runs dbt** — transforms raw pings into clean staging and mart models
4. **Runs 17 data quality tests** — ensures no nulls, no bad values, no duplicates
5. **Generates a markdown SLA report** — commits `report.md` back to the repo automatically

---

## Architecture

```
apis.yaml
    │
    ▼
poller.py  ──────────────────▶  raw_pings (SQLite)
    │                                   │
    │                                   ▼
    │                           stg_pings (dbt view)
    │                                   │
    │                     ┌─────────────┴──────────────┐
    │                     ▼                            ▼
    │         mart_api_sla_summary          mart_hourly_trends
    │                     │                            │
    │                     └─────────────┬──────────────┘
    │                                   ▼
    └──────────────────────────▶  generate_report.py
                                        │
                                        ▼
                                    report.md
```

---

## dbt layer

| Model | Type | Description |
|---|---|---|
| `stg_pings` | View | Cleans and types `raw_pings`. Adds `breached_sla`, `is_failure`, `failure_reason`, `sla_delta_ms` |
| `mart_api_sla_summary` | Table | One row per API — uptime %, SLA compliance %, avg/min/max response time, health status label |
| `mart_hourly_trends` | Table | One row per API per hour — identifies consistently slow time windows |

**17 data quality tests** cover: uniqueness, not-null constraints, boolean column integrity, and custom SQL assertions.

---

## Key skills demonstrated

- **Data ingestion** — Python + httpx polling with structured error handling and timeout capture
- **Dimensional modeling** — staging → mart layer following dbt best practices
- **Data quality** — dbt tests including custom SQL assertions for SQLite compatibility
- **Pipeline orchestration** — GitHub Actions cron scheduling with automated git commits
- **SLA metric design** — uptime %, SLA compliance %, p95 response time approximation, health status classification
- **Self-updating reporting** — markdown report generated and committed on every pipeline run

---

## Project structure

```
api-monitor/
├── ingestion/
│   ├── apis.yaml              # 12 monitored APIs with SLA thresholds
│   └── poller.py              # httpx pinger → SQLite writer
├── dbt/
│   ├── models/
│   │   ├── staging/
│   │   │   ├── stg_pings.sql
│   │   │   └── schema.yml
│   │   └── marts/
│   │       ├── mart_api_sla_summary.sql
│   │       ├── mart_hourly_trends.sql
│   │       └── schema.yml
│   ├── tests/
│   │   └── assert_boolean_columns.sql
│   └── dbt_project.yml
├── reports/
│   └── generate_report.py     # reads marts → writes report.md
├── data/
│   └── monitor.db             # SQLite database (auto-updated)
├── .github/workflows/
│   └── poll.yml               # GitHub Actions cron every 30 min
├── report.md                  # auto-generated SLA report (see this!)
└── requirements.txt
```

---

## Run locally

```bash
# 1. clone and install
git clone https://github.com/Dev-rja/api-monitor.git
cd api-monitor
pip install -r requirements.txt

# 2. poll APIs once
python ingestion/poller.py

# 3. run dbt transformations
cd dbt
dbt run
dbt test

# 4. generate the SLA report
cd ..
python reports/generate_report.py

# 5. open report.md to see results
```

---

## Sample output

| Status | API | Uptime | SLA compliance | Avg (ms) |
|--------|-----|-------:|---------------:|---------:|
| ✅ | `jsonplaceholder_posts` | 100.0% | 100.0% | 143.2 |
| ✅ | `open_meteo_weather` | 100.0% | 98.0% | 412.7 |
| ⚠️ | `nasa_apod` | 100.0% | 72.0% | 2341.8 |
| ❌ | `numbers_trivia` | 83.0% | 50.0% | 5821.4 |

---

## Tech stack

- **Python 3.11** — ingestion and report generation
- **httpx** — async-capable HTTP client with timeout handling
- **SQLite** — lightweight embedded database, zero infrastructure
- **dbt-core + dbt-sqlite** — transformation, testing, and documentation
- **GitHub Actions** — free cron scheduling, runs 24/7 with no server

---

*Pipeline runs automatically — the SLA report above reflects real data.*