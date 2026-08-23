# API Reliability Monitor — SLA Report

> Last updated: **2026-08-23 11:51 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **77.2%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 68.18% | 3312.9 | 10420.1 | 1000ms | 728/2288 |
| ❌ | `public_apis_list` | 0.0% | 99.48% | 138.8 | 5075.4 | 1500ms | 12/2288 |
| ❌ | `ipapi_check` | 52.05% | 99.96% | 144.9 | 4507.0 | 2500ms | 1/2288 |
| ❌ | `nasa_apod` | 79.81% | 57.26% | 2792.4 | 11152.5 | 2000ms | 978/2288 |
| ⚠️ | `dog_ceo_random` | 96.68% | 97.47% | 488.1 | 10244.1 | 2500ms | 58/2288 |
| ⚠️ | `open_meteo_weather` | 98.99% | 98.12% | 679.2 | 14877.1 | 2000ms | 43/2288 |
| ✅ | `rest_countries` | 99.34% | 99.08% | 270.1 | 10221.5 | 2500ms | 21/2288 |
| ✅ | `useless_fact` | 99.78% | 99.69% | 652.9 | 10229.6 | 2500ms | 7/2288 |
| ✅ | `catfact_random` | 99.78% | 99.43% | 262.2 | 10080.2 | 3000ms | 13/2288 |
| ✅ | `coingecko_bitcoin` | 99.83% | 99.91% | 96.9 | 4328.4 | 1500ms | 2/2288 |
| ✅ | `agify_name` | 99.91% | 99.61% | 399.0 | 16112.2 | 2000ms | 9/2288 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.91% | 186.3 | 3882.8 | 2000ms | 2/2288 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `numbers_trivia` | 03:00 | 4927.1 | 48.98% |
| `numbers_trivia` | 02:00 | 4003.5 | 38.1% |
| `numbers_trivia` | 10:00 | 3915.9 | 37.36% |
| `numbers_trivia` | 14:00 | 3780.0 | 36.63% |
| `numbers_trivia` | 00:00 | 3701.8 | 35.48% |
| `numbers_trivia` | 17:00 | 3595.1 | 35.9% |
| `numbers_trivia` | 09:00 | 3595.0 | 34.69% |
| `nasa_apod` | 05:00 | 3513.1 | 50.0% |
| `numbers_trivia` | 05:00 | 3496.2 | 34.38% |
| `nasa_apod` | 03:00 | 3476.6 | 51.02% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
