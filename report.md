# API Reliability Monitor — SLA Report

> Last updated: **2026-10-14 22:32 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **7/12** &nbsp;|&nbsp; Avg uptime: **76.6%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 72.92% | 2843.4 | 10420.1 | 1000ms | 728/2688 |
| ❌ | `public_apis_list` | 0.0% | 99.44% | 142.6 | 5075.4 | 1500ms | 15/2688 |
| ❌ | `ipapi_check` | 44.94% | 99.96% | 145.0 | 4507.0 | 2500ms | 1/2688 |
| ❌ | `nasa_apod` | 79.76% | 59.56% | 2671.8 | 11152.5 | 2000ms | 1087/2688 |
| ⚠️ | `dog_ceo_random` | 97.14% | 97.77% | 480.1 | 10509.6 | 2500ms | 60/2688 |
| ✅ | `open_meteo_weather` | 99.0% | 98.29% | 668.8 | 14877.1 | 2000ms | 46/2688 |
| ✅ | `useless_fact` | 99.11% | 99.52% | 669.8 | 10229.6 | 2500ms | 13/2688 |
| ✅ | `rest_countries` | 99.44% | 99.14% | 271.8 | 10221.5 | 2500ms | 23/2688 |
| ✅ | `coingecko_bitcoin` | 99.7% | 99.93% | 97.3 | 4328.4 | 1500ms | 2/2688 |
| ✅ | `catfact_random` | 99.81% | 99.52% | 262.6 | 10080.2 | 3000ms | 13/2688 |
| ✅ | `agify_name` | 99.93% | 99.55% | 402.0 | 16112.2 | 2000ms | 12/2688 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.89% | 181.4 | 3882.8 | 2000ms | 3/2688 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `numbers_trivia` | 03:00 | 4483.7 | 44.44% |
| `numbers_trivia` | 10:00 | 3478.4 | 33.01% |
| `nasa_apod` | 03:00 | 3208.5 | 46.3% |
| `numbers_trivia` | 14:00 | 3153.7 | 30.33% |
| `nasa_apod` | 11:00 | 3115.1 | 43.38% |
| `nasa_apod` | 09:00 | 3103.7 | 44.44% |
| `nasa_apod` | 17:00 | 3094.5 | 38.41% |
| `numbers_trivia` | 17:00 | 3050.8 | 30.22% |
| `nasa_apod` | 05:00 | 3039.7 | 44.19% |
| `nasa_apod` | 02:00 | 3024.0 | 40.0% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
