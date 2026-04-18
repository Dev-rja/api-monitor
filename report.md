# API Reliability Monitor — SLA Report

> Last updated: **2026-04-18 10:53 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **79.5%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 79.02% | 2355.2 | 10206.7 | 1000ms | 73/348 |
| ❌ | `public_apis_list` | 0.0% | 99.71% | 124.2 | 3806.8 | 1500ms | 1/348 |
| ❌ | `nasa_apod` | 65.52% | 42.24% | 3925.4 | 10538.0 | 2000ms | 201/348 |
| ❌ | `ipapi_check` | 93.1% | 100.0% | 160.7 | 353.0 | 2500ms | 0/348 |
| ⚠️ | `open_meteo_weather` | 97.7% | 96.55% | 777.8 | 14877.1 | 2000ms | 12/348 |
| ⚠️ | `dog_ceo_random` | 99.14% | 87.93% | 973.9 | 10244.1 | 2500ms | 42/348 |
| ✅ | `useless_fact` | 99.43% | 99.14% | 584.3 | 10229.6 | 2500ms | 3/348 |
| ✅ | `catfact_random` | 99.43% | 99.71% | 248.5 | 10070.5 | 3000ms | 1/348 |
| ✅ | `agify_name` | 100.0% | 99.71% | 377.1 | 3237.1 | 2000ms | 1/348 |
| ✅ | `rest_countries` | 100.0% | 98.85% | 268.8 | 7269.1 | 2500ms | 4/348 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.71% | 238.2 | 2314.9 | 2000ms | 1/348 |
| ✅ | `coingecko_bitcoin` | 100.0% | 100.0% | 101.6 | 252.0 | 1500ms | 0/348 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `nasa_apod` | 03:00 | 5840.5 | 88.89% |
| `nasa_apod` | 11:00 | 4698.9 | 61.9% |
| `nasa_apod` | 20:00 | 4616.2 | 65.22% |
| `nasa_apod` | 18:00 | 4610.5 | 78.57% |
| `nasa_apod` | 17:00 | 4582.4 | 63.16% |
| `nasa_apod` | 21:00 | 4372.0 | 45.0% |
| `numbers_trivia` | 00:00 | 4205.1 | 40.0% |
| `nasa_apod` | 08:00 | 4055.4 | 57.14% |
| `nasa_apod` | 14:00 | 4029.0 | 52.63% |
| `nasa_apod` | 09:00 | 3986.3 | 52.63% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
