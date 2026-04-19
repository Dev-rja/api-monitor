# API Reliability Monitor — SLA Report

> Last updated: **2026-04-19 07:09 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **79.5%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 74.53% | 2795.2 | 10206.7 | 1000ms | 94/369 |
| ❌ | `public_apis_list` | 0.0% | 99.73% | 122.7 | 3806.8 | 1500ms | 1/369 |
| ❌ | `nasa_apod` | 64.77% | 40.92% | 4011.6 | 10538.0 | 2000ms | 218/369 |
| ❌ | `ipapi_check` | 93.5% | 100.0% | 159.9 | 353.0 | 2500ms | 0/369 |
| ⚠️ | `open_meteo_weather` | 97.83% | 96.75% | 764.4 | 14877.1 | 2000ms | 12/369 |
| ⚠️ | `dog_ceo_random` | 99.19% | 88.62% | 939.1 | 10244.1 | 2500ms | 42/369 |
| ✅ | `useless_fact` | 99.46% | 98.92% | 592.6 | 10229.6 | 2500ms | 4/369 |
| ✅ | `catfact_random` | 99.46% | 99.73% | 246.4 | 10070.5 | 3000ms | 1/369 |
| ✅ | `agify_name` | 100.0% | 99.73% | 375.4 | 3237.1 | 2000ms | 1/369 |
| ✅ | `rest_countries` | 100.0% | 98.92% | 265.5 | 7269.1 | 2500ms | 4/369 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.73% | 236.0 | 2314.9 | 2000ms | 1/369 |
| ✅ | `coingecko_bitcoin` | 100.0% | 100.0% | 101.4 | 252.0 | 1500ms | 0/369 |

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
| `numbers_trivia` | 07:00 | 4087.0 | 38.46% |
| `nasa_apod` | 05:00 | 4071.7 | 71.43% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
