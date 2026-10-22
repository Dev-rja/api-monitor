# API Reliability Monitor — SLA Report

> Last updated: **2026-10-22 22:39 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **7/12** &nbsp;|&nbsp; Avg uptime: **76.4%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 73.42% | 2793.2 | 10420.1 | 1000ms | 728/2739 |
| ❌ | `public_apis_list` | 0.0% | 99.34% | 146.8 | 5075.4 | 1500ms | 18/2739 |
| ❌ | `ipapi_check` | 44.18% | 99.96% | 145.1 | 4507.0 | 2500ms | 1/2739 |
| ❌ | `nasa_apod` | 78.79% | 59.26% | 2707.5 | 11152.5 | 2000ms | 1116/2739 |
| ⚠️ | `dog_ceo_random` | 97.19% | 97.81% | 479.7 | 10509.6 | 2500ms | 60/2739 |
| ✅ | `open_meteo_weather` | 99.01% | 98.32% | 667.3 | 14877.1 | 2000ms | 46/2739 |
| ✅ | `useless_fact` | 99.09% | 99.53% | 669.8 | 10229.6 | 2500ms | 13/2739 |
| ✅ | `rest_countries` | 99.45% | 99.16% | 271.6 | 10221.5 | 2500ms | 23/2739 |
| ✅ | `coingecko_bitcoin` | 99.71% | 99.93% | 97.4 | 4328.4 | 1500ms | 2/2739 |
| ✅ | `catfact_random` | 99.82% | 99.49% | 264.5 | 10080.2 | 3000ms | 14/2739 |
| ✅ | `agify_name` | 99.93% | 99.38% | 409.2 | 16112.2 | 2000ms | 17/2739 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.89% | 180.3 | 3882.8 | 2000ms | 3/2739 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `numbers_trivia` | 03:00 | 4483.7 | 44.44% |
| `numbers_trivia` | 10:00 | 3353.8 | 31.78% |
| `nasa_apod` | 03:00 | 3208.5 | 46.3% |
| `nasa_apod` | 09:00 | 3139.6 | 44.54% |
| `nasa_apod` | 02:00 | 3117.3 | 41.94% |
| `nasa_apod` | 11:00 | 3115.1 | 43.38% |
| `nasa_apod` | 17:00 | 3071.4 | 38.57% |
| `numbers_trivia` | 14:00 | 3058.4 | 29.37% |
| `nasa_apod` | 05:00 | 3038.4 | 45.45% |
| `numbers_trivia` | 11:00 | 3021.4 | 28.47% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
