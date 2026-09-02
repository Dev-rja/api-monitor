# API Reliability Monitor — SLA Report

> Last updated: **2026-09-02 05:02 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **7/12** &nbsp;|&nbsp; Avg uptime: **77.0%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 70.1% | 3122.3 | 10420.1 | 1000ms | 728/2435 |
| ❌ | `public_apis_list` | 0.0% | 99.43% | 141.3 | 5075.4 | 1500ms | 14/2435 |
| ❌ | `ipapi_check` | 49.36% | 99.96% | 144.7 | 4507.0 | 2500ms | 1/2435 |
| ❌ | `nasa_apod` | 80.62% | 58.6% | 2708.0 | 11152.5 | 2000ms | 1008/2435 |
| ⚠️ | `dog_ceo_random` | 96.88% | 97.58% | 483.1 | 10244.1 | 2500ms | 59/2435 |
| ✅ | `open_meteo_weather` | 99.01% | 98.23% | 673.4 | 14877.1 | 2000ms | 43/2435 |
| ✅ | `rest_countries` | 99.38% | 99.1% | 268.7 | 10221.5 | 2500ms | 22/2435 |
| ✅ | `useless_fact` | 99.79% | 99.71% | 657.4 | 10229.6 | 2500ms | 7/2435 |
| ✅ | `catfact_random` | 99.79% | 99.47% | 261.7 | 10080.2 | 3000ms | 13/2435 |
| ✅ | `coingecko_bitcoin` | 99.84% | 99.92% | 96.4 | 4328.4 | 1500ms | 2/2435 |
| ✅ | `agify_name` | 99.92% | 99.51% | 403.5 | 16112.2 | 2000ms | 12/2435 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.92% | 184.5 | 3882.8 | 2000ms | 2/2435 |

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
| `nasa_apod` | 03:00 | 3307.4 | 48.08% |
| `nasa_apod` | 05:00 | 3266.3 | 47.14% |
| `nasa_apod` | 09:00 | 3264.7 | 45.63% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
