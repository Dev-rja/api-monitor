# API Reliability Monitor — SLA Report

> Last updated: **2026-08-19 10:37 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **77.4%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 66.45% | 3485.0 | 10420.1 | 1000ms | 713/2125 |
| ❌ | `public_apis_list` | 0.0% | 99.53% | 137.0 | 5075.4 | 1500ms | 10/2125 |
| ❌ | `ipapi_check` | 55.95% | 99.95% | 145.2 | 4507.0 | 2500ms | 1/2125 |
| ❌ | `nasa_apod` | 78.64% | 55.11% | 2936.2 | 11152.5 | 2000ms | 954/2125 |
| ⚠️ | `dog_ceo_random` | 96.42% | 97.27% | 499.5 | 10244.1 | 2500ms | 58/2125 |
| ⚠️ | `open_meteo_weather` | 98.96% | 97.98% | 686.3 | 14877.1 | 2000ms | 43/2125 |
| ✅ | `rest_countries` | 99.29% | 99.01% | 275.7 | 10221.5 | 2500ms | 21/2125 |
| ✅ | `useless_fact` | 99.76% | 99.67% | 651.5 | 10229.6 | 2500ms | 7/2125 |
| ✅ | `catfact_random` | 99.76% | 99.39% | 265.4 | 10080.2 | 3000ms | 13/2125 |
| ✅ | `coingecko_bitcoin` | 99.81% | 99.91% | 96.6 | 4328.4 | 1500ms | 2/2125 |
| ✅ | `agify_name` | 99.91% | 99.72% | 394.3 | 16112.2 | 2000ms | 6/2125 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.91% | 189.4 | 3882.8 | 2000ms | 2/2125 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `numbers_trivia` | 03:00 | 5018.2 | 50.0% |
| `numbers_trivia` | 10:00 | 4379.1 | 41.98% |
| `numbers_trivia` | 02:00 | 4334.9 | 41.18% |
| `numbers_trivia` | 14:00 | 4048.7 | 39.36% |
| `numbers_trivia` | 05:00 | 3912.1 | 38.6% |
| `nasa_apod` | 05:00 | 3869.5 | 56.14% |
| `numbers_trivia` | 09:00 | 3820.6 | 36.96% |
| `numbers_trivia` | 00:00 | 3712.5 | 35.59% |
| `numbers_trivia` | 17:00 | 3665.8 | 36.7% |
| `numbers_trivia` | 07:00 | 3634.1 | 34.38% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
