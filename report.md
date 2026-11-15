# API Reliability Monitor — SLA Report

> Last updated: **2026-11-15 07:44 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **7/12** &nbsp;|&nbsp; Avg uptime: **76.2%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 74.42% | 2693.7 | 10420.1 | 1000ms | 728/2846 |
| ❌ | `public_apis_list` | 0.0% | 99.37% | 145.9 | 5075.4 | 1500ms | 18/2846 |
| ❌ | `ipapi_check` | 42.73% | 99.96% | 145.1 | 4507.0 | 2500ms | 1/2846 |
| ❌ | `nasa_apod` | 77.13% | 59.1% | 2716.7 | 11152.5 | 2000ms | 1164/2846 |
| ⚠️ | `dog_ceo_random` | 97.29% | 97.86% | 480.4 | 10509.6 | 2500ms | 61/2846 |
| ✅ | `useless_fact` | 99.02% | 99.54% | 670.2 | 10229.6 | 2500ms | 13/2846 |
| ✅ | `open_meteo_weather` | 99.02% | 98.35% | 660.7 | 14877.1 | 2000ms | 47/2846 |
| ✅ | `rest_countries` | 99.47% | 99.19% | 270.4 | 10221.5 | 2500ms | 23/2846 |
| ✅ | `coingecko_bitcoin` | 99.72% | 99.93% | 97.2 | 4328.4 | 1500ms | 2/2846 |
| ✅ | `catfact_random` | 99.82% | 99.51% | 266.9 | 10080.2 | 3000ms | 14/2846 |
| ✅ | `agify_name` | 99.93% | 99.4% | 407.9 | 16112.2 | 2000ms | 17/2846 |
| ✅ | `jsonplaceholder_posts` | 99.96% | 99.86% | 181.9 | 10927.2 | 2000ms | 4/2846 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `numbers_trivia` | 03:00 | 4187.4 | 41.38% |
| `nasa_apod` | 11:00 | 3217.2 | 43.97% |
| `numbers_trivia` | 10:00 | 3182.9 | 30.09% |
| `nasa_apod` | 09:00 | 3117.8 | 44.17% |
| `nasa_apod` | 17:00 | 3083.2 | 38.89% |
| `nasa_apod` | 03:00 | 3067.0 | 44.83% |
| `nasa_apod` | 18:00 | 3039.7 | 44.44% |
| `numbers_trivia` | 14:00 | 3013.2 | 28.91% |
| `nasa_apod` | 05:00 | 3012.8 | 44.09% |
| `nasa_apod` | 02:00 | 2959.5 | 39.39% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
