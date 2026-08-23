# API Reliability Monitor — SLA Report

> Last updated: **2026-08-23 15:31 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **7/12** &nbsp;|&nbsp; Avg uptime: **77.2%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 68.28% | 3303.2 | 10420.1 | 1000ms | 728/2295 |
| ❌ | `public_apis_list` | 0.0% | 99.48% | 138.7 | 5075.4 | 1500ms | 12/2295 |
| ❌ | `ipapi_check` | 51.9% | 99.96% | 144.8 | 4507.0 | 2500ms | 1/2295 |
| ❌ | `nasa_apod` | 79.83% | 57.34% | 2789.5 | 11152.5 | 2000ms | 979/2295 |
| ⚠️ | `dog_ceo_random` | 96.69% | 97.43% | 488.9 | 10244.1 | 2500ms | 59/2295 |
| ✅ | `open_meteo_weather` | 99.0% | 98.13% | 678.9 | 14877.1 | 2000ms | 43/2295 |
| ✅ | `rest_countries` | 99.35% | 99.08% | 269.8 | 10221.5 | 2500ms | 21/2295 |
| ✅ | `useless_fact` | 99.78% | 99.69% | 653.0 | 10229.6 | 2500ms | 7/2295 |
| ✅ | `catfact_random` | 99.78% | 99.43% | 262.0 | 10080.2 | 3000ms | 13/2295 |
| ✅ | `coingecko_bitcoin` | 99.83% | 99.91% | 96.8 | 4328.4 | 1500ms | 2/2295 |
| ✅ | `agify_name` | 99.91% | 99.61% | 399.3 | 16112.2 | 2000ms | 9/2295 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.91% | 186.2 | 3882.8 | 2000ms | 2/2295 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `numbers_trivia` | 03:00 | 4927.1 | 48.98% |
| `numbers_trivia` | 02:00 | 4003.5 | 38.1% |
| `numbers_trivia` | 10:00 | 3915.9 | 37.36% |
| `numbers_trivia` | 00:00 | 3701.8 | 35.48% |
| `numbers_trivia` | 14:00 | 3674.3 | 35.58% |
| `numbers_trivia` | 17:00 | 3595.1 | 35.9% |
| `numbers_trivia` | 09:00 | 3595.0 | 34.69% |
| `nasa_apod` | 05:00 | 3513.1 | 50.0% |
| `numbers_trivia` | 05:00 | 3496.2 | 34.38% |
| `nasa_apod` | 03:00 | 3476.6 | 51.02% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
