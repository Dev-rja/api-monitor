# API Reliability Monitor — SLA Report

> Last updated: **2026-09-22 23:37 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **7/12** &nbsp;|&nbsp; Avg uptime: **76.8%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 71.76% | 2958.2 | 10420.1 | 1000ms | 728/2578 |
| ❌ | `public_apis_list` | 0.0% | 99.42% | 142.9 | 5075.4 | 1500ms | 15/2578 |
| ❌ | `ipapi_check` | 46.7% | 99.96% | 144.7 | 4507.0 | 2500ms | 1/2578 |
| ❌ | `nasa_apod` | 81.15% | 59.93% | 2634.5 | 11152.5 | 2000ms | 1033/2578 |
| ⚠️ | `dog_ceo_random` | 97.05% | 97.71% | 478.3 | 10244.1 | 2500ms | 59/2578 |
| ✅ | `open_meteo_weather` | 99.03% | 98.25% | 672.0 | 14877.1 | 2000ms | 45/2578 |
| ✅ | `useless_fact` | 99.11% | 99.53% | 668.8 | 10229.6 | 2500ms | 12/2578 |
| ✅ | `rest_countries` | 99.42% | 99.15% | 267.3 | 10221.5 | 2500ms | 22/2578 |
| ✅ | `catfact_random` | 99.81% | 99.5% | 262.2 | 10080.2 | 3000ms | 13/2578 |
| ✅ | `coingecko_bitcoin` | 99.84% | 99.92% | 96.8 | 4328.4 | 1500ms | 2/2578 |
| ✅ | `agify_name` | 99.92% | 99.53% | 403.1 | 16112.2 | 2000ms | 12/2578 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.88% | 182.6 | 3882.8 | 2000ms | 3/2578 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `numbers_trivia` | 03:00 | 4566.7 | 45.28% |
| `numbers_trivia` | 10:00 | 3544.5 | 33.66% |
| `numbers_trivia` | 02:00 | 3519.9 | 33.33% |
| `numbers_trivia` | 14:00 | 3255.8 | 31.36% |
| `nasa_apod` | 03:00 | 3254.9 | 47.17% |
| `nasa_apod` | 17:00 | 3172.5 | 39.55% |
| `nasa_apod` | 12:00 | 3169.6 | 49.48% |
| `numbers_trivia` | 09:00 | 3165.1 | 30.36% |
| `numbers_trivia` | 17:00 | 3137.0 | 31.11% |
| `numbers_trivia` | 00:00 | 3126.9 | 29.73% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
