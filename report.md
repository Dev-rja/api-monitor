# API Reliability Monitor — SLA Report

> Last updated: **2026-04-18 17:06 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **79.5%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 77.25% | 2528.8 | 10206.7 | 1000ms | 81/356 |
| ❌ | `public_apis_list` | 0.0% | 99.72% | 124.2 | 3806.8 | 1500ms | 1/356 |
| ❌ | `nasa_apod` | 65.17% | 41.57% | 3961.8 | 10538.0 | 2000ms | 208/356 |
| ❌ | `ipapi_check` | 93.26% | 100.0% | 160.2 | 353.0 | 2500ms | 0/356 |
| ⚠️ | `open_meteo_weather` | 97.75% | 96.63% | 773.0 | 14877.1 | 2000ms | 12/356 |
| ⚠️ | `dog_ceo_random` | 99.16% | 88.2% | 959.3 | 10244.1 | 2500ms | 42/356 |
| ✅ | `useless_fact` | 99.44% | 99.16% | 584.0 | 10229.6 | 2500ms | 3/356 |
| ✅ | `catfact_random` | 99.44% | 99.72% | 248.0 | 10070.5 | 3000ms | 1/356 |
| ✅ | `agify_name` | 100.0% | 99.72% | 377.3 | 3237.1 | 2000ms | 1/356 |
| ✅ | `rest_countries` | 100.0% | 98.88% | 267.6 | 7269.1 | 2500ms | 4/356 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.72% | 236.9 | 2314.9 | 2000ms | 1/356 |
| ✅ | `coingecko_bitcoin` | 100.0% | 100.0% | 101.4 | 252.0 | 1500ms | 0/356 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `nasa_apod` | 03:00 | 5840.5 | 88.89% |
| `nasa_apod` | 17:00 | 4861.4 | 65.0% |
| `nasa_apod` | 20:00 | 4616.2 | 65.22% |
| `nasa_apod` | 18:00 | 4610.5 | 78.57% |
| `nasa_apod` | 11:00 | 4496.8 | 59.09% |
| `nasa_apod` | 21:00 | 4372.0 | 45.0% |
| `numbers_trivia` | 00:00 | 4205.1 | 40.0% |
| `nasa_apod` | 08:00 | 4055.4 | 57.14% |
| `nasa_apod` | 14:00 | 4031.8 | 57.14% |
| `nasa_apod` | 12:00 | 3997.0 | 60.0% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
