# API Reliability Monitor — SLA Report

> Last updated: **2026-09-07 06:01 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **7/12** &nbsp;|&nbsp; Avg uptime: **77.0%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 70.57% | 3075.4 | 10420.1 | 1000ms | 728/2474 |
| ❌ | `public_apis_list` | 0.0% | 99.39% | 142.1 | 5075.4 | 1500ms | 15/2474 |
| ❌ | `ipapi_check` | 48.59% | 99.96% | 144.8 | 4507.0 | 2500ms | 1/2474 |
| ❌ | `nasa_apod` | 80.72% | 58.93% | 2693.3 | 11152.5 | 2000ms | 1016/2474 |
| ⚠️ | `dog_ceo_random` | 96.93% | 97.62% | 481.6 | 10244.1 | 2500ms | 59/2474 |
| ✅ | `open_meteo_weather` | 99.03% | 98.22% | 673.6 | 14877.1 | 2000ms | 44/2474 |
| ✅ | `rest_countries` | 99.39% | 99.11% | 268.3 | 10221.5 | 2500ms | 22/2474 |
| ✅ | `useless_fact` | 99.47% | 99.64% | 661.1 | 10229.6 | 2500ms | 9/2474 |
| ✅ | `catfact_random` | 99.8% | 99.47% | 261.3 | 10080.2 | 3000ms | 13/2474 |
| ✅ | `coingecko_bitcoin` | 99.84% | 99.92% | 96.4 | 4328.4 | 1500ms | 2/2474 |
| ✅ | `agify_name` | 99.92% | 99.51% | 402.6 | 16112.2 | 2000ms | 12/2474 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.92% | 183.7 | 3882.8 | 2000ms | 2/2474 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `numbers_trivia` | 03:00 | 4566.7 | 45.28% |
| `numbers_trivia` | 10:00 | 3720.9 | 35.42% |
| `numbers_trivia` | 02:00 | 3519.9 | 33.33% |
| `numbers_trivia` | 14:00 | 3451.0 | 33.33% |
| `numbers_trivia` | 00:00 | 3434.9 | 32.84% |
| `nasa_apod` | 17:00 | 3280.6 | 41.09% |
| `numbers_trivia` | 09:00 | 3274.8 | 31.48% |
| `nasa_apod` | 03:00 | 3254.9 | 47.17% |
| `numbers_trivia` | 17:00 | 3251.3 | 32.31% |
| `nasa_apod` | 11:00 | 3197.9 | 44.7% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
