# API Reliability Monitor — SLA Report

> Last updated: **2026-04-18 12:02 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **79.5%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 78.57% | 2399.4 | 10206.7 | 1000ms | 75/350 |
| ❌ | `public_apis_list` | 0.0% | 99.71% | 124.2 | 3806.8 | 1500ms | 1/350 |
| ❌ | `nasa_apod` | 65.43% | 42.29% | 3933.7 | 10538.0 | 2000ms | 202/350 |
| ❌ | `ipapi_check` | 93.14% | 100.0% | 160.5 | 353.0 | 2500ms | 0/350 |
| ⚠️ | `open_meteo_weather` | 97.71% | 96.57% | 776.5 | 14877.1 | 2000ms | 12/350 |
| ⚠️ | `dog_ceo_random` | 99.14% | 88.0% | 970.6 | 10244.1 | 2500ms | 42/350 |
| ✅ | `useless_fact` | 99.43% | 99.14% | 584.3 | 10229.6 | 2500ms | 3/350 |
| ✅ | `catfact_random` | 99.43% | 99.71% | 249.2 | 10070.5 | 3000ms | 1/350 |
| ✅ | `agify_name` | 100.0% | 99.71% | 377.2 | 3237.1 | 2000ms | 1/350 |
| ✅ | `rest_countries` | 100.0% | 98.86% | 268.5 | 7269.1 | 2500ms | 4/350 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.71% | 238.0 | 2314.9 | 2000ms | 1/350 |
| ✅ | `coingecko_bitcoin` | 100.0% | 100.0% | 101.5 | 252.0 | 1500ms | 0/350 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `nasa_apod` | 03:00 | 5840.5 | 88.89% |
| `nasa_apod` | 20:00 | 4616.2 | 65.22% |
| `nasa_apod` | 18:00 | 4610.5 | 78.57% |
| `nasa_apod` | 17:00 | 4582.4 | 63.16% |
| `nasa_apod` | 11:00 | 4496.8 | 59.09% |
| `nasa_apod` | 21:00 | 4372.0 | 45.0% |
| `numbers_trivia` | 00:00 | 4205.1 | 40.0% |
| `nasa_apod` | 08:00 | 4055.4 | 57.14% |
| `nasa_apod` | 14:00 | 4029.0 | 52.63% |
| `nasa_apod` | 12:00 | 3997.0 | 60.0% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
