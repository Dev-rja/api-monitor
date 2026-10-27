# API Reliability Monitor — SLA Report

> Last updated: **2026-10-27 05:41 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **7/12** &nbsp;|&nbsp; Avg uptime: **76.4%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 73.68% | 2767.3 | 10420.1 | 1000ms | 728/2766 |
| ❌ | `public_apis_list` | 0.0% | 99.35% | 146.8 | 5075.4 | 1500ms | 18/2766 |
| ❌ | `ipapi_check` | 43.82% | 99.96% | 145.0 | 4507.0 | 2500ms | 1/2766 |
| ❌ | `nasa_apod` | 78.2% | 59.26% | 2710.0 | 11152.5 | 2000ms | 1127/2766 |
| ⚠️ | `dog_ceo_random` | 97.22% | 97.83% | 478.9 | 10509.6 | 2500ms | 60/2766 |
| ✅ | `open_meteo_weather` | 99.02% | 98.34% | 665.2 | 14877.1 | 2000ms | 46/2766 |
| ✅ | `useless_fact` | 99.06% | 99.53% | 669.6 | 10229.6 | 2500ms | 13/2766 |
| ✅ | `rest_countries` | 99.46% | 99.17% | 271.1 | 10221.5 | 2500ms | 23/2766 |
| ✅ | `coingecko_bitcoin` | 99.71% | 99.93% | 97.4 | 4328.4 | 1500ms | 2/2766 |
| ✅ | `catfact_random` | 99.82% | 99.49% | 265.2 | 10080.2 | 3000ms | 14/2766 |
| ✅ | `agify_name` | 99.93% | 99.39% | 408.7 | 16112.2 | 2000ms | 17/2766 |
| ✅ | `jsonplaceholder_posts` | 99.96% | 99.86% | 183.5 | 10927.2 | 2000ms | 4/2766 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `numbers_trivia` | 03:00 | 4483.7 | 44.44% |
| `numbers_trivia` | 10:00 | 3324.8 | 31.48% |
| `nasa_apod` | 03:00 | 3208.5 | 46.3% |
| `nasa_apod` | 09:00 | 3117.8 | 44.17% |
| `nasa_apod` | 02:00 | 3117.3 | 41.94% |
| `nasa_apod` | 11:00 | 3097.2 | 43.07% |
| `nasa_apod` | 17:00 | 3069.3 | 39.01% |
| `nasa_apod` | 05:00 | 3064.5 | 45.05% |
| `numbers_trivia` | 14:00 | 3058.4 | 29.37% |
| `numbers_trivia` | 11:00 | 3000.2 | 28.26% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
