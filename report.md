# API Reliability Monitor — SLA Report

> Last updated: **2026-08-28 22:43 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **7/12** &nbsp;|&nbsp; Avg uptime: **77.1%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 69.79% | 3153.0 | 10420.1 | 1000ms | 728/2410 |
| ❌ | `public_apis_list` | 0.0% | 99.46% | 139.7 | 5075.4 | 1500ms | 13/2410 |
| ❌ | `ipapi_check` | 49.79% | 99.96% | 144.6 | 4507.0 | 2500ms | 1/2410 |
| ❌ | `nasa_apod` | 80.41% | 58.26% | 2727.2 | 11152.5 | 2000ms | 1006/2410 |
| ⚠️ | `dog_ceo_random` | 96.85% | 97.55% | 484.0 | 10244.1 | 2500ms | 59/2410 |
| ✅ | `open_meteo_weather` | 99.0% | 98.22% | 674.0 | 14877.1 | 2000ms | 43/2410 |
| ✅ | `rest_countries` | 99.38% | 99.13% | 266.0 | 10221.5 | 2500ms | 21/2410 |
| ✅ | `useless_fact` | 99.79% | 99.71% | 656.5 | 10229.6 | 2500ms | 7/2410 |
| ✅ | `catfact_random` | 99.79% | 99.46% | 261.5 | 10080.2 | 3000ms | 13/2410 |
| ✅ | `coingecko_bitcoin` | 99.83% | 99.92% | 96.4 | 4328.4 | 1500ms | 2/2410 |
| ✅ | `agify_name` | 99.92% | 99.5% | 403.2 | 16112.2 | 2000ms | 12/2410 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.92% | 184.6 | 3882.8 | 2000ms | 2/2410 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `numbers_trivia` | 03:00 | 4740.2 | 47.06% |
| `numbers_trivia` | 10:00 | 3758.2 | 35.79% |
| `numbers_trivia` | 00:00 | 3645.0 | 34.92% |
| `numbers_trivia` | 02:00 | 3519.9 | 33.33% |
| `numbers_trivia` | 14:00 | 3512.8 | 33.94% |
| `numbers_trivia` | 09:00 | 3427.7 | 33.01% |
| `numbers_trivia` | 17:00 | 3401.9 | 33.87% |
| `nasa_apod` | 03:00 | 3359.4 | 49.02% |
| `nasa_apod` | 05:00 | 3310.8 | 47.83% |
| `nasa_apod` | 09:00 | 3291.4 | 46.08% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
