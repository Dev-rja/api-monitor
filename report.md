# API Reliability Monitor — SLA Report

> Last updated: **2026-08-20 07:25 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **77.3%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 66.28% | 3501.5 | 10420.1 | 1000ms | 728/2159 |
| ❌ | `public_apis_list` | 0.0% | 99.54% | 137.1 | 5075.4 | 1500ms | 10/2159 |
| ❌ | `ipapi_check` | 55.07% | 99.95% | 145.1 | 4507.0 | 2500ms | 1/2159 |
| ❌ | `nasa_apod` | 78.97% | 55.67% | 2899.6 | 11152.5 | 2000ms | 957/2159 |
| ⚠️ | `dog_ceo_random` | 96.48% | 97.31% | 496.6 | 10244.1 | 2500ms | 58/2159 |
| ⚠️ | `open_meteo_weather` | 98.98% | 98.01% | 684.9 | 14877.1 | 2000ms | 43/2159 |
| ✅ | `rest_countries` | 99.31% | 99.03% | 274.2 | 10221.5 | 2500ms | 21/2159 |
| ✅ | `useless_fact` | 99.77% | 99.68% | 651.9 | 10229.6 | 2500ms | 7/2159 |
| ✅ | `catfact_random` | 99.77% | 99.4% | 264.1 | 10080.2 | 3000ms | 13/2159 |
| ✅ | `coingecko_bitcoin` | 99.81% | 99.91% | 96.4 | 4328.4 | 1500ms | 2/2159 |
| ✅ | `agify_name` | 99.91% | 99.72% | 394.6 | 16112.2 | 2000ms | 6/2159 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.91% | 188.5 | 3882.8 | 2000ms | 2/2159 |

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
| `nasa_apod` | 09:00 | 3620.0 | 50.55% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
