# API Reliability Monitor — SLA Report

> Last updated: **2026-09-04 19:31 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **7/12** &nbsp;|&nbsp; Avg uptime: **77.0%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 70.32% | 3100.5 | 10420.1 | 1000ms | 728/2453 |
| ❌ | `public_apis_list` | 0.0% | 99.39% | 142.1 | 5075.4 | 1500ms | 15/2453 |
| ❌ | `ipapi_check` | 49.0% | 99.96% | 144.9 | 4507.0 | 2500ms | 1/2453 |
| ❌ | `nasa_apod` | 80.64% | 58.7% | 2703.2 | 11152.5 | 2000ms | 1013/2453 |
| ⚠️ | `dog_ceo_random` | 96.9% | 97.59% | 482.5 | 10244.1 | 2500ms | 59/2453 |
| ✅ | `open_meteo_weather` | 99.02% | 98.21% | 674.7 | 14877.1 | 2000ms | 44/2453 |
| ✅ | `rest_countries` | 99.39% | 99.1% | 268.7 | 10221.5 | 2500ms | 22/2453 |
| ✅ | `useless_fact` | 99.47% | 99.67% | 659.7 | 10229.6 | 2500ms | 8/2453 |
| ✅ | `catfact_random` | 99.8% | 99.47% | 261.5 | 10080.2 | 3000ms | 13/2453 |
| ✅ | `coingecko_bitcoin` | 99.84% | 99.92% | 96.4 | 4328.4 | 1500ms | 2/2453 |
| ✅ | `agify_name` | 99.92% | 99.51% | 403.1 | 16112.2 | 2000ms | 12/2453 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.92% | 184.2 | 3882.8 | 2000ms | 2/2453 |

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
| `numbers_trivia` | 09:00 | 3304.7 | 31.78% |
| `nasa_apod` | 17:00 | 3300.9 | 41.41% |
| `numbers_trivia` | 17:00 | 3275.5 | 32.56% |
| `nasa_apod` | 05:00 | 3228.7 | 46.48% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
