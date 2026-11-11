# API Reliability Monitor — SLA Report

> Last updated: **2026-11-11 18:33 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **7/12** &nbsp;|&nbsp; Avg uptime: **76.2%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 74.29% | 2706.5 | 10420.1 | 1000ms | 728/2832 |
| ❌ | `public_apis_list` | 0.0% | 99.36% | 146.3 | 5075.4 | 1500ms | 18/2832 |
| ❌ | `ipapi_check` | 42.94% | 99.96% | 145.1 | 4507.0 | 2500ms | 1/2832 |
| ❌ | `nasa_apod` | 77.26% | 59.11% | 2717.9 | 11152.5 | 2000ms | 1158/2832 |
| ⚠️ | `dog_ceo_random` | 97.28% | 97.85% | 481.2 | 10509.6 | 2500ms | 61/2832 |
| ✅ | `useless_fact` | 99.01% | 99.54% | 670.3 | 10229.6 | 2500ms | 13/2832 |
| ✅ | `open_meteo_weather` | 99.05% | 98.38% | 659.3 | 14877.1 | 2000ms | 46/2832 |
| ✅ | `rest_countries` | 99.47% | 99.19% | 270.7 | 10221.5 | 2500ms | 23/2832 |
| ✅ | `coingecko_bitcoin` | 99.72% | 99.93% | 97.2 | 4328.4 | 1500ms | 2/2832 |
| ✅ | `catfact_random` | 99.82% | 99.51% | 266.8 | 10080.2 | 3000ms | 14/2832 |
| ✅ | `agify_name` | 99.93% | 99.4% | 408.3 | 16112.2 | 2000ms | 17/2832 |
| ✅ | `jsonplaceholder_posts` | 99.96% | 99.86% | 182.3 | 10927.2 | 2000ms | 4/2832 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `numbers_trivia` | 03:00 | 4258.9 | 42.11% |
| `numbers_trivia` | 10:00 | 3237.5 | 30.63% |
| `nasa_apod` | 11:00 | 3217.2 | 43.97% |
| `nasa_apod` | 09:00 | 3117.8 | 44.17% |
| `nasa_apod` | 17:00 | 3102.3 | 39.16% |
| `nasa_apod` | 03:00 | 3074.7 | 43.86% |
| `nasa_apod` | 18:00 | 3039.7 | 44.44% |
| `nasa_apod` | 02:00 | 3038.3 | 40.63% |
| `numbers_trivia` | 14:00 | 3013.2 | 28.91% |
| `nasa_apod` | 05:00 | 3012.8 | 44.09% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
