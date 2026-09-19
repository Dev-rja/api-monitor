# API Reliability Monitor — SLA Report

> Last updated: **2026-09-19 13:22 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **7/12** &nbsp;|&nbsp; Avg uptime: **76.9%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 71.51% | 2983.3 | 10420.1 | 1000ms | 728/2555 |
| ❌ | `public_apis_list` | 0.0% | 99.41% | 142.5 | 5075.4 | 1500ms | 15/2555 |
| ❌ | `ipapi_check` | 47.12% | 99.96% | 144.8 | 4507.0 | 2500ms | 1/2555 |
| ❌ | `nasa_apod` | 81.02% | 59.73% | 2648.1 | 11152.5 | 2000ms | 1029/2555 |
| ⚠️ | `dog_ceo_random` | 97.03% | 97.69% | 478.9 | 10244.1 | 2500ms | 59/2555 |
| ✅ | `open_meteo_weather` | 99.06% | 98.28% | 668.9 | 14877.1 | 2000ms | 44/2555 |
| ✅ | `useless_fact` | 99.1% | 99.53% | 668.8 | 10229.6 | 2500ms | 12/2555 |
| ✅ | `rest_countries` | 99.41% | 99.14% | 267.6 | 10221.5 | 2500ms | 22/2555 |
| ✅ | `catfact_random` | 99.8% | 99.49% | 262.1 | 10080.2 | 3000ms | 13/2555 |
| ✅ | `coingecko_bitcoin` | 99.84% | 99.92% | 96.6 | 4328.4 | 1500ms | 2/2555 |
| ✅ | `agify_name` | 99.92% | 99.53% | 402.8 | 16112.2 | 2000ms | 12/2555 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.88% | 182.9 | 3882.8 | 2000ms | 3/2555 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `numbers_trivia` | 03:00 | 4566.7 | 45.28% |
| `numbers_trivia` | 10:00 | 3578.9 | 34.0% |
| `numbers_trivia` | 02:00 | 3519.9 | 33.33% |
| `numbers_trivia` | 14:00 | 3308.7 | 31.9% |
| `nasa_apod` | 03:00 | 3254.9 | 47.17% |
| `numbers_trivia` | 00:00 | 3208.0 | 30.56% |
| `numbers_trivia` | 09:00 | 3192.0 | 30.63% |
| `nasa_apod` | 17:00 | 3172.5 | 39.55% |
| `nasa_apod` | 12:00 | 3169.6 | 49.48% |
| `numbers_trivia` | 17:00 | 3137.0 | 31.11% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
