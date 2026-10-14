# API Reliability Monitor — SLA Report

> Last updated: **2026-10-14 19:27 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **7/12** &nbsp;|&nbsp; Avg uptime: **76.6%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 72.91% | 2844.4 | 10420.1 | 1000ms | 728/2687 |
| ❌ | `public_apis_list` | 0.0% | 99.44% | 142.6 | 5075.4 | 1500ms | 15/2687 |
| ❌ | `ipapi_check` | 44.96% | 99.96% | 145.0 | 4507.0 | 2500ms | 1/2687 |
| ❌ | `nasa_apod` | 79.79% | 59.55% | 2672.5 | 11152.5 | 2000ms | 1087/2687 |
| ⚠️ | `dog_ceo_random` | 97.13% | 97.77% | 480.1 | 10509.6 | 2500ms | 60/2687 |
| ✅ | `open_meteo_weather` | 99.0% | 98.29% | 668.8 | 14877.1 | 2000ms | 46/2687 |
| ✅ | `useless_fact` | 99.11% | 99.52% | 669.7 | 10229.6 | 2500ms | 13/2687 |
| ✅ | `rest_countries` | 99.44% | 99.14% | 271.8 | 10221.5 | 2500ms | 23/2687 |
| ✅ | `coingecko_bitcoin` | 99.7% | 99.93% | 97.3 | 4328.4 | 1500ms | 2/2687 |
| ✅ | `catfact_random` | 99.81% | 99.52% | 262.6 | 10080.2 | 3000ms | 13/2687 |
| ✅ | `agify_name` | 99.93% | 99.55% | 402.0 | 16112.2 | 2000ms | 12/2687 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.89% | 181.4 | 3882.8 | 2000ms | 3/2687 |

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
