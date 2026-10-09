# API Reliability Monitor — SLA Report

> Last updated: **2026-10-09 15:50 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **7/12** &nbsp;|&nbsp; Avg uptime: **76.7%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 72.66% | 2868.6 | 10420.1 | 1000ms | 728/2663 |
| ❌ | `public_apis_list` | 0.0% | 99.44% | 142.5 | 5075.4 | 1500ms | 15/2663 |
| ❌ | `ipapi_check` | 45.36% | 99.96% | 144.8 | 4507.0 | 2500ms | 1/2663 |
| ❌ | `nasa_apod` | 80.32% | 59.67% | 2658.1 | 11152.5 | 2000ms | 1074/2663 |
| ⚠️ | `dog_ceo_random` | 97.15% | 97.78% | 476.5 | 10244.1 | 2500ms | 59/2663 |
| ✅ | `open_meteo_weather` | 99.02% | 98.27% | 670.3 | 14877.1 | 2000ms | 46/2663 |
| ✅ | `useless_fact` | 99.1% | 99.51% | 669.3 | 10229.6 | 2500ms | 13/2663 |
| ✅ | `rest_countries` | 99.44% | 99.14% | 271.4 | 10221.5 | 2500ms | 23/2663 |
| ✅ | `coingecko_bitcoin` | 99.7% | 99.92% | 97.1 | 4328.4 | 1500ms | 2/2663 |
| ✅ | `catfact_random` | 99.81% | 99.51% | 261.9 | 10080.2 | 3000ms | 13/2663 |
| ✅ | `agify_name` | 99.92% | 99.55% | 402.6 | 16112.2 | 2000ms | 12/2663 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.89% | 181.5 | 3882.8 | 2000ms | 3/2663 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `numbers_trivia` | 03:00 | 4483.7 | 44.44% |
| `numbers_trivia` | 10:00 | 3511.2 | 33.33% |
| `nasa_apod` | 03:00 | 3208.5 | 46.3% |
| `numbers_trivia` | 14:00 | 3153.7 | 30.33% |
| `nasa_apod` | 11:00 | 3115.1 | 43.38% |
| `nasa_apod` | 17:00 | 3111.5 | 38.69% |
| `numbers_trivia` | 17:00 | 3071.9 | 30.43% |
| `nasa_apod` | 09:00 | 3063.5 | 44.35% |
| `numbers_trivia` | 09:00 | 3062.7 | 29.31% |
| `numbers_trivia` | 02:00 | 3037.2 | 28.57% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
