# API Reliability Monitor — SLA Report

> Last updated: **2026-11-02 00:34 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **7/12** &nbsp;|&nbsp; Avg uptime: **76.3%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 73.94% | 2741.0 | 10420.1 | 1000ms | 728/2794 |
| ❌ | `public_apis_list` | 0.0% | 99.36% | 146.6 | 5075.4 | 1500ms | 18/2794 |
| ❌ | `ipapi_check` | 43.41% | 99.96% | 145.0 | 4507.0 | 2500ms | 1/2794 |
| ❌ | `nasa_apod` | 77.67% | 59.09% | 2726.9 | 11152.5 | 2000ms | 1143/2794 |
| ⚠️ | `dog_ceo_random` | 97.24% | 97.82% | 481.6 | 10509.6 | 2500ms | 61/2794 |
| ✅ | `useless_fact` | 99.0% | 99.53% | 670.3 | 10229.6 | 2500ms | 13/2794 |
| ✅ | `open_meteo_weather` | 99.03% | 98.35% | 662.3 | 14877.1 | 2000ms | 46/2794 |
| ✅ | `rest_countries` | 99.46% | 99.18% | 271.1 | 10221.5 | 2500ms | 23/2794 |
| ✅ | `coingecko_bitcoin` | 99.71% | 99.93% | 97.3 | 4328.4 | 1500ms | 2/2794 |
| ✅ | `catfact_random` | 99.82% | 99.5% | 266.2 | 10080.2 | 3000ms | 14/2794 |
| ✅ | `agify_name` | 99.93% | 99.39% | 408.1 | 16112.2 | 2000ms | 17/2794 |
| ✅ | `jsonplaceholder_posts` | 99.96% | 99.86% | 183.1 | 10927.2 | 2000ms | 4/2794 |

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
