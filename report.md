# API Reliability Monitor — SLA Report

> Last updated: **2026-09-05 16:01 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **7/12** &nbsp;|&nbsp; Avg uptime: **77.0%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 70.41% | 3092.1 | 10420.1 | 1000ms | 728/2460 |
| ❌ | `public_apis_list` | 0.0% | 99.39% | 142.1 | 5075.4 | 1500ms | 15/2460 |
| ❌ | `ipapi_check` | 48.86% | 99.96% | 144.9 | 4507.0 | 2500ms | 1/2460 |
| ❌ | `nasa_apod` | 80.69% | 58.82% | 2696.7 | 11152.5 | 2000ms | 1013/2460 |
| ⚠️ | `dog_ceo_random` | 96.91% | 97.6% | 482.2 | 10244.1 | 2500ms | 59/2460 |
| ✅ | `open_meteo_weather` | 99.02% | 98.21% | 674.3 | 14877.1 | 2000ms | 44/2460 |
| ✅ | `rest_countries` | 99.39% | 99.11% | 268.5 | 10221.5 | 2500ms | 22/2460 |
| ✅ | `useless_fact` | 99.47% | 99.63% | 661.3 | 10229.6 | 2500ms | 9/2460 |
| ✅ | `catfact_random` | 99.8% | 99.47% | 261.6 | 10080.2 | 3000ms | 13/2460 |
| ✅ | `coingecko_bitcoin` | 99.84% | 99.92% | 96.4 | 4328.4 | 1500ms | 2/2460 |
| ✅ | `agify_name` | 99.92% | 99.51% | 402.8 | 16112.2 | 2000ms | 12/2460 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.92% | 184.0 | 3882.8 | 2000ms | 2/2460 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `numbers_trivia` | 03:00 | 4651.1 | 46.15% |
| `numbers_trivia` | 10:00 | 3720.9 | 35.42% |
| `numbers_trivia` | 02:00 | 3519.9 | 33.33% |
| `numbers_trivia` | 14:00 | 3451.0 | 33.33% |
| `numbers_trivia` | 00:00 | 3434.9 | 32.84% |
| `nasa_apod` | 03:00 | 3307.4 | 48.08% |
| `nasa_apod` | 17:00 | 3300.9 | 41.41% |
| `numbers_trivia` | 17:00 | 3275.5 | 32.56% |
| `numbers_trivia` | 09:00 | 3274.8 | 31.48% |
| `numbers_trivia` | 12:00 | 3212.5 | 30.11% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
