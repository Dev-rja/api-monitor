# API Reliability Monitor — SLA Report

> Last updated: **2026-04-14 19:45 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **79.9%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 97.17% | 577.1 | 10117.1 | 1000ms | 8/283 |
| ❌ | `public_apis_list` | 0.0% | 99.65% | 126.3 | 3806.8 | 1500ms | 1/283 |
| ❌ | `nasa_apod` | 69.26% | 48.41% | 3431.9 | 10538.0 | 2000ms | 146/283 |
| ❌ | `ipapi_check` | 94.35% | 100.0% | 159.1 | 353.0 | 2500ms | 0/283 |
| ⚠️ | `open_meteo_weather` | 97.17% | 96.11% | 824.7 | 14877.1 | 2000ms | 11/283 |
| ⚠️ | `dog_ceo_random` | 99.29% | 85.51% | 1080.3 | 5586.8 | 2500ms | 41/283 |
| ✅ | `useless_fact` | 99.29% | 99.65% | 573.9 | 10229.6 | 2500ms | 1/283 |
| ✅ | `catfact_random` | 99.29% | 99.65% | 260.4 | 10070.5 | 3000ms | 1/283 |
| ✅ | `agify_name` | 100.0% | 99.65% | 387.7 | 3237.1 | 2000ms | 1/283 |
| ✅ | `rest_countries` | 100.0% | 98.94% | 274.2 | 7269.1 | 2500ms | 3/283 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.65% | 239.8 | 2314.9 | 2000ms | 1/283 |
| ✅ | `coingecko_bitcoin` | 100.0% | 100.0% | 100.8 | 252.0 | 1500ms | 0/283 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `nasa_apod` | 03:00 | 5624.1 | 85.71% |
| `nasa_apod` | 18:00 | 4952.5 | 75.0% |
| `nasa_apod` | 20:00 | 4763.5 | 63.16% |
| `nasa_apod` | 14:00 | 4442.8 | 50.0% |
| `nasa_apod` | 17:00 | 3994.7 | 56.25% |
| `nasa_apod` | 08:00 | 3821.0 | 58.33% |
| `nasa_apod` | 11:00 | 3748.3 | 55.56% |
| `nasa_apod` | 13:00 | 3734.4 | 57.14% |
| `nasa_apod` | 23:00 | 3531.7 | 42.86% |
| `catfact_random` | 00:00 | 3471.7 | 33.33% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
