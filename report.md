# API Reliability Monitor — SLA Report

> Last updated: **2026-04-15 11:35 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **79.7%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 93.54% | 932.9 | 10146.1 | 1000ms | 19/294 |
| ❌ | `public_apis_list` | 0.0% | 99.66% | 126.9 | 3806.8 | 1500ms | 1/294 |
| ❌ | `nasa_apod` | 67.69% | 46.94% | 3584.2 | 10538.0 | 2000ms | 156/294 |
| ❌ | `ipapi_check` | 93.88% | 100.0% | 159.7 | 353.0 | 2500ms | 0/294 |
| ⚠️ | `open_meteo_weather` | 97.28% | 96.26% | 814.0 | 14877.1 | 2000ms | 11/294 |
| ⚠️ | `dog_ceo_random` | 99.32% | 86.05% | 1057.2 | 5586.8 | 2500ms | 41/294 |
| ✅ | `useless_fact` | 99.32% | 99.66% | 570.2 | 10229.6 | 2500ms | 1/294 |
| ✅ | `catfact_random` | 99.32% | 99.66% | 258.7 | 10070.5 | 3000ms | 1/294 |
| ✅ | `agify_name` | 100.0% | 99.66% | 385.8 | 3237.1 | 2000ms | 1/294 |
| ✅ | `rest_countries` | 100.0% | 98.98% | 271.2 | 7269.1 | 2500ms | 3/294 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.66% | 239.5 | 2314.9 | 2000ms | 1/294 |
| ✅ | `coingecko_bitcoin` | 100.0% | 100.0% | 101.4 | 252.0 | 1500ms | 0/294 |

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
