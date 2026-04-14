# API Reliability Monitor — SLA Report

> Last updated: **2026-04-14 15:53 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **79.9%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 98.21% | 475.5 | 10117.1 | 1000ms | 5/280 |
| ❌ | `public_apis_list` | 0.0% | 99.64% | 126.9 | 3806.8 | 1500ms | 1/280 |
| ❌ | `nasa_apod` | 69.29% | 48.93% | 3412.7 | 10538.0 | 2000ms | 143/280 |
| ❌ | `ipapi_check` | 94.29% | 100.0% | 158.6 | 353.0 | 2500ms | 0/280 |
| ⚠️ | `open_meteo_weather` | 97.14% | 96.07% | 827.5 | 14877.1 | 2000ms | 11/280 |
| ⚠️ | `dog_ceo_random` | 99.29% | 85.36% | 1087.2 | 5586.8 | 2500ms | 41/280 |
| ✅ | `useless_fact` | 99.29% | 99.64% | 575.3 | 10229.6 | 2500ms | 1/280 |
| ✅ | `catfact_random` | 99.29% | 99.64% | 260.3 | 10070.5 | 3000ms | 1/280 |
| ✅ | `agify_name` | 100.0% | 99.64% | 387.2 | 3237.1 | 2000ms | 1/280 |
| ✅ | `rest_countries` | 100.0% | 98.93% | 274.9 | 7269.1 | 2500ms | 3/280 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.64% | 239.7 | 2314.9 | 2000ms | 1/280 |
| ✅ | `coingecko_bitcoin` | 100.0% | 100.0% | 100.6 | 252.0 | 1500ms | 0/280 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `nasa_apod` | 03:00 | 5624.1 | 85.71% |
| `nasa_apod` | 20:00 | 4763.5 | 63.16% |
| `nasa_apod` | 18:00 | 4464.9 | 72.73% |
| `nasa_apod` | 14:00 | 4442.8 | 50.0% |
| `nasa_apod` | 17:00 | 4072.6 | 53.33% |
| `nasa_apod` | 08:00 | 3821.0 | 58.33% |
| `nasa_apod` | 11:00 | 3748.3 | 55.56% |
| `nasa_apod` | 13:00 | 3734.4 | 57.14% |
| `nasa_apod` | 23:00 | 3531.7 | 42.86% |
| `nasa_apod` | 19:00 | 3524.3 | 50.0% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
