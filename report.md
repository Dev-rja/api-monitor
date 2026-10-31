# API Reliability Monitor — SLA Report

> Last updated: **2026-10-31 13:23 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **7/12** &nbsp;|&nbsp; Avg uptime: **76.3%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 73.87% | 2748.4 | 10420.1 | 1000ms | 728/2786 |
| ❌ | `public_apis_list` | 0.0% | 99.35% | 146.5 | 5075.4 | 1500ms | 18/2786 |
| ❌ | `ipapi_check` | 43.54% | 99.96% | 145.1 | 4507.0 | 2500ms | 1/2786 |
| ❌ | `nasa_apod` | 77.82% | 59.12% | 2723.4 | 11152.5 | 2000ms | 1139/2786 |
| ⚠️ | `dog_ceo_random` | 97.24% | 97.81% | 481.9 | 10509.6 | 2500ms | 61/2786 |
| ✅ | `open_meteo_weather` | 99.03% | 98.35% | 662.7 | 14877.1 | 2000ms | 46/2786 |
| ✅ | `useless_fact` | 99.07% | 99.53% | 670.1 | 10229.6 | 2500ms | 13/2786 |
| ✅ | `rest_countries` | 99.46% | 99.17% | 271.3 | 10221.5 | 2500ms | 23/2786 |
| ✅ | `coingecko_bitcoin` | 99.71% | 99.93% | 97.3 | 4328.4 | 1500ms | 2/2786 |
| ✅ | `catfact_random` | 99.82% | 99.5% | 266.2 | 10080.2 | 3000ms | 14/2786 |
| ✅ | `agify_name` | 99.93% | 99.39% | 408.1 | 16112.2 | 2000ms | 17/2786 |
| ✅ | `jsonplaceholder_posts` | 99.96% | 99.86% | 183.4 | 10927.2 | 2000ms | 4/2786 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `numbers_trivia` | 03:00 | 4483.7 | 44.44% |
| `numbers_trivia` | 10:00 | 3324.8 | 31.48% |
| `nasa_apod` | 03:00 | 3208.5 | 46.3% |
| `nasa_apod` | 11:00 | 3200.7 | 43.88% |
| `nasa_apod` | 17:00 | 3120.8 | 39.44% |
| `nasa_apod` | 09:00 | 3117.8 | 44.17% |
| `nasa_apod` | 02:00 | 3117.3 | 41.94% |
| `numbers_trivia` | 14:00 | 3058.4 | 29.37% |
| `nasa_apod` | 18:00 | 3047.8 | 43.57% |
| `nasa_apod` | 05:00 | 3012.8 | 44.09% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
