# API Reliability Monitor — SLA Report

> Last updated: **2026-10-03 03:17 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **7/12** &nbsp;|&nbsp; Avg uptime: **76.7%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 72.35% | 2899.6 | 10420.1 | 1000ms | 728/2633 |
| ❌ | `public_apis_list` | 0.0% | 99.43% | 142.7 | 5075.4 | 1500ms | 15/2633 |
| ❌ | `ipapi_check` | 45.88% | 99.96% | 144.9 | 4507.0 | 2500ms | 1/2633 |
| ❌ | `nasa_apod` | 80.86% | 59.93% | 2637.8 | 11152.5 | 2000ms | 1055/2633 |
| ⚠️ | `dog_ceo_random` | 97.11% | 97.76% | 477.3 | 10244.1 | 2500ms | 59/2633 |
| ✅ | `open_meteo_weather` | 99.05% | 98.29% | 668.4 | 14877.1 | 2000ms | 45/2633 |
| ✅ | `useless_fact` | 99.13% | 99.51% | 669.0 | 10229.6 | 2500ms | 13/2633 |
| ✅ | `rest_countries` | 99.43% | 99.13% | 271.9 | 10221.5 | 2500ms | 23/2633 |
| ✅ | `coingecko_bitcoin` | 99.7% | 99.92% | 96.9 | 4328.4 | 1500ms | 2/2633 |
| ✅ | `catfact_random` | 99.81% | 99.51% | 262.2 | 10080.2 | 3000ms | 13/2633 |
| ✅ | `agify_name` | 99.92% | 99.54% | 402.4 | 16112.2 | 2000ms | 12/2633 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.89% | 182.0 | 3882.8 | 2000ms | 3/2633 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `numbers_trivia` | 03:00 | 4483.7 | 44.44% |
| `numbers_trivia` | 10:00 | 3511.2 | 33.33% |
| `numbers_trivia` | 02:00 | 3385.1 | 32.0% |
| `numbers_trivia` | 14:00 | 3229.8 | 31.09% |
| `nasa_apod` | 03:00 | 3208.5 | 46.3% |
| `numbers_trivia` | 09:00 | 3138.9 | 30.09% |
| `nasa_apod` | 11:00 | 3115.1 | 43.38% |
| `nasa_apod` | 17:00 | 3111.5 | 38.69% |
| `nasa_apod` | 09:00 | 3096.9 | 43.75% |
| `numbers_trivia` | 17:00 | 3071.9 | 30.43% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
