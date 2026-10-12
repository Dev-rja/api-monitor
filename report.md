# API Reliability Monitor — SLA Report

> Last updated: **2026-10-12 02:39 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **7/12** &nbsp;|&nbsp; Avg uptime: **76.6%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 72.8% | 2855.5 | 10420.1 | 1000ms | 728/2676 |
| ❌ | `public_apis_list` | 0.0% | 99.44% | 142.7 | 5075.4 | 1500ms | 15/2676 |
| ❌ | `ipapi_check` | 45.14% | 99.96% | 144.8 | 4507.0 | 2500ms | 1/2676 |
| ❌ | `nasa_apod` | 80.01% | 59.53% | 2668.8 | 11152.5 | 2000ms | 1083/2676 |
| ⚠️ | `dog_ceo_random` | 97.16% | 97.8% | 476.1 | 10244.1 | 2500ms | 59/2676 |
| ✅ | `open_meteo_weather` | 99.03% | 98.28% | 669.6 | 14877.1 | 2000ms | 46/2676 |
| ✅ | `useless_fact` | 99.1% | 99.51% | 669.2 | 10229.6 | 2500ms | 13/2676 |
| ✅ | `rest_countries` | 99.44% | 99.14% | 271.2 | 10221.5 | 2500ms | 23/2676 |
| ✅ | `coingecko_bitcoin` | 99.7% | 99.93% | 97.0 | 4328.4 | 1500ms | 2/2676 |
| ✅ | `catfact_random` | 99.81% | 99.51% | 262.1 | 10080.2 | 3000ms | 13/2676 |
| ✅ | `agify_name` | 99.93% | 99.55% | 402.4 | 16112.2 | 2000ms | 12/2676 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.89% | 181.2 | 3882.8 | 2000ms | 3/2676 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `numbers_trivia` | 03:00 | 4483.7 | 44.44% |
| `numbers_trivia` | 10:00 | 3511.2 | 33.33% |
| `nasa_apod` | 03:00 | 3208.5 | 46.3% |
| `numbers_trivia` | 14:00 | 3153.7 | 30.33% |
| `nasa_apod` | 09:00 | 3126.3 | 44.83% |
| `nasa_apod` | 11:00 | 3115.1 | 43.38% |
| `nasa_apod` | 17:00 | 3094.5 | 38.41% |
| `nasa_apod` | 05:00 | 3071.0 | 44.71% |
| `numbers_trivia` | 17:00 | 3050.8 | 30.22% |
| `numbers_trivia` | 09:00 | 3037.7 | 29.06% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
