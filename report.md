# API Reliability Monitor — SLA Report

> Last updated: **2026-06-09 15:28 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **79.0%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 74.55% | 2737.8 | 10206.7 | 1000ms | 266/1045 |
| ❌ | `public_apis_list` | 0.0% | 99.62% | 125.4 | 4595.4 | 1500ms | 4/1045 |
| ❌ | `ipapi_check` | 76.08% | 99.9% | 156.6 | 4507.0 | 2500ms | 1/1045 |
| ❌ | `nasa_apod` | 76.27% | 55.22% | 3075.1 | 10565.8 | 2000ms | 468/1045 |
| ⚠️ | `rest_countries` | 98.56% | 98.28% | 349.9 | 10221.5 | 2500ms | 18/1045 |
| ⚠️ | `open_meteo_weather` | 98.95% | 96.94% | 704.2 | 14877.1 | 2000ms | 32/1045 |
| ✅ | `dog_ceo_random` | 99.52% | 95.98% | 571.8 | 10244.1 | 2500ms | 42/1045 |
| ✅ | `catfact_random` | 99.71% | 99.14% | 267.0 | 10080.2 | 3000ms | 9/1045 |
| ✅ | `coingecko_bitcoin` | 99.71% | 100.0% | 96.6 | 253.3 | 1500ms | 0/1045 |
| ✅ | `useless_fact` | 99.81% | 99.62% | 622.8 | 10229.6 | 2500ms | 4/1045 |
| ✅ | `agify_name` | 99.9% | 99.71% | 380.3 | 16112.2 | 2000ms | 3/1045 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.81% | 221.7 | 3882.8 | 2000ms | 2/1045 |

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
