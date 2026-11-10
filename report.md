# API Reliability Monitor — SLA Report

> Last updated: **2026-11-10 11:13 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **7/12** &nbsp;|&nbsp; Avg uptime: **76.2%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 74.25% | 2711.0 | 10420.1 | 1000ms | 728/2827 |
| ❌ | `public_apis_list` | 0.0% | 99.36% | 146.4 | 5075.4 | 1500ms | 18/2827 |
| ❌ | `ipapi_check` | 43.01% | 99.96% | 144.7 | 4507.0 | 2500ms | 1/2827 |
| ❌ | `nasa_apod` | 77.33% | 59.14% | 2719.2 | 11152.5 | 2000ms | 1155/2827 |
| ⚠️ | `dog_ceo_random` | 97.28% | 97.84% | 481.3 | 10509.6 | 2500ms | 61/2827 |
| ✅ | `useless_fact` | 99.01% | 99.54% | 670.4 | 10229.6 | 2500ms | 13/2827 |
| ✅ | `open_meteo_weather` | 99.04% | 98.37% | 659.6 | 14877.1 | 2000ms | 46/2827 |
| ✅ | `rest_countries` | 99.47% | 99.19% | 270.7 | 10221.5 | 2500ms | 23/2827 |
| ✅ | `coingecko_bitcoin` | 99.72% | 99.93% | 97.2 | 4328.4 | 1500ms | 2/2827 |
| ✅ | `catfact_random` | 99.82% | 99.5% | 266.7 | 10080.2 | 3000ms | 14/2827 |
| ✅ | `agify_name` | 99.93% | 99.4% | 408.2 | 16112.2 | 2000ms | 17/2827 |
| ✅ | `jsonplaceholder_posts` | 99.96% | 99.86% | 182.3 | 10927.2 | 2000ms | 4/2827 |

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
| `nasa_apod` | 18:00 | 3063.9 | 44.37% |
| `nasa_apod` | 02:00 | 3038.3 | 40.63% |
| `numbers_trivia` | 14:00 | 3013.2 | 28.91% |
| `nasa_apod` | 05:00 | 3012.8 | 44.09% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
