# API Reliability Monitor — SLA Report

> Last updated: **2026-11-18 22:57 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **76.1%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 74.53% | 2683.1 | 10420.1 | 1000ms | 728/2858 |
| ❌ | `public_apis_list` | 0.0% | 99.37% | 145.6 | 5075.4 | 1500ms | 18/2858 |
| ❌ | `ipapi_check` | 42.55% | 99.97% | 144.9 | 4507.0 | 2500ms | 1/2858 |
| ❌ | `nasa_apod` | 76.91% | 59.06% | 2722.1 | 11152.5 | 2000ms | 1170/2858 |
| ⚠️ | `dog_ceo_random` | 97.31% | 97.87% | 480.7 | 10509.6 | 2500ms | 61/2858 |
| ⚠️ | `open_meteo_weather` | 98.95% | 98.29% | 665.5 | 14877.1 | 2000ms | 49/2858 |
| ✅ | `useless_fact` | 99.02% | 99.55% | 670.0 | 10229.6 | 2500ms | 13/2858 |
| ✅ | `rest_countries` | 99.48% | 99.2% | 270.4 | 10221.5 | 2500ms | 23/2858 |
| ✅ | `coingecko_bitcoin` | 99.72% | 99.93% | 97.1 | 4328.4 | 1500ms | 2/2858 |
| ✅ | `catfact_random` | 99.83% | 99.51% | 267.3 | 10080.2 | 3000ms | 14/2858 |
| ✅ | `agify_name` | 99.93% | 99.41% | 407.9 | 16112.2 | 2000ms | 17/2858 |
| ✅ | `jsonplaceholder_posts` | 99.97% | 99.86% | 181.7 | 10927.2 | 2000ms | 4/2858 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `numbers_trivia` | 03:00 | 4187.4 | 41.38% |
| `nasa_apod` | 11:00 | 3217.2 | 43.97% |
| `numbers_trivia` | 10:00 | 3182.9 | 30.09% |
| `nasa_apod` | 09:00 | 3117.8 | 44.17% |
| `nasa_apod` | 03:00 | 3067.0 | 44.83% |
| `nasa_apod` | 17:00 | 3064.7 | 38.62% |
| `nasa_apod` | 18:00 | 3039.7 | 44.44% |
| `nasa_apod` | 00:00 | 3032.6 | 40.0% |
| `nasa_apod` | 05:00 | 3012.8 | 44.09% |
| `numbers_trivia` | 14:00 | 2991.4 | 28.68% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
