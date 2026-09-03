# API Reliability Monitor — SLA Report

> Last updated: **2026-09-03 20:06 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **7/12** &nbsp;|&nbsp; Avg uptime: **77.0%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 70.24% | 3108.9 | 10420.1 | 1000ms | 728/2446 |
| ❌ | `public_apis_list` | 0.0% | 99.39% | 142.2 | 5075.4 | 1500ms | 15/2446 |
| ❌ | `ipapi_check` | 49.14% | 99.96% | 144.9 | 4507.0 | 2500ms | 1/2446 |
| ❌ | `nasa_apod` | 80.62% | 58.67% | 2707.3 | 11152.5 | 2000ms | 1011/2446 |
| ⚠️ | `dog_ceo_random` | 96.89% | 97.59% | 482.9 | 10244.1 | 2500ms | 59/2446 |
| ✅ | `open_meteo_weather` | 99.02% | 98.2% | 675.6 | 14877.1 | 2000ms | 44/2446 |
| ✅ | `rest_countries` | 99.39% | 99.1% | 269.0 | 10221.5 | 2500ms | 22/2446 |
| ✅ | `useless_fact` | 99.59% | 99.67% | 659.1 | 10229.6 | 2500ms | 8/2446 |
| ✅ | `catfact_random` | 99.8% | 99.47% | 261.8 | 10080.2 | 3000ms | 13/2446 |
| ✅ | `coingecko_bitcoin` | 99.84% | 99.92% | 96.4 | 4328.4 | 1500ms | 2/2446 |
| ✅ | `agify_name` | 99.92% | 99.51% | 403.4 | 16112.2 | 2000ms | 12/2446 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.92% | 184.4 | 3882.8 | 2000ms | 2/2446 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `numbers_trivia` | 03:00 | 4651.1 | 46.15% |
| `numbers_trivia` | 10:00 | 3720.9 | 35.42% |
| `numbers_trivia` | 02:00 | 3519.9 | 33.33% |
| `numbers_trivia` | 00:00 | 3486.1 | 33.33% |
| `numbers_trivia` | 14:00 | 3451.0 | 33.33% |
| `numbers_trivia` | 09:00 | 3334.7 | 32.08% |
| `nasa_apod` | 17:00 | 3323.2 | 41.73% |
| `nasa_apod` | 03:00 | 3307.4 | 48.08% |
| `numbers_trivia` | 17:00 | 3299.9 | 32.81% |
| `nasa_apod` | 05:00 | 3228.7 | 46.48% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
