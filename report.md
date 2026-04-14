# API Reliability Monitor — SLA Report

> Last updated: **2026-04-14 18:16 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **79.9%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 97.52% | 543.5 | 10117.1 | 1000ms | 7/282 |
| ❌ | `public_apis_list` | 0.0% | 99.65% | 126.4 | 3806.8 | 1500ms | 1/282 |
| ❌ | `nasa_apod` | 69.15% | 48.58% | 3435.1 | 10538.0 | 2000ms | 145/282 |
| ❌ | `ipapi_check` | 94.33% | 100.0% | 159.0 | 353.0 | 2500ms | 0/282 |
| ⚠️ | `open_meteo_weather` | 97.16% | 96.1% | 825.3 | 14877.1 | 2000ms | 11/282 |
| ⚠️ | `dog_ceo_random` | 99.29% | 85.46% | 1082.6 | 5586.8 | 2500ms | 41/282 |
| ✅ | `useless_fact` | 99.29% | 99.65% | 574.5 | 10229.6 | 2500ms | 1/282 |
| ✅ | `catfact_random` | 99.29% | 99.65% | 260.2 | 10070.5 | 3000ms | 1/282 |
| ✅ | `agify_name` | 100.0% | 99.65% | 387.5 | 3237.1 | 2000ms | 1/282 |
| ✅ | `rest_countries` | 100.0% | 98.94% | 274.3 | 7269.1 | 2500ms | 3/282 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.65% | 239.7 | 2314.9 | 2000ms | 1/282 |
| ✅ | `coingecko_bitcoin` | 100.0% | 100.0% | 100.8 | 252.0 | 1500ms | 0/282 |

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
| `nasa_apod` | 19:00 | 3524.3 | 50.0% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
