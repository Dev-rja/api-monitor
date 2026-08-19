# API Reliability Monitor — SLA Report

> Last updated: **2026-08-19 19:44 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **77.4%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 66.32% | 3497.1 | 10420.1 | 1000ms | 721/2141 |
| ❌ | `public_apis_list` | 0.0% | 99.53% | 137.0 | 5075.4 | 1500ms | 10/2141 |
| ❌ | `ipapi_check` | 55.53% | 99.95% | 145.0 | 4507.0 | 2500ms | 1/2141 |
| ❌ | `nasa_apod` | 78.79% | 55.39% | 2918.0 | 11152.5 | 2000ms | 955/2141 |
| ⚠️ | `dog_ceo_random` | 96.45% | 97.29% | 498.3 | 10244.1 | 2500ms | 58/2141 |
| ⚠️ | `open_meteo_weather` | 98.97% | 97.99% | 686.2 | 14877.1 | 2000ms | 43/2141 |
| ✅ | `rest_countries` | 99.3% | 99.02% | 275.1 | 10221.5 | 2500ms | 21/2141 |
| ✅ | `useless_fact` | 99.77% | 99.67% | 652.0 | 10229.6 | 2500ms | 7/2141 |
| ✅ | `catfact_random` | 99.77% | 99.39% | 265.0 | 10080.2 | 3000ms | 13/2141 |
| ✅ | `coingecko_bitcoin` | 99.81% | 99.91% | 96.6 | 4328.4 | 1500ms | 2/2141 |
| ✅ | `agify_name` | 99.91% | 99.72% | 394.6 | 16112.2 | 2000ms | 6/2141 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.91% | 189.0 | 3882.8 | 2000ms | 2/2141 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `numbers_trivia` | 03:00 | 5018.2 | 50.0% |
| `numbers_trivia` | 10:00 | 4379.1 | 41.98% |
| `numbers_trivia` | 02:00 | 4334.9 | 41.18% |
| `numbers_trivia` | 14:00 | 4007.5 | 38.95% |
| `numbers_trivia` | 05:00 | 3912.1 | 38.6% |
| `nasa_apod` | 05:00 | 3869.5 | 56.14% |
| `numbers_trivia` | 09:00 | 3820.6 | 36.96% |
| `numbers_trivia` | 17:00 | 3781.4 | 37.84% |
| `numbers_trivia` | 00:00 | 3712.5 | 35.59% |
| `numbers_trivia` | 07:00 | 3634.1 | 34.38% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
