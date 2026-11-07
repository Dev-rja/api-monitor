# API Reliability Monitor — SLA Report

> Last updated: **2026-11-07 18:45 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **7/12** &nbsp;|&nbsp; Avg uptime: **76.2%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 74.15% | 2720.8 | 10420.1 | 1000ms | 728/2816 |
| ❌ | `public_apis_list` | 0.0% | 99.36% | 146.5 | 5075.4 | 1500ms | 18/2816 |
| ❌ | `ipapi_check` | 43.11% | 99.96% | 144.9 | 4507.0 | 2500ms | 1/2816 |
| ❌ | `nasa_apod` | 77.56% | 59.2% | 2719.1 | 11152.5 | 2000ms | 1149/2816 |
| ⚠️ | `dog_ceo_random` | 97.27% | 97.83% | 481.4 | 10509.6 | 2500ms | 61/2816 |
| ✅ | `useless_fact` | 99.01% | 99.54% | 670.2 | 10229.6 | 2500ms | 13/2816 |
| ✅ | `open_meteo_weather` | 99.04% | 98.37% | 660.3 | 14877.1 | 2000ms | 46/2816 |
| ✅ | `rest_countries` | 99.47% | 99.18% | 270.9 | 10221.5 | 2500ms | 23/2816 |
| ✅ | `coingecko_bitcoin` | 99.72% | 99.93% | 97.2 | 4328.4 | 1500ms | 2/2816 |
| ✅ | `catfact_random` | 99.82% | 99.5% | 266.7 | 10080.2 | 3000ms | 14/2816 |
| ✅ | `agify_name` | 99.93% | 99.4% | 408.2 | 16112.2 | 2000ms | 17/2816 |
| ✅ | `jsonplaceholder_posts` | 99.96% | 99.86% | 182.7 | 10927.2 | 2000ms | 4/2816 |

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
| `nasa_apod` | 18:00 | 3063.9 | 44.37% |
| `numbers_trivia` | 14:00 | 3035.5 | 29.13% |
| `nasa_apod` | 05:00 | 3012.8 | 44.09% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
