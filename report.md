# API Reliability Monitor — SLA Report

> Last updated: **2026-10-14 00:24 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **76.6%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 72.87% | 2848.4 | 10420.1 | 1000ms | 728/2683 |
| ❌ | `public_apis_list` | 0.0% | 99.44% | 142.6 | 5075.4 | 1500ms | 15/2683 |
| ❌ | `ipapi_check` | 45.02% | 99.96% | 145.0 | 4507.0 | 2500ms | 1/2683 |
| ❌ | `nasa_apod` | 79.84% | 59.52% | 2673.2 | 11152.5 | 2000ms | 1086/2683 |
| ⚠️ | `dog_ceo_random` | 97.13% | 97.76% | 480.2 | 10509.6 | 2500ms | 60/2683 |
| ⚠️ | `open_meteo_weather` | 98.99% | 98.29% | 669.1 | 14877.1 | 2000ms | 46/2683 |
| ✅ | `useless_fact` | 99.11% | 99.52% | 669.8 | 10229.6 | 2500ms | 13/2683 |
| ✅ | `rest_countries` | 99.44% | 99.14% | 271.8 | 10221.5 | 2500ms | 23/2683 |
| ✅ | `coingecko_bitcoin` | 99.7% | 99.93% | 97.2 | 4328.4 | 1500ms | 2/2683 |
| ✅ | `catfact_random` | 99.81% | 99.52% | 262.4 | 10080.2 | 3000ms | 13/2683 |
| ✅ | `agify_name` | 99.93% | 99.55% | 402.2 | 16112.2 | 2000ms | 12/2683 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.89% | 181.3 | 3882.8 | 2000ms | 3/2683 |

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
| `nasa_apod` | 02:00 | 3024.0 | 40.0% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
