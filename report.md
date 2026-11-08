# API Reliability Monitor — SLA Report

> Last updated: **2026-11-08 19:31 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **7/12** &nbsp;|&nbsp; Avg uptime: **76.2%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 74.19% | 2716.3 | 10420.1 | 1000ms | 728/2821 |
| ❌ | `public_apis_list` | 0.0% | 99.36% | 146.5 | 5075.4 | 1500ms | 18/2821 |
| ❌ | `ipapi_check` | 43.11% | 99.96% | 144.8 | 4507.0 | 2500ms | 1/2821 |
| ❌ | `nasa_apod` | 77.49% | 59.16% | 2719.9 | 11152.5 | 2000ms | 1152/2821 |
| ⚠️ | `dog_ceo_random` | 97.27% | 97.84% | 481.4 | 10509.6 | 2500ms | 61/2821 |
| ✅ | `useless_fact` | 99.01% | 99.54% | 670.3 | 10229.6 | 2500ms | 13/2821 |
| ✅ | `open_meteo_weather` | 99.04% | 98.37% | 659.8 | 14877.1 | 2000ms | 46/2821 |
| ✅ | `rest_countries` | 99.47% | 99.18% | 270.9 | 10221.5 | 2500ms | 23/2821 |
| ✅ | `coingecko_bitcoin` | 99.72% | 99.93% | 97.3 | 4328.4 | 1500ms | 2/2821 |
| ✅ | `catfact_random` | 99.82% | 99.5% | 266.8 | 10080.2 | 3000ms | 14/2821 |
| ✅ | `agify_name` | 99.93% | 99.4% | 408.2 | 16112.2 | 2000ms | 17/2821 |
| ✅ | `jsonplaceholder_posts` | 99.96% | 99.86% | 182.5 | 10927.2 | 2000ms | 4/2821 |

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
| `numbers_trivia` | 14:00 | 3013.2 | 28.91% |
| `nasa_apod` | 05:00 | 3012.8 | 44.09% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
