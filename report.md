# API Reliability Monitor — SLA Report

> Last updated: **2026-04-19 10:55 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **79.6%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 73.73% | 2873.3 | 10206.7 | 1000ms | 98/373 |
| ❌ | `public_apis_list` | 0.0% | 99.73% | 122.9 | 3806.8 | 1500ms | 1/373 |
| ❌ | `nasa_apod` | 65.15% | 41.29% | 3979.5 | 10538.0 | 2000ms | 219/373 |
| ❌ | `ipapi_check` | 93.57% | 100.0% | 159.9 | 353.0 | 2500ms | 0/373 |
| ⚠️ | `open_meteo_weather` | 97.86% | 96.78% | 762.1 | 14877.1 | 2000ms | 12/373 |
| ⚠️ | `dog_ceo_random` | 99.2% | 88.74% | 932.5 | 10244.1 | 2500ms | 42/373 |
| ✅ | `useless_fact` | 99.46% | 98.93% | 592.3 | 10229.6 | 2500ms | 4/373 |
| ✅ | `catfact_random` | 99.46% | 99.73% | 246.0 | 10070.5 | 3000ms | 1/373 |
| ✅ | `agify_name` | 100.0% | 99.73% | 375.1 | 3237.1 | 2000ms | 1/373 |
| ✅ | `rest_countries` | 100.0% | 98.93% | 265.2 | 7269.1 | 2500ms | 4/373 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.73% | 235.7 | 2314.9 | 2000ms | 1/373 |
| ✅ | `coingecko_bitcoin` | 100.0% | 100.0% | 101.2 | 252.0 | 1500ms | 0/373 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `nasa_apod` | 03:00 | 5533.2 | 90.0% |
| `numbers_trivia` | 00:00 | 5183.1 | 50.0% |
| `nasa_apod` | 17:00 | 5121.2 | 66.67% |
| `nasa_apod` | 18:00 | 4979.5 | 80.0% |
| `nasa_apod` | 20:00 | 4677.6 | 64.0% |
| `nasa_apod` | 11:00 | 4496.8 | 59.09% |
| `nasa_apod` | 21:00 | 4275.9 | 47.62% |
| `nasa_apod` | 23:00 | 4115.2 | 51.85% |
| `numbers_trivia` | 10:00 | 4091.8 | 38.89% |
| `numbers_trivia` | 07:00 | 4087.0 | 38.46% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
