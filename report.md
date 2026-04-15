# API Reliability Monitor — SLA Report

> Last updated: **2026-04-15 05:52 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **79.9%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 94.83% | 806.7 | 10146.1 | 1000ms | 15/290 |
| ❌ | `public_apis_list` | 0.0% | 99.66% | 126.0 | 3806.8 | 1500ms | 1/290 |
| ❌ | `nasa_apod` | 68.62% | 47.59% | 3489.9 | 10538.0 | 2000ms | 152/290 |
| ❌ | `ipapi_check` | 94.48% | 100.0% | 159.5 | 353.0 | 2500ms | 0/290 |
| ⚠️ | `open_meteo_weather` | 97.24% | 96.21% | 817.7 | 14877.1 | 2000ms | 11/290 |
| ⚠️ | `dog_ceo_random` | 99.31% | 85.86% | 1062.6 | 5586.8 | 2500ms | 41/290 |
| ✅ | `useless_fact` | 99.31% | 99.66% | 572.2 | 10229.6 | 2500ms | 1/290 |
| ✅ | `catfact_random` | 99.31% | 99.66% | 260.7 | 10070.5 | 3000ms | 1/290 |
| ✅ | `agify_name` | 100.0% | 99.66% | 387.7 | 3237.1 | 2000ms | 1/290 |
| ✅ | `rest_countries` | 100.0% | 98.97% | 272.6 | 7269.1 | 2500ms | 3/290 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.66% | 239.8 | 2314.9 | 2000ms | 1/290 |
| ✅ | `coingecko_bitcoin` | 100.0% | 100.0% | 100.9 | 252.0 | 1500ms | 0/290 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `nasa_apod` | 03:00 | 5273.5 | 87.5% |
| `nasa_apod` | 18:00 | 4952.5 | 75.0% |
| `nasa_apod` | 20:00 | 4651.7 | 65.0% |
| `nasa_apod` | 14:00 | 4442.8 | 50.0% |
| `nasa_apod` | 17:00 | 3994.7 | 56.25% |
| `nasa_apod` | 08:00 | 3821.0 | 58.33% |
| `nasa_apod` | 11:00 | 3748.3 | 55.56% |
| `nasa_apod` | 13:00 | 3734.4 | 57.14% |
| `nasa_apod` | 22:00 | 3660.8 | 50.0% |
| `nasa_apod` | 05:00 | 3550.9 | 60.0% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
