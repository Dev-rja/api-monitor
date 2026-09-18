# API Reliability Monitor — SLA Report

> Last updated: **2026-09-18 05:56 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **7/12** &nbsp;|&nbsp; Avg uptime: **76.9%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 71.41% | 2993.3 | 10420.1 | 1000ms | 728/2546 |
| ❌ | `public_apis_list` | 0.0% | 99.41% | 142.6 | 5075.4 | 1500ms | 15/2546 |
| ❌ | `ipapi_check` | 47.29% | 99.96% | 144.8 | 4507.0 | 2500ms | 1/2546 |
| ❌ | `nasa_apod` | 80.99% | 59.66% | 2651.3 | 11152.5 | 2000ms | 1027/2546 |
| ⚠️ | `dog_ceo_random` | 97.01% | 97.68% | 479.3 | 10244.1 | 2500ms | 59/2546 |
| ✅ | `open_meteo_weather` | 99.06% | 98.27% | 669.3 | 14877.1 | 2000ms | 44/2546 |
| ✅ | `useless_fact` | 99.1% | 99.53% | 668.8 | 10229.6 | 2500ms | 12/2546 |
| ✅ | `rest_countries` | 99.41% | 99.14% | 267.6 | 10221.5 | 2500ms | 22/2546 |
| ✅ | `catfact_random` | 99.8% | 99.49% | 262.2 | 10080.2 | 3000ms | 13/2546 |
| ✅ | `coingecko_bitcoin` | 99.84% | 99.92% | 96.6 | 4328.4 | 1500ms | 2/2546 |
| ✅ | `agify_name` | 99.92% | 99.53% | 403.0 | 16112.2 | 2000ms | 12/2546 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.88% | 183.1 | 3882.8 | 2000ms | 3/2546 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `numbers_trivia` | 03:00 | 4566.7 | 45.28% |
| `numbers_trivia` | 10:00 | 3613.8 | 34.34% |
| `numbers_trivia` | 02:00 | 3519.9 | 33.33% |
| `numbers_trivia` | 14:00 | 3336.0 | 32.17% |
| `nasa_apod` | 03:00 | 3254.9 | 47.17% |
| `numbers_trivia` | 00:00 | 3250.5 | 30.99% |
| `numbers_trivia` | 09:00 | 3219.5 | 30.91% |
| `nasa_apod` | 17:00 | 3192.9 | 39.85% |
| `nasa_apod` | 12:00 | 3169.6 | 49.48% |
| `numbers_trivia` | 17:00 | 3159.8 | 31.34% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
