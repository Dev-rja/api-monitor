# API Reliability Monitor — SLA Report

> Last updated: **2026-04-19 12:04 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **79.5%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 73.33% | 2911.6 | 10206.7 | 1000ms | 100/375 |
| ❌ | `public_apis_list` | 0.0% | 99.73% | 122.5 | 3806.8 | 1500ms | 1/375 |
| ❌ | `nasa_apod` | 64.8% | 41.07% | 4012.9 | 10538.0 | 2000ms | 221/375 |
| ❌ | `ipapi_check` | 93.6% | 100.0% | 159.8 | 353.0 | 2500ms | 0/375 |
| ⚠️ | `open_meteo_weather` | 97.87% | 96.8% | 761.0 | 14877.1 | 2000ms | 12/375 |
| ⚠️ | `dog_ceo_random` | 99.2% | 88.8% | 929.1 | 10244.1 | 2500ms | 42/375 |
| ✅ | `useless_fact` | 99.47% | 98.93% | 592.0 | 10229.6 | 2500ms | 4/375 |
| ✅ | `catfact_random` | 99.47% | 99.73% | 246.2 | 10070.5 | 3000ms | 1/375 |
| ✅ | `agify_name` | 100.0% | 99.73% | 374.8 | 3237.1 | 2000ms | 1/375 |
| ✅ | `rest_countries` | 100.0% | 98.93% | 264.8 | 7269.1 | 2500ms | 4/375 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.73% | 235.3 | 2314.9 | 2000ms | 1/375 |
| ✅ | `coingecko_bitcoin` | 100.0% | 100.0% | 101.1 | 252.0 | 1500ms | 0/375 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `nasa_apod` | 03:00 | 5533.2 | 90.0% |
| `numbers_trivia` | 00:00 | 5183.1 | 50.0% |
| `nasa_apod` | 17:00 | 5121.2 | 66.67% |
| `nasa_apod` | 18:00 | 4979.5 | 80.0% |
| `nasa_apod` | 11:00 | 4750.3 | 60.87% |
| `nasa_apod` | 20:00 | 4677.6 | 64.0% |
| `nasa_apod` | 12:00 | 4380.0 | 62.5% |
| `nasa_apod` | 21:00 | 4275.9 | 47.62% |
| `nasa_apod` | 23:00 | 4115.2 | 51.85% |
| `numbers_trivia` | 10:00 | 4091.8 | 38.89% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
