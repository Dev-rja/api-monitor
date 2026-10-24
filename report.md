# API Reliability Monitor — SLA Report

> Last updated: **2026-10-24 09:50 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **7/12** &nbsp;|&nbsp; Avg uptime: **76.4%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 73.51% | 2784.5 | 10420.1 | 1000ms | 728/2748 |
| ❌ | `public_apis_list` | 0.0% | 99.34% | 146.8 | 5075.4 | 1500ms | 18/2748 |
| ❌ | `ipapi_check` | 44.07% | 99.96% | 145.1 | 4507.0 | 2500ms | 1/2748 |
| ❌ | `nasa_apod` | 78.64% | 59.28% | 2705.5 | 11152.5 | 2000ms | 1119/2748 |
| ⚠️ | `dog_ceo_random` | 97.2% | 97.82% | 479.5 | 10509.6 | 2500ms | 60/2748 |
| ✅ | `open_meteo_weather` | 99.02% | 98.33% | 666.8 | 14877.1 | 2000ms | 46/2748 |
| ✅ | `useless_fact` | 99.09% | 99.53% | 669.7 | 10229.6 | 2500ms | 13/2748 |
| ✅ | `rest_countries` | 99.45% | 99.16% | 271.5 | 10221.5 | 2500ms | 23/2748 |
| ✅ | `coingecko_bitcoin` | 99.71% | 99.93% | 97.4 | 4328.4 | 1500ms | 2/2748 |
| ✅ | `catfact_random` | 99.82% | 99.49% | 264.5 | 10080.2 | 3000ms | 14/2748 |
| ✅ | `agify_name` | 99.93% | 99.38% | 409.0 | 16112.2 | 2000ms | 17/2748 |
| ✅ | `jsonplaceholder_posts` | 99.96% | 99.85% | 184.0 | 10927.2 | 2000ms | 4/2748 |

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
| `nasa_apod` | 17:00 | 3071.4 | 38.57% |
| `numbers_trivia` | 14:00 | 3058.4 | 29.37% |
| `numbers_trivia` | 17:00 | 3009.8 | 29.79% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
