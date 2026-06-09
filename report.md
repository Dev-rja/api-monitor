# API Reliability Monitor — SLA Report

> Last updated: **2026-06-09 12:12 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **79.0%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 74.52% | 2740.3 | 10206.7 | 1000ms | 266/1044 |
| ❌ | `public_apis_list` | 0.0% | 99.62% | 125.4 | 4595.4 | 1500ms | 4/1044 |
| ❌ | `ipapi_check` | 76.05% | 99.9% | 156.5 | 4507.0 | 2500ms | 1/1044 |
| ❌ | `nasa_apod` | 76.25% | 55.27% | 3075.4 | 10565.8 | 2000ms | 467/1044 |
| ⚠️ | `rest_countries` | 98.56% | 98.28% | 350.2 | 10221.5 | 2500ms | 18/1044 |
| ⚠️ | `open_meteo_weather` | 98.95% | 96.93% | 704.5 | 14877.1 | 2000ms | 32/1044 |
| ✅ | `dog_ceo_random` | 99.52% | 95.98% | 572.0 | 10244.1 | 2500ms | 42/1044 |
| ✅ | `catfact_random` | 99.71% | 99.14% | 267.1 | 10080.2 | 3000ms | 9/1044 |
| ✅ | `coingecko_bitcoin` | 99.71% | 100.0% | 96.6 | 253.3 | 1500ms | 0/1044 |
| ✅ | `useless_fact` | 99.81% | 99.62% | 622.8 | 10229.6 | 2500ms | 4/1044 |
| ✅ | `agify_name` | 99.9% | 99.71% | 380.2 | 16112.2 | 2000ms | 3/1044 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.81% | 221.7 | 3882.8 | 2000ms | 2/1044 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `nasa_apod` | 03:00 | 4611.9 | 78.95% |
| `nasa_apod` | 02:00 | 4606.1 | 62.5% |
| `numbers_trivia` | 03:00 | 4408.7 | 42.11% |
| `nasa_apod` | 17:00 | 4070.4 | 51.72% |
| `nasa_apod` | 05:00 | 3993.8 | 64.29% |
| `nasa_apod` | 09:00 | 3820.6 | 50.0% |
| `nasa_apod` | 11:00 | 3771.4 | 48.28% |
| `nasa_apod` | 01:00 | 3603.5 | 45.45% |
| `nasa_apod` | 12:00 | 3508.4 | 48.94% |
| `numbers_trivia` | 05:00 | 3427.1 | 32.14% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
