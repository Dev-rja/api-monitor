# API Reliability Monitor — SLA Report

> Last updated: **2026-06-14 17:49 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **79.0%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 75.64% | 2628.1 | 10206.7 | 1000ms | 266/1092 |
| ❌ | `public_apis_list` | 0.0% | 99.63% | 125.7 | 4595.4 | 1500ms | 4/1092 |
| ❌ | `nasa_apod` | 75.73% | 53.66% | 3154.2 | 10565.8 | 2000ms | 506/1092 |
| ❌ | `ipapi_check` | 76.37% | 99.91% | 156.4 | 4507.0 | 2500ms | 1/1092 |
| ⚠️ | `rest_countries` | 98.63% | 98.35% | 342.5 | 10221.5 | 2500ms | 18/1092 |
| ⚠️ | `open_meteo_weather` | 98.9% | 96.7% | 719.7 | 14877.1 | 2000ms | 36/1092 |
| ✅ | `dog_ceo_random` | 99.54% | 96.15% | 563.6 | 10244.1 | 2500ms | 42/1092 |
| ✅ | `catfact_random` | 99.73% | 99.18% | 264.1 | 10080.2 | 3000ms | 9/1092 |
| ✅ | `coingecko_bitcoin` | 99.73% | 100.0% | 96.4 | 253.3 | 1500ms | 0/1092 |
| ✅ | `useless_fact` | 99.82% | 99.63% | 626.5 | 10229.6 | 2500ms | 4/1092 |
| ✅ | `agify_name` | 99.91% | 99.73% | 378.0 | 16112.2 | 2000ms | 3/1092 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.82% | 219.5 | 3882.8 | 2000ms | 2/1092 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `nasa_apod` | 03:00 | 4611.9 | 78.95% |
| `nasa_apod` | 02:00 | 4606.1 | 62.5% |
| `numbers_trivia` | 03:00 | 4408.7 | 42.11% |
| `nasa_apod` | 05:00 | 4214.9 | 65.52% |
| `nasa_apod` | 09:00 | 4014.2 | 52.08% |
| `nasa_apod` | 17:00 | 3993.9 | 54.1% |
| `nasa_apod` | 11:00 | 3861.7 | 50.0% |
| `nasa_apod` | 01:00 | 3797.2 | 52.0% |
| `nasa_apod` | 18:00 | 3491.9 | 51.85% |
| `nasa_apod` | 14:00 | 3469.5 | 47.17% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
