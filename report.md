# API Reliability Monitor — SLA Report

> Last updated: **2026-11-16 06:15 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **76.2%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 74.46% | 2690.2 | 10420.1 | 1000ms | 728/2850 |
| ❌ | `public_apis_list` | 0.0% | 99.37% | 145.8 | 5075.4 | 1500ms | 18/2850 |
| ❌ | `ipapi_check` | 42.67% | 99.96% | 145.0 | 4507.0 | 2500ms | 1/2850 |
| ❌ | `nasa_apod` | 77.02% | 59.09% | 2718.3 | 11152.5 | 2000ms | 1166/2850 |
| ⚠️ | `dog_ceo_random` | 97.3% | 97.86% | 480.1 | 10509.6 | 2500ms | 61/2850 |
| ⚠️ | `open_meteo_weather` | 98.98% | 98.32% | 663.4 | 14877.1 | 2000ms | 48/2850 |
| ✅ | `useless_fact` | 99.02% | 99.54% | 670.2 | 10229.6 | 2500ms | 13/2850 |
| ✅ | `rest_countries` | 99.47% | 99.19% | 270.3 | 10221.5 | 2500ms | 23/2850 |
| ✅ | `coingecko_bitcoin` | 99.72% | 99.93% | 97.1 | 4328.4 | 1500ms | 2/2850 |
| ✅ | `catfact_random` | 99.82% | 99.51% | 266.9 | 10080.2 | 3000ms | 14/2850 |
| ✅ | `agify_name` | 99.93% | 99.4% | 407.9 | 16112.2 | 2000ms | 17/2850 |
| ✅ | `jsonplaceholder_posts` | 99.96% | 99.86% | 181.7 | 10927.2 | 2000ms | 4/2850 |

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
| `nasa_apod` | 05:00 | 3012.8 | 44.09% |
| `numbers_trivia` | 14:00 | 2991.4 | 28.68% |
| `nasa_apod` | 02:00 | 2959.5 | 39.39% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
