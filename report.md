# API Reliability Monitor — SLA Report

> Last updated: **2026-09-16 23:48 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **7/12** &nbsp;|&nbsp; Avg uptime: **76.9%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 71.32% | 3002.2 | 10420.1 | 1000ms | 728/2538 |
| ❌ | `public_apis_list` | 0.0% | 99.41% | 142.7 | 5075.4 | 1500ms | 15/2538 |
| ❌ | `ipapi_check` | 47.44% | 99.96% | 144.7 | 4507.0 | 2500ms | 1/2538 |
| ❌ | `nasa_apod` | 80.97% | 59.61% | 2656.4 | 11152.5 | 2000ms | 1025/2538 |
| ⚠️ | `dog_ceo_random` | 97.01% | 97.68% | 479.7 | 10244.1 | 2500ms | 59/2538 |
| ✅ | `open_meteo_weather` | 99.05% | 98.27% | 669.8 | 14877.1 | 2000ms | 44/2538 |
| ✅ | `useless_fact` | 99.09% | 99.53% | 668.5 | 10229.6 | 2500ms | 12/2538 |
| ✅ | `rest_countries` | 99.41% | 99.13% | 267.5 | 10221.5 | 2500ms | 22/2538 |
| ✅ | `catfact_random` | 99.8% | 99.49% | 262.1 | 10080.2 | 3000ms | 13/2538 |
| ✅ | `coingecko_bitcoin` | 99.84% | 99.92% | 96.5 | 4328.4 | 1500ms | 2/2538 |
| ✅ | `agify_name` | 99.92% | 99.53% | 402.6 | 16112.2 | 2000ms | 12/2538 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.88% | 183.1 | 3882.8 | 2000ms | 3/2538 |

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
| `nasa_apod` | 17:00 | 3213.2 | 40.15% |
| `nasa_apod` | 12:00 | 3197.2 | 50.0% |
| `numbers_trivia` | 17:00 | 3182.1 | 31.58% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
