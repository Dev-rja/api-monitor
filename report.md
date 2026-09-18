# API Reliability Monitor — SLA Report

> Last updated: **2026-09-18 20:35 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **7/12** &nbsp;|&nbsp; Avg uptime: **76.9%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 71.45% | 2988.9 | 10420.1 | 1000ms | 728/2550 |
| ❌ | `public_apis_list` | 0.0% | 99.41% | 142.6 | 5075.4 | 1500ms | 15/2550 |
| ❌ | `ipapi_check` | 47.22% | 99.96% | 144.8 | 4507.0 | 2500ms | 1/2550 |
| ❌ | `nasa_apod` | 80.98% | 59.65% | 2652.5 | 11152.5 | 2000ms | 1029/2550 |
| ⚠️ | `dog_ceo_random` | 97.02% | 97.69% | 479.1 | 10244.1 | 2500ms | 59/2550 |
| ✅ | `open_meteo_weather` | 99.06% | 98.27% | 669.1 | 14877.1 | 2000ms | 44/2550 |
| ✅ | `useless_fact` | 99.1% | 99.53% | 668.8 | 10229.6 | 2500ms | 12/2550 |
| ✅ | `rest_countries` | 99.41% | 99.14% | 267.6 | 10221.5 | 2500ms | 22/2550 |
| ✅ | `catfact_random` | 99.8% | 99.49% | 262.1 | 10080.2 | 3000ms | 13/2550 |
| ✅ | `coingecko_bitcoin` | 99.84% | 99.92% | 96.6 | 4328.4 | 1500ms | 2/2550 |
| ✅ | `agify_name` | 99.92% | 99.53% | 402.9 | 16112.2 | 2000ms | 12/2550 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.88% | 183.0 | 3882.8 | 2000ms | 3/2550 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `numbers_trivia` | 03:00 | 4566.7 | 45.28% |
| `numbers_trivia` | 10:00 | 3578.9 | 34.0% |
| `numbers_trivia` | 02:00 | 3519.9 | 33.33% |
| `numbers_trivia` | 14:00 | 3308.7 | 31.9% |
| `nasa_apod` | 03:00 | 3254.9 | 47.17% |
| `numbers_trivia` | 00:00 | 3250.5 | 30.99% |
| `numbers_trivia` | 09:00 | 3219.5 | 30.91% |
| `nasa_apod` | 17:00 | 3172.5 | 39.55% |
| `nasa_apod` | 12:00 | 3169.6 | 49.48% |
| `numbers_trivia` | 17:00 | 3137.0 | 31.11% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
