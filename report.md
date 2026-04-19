# API Reliability Monitor — SLA Report

> Last updated: **2026-04-19 13:24 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **79.5%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 73.14% | 2930.9 | 10206.7 | 1000ms | 101/376 |
| ❌ | `public_apis_list` | 0.0% | 99.73% | 122.4 | 3806.8 | 1500ms | 1/376 |
| ❌ | `nasa_apod` | 64.63% | 40.96% | 4029.5 | 10538.0 | 2000ms | 222/376 |
| ❌ | `ipapi_check` | 93.62% | 100.0% | 159.8 | 353.0 | 2500ms | 0/376 |
| ⚠️ | `open_meteo_weather` | 97.87% | 96.81% | 760.7 | 14877.1 | 2000ms | 12/376 |
| ⚠️ | `dog_ceo_random` | 99.2% | 88.83% | 928.2 | 10244.1 | 2500ms | 42/376 |
| ✅ | `useless_fact` | 99.47% | 98.94% | 591.9 | 10229.6 | 2500ms | 4/376 |
| ✅ | `catfact_random` | 99.47% | 99.73% | 246.0 | 10070.5 | 3000ms | 1/376 |
| ✅ | `agify_name` | 100.0% | 99.73% | 375.0 | 3237.1 | 2000ms | 1/376 |
| ✅ | `rest_countries` | 100.0% | 98.94% | 264.7 | 7269.1 | 2500ms | 4/376 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.73% | 235.5 | 2314.9 | 2000ms | 1/376 |
| ✅ | `coingecko_bitcoin` | 100.0% | 100.0% | 101.3 | 252.0 | 1500ms | 0/376 |

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
| `nasa_apod` | 21:00 | 4275.9 | 47.62% |
| `nasa_apod` | 23:00 | 4115.2 | 51.85% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
