# API Reliability Monitor — SLA Report

> Last updated: **2026-08-20 10:03 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **77.3%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 66.34% | 3495.3 | 10420.1 | 1000ms | 728/2163 |
| ❌ | `public_apis_list` | 0.0% | 99.54% | 137.1 | 5075.4 | 1500ms | 10/2163 |
| ❌ | `ipapi_check` | 54.97% | 99.95% | 145.1 | 4507.0 | 2500ms | 1/2163 |
| ❌ | `nasa_apod` | 79.01% | 55.71% | 2895.9 | 11152.5 | 2000ms | 958/2163 |
| ⚠️ | `dog_ceo_random` | 96.49% | 97.32% | 496.3 | 10244.1 | 2500ms | 58/2163 |
| ⚠️ | `open_meteo_weather` | 98.98% | 98.01% | 684.8 | 14877.1 | 2000ms | 43/2163 |
| ✅ | `rest_countries` | 99.31% | 99.03% | 274.0 | 10221.5 | 2500ms | 21/2163 |
| ✅ | `useless_fact` | 99.77% | 99.68% | 652.0 | 10229.6 | 2500ms | 7/2163 |
| ✅ | `catfact_random` | 99.77% | 99.4% | 264.0 | 10080.2 | 3000ms | 13/2163 |
| ✅ | `coingecko_bitcoin` | 99.82% | 99.91% | 96.3 | 4328.4 | 1500ms | 2/2163 |
| ✅ | `agify_name` | 99.91% | 99.72% | 394.6 | 16112.2 | 2000ms | 6/2163 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.91% | 188.4 | 3882.8 | 2000ms | 2/2163 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `numbers_trivia` | 03:00 | 5237.4 | 52.17% |
| `numbers_trivia` | 02:00 | 4653.3 | 44.44% |
| `numbers_trivia` | 10:00 | 4327.2 | 41.46% |
| `numbers_trivia` | 14:00 | 4007.5 | 38.95% |
| `numbers_trivia` | 00:00 | 3818.8 | 36.67% |
| `numbers_trivia` | 05:00 | 3783.9 | 37.29% |
| `numbers_trivia` | 17:00 | 3781.4 | 37.84% |
| `numbers_trivia` | 09:00 | 3780.7 | 36.56% |
| `nasa_apod` | 05:00 | 3759.6 | 54.24% |
| `nasa_apod` | 09:00 | 3582.8 | 50.0% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
