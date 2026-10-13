# API Reliability Monitor — SLA Report

> Last updated: **2026-10-13 01:32 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **7/12** &nbsp;|&nbsp; Avg uptime: **76.6%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 72.83% | 2852.4 | 10420.1 | 1000ms | 728/2679 |
| ❌ | `public_apis_list` | 0.0% | 99.44% | 142.7 | 5075.4 | 1500ms | 15/2679 |
| ❌ | `ipapi_check` | 45.09% | 99.96% | 144.8 | 4507.0 | 2500ms | 1/2679 |
| ❌ | `nasa_apod` | 79.92% | 59.54% | 2670.1 | 11152.5 | 2000ms | 1084/2679 |
| ⚠️ | `dog_ceo_random` | 97.13% | 97.76% | 480.3 | 10509.6 | 2500ms | 60/2679 |
| ✅ | `open_meteo_weather` | 99.03% | 98.28% | 669.4 | 14877.1 | 2000ms | 46/2679 |
| ✅ | `useless_fact` | 99.1% | 99.51% | 669.8 | 10229.6 | 2500ms | 13/2679 |
| ✅ | `rest_countries` | 99.44% | 99.14% | 271.5 | 10221.5 | 2500ms | 23/2679 |
| ✅ | `coingecko_bitcoin` | 99.7% | 99.93% | 97.1 | 4328.4 | 1500ms | 2/2679 |
| ✅ | `catfact_random` | 99.81% | 99.51% | 262.3 | 10080.2 | 3000ms | 13/2679 |
| ✅ | `agify_name` | 99.93% | 99.55% | 402.3 | 16112.2 | 2000ms | 12/2679 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.89% | 181.2 | 3882.8 | 2000ms | 3/2679 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `numbers_trivia` | 03:00 | 4483.7 | 44.44% |
| `numbers_trivia` | 10:00 | 3511.2 | 33.33% |
| `nasa_apod` | 03:00 | 3208.5 | 46.3% |
| `numbers_trivia` | 14:00 | 3153.7 | 30.33% |
| `nasa_apod` | 11:00 | 3115.1 | 43.38% |
| `nasa_apod` | 09:00 | 3103.7 | 44.44% |
| `nasa_apod` | 17:00 | 3094.5 | 38.41% |
| `nasa_apod` | 05:00 | 3071.0 | 44.71% |
| `numbers_trivia` | 17:00 | 3050.8 | 30.22% |
| `numbers_trivia` | 16:00 | 3029.7 | 28.8% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
