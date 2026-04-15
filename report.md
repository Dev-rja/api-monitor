# API Reliability Monitor — SLA Report

> Last updated: **2026-04-15 12:43 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **79.7%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 93.22% | 964.2 | 10176.4 | 1000ms | 20/295 |
| ❌ | `public_apis_list` | 0.0% | 99.66% | 126.6 | 3806.8 | 1500ms | 1/295 |
| ❌ | `nasa_apod` | 67.8% | 47.12% | 3572.9 | 10538.0 | 2000ms | 156/295 |
| ❌ | `ipapi_check` | 93.9% | 100.0% | 159.5 | 353.0 | 2500ms | 0/295 |
| ⚠️ | `open_meteo_weather` | 97.29% | 96.27% | 814.0 | 14877.1 | 2000ms | 11/295 |
| ⚠️ | `dog_ceo_random` | 99.32% | 86.1% | 1054.3 | 5586.8 | 2500ms | 41/295 |
| ✅ | `useless_fact` | 99.32% | 99.66% | 570.8 | 10229.6 | 2500ms | 1/295 |
| ✅ | `catfact_random` | 99.32% | 99.66% | 258.9 | 10070.5 | 3000ms | 1/295 |
| ✅ | `agify_name` | 100.0% | 99.66% | 386.2 | 3237.1 | 2000ms | 1/295 |
| ✅ | `rest_countries` | 100.0% | 98.98% | 271.7 | 7269.1 | 2500ms | 3/295 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.66% | 239.4 | 2314.9 | 2000ms | 1/295 |
| ✅ | `coingecko_bitcoin` | 100.0% | 100.0% | 101.2 | 252.0 | 1500ms | 0/295 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `nasa_apod` | 03:00 | 5273.5 | 87.5% |
| `nasa_apod` | 18:00 | 4952.5 | 75.0% |
| `nasa_apod` | 20:00 | 4651.7 | 65.0% |
| `nasa_apod` | 14:00 | 4442.8 | 50.0% |
| `nasa_apod` | 11:00 | 4098.4 | 57.89% |
| `nasa_apod` | 17:00 | 3994.7 | 56.25% |
| `nasa_apod` | 10:00 | 3989.3 | 53.85% |
| `nasa_apod` | 08:00 | 3821.0 | 58.33% |
| `nasa_apod` | 13:00 | 3734.4 | 57.14% |
| `nasa_apod` | 22:00 | 3660.8 | 50.0% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
