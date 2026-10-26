# API Reliability Monitor — SLA Report

> Last updated: **2026-10-26 04:33 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **7/12** &nbsp;|&nbsp; Avg uptime: **76.4%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 73.63% | 2772.1 | 10420.1 | 1000ms | 728/2761 |
| ❌ | `public_apis_list` | 0.0% | 99.35% | 146.7 | 5075.4 | 1500ms | 18/2761 |
| ❌ | `ipapi_check` | 43.86% | 99.96% | 145.0 | 4507.0 | 2500ms | 1/2761 |
| ❌ | `nasa_apod` | 78.3% | 59.33% | 2702.7 | 11152.5 | 2000ms | 1123/2761 |
| ⚠️ | `dog_ceo_random` | 97.21% | 97.83% | 479.1 | 10509.6 | 2500ms | 60/2761 |
| ✅ | `open_meteo_weather` | 99.02% | 98.33% | 665.7 | 14877.1 | 2000ms | 46/2761 |
| ✅ | `useless_fact` | 99.09% | 99.53% | 669.6 | 10229.6 | 2500ms | 13/2761 |
| ✅ | `rest_countries` | 99.46% | 99.17% | 271.1 | 10221.5 | 2500ms | 23/2761 |
| ✅ | `coingecko_bitcoin` | 99.71% | 99.93% | 97.4 | 4328.4 | 1500ms | 2/2761 |
| ✅ | `catfact_random` | 99.82% | 99.49% | 265.4 | 10080.2 | 3000ms | 14/2761 |
| ✅ | `agify_name` | 99.93% | 99.38% | 408.7 | 16112.2 | 2000ms | 17/2761 |
| ✅ | `jsonplaceholder_posts` | 99.96% | 99.86% | 183.6 | 10927.2 | 2000ms | 4/2761 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `numbers_trivia` | 03:00 | 4483.7 | 44.44% |
| `numbers_trivia` | 10:00 | 3353.8 | 31.78% |
| `nasa_apod` | 03:00 | 3208.5 | 46.3% |
| `nasa_apod` | 09:00 | 3117.8 | 44.17% |
| `nasa_apod` | 02:00 | 3117.3 | 41.94% |
| `nasa_apod` | 11:00 | 3097.2 | 43.07% |
| `nasa_apod` | 05:00 | 3090.2 | 45.56% |
| `nasa_apod` | 17:00 | 3069.3 | 39.01% |
| `numbers_trivia` | 14:00 | 3058.4 | 29.37% |
| `numbers_trivia` | 11:00 | 3000.2 | 28.26% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
