# API Reliability Monitor — SLA Report

> Last updated: **2026-09-13 05:16 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **7/12** &nbsp;|&nbsp; Avg uptime: **76.9%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 71.07% | 3027.0 | 10420.1 | 1000ms | 728/2516 |
| ❌ | `public_apis_list` | 0.0% | 99.4% | 142.5 | 5075.4 | 1500ms | 15/2516 |
| ❌ | `ipapi_check` | 47.85% | 99.96% | 144.9 | 4507.0 | 2500ms | 1/2516 |
| ❌ | `nasa_apod` | 80.84% | 59.42% | 2665.5 | 11152.5 | 2000ms | 1021/2516 |
| ⚠️ | `dog_ceo_random` | 96.98% | 97.66% | 480.4 | 10244.1 | 2500ms | 59/2516 |
| ✅ | `open_meteo_weather` | 99.05% | 98.25% | 671.2 | 14877.1 | 2000ms | 44/2516 |
| ✅ | `useless_fact` | 99.4% | 99.56% | 665.6 | 10229.6 | 2500ms | 11/2516 |
| ✅ | `rest_countries` | 99.4% | 99.13% | 268.0 | 10221.5 | 2500ms | 22/2516 |
| ✅ | `catfact_random` | 99.8% | 99.48% | 262.0 | 10080.2 | 3000ms | 13/2516 |
| ✅ | `coingecko_bitcoin` | 99.84% | 99.92% | 96.6 | 4328.4 | 1500ms | 2/2516 |
| ✅ | `agify_name` | 99.92% | 99.52% | 403.0 | 16112.2 | 2000ms | 12/2516 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.88% | 183.7 | 3882.8 | 2000ms | 3/2516 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `numbers_trivia` | 03:00 | 4566.7 | 45.28% |
| `numbers_trivia` | 10:00 | 3684.4 | 35.05% |
| `numbers_trivia` | 02:00 | 3519.9 | 33.33% |
| `numbers_trivia` | 14:00 | 3421.8 | 33.04% |
| `numbers_trivia` | 00:00 | 3339.2 | 31.88% |
| `nasa_apod` | 03:00 | 3254.9 | 47.17% |
| `numbers_trivia` | 09:00 | 3246.5 | 31.19% |
| `nasa_apod` | 17:00 | 3235.8 | 40.46% |
| `numbers_trivia` | 17:00 | 3204.6 | 31.82% |
| `nasa_apod` | 12:00 | 3197.2 | 50.0% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
