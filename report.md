# API Reliability Monitor — SLA Report

> Last updated: **2026-11-23 02:02 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **76.1%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 74.66% | 2669.6 | 10420.1 | 1000ms | 728/2873 |
| ❌ | `public_apis_list` | 0.0% | 99.37% | 145.3 | 5075.4 | 1500ms | 18/2873 |
| ❌ | `ipapi_check` | 42.36% | 99.97% | 145.0 | 4507.0 | 2500ms | 1/2873 |
| ❌ | `nasa_apod` | 76.71% | 59.14% | 2721.5 | 11152.5 | 2000ms | 1174/2873 |
| ⚠️ | `dog_ceo_random` | 97.32% | 97.88% | 479.7 | 10509.6 | 2500ms | 61/2873 |
| ⚠️ | `open_meteo_weather` | 98.92% | 98.29% | 662.9 | 14877.1 | 2000ms | 49/2873 |
| ✅ | `useless_fact` | 99.03% | 99.55% | 669.9 | 10229.6 | 2500ms | 13/2873 |
| ✅ | `rest_countries` | 99.48% | 99.2% | 270.0 | 10221.5 | 2500ms | 23/2873 |
| ✅ | `coingecko_bitcoin` | 99.72% | 99.93% | 96.9 | 4328.4 | 1500ms | 2/2873 |
| ✅ | `catfact_random` | 99.83% | 99.51% | 267.1 | 10080.2 | 3000ms | 14/2873 |
| ✅ | `agify_name` | 99.93% | 99.41% | 407.5 | 16112.2 | 2000ms | 17/2873 |
| ✅ | `jsonplaceholder_posts` | 99.97% | 99.86% | 181.2 | 10927.2 | 2000ms | 4/2873 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `numbers_trivia` | 03:00 | 4187.4 | 41.38% |
| `nasa_apod` | 11:00 | 3217.2 | 43.97% |
| `numbers_trivia` | 10:00 | 3155.6 | 29.82% |
| `nasa_apod` | 09:00 | 3117.8 | 44.17% |
| `nasa_apod` | 00:00 | 3108.8 | 40.63% |
| `nasa_apod` | 02:00 | 3101.0 | 40.0% |
| `nasa_apod` | 18:00 | 3089.8 | 44.83% |
| `nasa_apod` | 03:00 | 3067.0 | 44.83% |
| `nasa_apod` | 17:00 | 3064.7 | 38.62% |
| `nasa_apod` | 05:00 | 3012.8 | 44.09% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
