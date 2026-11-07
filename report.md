# API Reliability Monitor — SLA Report

> Last updated: **2026-11-07 07:13 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **7/12** &nbsp;|&nbsp; Avg uptime: **76.2%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 74.13% | 2722.7 | 10420.1 | 1000ms | 728/2814 |
| ❌ | `public_apis_list` | 0.0% | 99.36% | 146.5 | 5075.4 | 1500ms | 18/2814 |
| ❌ | `ipapi_check` | 43.14% | 99.96% | 144.8 | 4507.0 | 2500ms | 1/2814 |
| ❌ | `nasa_apod` | 77.58% | 59.2% | 2719.8 | 11152.5 | 2000ms | 1148/2814 |
| ⚠️ | `dog_ceo_random` | 97.26% | 97.83% | 481.5 | 10509.6 | 2500ms | 61/2814 |
| ✅ | `useless_fact` | 99.0% | 99.54% | 670.3 | 10229.6 | 2500ms | 13/2814 |
| ✅ | `open_meteo_weather` | 99.04% | 98.37% | 660.5 | 14877.1 | 2000ms | 46/2814 |
| ✅ | `rest_countries` | 99.47% | 99.18% | 271.0 | 10221.5 | 2500ms | 23/2814 |
| ✅ | `coingecko_bitcoin` | 99.72% | 99.93% | 97.2 | 4328.4 | 1500ms | 2/2814 |
| ✅ | `catfact_random` | 99.82% | 99.5% | 266.7 | 10080.2 | 3000ms | 14/2814 |
| ✅ | `agify_name` | 99.93% | 99.4% | 408.2 | 16112.2 | 2000ms | 17/2814 |
| ✅ | `jsonplaceholder_posts` | 99.96% | 99.86% | 182.7 | 10927.2 | 2000ms | 4/2814 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `numbers_trivia` | 03:00 | 4406.0 | 43.64% |
| `numbers_trivia` | 10:00 | 3294.8 | 31.19% |
| `nasa_apod` | 11:00 | 3190.0 | 43.57% |
| `nasa_apod` | 03:00 | 3157.3 | 45.45% |
| `nasa_apod` | 09:00 | 3117.8 | 44.17% |
| `nasa_apod` | 02:00 | 3117.3 | 41.94% |
| `nasa_apod` | 17:00 | 3102.3 | 39.16% |
| `nasa_apod` | 18:00 | 3063.8 | 43.97% |
| `numbers_trivia` | 14:00 | 3058.4 | 29.37% |
| `nasa_apod` | 05:00 | 3012.8 | 44.09% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
