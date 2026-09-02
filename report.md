# API Reliability Monitor — SLA Report

> Last updated: **2026-09-02 00:34 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **7/12** &nbsp;|&nbsp; Avg uptime: **77.0%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 70.09% | 3123.5 | 10420.1 | 1000ms | 728/2434 |
| ❌ | `public_apis_list` | 0.0% | 99.42% | 141.2 | 5075.4 | 1500ms | 14/2434 |
| ❌ | `ipapi_check` | 49.38% | 99.96% | 144.7 | 4507.0 | 2500ms | 1/2434 |
| ❌ | `nasa_apod` | 80.61% | 58.59% | 2709.0 | 11152.5 | 2000ms | 1008/2434 |
| ⚠️ | `dog_ceo_random` | 96.88% | 97.58% | 483.2 | 10244.1 | 2500ms | 59/2434 |
| ✅ | `open_meteo_weather` | 99.01% | 98.23% | 673.4 | 14877.1 | 2000ms | 43/2434 |
| ✅ | `rest_countries` | 99.38% | 99.1% | 268.7 | 10221.5 | 2500ms | 22/2434 |
| ✅ | `useless_fact` | 99.79% | 99.71% | 657.4 | 10229.6 | 2500ms | 7/2434 |
| ✅ | `catfact_random` | 99.79% | 99.47% | 261.7 | 10080.2 | 3000ms | 13/2434 |
| ✅ | `coingecko_bitcoin` | 99.84% | 99.92% | 96.5 | 4328.4 | 1500ms | 2/2434 |
| ✅ | `agify_name` | 99.92% | 99.51% | 403.4 | 16112.2 | 2000ms | 12/2434 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.92% | 184.5 | 3882.8 | 2000ms | 2/2434 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `numbers_trivia` | 03:00 | 4651.1 | 46.15% |
| `numbers_trivia` | 10:00 | 3720.9 | 35.42% |
| `numbers_trivia` | 00:00 | 3536.6 | 33.85% |
| `numbers_trivia` | 02:00 | 3519.9 | 33.33% |
| `numbers_trivia` | 14:00 | 3451.0 | 33.33% |
| `numbers_trivia` | 09:00 | 3395.5 | 32.69% |
| `numbers_trivia` | 17:00 | 3349.8 | 33.33% |
| `nasa_apod` | 05:00 | 3310.8 | 47.83% |
| `nasa_apod` | 03:00 | 3307.4 | 48.08% |
| `nasa_apod` | 09:00 | 3264.7 | 45.63% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
