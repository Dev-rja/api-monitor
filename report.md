# API Reliability Monitor — SLA Report

> Last updated: **2026-09-14 14:04 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **7/12** &nbsp;|&nbsp; Avg uptime: **76.9%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 71.17% | 3016.8 | 10420.1 | 1000ms | 728/2525 |
| ❌ | `public_apis_list` | 0.0% | 99.41% | 142.7 | 5075.4 | 1500ms | 15/2525 |
| ❌ | `ipapi_check` | 47.68% | 99.96% | 144.8 | 4507.0 | 2500ms | 1/2525 |
| ❌ | `nasa_apod` | 80.91% | 59.56% | 2657.5 | 11152.5 | 2000ms | 1021/2525 |
| ⚠️ | `dog_ceo_random` | 96.99% | 97.66% | 480.0 | 10244.1 | 2500ms | 59/2525 |
| ✅ | `open_meteo_weather` | 99.05% | 98.26% | 670.3 | 14877.1 | 2000ms | 44/2525 |
| ✅ | `useless_fact` | 99.09% | 99.52% | 668.5 | 10229.6 | 2500ms | 12/2525 |
| ✅ | `rest_countries` | 99.41% | 99.13% | 267.6 | 10221.5 | 2500ms | 22/2525 |
| ✅ | `catfact_random` | 99.8% | 99.49% | 262.0 | 10080.2 | 3000ms | 13/2525 |
| ✅ | `coingecko_bitcoin` | 99.84% | 99.92% | 96.5 | 4328.4 | 1500ms | 2/2525 |
| ✅ | `agify_name` | 99.92% | 99.52% | 402.7 | 16112.2 | 2000ms | 12/2525 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.88% | 183.3 | 3882.8 | 2000ms | 3/2525 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `numbers_trivia` | 03:00 | 4566.7 | 45.28% |
| `numbers_trivia` | 10:00 | 3648.7 | 34.69% |
| `numbers_trivia` | 02:00 | 3519.9 | 33.33% |
| `numbers_trivia` | 14:00 | 3364.1 | 32.46% |
| `numbers_trivia` | 00:00 | 3339.2 | 31.88% |
| `nasa_apod` | 03:00 | 3254.9 | 47.17% |
| `numbers_trivia` | 09:00 | 3246.5 | 31.19% |
| `nasa_apod` | 17:00 | 3213.2 | 40.15% |
| `nasa_apod` | 12:00 | 3197.2 | 50.0% |
| `numbers_trivia` | 17:00 | 3182.1 | 31.58% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
