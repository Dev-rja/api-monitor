# API Reliability Monitor — SLA Report

> Last updated: **2026-11-13 10:24 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **7/12** &nbsp;|&nbsp; Avg uptime: **76.2%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 74.35% | 2700.9 | 10420.1 | 1000ms | 728/2838 |
| ❌ | `public_apis_list` | 0.0% | 99.37% | 146.1 | 5075.4 | 1500ms | 18/2838 |
| ❌ | `ipapi_check` | 42.85% | 99.96% | 145.1 | 4507.0 | 2500ms | 1/2838 |
| ❌ | `nasa_apod` | 77.2% | 59.16% | 2716.7 | 11152.5 | 2000ms | 1159/2838 |
| ⚠️ | `dog_ceo_random` | 97.29% | 97.85% | 480.8 | 10509.6 | 2500ms | 61/2838 |
| ✅ | `useless_fact` | 99.01% | 99.54% | 670.2 | 10229.6 | 2500ms | 13/2838 |
| ✅ | `open_meteo_weather` | 99.05% | 98.38% | 658.5 | 14877.1 | 2000ms | 46/2838 |
| ✅ | `rest_countries` | 99.47% | 99.19% | 270.5 | 10221.5 | 2500ms | 23/2838 |
| ✅ | `coingecko_bitcoin` | 99.72% | 99.93% | 97.2 | 4328.4 | 1500ms | 2/2838 |
| ✅ | `catfact_random` | 99.82% | 99.51% | 266.7 | 10080.2 | 3000ms | 14/2838 |
| ✅ | `agify_name` | 99.93% | 99.4% | 408.0 | 16112.2 | 2000ms | 17/2838 |
| ✅ | `jsonplaceholder_posts` | 99.96% | 99.86% | 182.0 | 10927.2 | 2000ms | 4/2838 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `numbers_trivia` | 03:00 | 4258.9 | 42.11% |
| `nasa_apod` | 11:00 | 3217.2 | 43.97% |
| `numbers_trivia` | 10:00 | 3209.8 | 30.36% |
| `nasa_apod` | 09:00 | 3117.8 | 44.17% |
| `nasa_apod` | 17:00 | 3102.3 | 39.16% |
| `nasa_apod` | 03:00 | 3074.7 | 43.86% |
| `nasa_apod` | 18:00 | 3039.7 | 44.44% |
| `numbers_trivia` | 14:00 | 3013.2 | 28.91% |
| `nasa_apod` | 05:00 | 3012.8 | 44.09% |
| `nasa_apod` | 02:00 | 2959.5 | 39.39% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
