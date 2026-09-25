# API Reliability Monitor — SLA Report

> Last updated: **2026-09-25 12:18 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **7/12** &nbsp;|&nbsp; Avg uptime: **76.8%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 71.92% | 2942.0 | 10420.1 | 1000ms | 728/2593 |
| ❌ | `public_apis_list` | 0.0% | 99.42% | 142.6 | 5075.4 | 1500ms | 15/2593 |
| ❌ | `ipapi_check` | 46.47% | 99.96% | 144.7 | 4507.0 | 2500ms | 1/2593 |
| ❌ | `nasa_apod` | 81.18% | 59.97% | 2628.7 | 11152.5 | 2000ms | 1038/2593 |
| ⚠️ | `dog_ceo_random` | 97.07% | 97.72% | 478.0 | 10244.1 | 2500ms | 59/2593 |
| ✅ | `open_meteo_weather` | 99.04% | 98.26% | 670.5 | 14877.1 | 2000ms | 45/2593 |
| ✅ | `useless_fact` | 99.11% | 99.5% | 669.7 | 10229.6 | 2500ms | 13/2593 |
| ✅ | `rest_countries` | 99.42% | 99.15% | 268.3 | 10221.5 | 2500ms | 22/2593 |
| ✅ | `catfact_random` | 99.81% | 99.5% | 262.7 | 10080.2 | 3000ms | 13/2593 |
| ✅ | `coingecko_bitcoin` | 99.85% | 99.92% | 96.8 | 4328.4 | 1500ms | 2/2593 |
| ✅ | `agify_name` | 99.92% | 99.54% | 402.8 | 16112.2 | 2000ms | 12/2593 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.88% | 182.6 | 3882.8 | 2000ms | 3/2593 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `numbers_trivia` | 03:00 | 4566.7 | 45.28% |
| `numbers_trivia` | 10:00 | 3544.5 | 33.66% |
| `numbers_trivia` | 02:00 | 3519.9 | 33.33% |
| `numbers_trivia` | 14:00 | 3255.8 | 31.36% |
| `nasa_apod` | 03:00 | 3254.9 | 47.17% |
| `numbers_trivia` | 09:00 | 3165.1 | 30.36% |
| `nasa_apod` | 17:00 | 3132.3 | 38.97% |
| `numbers_trivia` | 00:00 | 3126.9 | 29.73% |
| `nasa_apod` | 11:00 | 3115.1 | 43.38% |
| `numbers_trivia` | 17:00 | 3092.8 | 30.66% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
