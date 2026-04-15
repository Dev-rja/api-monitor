# API Reliability Monitor — SLA Report

> Last updated: **2026-04-15 07:22 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **79.8%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 94.5% | 838.8 | 10146.1 | 1000ms | 16/291 |
| ❌ | `public_apis_list` | 0.0% | 99.66% | 126.6 | 3806.8 | 1500ms | 1/291 |
| ❌ | `nasa_apod` | 68.38% | 47.42% | 3513.7 | 10538.0 | 2000ms | 153/291 |
| ❌ | `ipapi_check` | 94.16% | 100.0% | 159.4 | 353.0 | 2500ms | 0/291 |
| ⚠️ | `open_meteo_weather` | 97.25% | 96.22% | 816.3 | 14877.1 | 2000ms | 11/291 |
| ⚠️ | `dog_ceo_random` | 99.31% | 85.91% | 1059.9 | 5586.8 | 2500ms | 41/291 |
| ✅ | `useless_fact` | 99.31% | 99.66% | 571.8 | 10229.6 | 2500ms | 1/291 |
| ✅ | `catfact_random` | 99.31% | 99.66% | 260.0 | 10070.5 | 3000ms | 1/291 |
| ✅ | `agify_name` | 100.0% | 99.66% | 387.0 | 3237.1 | 2000ms | 1/291 |
| ✅ | `rest_countries` | 100.0% | 98.97% | 272.2 | 7269.1 | 2500ms | 3/291 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.66% | 239.6 | 2314.9 | 2000ms | 1/291 |
| ✅ | `coingecko_bitcoin` | 100.0% | 100.0% | 101.0 | 252.0 | 1500ms | 0/291 |

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
