# API Reliability Monitor — SLA Report

> Last updated: **2026-10-07 23:29 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **7/12** &nbsp;|&nbsp; Avg uptime: **76.7%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 72.59% | 2875.8 | 10420.1 | 1000ms | 728/2656 |
| ❌ | `public_apis_list` | 0.0% | 99.44% | 142.7 | 5075.4 | 1500ms | 15/2656 |
| ❌ | `ipapi_check` | 45.48% | 99.96% | 144.8 | 4507.0 | 2500ms | 1/2656 |
| ❌ | `nasa_apod` | 80.42% | 59.68% | 2654.8 | 11152.5 | 2000ms | 1071/2656 |
| ⚠️ | `dog_ceo_random` | 97.14% | 97.78% | 476.6 | 10244.1 | 2500ms | 59/2656 |
| ✅ | `open_meteo_weather` | 99.06% | 98.31% | 667.0 | 14877.1 | 2000ms | 45/2656 |
| ✅ | `useless_fact` | 99.1% | 99.51% | 669.4 | 10229.6 | 2500ms | 13/2656 |
| ✅ | `rest_countries` | 99.44% | 99.13% | 271.5 | 10221.5 | 2500ms | 23/2656 |
| ✅ | `coingecko_bitcoin` | 99.7% | 99.92% | 97.0 | 4328.4 | 1500ms | 2/2656 |
| ✅ | `catfact_random` | 99.81% | 99.51% | 262.0 | 10080.2 | 3000ms | 13/2656 |
| ✅ | `agify_name` | 99.92% | 99.55% | 402.5 | 16112.2 | 2000ms | 12/2656 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.89% | 181.5 | 3882.8 | 2000ms | 3/2656 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `numbers_trivia` | 03:00 | 4483.7 | 44.44% |
| `numbers_trivia` | 10:00 | 3511.2 | 33.33% |
| `numbers_trivia` | 02:00 | 3261.8 | 30.77% |
| `nasa_apod` | 03:00 | 3208.5 | 46.3% |
| `numbers_trivia` | 14:00 | 3153.7 | 30.33% |
| `nasa_apod` | 11:00 | 3115.1 | 43.38% |
| `nasa_apod` | 17:00 | 3111.5 | 38.69% |
| `numbers_trivia` | 09:00 | 3088.0 | 29.57% |
| `nasa_apod` | 09:00 | 3080.4 | 44.74% |
| `numbers_trivia` | 17:00 | 3071.9 | 30.43% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
