# API Reliability Monitor — SLA Report

> Last updated: **2026-04-14 22:27 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **79.9%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 96.15% | 676.7 | 10117.1 | 1000ms | 11/286 |
| ❌ | `public_apis_list` | 0.0% | 99.65% | 126.5 | 3806.8 | 1500ms | 1/286 |
| ❌ | `nasa_apod` | 68.88% | 47.9% | 3471.0 | 10538.0 | 2000ms | 149/286 |
| ❌ | `ipapi_check` | 94.41% | 100.0% | 159.4 | 353.0 | 2500ms | 0/286 |
| ⚠️ | `open_meteo_weather` | 97.2% | 96.15% | 821.4 | 14877.1 | 2000ms | 11/286 |
| ⚠️ | `dog_ceo_random` | 99.3% | 85.66% | 1073.5 | 5586.8 | 2500ms | 41/286 |
| ✅ | `useless_fact` | 99.3% | 99.65% | 572.3 | 10229.6 | 2500ms | 1/286 |
| ✅ | `catfact_random` | 99.3% | 99.65% | 260.3 | 10070.5 | 3000ms | 1/286 |
| ✅ | `agify_name` | 100.0% | 99.65% | 386.4 | 3237.1 | 2000ms | 1/286 |
| ✅ | `rest_countries` | 100.0% | 98.95% | 273.1 | 7269.1 | 2500ms | 3/286 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.65% | 239.8 | 2314.9 | 2000ms | 1/286 |
| ✅ | `coingecko_bitcoin` | 100.0% | 100.0% | 100.9 | 252.0 | 1500ms | 0/286 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `nasa_apod` | 03:00 | 5624.1 | 85.71% |
| `nasa_apod` | 18:00 | 4952.5 | 75.0% |
| `nasa_apod` | 20:00 | 4651.7 | 65.0% |
| `nasa_apod` | 14:00 | 4442.8 | 50.0% |
| `nasa_apod` | 17:00 | 3994.7 | 56.25% |
| `nasa_apod` | 08:00 | 3821.0 | 58.33% |
| `nasa_apod` | 11:00 | 3748.3 | 55.56% |
| `nasa_apod` | 13:00 | 3734.4 | 57.14% |
| `nasa_apod` | 22:00 | 3660.8 | 50.0% |
| `nasa_apod` | 23:00 | 3531.7 | 42.86% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
