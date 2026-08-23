# API Reliability Monitor — SLA Report

> Last updated: **2026-08-23 22:01 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **7/12** &nbsp;|&nbsp; Avg uptime: **77.2%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 68.5% | 3281.3 | 10420.1 | 1000ms | 728/2311 |
| ❌ | `public_apis_list` | 0.0% | 99.48% | 138.5 | 5075.4 | 1500ms | 12/2311 |
| ❌ | `ipapi_check` | 51.54% | 99.96% | 144.7 | 4507.0 | 2500ms | 1/2311 |
| ❌ | `nasa_apod` | 79.92% | 57.59% | 2777.8 | 11152.5 | 2000ms | 980/2311 |
| ⚠️ | `dog_ceo_random` | 96.71% | 97.45% | 488.2 | 10244.1 | 2500ms | 59/2311 |
| ✅ | `open_meteo_weather` | 99.0% | 98.14% | 678.1 | 14877.1 | 2000ms | 43/2311 |
| ✅ | `rest_countries` | 99.35% | 99.09% | 269.1 | 10221.5 | 2500ms | 21/2311 |
| ✅ | `useless_fact` | 99.78% | 99.7% | 653.1 | 10229.6 | 2500ms | 7/2311 |
| ✅ | `catfact_random` | 99.78% | 99.44% | 262.1 | 10080.2 | 3000ms | 13/2311 |
| ✅ | `coingecko_bitcoin` | 99.83% | 99.91% | 96.7 | 4328.4 | 1500ms | 2/2311 |
| ✅ | `agify_name` | 99.91% | 99.52% | 401.1 | 16112.2 | 2000ms | 11/2311 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.91% | 185.9 | 3882.8 | 2000ms | 2/2311 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `numbers_trivia` | 03:00 | 4927.1 | 48.98% |
| `numbers_trivia` | 02:00 | 4003.5 | 38.1% |
| `numbers_trivia` | 10:00 | 3915.9 | 37.36% |
| `numbers_trivia` | 00:00 | 3701.8 | 35.48% |
| `numbers_trivia` | 14:00 | 3674.3 | 35.58% |
| `numbers_trivia` | 09:00 | 3595.0 | 34.69% |
| `nasa_apod` | 05:00 | 3513.1 | 50.0% |
| `numbers_trivia` | 17:00 | 3510.1 | 35.0% |
| `numbers_trivia` | 05:00 | 3496.2 | 34.38% |
| `nasa_apod` | 03:00 | 3476.6 | 51.02% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
