# API Reliability Monitor — SLA Report

> Last updated: **2026-08-19 23:51 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **77.3%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 66.33% | 3497.2 | 10420.1 | 1000ms | 724/2150 |
| ❌ | `public_apis_list` | 0.0% | 99.53% | 137.1 | 5075.4 | 1500ms | 10/2150 |
| ❌ | `ipapi_check` | 55.3% | 99.95% | 144.9 | 4507.0 | 2500ms | 1/2150 |
| ❌ | `nasa_apod` | 78.88% | 55.53% | 2908.4 | 11152.5 | 2000ms | 956/2150 |
| ⚠️ | `dog_ceo_random` | 96.47% | 97.3% | 497.6 | 10244.1 | 2500ms | 58/2150 |
| ⚠️ | `open_meteo_weather` | 98.98% | 98.0% | 685.6 | 14877.1 | 2000ms | 43/2150 |
| ✅ | `rest_countries` | 99.3% | 99.02% | 274.6 | 10221.5 | 2500ms | 21/2150 |
| ✅ | `useless_fact` | 99.77% | 99.67% | 652.0 | 10229.6 | 2500ms | 7/2150 |
| ✅ | `catfact_random` | 99.77% | 99.4% | 264.6 | 10080.2 | 3000ms | 13/2150 |
| ✅ | `coingecko_bitcoin` | 99.81% | 99.91% | 96.5 | 4328.4 | 1500ms | 2/2150 |
| ✅ | `agify_name` | 99.91% | 99.72% | 394.7 | 16112.2 | 2000ms | 6/2150 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.91% | 188.8 | 3882.8 | 2000ms | 2/2150 |

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
