# API Reliability Monitor — SLA Report

> Last updated: **2026-04-15 09:01 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **79.8%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 94.18% | 870.4 | 10146.1 | 1000ms | 17/292 |
| ❌ | `public_apis_list` | 0.0% | 99.66% | 126.9 | 3806.8 | 1500ms | 1/292 |
| ❌ | `nasa_apod` | 68.15% | 47.26% | 3537.6 | 10538.0 | 2000ms | 154/292 |
| ❌ | `ipapi_check` | 94.18% | 100.0% | 159.6 | 353.0 | 2500ms | 0/292 |
| ⚠️ | `open_meteo_weather` | 97.26% | 96.23% | 816.3 | 14877.1 | 2000ms | 11/292 |
| ⚠️ | `dog_ceo_random` | 99.32% | 85.96% | 1061.4 | 5586.8 | 2500ms | 41/292 |
| ✅ | `useless_fact` | 99.32% | 99.66% | 571.0 | 10229.6 | 2500ms | 1/292 |
| ✅ | `catfact_random` | 99.32% | 99.66% | 259.5 | 10070.5 | 3000ms | 1/292 |
| ✅ | `agify_name` | 100.0% | 99.66% | 386.8 | 3237.1 | 2000ms | 1/292 |
| ✅ | `rest_countries` | 100.0% | 98.97% | 271.9 | 7269.1 | 2500ms | 3/292 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.66% | 239.8 | 2314.9 | 2000ms | 1/292 |
| ✅ | `coingecko_bitcoin` | 100.0% | 100.0% | 101.2 | 252.0 | 1500ms | 0/292 |

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
