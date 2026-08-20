# API Reliability Monitor — SLA Report

> Last updated: **2026-08-20 02:07 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **77.3%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 66.26% | 3503.3 | 10420.1 | 1000ms | 726/2152 |
| ❌ | `public_apis_list` | 0.0% | 99.54% | 137.1 | 5075.4 | 1500ms | 10/2152 |
| ❌ | `ipapi_check` | 55.25% | 99.95% | 144.9 | 4507.0 | 2500ms | 1/2152 |
| ❌ | `nasa_apod` | 78.9% | 55.58% | 2906.1 | 11152.5 | 2000ms | 956/2152 |
| ⚠️ | `dog_ceo_random` | 96.47% | 97.3% | 497.5 | 10244.1 | 2500ms | 58/2152 |
| ⚠️ | `open_meteo_weather` | 98.98% | 98.0% | 685.5 | 14877.1 | 2000ms | 43/2152 |
| ✅ | `rest_countries` | 99.3% | 99.02% | 274.5 | 10221.5 | 2500ms | 21/2152 |
| ✅ | `useless_fact` | 99.77% | 99.67% | 652.0 | 10229.6 | 2500ms | 7/2152 |
| ✅ | `catfact_random` | 99.77% | 99.4% | 264.5 | 10080.2 | 3000ms | 13/2152 |
| ✅ | `coingecko_bitcoin` | 99.81% | 99.91% | 96.5 | 4328.4 | 1500ms | 2/2152 |
| ✅ | `agify_name` | 99.91% | 99.72% | 394.9 | 16112.2 | 2000ms | 6/2152 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.91% | 188.7 | 3882.8 | 2000ms | 2/2152 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `numbers_trivia` | 03:00 | 5018.2 | 50.0% |
| `numbers_trivia` | 02:00 | 4653.3 | 44.44% |
| `numbers_trivia` | 10:00 | 4379.1 | 41.98% |
| `numbers_trivia` | 14:00 | 4007.5 | 38.95% |
| `numbers_trivia` | 05:00 | 3912.1 | 38.6% |
| `nasa_apod` | 05:00 | 3869.5 | 56.14% |
| `numbers_trivia` | 09:00 | 3820.6 | 36.96% |
| `numbers_trivia` | 00:00 | 3818.8 | 36.67% |
| `numbers_trivia` | 17:00 | 3781.4 | 37.84% |
| `numbers_trivia` | 07:00 | 3634.1 | 34.38% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
