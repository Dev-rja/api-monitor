# API Reliability Monitor — SLA Report

> Last updated: **2026-10-15 00:49 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **7/12** &nbsp;|&nbsp; Avg uptime: **76.6%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 72.93% | 2842.4 | 10420.1 | 1000ms | 728/2689 |
| ❌ | `public_apis_list` | 0.0% | 99.44% | 142.5 | 5075.4 | 1500ms | 15/2689 |
| ❌ | `ipapi_check` | 44.92% | 99.96% | 145.1 | 4507.0 | 2500ms | 1/2689 |
| ❌ | `nasa_apod` | 79.73% | 59.54% | 2674.7 | 11152.5 | 2000ms | 1088/2689 |
| ⚠️ | `dog_ceo_random` | 97.14% | 97.77% | 480.0 | 10509.6 | 2500ms | 60/2689 |
| ✅ | `open_meteo_weather` | 99.0% | 98.29% | 668.7 | 14877.1 | 2000ms | 46/2689 |
| ✅ | `useless_fact` | 99.11% | 99.52% | 669.7 | 10229.6 | 2500ms | 13/2689 |
| ✅ | `rest_countries` | 99.44% | 99.14% | 271.8 | 10221.5 | 2500ms | 23/2689 |
| ✅ | `coingecko_bitcoin` | 99.7% | 99.93% | 97.2 | 4328.4 | 1500ms | 2/2689 |
| ✅ | `catfact_random` | 99.81% | 99.52% | 262.6 | 10080.2 | 3000ms | 13/2689 |
| ✅ | `agify_name` | 99.93% | 99.55% | 401.9 | 16112.2 | 2000ms | 12/2689 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.89% | 181.4 | 3882.8 | 2000ms | 3/2689 |

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
