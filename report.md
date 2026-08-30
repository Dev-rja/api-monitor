# API Reliability Monitor — SLA Report

> Last updated: **2026-08-30 17:25 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **7/12** &nbsp;|&nbsp; Avg uptime: **77.1%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 69.92% | 3140.7 | 10420.1 | 1000ms | 728/2420 |
| ❌ | `public_apis_list` | 0.0% | 99.46% | 139.7 | 5075.4 | 1500ms | 13/2420 |
| ❌ | `ipapi_check` | 49.59% | 99.96% | 144.5 | 4507.0 | 2500ms | 1/2420 |
| ❌ | `nasa_apod` | 80.5% | 58.43% | 2717.8 | 11152.5 | 2000ms | 1006/2420 |
| ⚠️ | `dog_ceo_random` | 96.86% | 97.56% | 483.6 | 10244.1 | 2500ms | 59/2420 |
| ✅ | `open_meteo_weather` | 99.01% | 98.22% | 673.8 | 14877.1 | 2000ms | 43/2420 |
| ✅ | `rest_countries` | 99.38% | 99.13% | 265.7 | 10221.5 | 2500ms | 21/2420 |
| ✅ | `useless_fact` | 99.79% | 99.71% | 657.2 | 10229.6 | 2500ms | 7/2420 |
| ✅ | `catfact_random` | 99.79% | 99.46% | 261.4 | 10080.2 | 3000ms | 13/2420 |
| ✅ | `coingecko_bitcoin` | 99.83% | 99.92% | 96.4 | 4328.4 | 1500ms | 2/2420 |
| ✅ | `agify_name` | 99.92% | 99.5% | 403.6 | 16112.2 | 2000ms | 12/2420 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.92% | 184.4 | 3882.8 | 2000ms | 2/2420 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `numbers_trivia` | 03:00 | 4651.1 | 46.15% |
| `numbers_trivia` | 10:00 | 3720.9 | 35.42% |
| `numbers_trivia` | 00:00 | 3645.0 | 34.92% |
| `numbers_trivia` | 02:00 | 3519.9 | 33.33% |
| `numbers_trivia` | 14:00 | 3512.8 | 33.94% |
| `numbers_trivia` | 09:00 | 3427.7 | 33.01% |
| `numbers_trivia` | 17:00 | 3375.4 | 33.6% |
| `nasa_apod` | 05:00 | 3310.8 | 47.83% |
| `nasa_apod` | 03:00 | 3307.4 | 48.08% |
| `nasa_apod` | 09:00 | 3291.4 | 46.08% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
