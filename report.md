# API Reliability Monitor — SLA Report

> Last updated: **2026-11-24 17:43 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **76.1%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 74.7% | 2666.1 | 10420.1 | 1000ms | 728/2877 |
| ❌ | `public_apis_list` | 0.0% | 99.37% | 145.3 | 5075.4 | 1500ms | 18/2877 |
| ❌ | `ipapi_check` | 42.3% | 99.97% | 144.9 | 4507.0 | 2500ms | 1/2877 |
| ❌ | `nasa_apod` | 76.64% | 59.19% | 2718.5 | 11152.5 | 2000ms | 1174/2877 |
| ⚠️ | `dog_ceo_random` | 97.32% | 97.88% | 479.5 | 10509.6 | 2500ms | 61/2877 |
| ⚠️ | `open_meteo_weather` | 98.89% | 98.26% | 665.6 | 14877.1 | 2000ms | 50/2877 |
| ✅ | `useless_fact` | 99.03% | 99.55% | 669.9 | 10229.6 | 2500ms | 13/2877 |
| ✅ | `rest_countries` | 99.48% | 99.2% | 269.9 | 10221.5 | 2500ms | 23/2877 |
| ✅ | `coingecko_bitcoin` | 99.72% | 99.93% | 96.9 | 4328.4 | 1500ms | 2/2877 |
| ✅ | `catfact_random` | 99.83% | 99.51% | 267.2 | 10080.2 | 3000ms | 14/2877 |
| ✅ | `agify_name` | 99.93% | 99.41% | 407.3 | 16112.2 | 2000ms | 17/2877 |
| ✅ | `jsonplaceholder_posts` | 99.97% | 99.86% | 181.1 | 10927.2 | 2000ms | 4/2877 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `numbers_trivia` | 03:00 | 4187.4 | 41.38% |
| `nasa_apod` | 11:00 | 3217.2 | 43.97% |
| `numbers_trivia` | 10:00 | 3128.5 | 29.57% |
| `nasa_apod` | 09:00 | 3117.8 | 44.17% |
| `nasa_apod` | 00:00 | 3108.8 | 40.63% |
| `nasa_apod` | 02:00 | 3101.0 | 40.0% |
| `nasa_apod` | 18:00 | 3089.8 | 44.83% |
| `nasa_apod` | 03:00 | 3067.0 | 44.83% |
| `nasa_apod` | 17:00 | 3048.7 | 38.36% |
| `nasa_apod` | 05:00 | 3012.8 | 44.09% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
