# API Reliability Monitor — SLA Report

> Last updated: **2026-04-19 14:09 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **79.5%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 72.94% | 2950.0 | 10206.7 | 1000ms | 102/377 |
| ❌ | `public_apis_list` | 0.0% | 99.73% | 122.2 | 3806.8 | 1500ms | 1/377 |
| ❌ | `nasa_apod` | 64.46% | 40.85% | 4046.7 | 10538.0 | 2000ms | 223/377 |
| ❌ | `ipapi_check` | 93.63% | 100.0% | 159.8 | 353.0 | 2500ms | 0/377 |
| ⚠️ | `open_meteo_weather` | 97.88% | 96.82% | 759.8 | 14877.1 | 2000ms | 12/377 |
| ⚠️ | `dog_ceo_random` | 99.2% | 88.86% | 926.7 | 10244.1 | 2500ms | 42/377 |
| ✅ | `useless_fact` | 99.47% | 98.94% | 591.7 | 10229.6 | 2500ms | 4/377 |
| ✅ | `catfact_random` | 99.47% | 99.73% | 245.6 | 10070.5 | 3000ms | 1/377 |
| ✅ | `agify_name` | 100.0% | 99.73% | 374.4 | 3237.1 | 2000ms | 1/377 |
| ✅ | `rest_countries` | 100.0% | 98.94% | 264.2 | 7269.1 | 2500ms | 4/377 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.73% | 235.2 | 2314.9 | 2000ms | 1/377 |
| ✅ | `coingecko_bitcoin` | 100.0% | 100.0% | 101.2 | 252.0 | 1500ms | 0/377 |

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
| `nasa_apod` | 13:00 | 4333.9 | 66.67% |
| `nasa_apod` | 14:00 | 4325.3 | 59.09% |
| `nasa_apod` | 21:00 | 4275.9 | 47.62% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
