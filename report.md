# API Reliability Monitor — SLA Report

> Last updated: **2026-11-01 16:55 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **7/12** &nbsp;|&nbsp; Avg uptime: **76.3%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 73.93% | 2742.8 | 10420.1 | 1000ms | 728/2792 |
| ❌ | `public_apis_list` | 0.0% | 99.36% | 146.6 | 5075.4 | 1500ms | 18/2792 |
| ❌ | `ipapi_check` | 43.45% | 99.96% | 145.0 | 4507.0 | 2500ms | 1/2792 |
| ❌ | `nasa_apod` | 77.72% | 59.13% | 2721.5 | 11152.5 | 2000ms | 1141/2792 |
| ⚠️ | `dog_ceo_random` | 97.24% | 97.82% | 481.7 | 10509.6 | 2500ms | 61/2792 |
| ✅ | `open_meteo_weather` | 99.03% | 98.35% | 662.3 | 14877.1 | 2000ms | 46/2792 |
| ✅ | `useless_fact` | 99.07% | 99.53% | 670.3 | 10229.6 | 2500ms | 13/2792 |
| ✅ | `rest_countries` | 99.46% | 99.18% | 271.2 | 10221.5 | 2500ms | 23/2792 |
| ✅ | `coingecko_bitcoin` | 99.71% | 99.93% | 97.2 | 4328.4 | 1500ms | 2/2792 |
| ✅ | `catfact_random` | 99.82% | 99.5% | 266.2 | 10080.2 | 3000ms | 14/2792 |
| ✅ | `agify_name` | 99.93% | 99.39% | 408.3 | 16112.2 | 2000ms | 17/2792 |
| ✅ | `jsonplaceholder_posts` | 99.96% | 99.86% | 183.2 | 10927.2 | 2000ms | 4/2792 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `numbers_trivia` | 03:00 | 4406.0 | 43.64% |
| `numbers_trivia` | 10:00 | 3294.8 | 31.19% |
| `nasa_apod` | 11:00 | 3200.7 | 43.88% |
| `nasa_apod` | 03:00 | 3157.3 | 45.45% |
| `nasa_apod` | 09:00 | 3117.8 | 44.17% |
| `nasa_apod` | 02:00 | 3117.3 | 41.94% |
| `nasa_apod` | 17:00 | 3102.3 | 39.16% |
| `numbers_trivia` | 14:00 | 3058.4 | 29.37% |
| `nasa_apod` | 18:00 | 3047.8 | 43.57% |
| `nasa_apod` | 05:00 | 3012.8 | 44.09% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
