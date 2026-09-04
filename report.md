# API Reliability Monitor — SLA Report

> Last updated: **2026-09-04 09:11 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **7/12** &nbsp;|&nbsp; Avg uptime: **77.0%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 70.29% | 3104.1 | 10420.1 | 1000ms | 728/2450 |
| ❌ | `public_apis_list` | 0.0% | 99.39% | 142.1 | 5075.4 | 1500ms | 15/2450 |
| ❌ | `ipapi_check` | 49.06% | 99.96% | 144.9 | 4507.0 | 2500ms | 1/2450 |
| ❌ | `nasa_apod` | 80.61% | 58.69% | 2705.0 | 11152.5 | 2000ms | 1012/2450 |
| ⚠️ | `dog_ceo_random` | 96.9% | 97.59% | 482.5 | 10244.1 | 2500ms | 59/2450 |
| ✅ | `open_meteo_weather` | 99.02% | 98.2% | 675.1 | 14877.1 | 2000ms | 44/2450 |
| ✅ | `rest_countries` | 99.39% | 99.1% | 268.8 | 10221.5 | 2500ms | 22/2450 |
| ✅ | `useless_fact` | 99.47% | 99.67% | 659.2 | 10229.6 | 2500ms | 8/2450 |
| ✅ | `catfact_random` | 99.8% | 99.47% | 261.7 | 10080.2 | 3000ms | 13/2450 |
| ✅ | `coingecko_bitcoin` | 99.84% | 99.92% | 96.4 | 4328.4 | 1500ms | 2/2450 |
| ✅ | `agify_name` | 99.92% | 99.51% | 403.3 | 16112.2 | 2000ms | 12/2450 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.92% | 184.3 | 3882.8 | 2000ms | 2/2450 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `numbers_trivia` | 03:00 | 4651.1 | 46.15% |
| `numbers_trivia` | 10:00 | 3720.9 | 35.42% |
| `numbers_trivia` | 02:00 | 3519.9 | 33.33% |
| `numbers_trivia` | 14:00 | 3451.0 | 33.33% |
| `numbers_trivia` | 00:00 | 3434.9 | 32.84% |
| `nasa_apod` | 17:00 | 3323.2 | 41.73% |
| `nasa_apod` | 03:00 | 3307.4 | 48.08% |
| `numbers_trivia` | 09:00 | 3304.7 | 31.78% |
| `numbers_trivia` | 17:00 | 3299.9 | 32.81% |
| `nasa_apod` | 05:00 | 3228.7 | 46.48% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
