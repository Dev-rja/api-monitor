# API Reliability Monitor — SLA Report

> Last updated: **2026-08-20 05:51 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **77.3%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 66.25% | 3504.7 | 10420.1 | 1000ms | 728/2157 |
| ❌ | `public_apis_list` | 0.0% | 99.54% | 137.1 | 5075.4 | 1500ms | 10/2157 |
| ❌ | `ipapi_check` | 55.12% | 99.95% | 145.1 | 4507.0 | 2500ms | 1/2157 |
| ❌ | `nasa_apod` | 78.95% | 55.63% | 2901.8 | 11152.5 | 2000ms | 957/2157 |
| ⚠️ | `dog_ceo_random` | 96.48% | 97.31% | 496.9 | 10244.1 | 2500ms | 58/2157 |
| ⚠️ | `open_meteo_weather` | 98.98% | 98.01% | 685.1 | 14877.1 | 2000ms | 43/2157 |
| ✅ | `rest_countries` | 99.3% | 99.03% | 274.3 | 10221.5 | 2500ms | 21/2157 |
| ✅ | `useless_fact` | 99.77% | 99.68% | 651.9 | 10229.6 | 2500ms | 7/2157 |
| ✅ | `catfact_random` | 99.77% | 99.4% | 264.1 | 10080.2 | 3000ms | 13/2157 |
| ✅ | `coingecko_bitcoin` | 99.81% | 99.91% | 96.4 | 4328.4 | 1500ms | 2/2157 |
| ✅ | `agify_name` | 99.91% | 99.72% | 394.8 | 16112.2 | 2000ms | 6/2157 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.91% | 188.6 | 3882.8 | 2000ms | 2/2157 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `numbers_trivia` | 03:00 | 5237.4 | 52.17% |
| `numbers_trivia` | 02:00 | 4653.3 | 44.44% |
| `numbers_trivia` | 10:00 | 4379.1 | 41.98% |
| `numbers_trivia` | 14:00 | 4007.5 | 38.95% |
| `numbers_trivia` | 09:00 | 3820.6 | 36.96% |
| `numbers_trivia` | 00:00 | 3818.8 | 36.67% |
| `numbers_trivia` | 05:00 | 3783.9 | 37.29% |
| `numbers_trivia` | 17:00 | 3781.4 | 37.84% |
| `nasa_apod` | 05:00 | 3759.6 | 54.24% |
| `numbers_trivia` | 07:00 | 3634.1 | 34.38% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
