# API Reliability Monitor — SLA Report

> Last updated: **2026-10-25 07:00 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **7/12** &nbsp;|&nbsp; Avg uptime: **76.4%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 73.58% | 2777.8 | 10420.1 | 1000ms | 728/2755 |
| ❌ | `public_apis_list` | 0.0% | 99.35% | 146.7 | 5075.4 | 1500ms | 18/2755 |
| ❌ | `ipapi_check` | 43.96% | 99.96% | 145.1 | 4507.0 | 2500ms | 1/2755 |
| ❌ | `nasa_apod` | 78.44% | 59.31% | 2704.6 | 11152.5 | 2000ms | 1121/2755 |
| ⚠️ | `dog_ceo_random` | 97.21% | 97.82% | 479.2 | 10509.6 | 2500ms | 60/2755 |
| ✅ | `open_meteo_weather` | 99.02% | 98.33% | 666.1 | 14877.1 | 2000ms | 46/2755 |
| ✅ | `useless_fact` | 99.09% | 99.53% | 669.7 | 10229.6 | 2500ms | 13/2755 |
| ✅ | `rest_countries` | 99.46% | 99.17% | 271.3 | 10221.5 | 2500ms | 23/2755 |
| ✅ | `coingecko_bitcoin` | 99.71% | 99.93% | 97.4 | 4328.4 | 1500ms | 2/2755 |
| ✅ | `catfact_random` | 99.82% | 99.49% | 264.5 | 10080.2 | 3000ms | 14/2755 |
| ✅ | `agify_name` | 99.93% | 99.38% | 408.9 | 16112.2 | 2000ms | 17/2755 |
| ✅ | `jsonplaceholder_posts` | 99.96% | 99.85% | 183.8 | 10927.2 | 2000ms | 4/2755 |

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
| `nasa_apod` | 12:00 | 3003.8 | 47.62% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
