# API Reliability Monitor — SLA Report

> Last updated: **2026-08-23 09:18 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **77.2%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 68.1% | 3321.1 | 10420.1 | 1000ms | 728/2282 |
| ❌ | `public_apis_list` | 0.0% | 99.47% | 138.9 | 5075.4 | 1500ms | 12/2282 |
| ❌ | `ipapi_check` | 52.19% | 99.96% | 144.9 | 4507.0 | 2500ms | 1/2282 |
| ❌ | `nasa_apod` | 79.75% | 57.19% | 2797.9 | 11152.5 | 2000ms | 977/2282 |
| ⚠️ | `dog_ceo_random` | 96.67% | 97.46% | 488.4 | 10244.1 | 2500ms | 58/2282 |
| ⚠️ | `open_meteo_weather` | 98.99% | 98.12% | 679.5 | 14877.1 | 2000ms | 43/2282 |
| ✅ | `rest_countries` | 99.34% | 99.08% | 270.3 | 10221.5 | 2500ms | 21/2282 |
| ✅ | `useless_fact` | 99.78% | 99.69% | 653.0 | 10229.6 | 2500ms | 7/2282 |
| ✅ | `catfact_random` | 99.78% | 99.43% | 262.2 | 10080.2 | 3000ms | 13/2282 |
| ✅ | `coingecko_bitcoin` | 99.82% | 99.91% | 96.9 | 4328.4 | 1500ms | 2/2282 |
| ✅ | `agify_name` | 99.91% | 99.61% | 399.1 | 16112.2 | 2000ms | 9/2282 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.91% | 186.5 | 3882.8 | 2000ms | 2/2282 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `numbers_trivia` | 03:00 | 4927.1 | 48.98% |
| `numbers_trivia` | 10:00 | 4043.1 | 38.64% |
| `numbers_trivia` | 02:00 | 4003.5 | 38.1% |
| `numbers_trivia` | 14:00 | 3780.0 | 36.63% |
| `numbers_trivia` | 00:00 | 3701.8 | 35.48% |
| `numbers_trivia` | 09:00 | 3630.5 | 35.05% |
| `numbers_trivia` | 17:00 | 3595.1 | 35.9% |
| `nasa_apod` | 05:00 | 3513.1 | 50.0% |
| `numbers_trivia` | 05:00 | 3496.2 | 34.38% |
| `nasa_apod` | 03:00 | 3476.6 | 51.02% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
