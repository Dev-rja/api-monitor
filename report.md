# API Reliability Monitor — SLA Report

> Last updated: **2026-11-21 15:31 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **76.1%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 74.61% | 2675.0 | 10420.1 | 1000ms | 728/2867 |
| ❌ | `public_apis_list` | 0.0% | 99.37% | 145.4 | 5075.4 | 1500ms | 18/2867 |
| ❌ | `ipapi_check` | 42.41% | 99.97% | 145.1 | 4507.0 | 2500ms | 1/2867 |
| ❌ | `nasa_apod` | 76.84% | 59.09% | 2722.6 | 11152.5 | 2000ms | 1173/2867 |
| ⚠️ | `dog_ceo_random` | 97.31% | 97.87% | 480.2 | 10509.6 | 2500ms | 61/2867 |
| ⚠️ | `open_meteo_weather` | 98.95% | 98.29% | 664.0 | 14877.1 | 2000ms | 49/2867 |
| ✅ | `useless_fact` | 99.02% | 99.55% | 670.0 | 10229.6 | 2500ms | 13/2867 |
| ✅ | `rest_countries` | 99.48% | 99.2% | 270.3 | 10221.5 | 2500ms | 23/2867 |
| ✅ | `coingecko_bitcoin` | 99.72% | 99.93% | 97.0 | 4328.4 | 1500ms | 2/2867 |
| ✅ | `catfact_random` | 99.83% | 99.51% | 267.4 | 10080.2 | 3000ms | 14/2867 |
| ✅ | `agify_name` | 99.93% | 99.41% | 407.6 | 16112.2 | 2000ms | 17/2867 |
| ✅ | `jsonplaceholder_posts` | 99.97% | 99.86% | 181.5 | 10927.2 | 2000ms | 4/2867 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `numbers_trivia` | 03:00 | 4187.4 | 41.38% |
| `nasa_apod` | 11:00 | 3217.2 | 43.97% |
| `numbers_trivia` | 10:00 | 3155.6 | 29.82% |
| `nasa_apod` | 09:00 | 3117.8 | 44.17% |
| `nasa_apod` | 00:00 | 3108.8 | 40.63% |
| `nasa_apod` | 18:00 | 3089.8 | 44.83% |
| `nasa_apod` | 03:00 | 3067.0 | 44.83% |
| `nasa_apod` | 17:00 | 3064.7 | 38.62% |
| `nasa_apod` | 05:00 | 3012.8 | 44.09% |
| `numbers_trivia` | 14:00 | 2991.4 | 28.68% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
