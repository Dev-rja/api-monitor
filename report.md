# API Reliability Monitor — SLA Report

> Last updated: **2026-11-20 10:16 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **76.1%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 74.57% | 2678.6 | 10420.1 | 1000ms | 728/2863 |
| ❌ | `public_apis_list` | 0.0% | 99.37% | 145.4 | 5075.4 | 1500ms | 18/2863 |
| ❌ | `ipapi_check` | 42.47% | 99.97% | 145.1 | 4507.0 | 2500ms | 1/2863 |
| ❌ | `nasa_apod` | 76.88% | 59.13% | 2718.2 | 11152.5 | 2000ms | 1170/2863 |
| ⚠️ | `dog_ceo_random` | 97.31% | 97.87% | 480.3 | 10509.6 | 2500ms | 61/2863 |
| ⚠️ | `open_meteo_weather` | 98.95% | 98.29% | 664.6 | 14877.1 | 2000ms | 49/2863 |
| ✅ | `useless_fact` | 99.02% | 99.55% | 670.0 | 10229.6 | 2500ms | 13/2863 |
| ✅ | `rest_countries` | 99.48% | 99.2% | 270.4 | 10221.5 | 2500ms | 23/2863 |
| ✅ | `coingecko_bitcoin` | 99.72% | 99.93% | 97.0 | 4328.4 | 1500ms | 2/2863 |
| ✅ | `catfact_random` | 99.83% | 99.51% | 267.3 | 10080.2 | 3000ms | 14/2863 |
| ✅ | `agify_name` | 99.93% | 99.41% | 407.7 | 16112.2 | 2000ms | 17/2863 |
| ✅ | `jsonplaceholder_posts` | 99.97% | 99.86% | 181.6 | 10927.2 | 2000ms | 4/2863 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `numbers_trivia` | 03:00 | 4187.4 | 41.38% |
| `nasa_apod` | 11:00 | 3217.2 | 43.97% |
| `numbers_trivia` | 10:00 | 3155.6 | 29.82% |
| `nasa_apod` | 09:00 | 3117.8 | 44.17% |
| `nasa_apod` | 03:00 | 3067.0 | 44.83% |
| `nasa_apod` | 17:00 | 3064.7 | 38.62% |
| `nasa_apod` | 18:00 | 3039.7 | 44.44% |
| `nasa_apod` | 00:00 | 3032.6 | 40.0% |
| `nasa_apod` | 05:00 | 3012.8 | 44.09% |
| `numbers_trivia` | 14:00 | 2991.4 | 28.68% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
