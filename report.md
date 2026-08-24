# API Reliability Monitor — SLA Report

> Last updated: **2026-08-24 00:00 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **7/12** &nbsp;|&nbsp; Avg uptime: **77.1%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 68.57% | 3274.6 | 10420.1 | 1000ms | 728/2316 |
| ❌ | `public_apis_list` | 0.0% | 99.44% | 139.2 | 5075.4 | 1500ms | 13/2316 |
| ❌ | `ipapi_check` | 51.47% | 99.96% | 144.6 | 4507.0 | 2500ms | 1/2316 |
| ❌ | `nasa_apod` | 79.88% | 57.6% | 2781.1 | 11152.5 | 2000ms | 982/2316 |
| ⚠️ | `dog_ceo_random` | 96.72% | 97.45% | 487.8 | 10244.1 | 2500ms | 59/2316 |
| ✅ | `open_meteo_weather` | 99.01% | 98.14% | 677.8 | 14877.1 | 2000ms | 43/2316 |
| ✅ | `rest_countries` | 99.35% | 99.09% | 268.9 | 10221.5 | 2500ms | 21/2316 |
| ✅ | `useless_fact` | 99.78% | 99.7% | 653.6 | 10229.6 | 2500ms | 7/2316 |
| ✅ | `catfact_random` | 99.78% | 99.44% | 262.1 | 10080.2 | 3000ms | 13/2316 |
| ✅ | `coingecko_bitcoin` | 99.83% | 99.91% | 96.6 | 4328.4 | 1500ms | 2/2316 |
| ✅ | `agify_name` | 99.91% | 99.53% | 401.1 | 16112.2 | 2000ms | 11/2316 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.91% | 185.7 | 3882.8 | 2000ms | 2/2316 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `numbers_trivia` | 03:00 | 4927.1 | 48.98% |
| `numbers_trivia` | 02:00 | 4003.5 | 38.1% |
| `numbers_trivia` | 10:00 | 3915.9 | 37.36% |
| `numbers_trivia` | 14:00 | 3674.3 | 35.58% |
| `numbers_trivia` | 00:00 | 3645.0 | 34.92% |
| `numbers_trivia` | 09:00 | 3595.0 | 34.69% |
| `nasa_apod` | 05:00 | 3513.1 | 50.0% |
| `numbers_trivia` | 17:00 | 3510.1 | 35.0% |
| `numbers_trivia` | 05:00 | 3496.2 | 34.38% |
| `nasa_apod` | 03:00 | 3476.6 | 51.02% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
