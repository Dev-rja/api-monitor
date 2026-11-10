# API Reliability Monitor — SLA Report

> Last updated: **2026-11-10 18:42 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **7/12** &nbsp;|&nbsp; Avg uptime: **76.2%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 74.26% | 2710.1 | 10420.1 | 1000ms | 728/2828 |
| ❌ | `public_apis_list` | 0.0% | 99.36% | 146.4 | 5075.4 | 1500ms | 18/2828 |
| ❌ | `ipapi_check` | 43.0% | 99.96% | 145.1 | 4507.0 | 2500ms | 1/2828 |
| ❌ | `nasa_apod` | 77.33% | 59.16% | 2718.3 | 11152.5 | 2000ms | 1155/2828 |
| ⚠️ | `dog_ceo_random` | 97.28% | 97.84% | 481.3 | 10509.6 | 2500ms | 61/2828 |
| ✅ | `useless_fact` | 99.01% | 99.54% | 670.3 | 10229.6 | 2500ms | 13/2828 |
| ✅ | `open_meteo_weather` | 99.05% | 98.37% | 659.6 | 14877.1 | 2000ms | 46/2828 |
| ✅ | `rest_countries` | 99.47% | 99.19% | 270.7 | 10221.5 | 2500ms | 23/2828 |
| ✅ | `coingecko_bitcoin` | 99.72% | 99.93% | 97.2 | 4328.4 | 1500ms | 2/2828 |
| ✅ | `catfact_random` | 99.82% | 99.5% | 266.7 | 10080.2 | 3000ms | 14/2828 |
| ✅ | `agify_name` | 99.93% | 99.4% | 408.3 | 16112.2 | 2000ms | 17/2828 |
| ✅ | `jsonplaceholder_posts` | 99.96% | 99.86% | 182.3 | 10927.2 | 2000ms | 4/2828 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `numbers_trivia` | 03:00 | 4331.3 | 42.86% |
| `numbers_trivia` | 10:00 | 3266.0 | 30.91% |
| `nasa_apod` | 11:00 | 3217.2 | 43.97% |
| `nasa_apod` | 09:00 | 3117.8 | 44.17% |
| `nasa_apod` | 03:00 | 3116.7 | 44.64% |
| `nasa_apod` | 17:00 | 3102.3 | 39.16% |
| `nasa_apod` | 18:00 | 3043.9 | 44.06% |
| `nasa_apod` | 02:00 | 3038.3 | 40.63% |
| `numbers_trivia` | 14:00 | 3013.2 | 28.91% |
| `nasa_apod` | 05:00 | 3012.8 | 44.09% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
