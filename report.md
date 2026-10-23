# API Reliability Monitor — SLA Report

> Last updated: **2026-10-23 19:34 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **7/12** &nbsp;|&nbsp; Avg uptime: **76.4%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 73.47% | 2788.4 | 10420.1 | 1000ms | 728/2744 |
| ❌ | `public_apis_list` | 0.0% | 99.34% | 146.8 | 5075.4 | 1500ms | 18/2744 |
| ❌ | `ipapi_check` | 44.1% | 99.96% | 145.2 | 4507.0 | 2500ms | 1/2744 |
| ❌ | `nasa_apod` | 78.68% | 59.22% | 2708.6 | 11152.5 | 2000ms | 1119/2744 |
| ⚠️ | `dog_ceo_random` | 97.19% | 97.81% | 479.7 | 10509.6 | 2500ms | 60/2744 |
| ✅ | `open_meteo_weather` | 99.02% | 98.32% | 667.1 | 14877.1 | 2000ms | 46/2744 |
| ✅ | `useless_fact` | 99.09% | 99.53% | 669.8 | 10229.6 | 2500ms | 13/2744 |
| ✅ | `rest_countries` | 99.45% | 99.16% | 271.6 | 10221.5 | 2500ms | 23/2744 |
| ✅ | `coingecko_bitcoin` | 99.71% | 99.93% | 97.4 | 4328.4 | 1500ms | 2/2744 |
| ✅ | `catfact_random` | 99.82% | 99.49% | 264.6 | 10080.2 | 3000ms | 14/2744 |
| ✅ | `agify_name` | 99.93% | 99.38% | 409.2 | 16112.2 | 2000ms | 17/2744 |
| ✅ | `jsonplaceholder_posts` | 99.96% | 99.85% | 184.1 | 10927.2 | 2000ms | 4/2744 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `numbers_trivia` | 03:00 | 4483.7 | 44.44% |
| `numbers_trivia` | 10:00 | 3353.8 | 31.78% |
| `nasa_apod` | 03:00 | 3208.5 | 46.3% |
| `nasa_apod` | 09:00 | 3139.6 | 44.54% |
| `nasa_apod` | 05:00 | 3119.5 | 46.07% |
| `nasa_apod` | 02:00 | 3117.3 | 41.94% |
| `nasa_apod` | 11:00 | 3097.2 | 43.07% |
| `nasa_apod` | 17:00 | 3071.4 | 38.57% |
| `numbers_trivia` | 14:00 | 3058.4 | 29.37% |
| `numbers_trivia` | 17:00 | 3009.8 | 29.79% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
