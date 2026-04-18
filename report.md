# API Reliability Monitor — SLA Report

> Last updated: **2026-04-18 07:00 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **79.5%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 79.94% | 2265.3 | 10206.7 | 1000ms | 69/344 |
| ❌ | `public_apis_list` | 0.0% | 99.71% | 124.7 | 3806.8 | 1500ms | 1/344 |
| ❌ | `nasa_apod` | 65.7% | 42.44% | 3901.8 | 10538.0 | 2000ms | 198/344 |
| ❌ | `ipapi_check` | 93.02% | 100.0% | 160.7 | 353.0 | 2500ms | 0/344 |
| ⚠️ | `open_meteo_weather` | 97.67% | 96.51% | 780.7 | 14877.1 | 2000ms | 12/344 |
| ⚠️ | `dog_ceo_random` | 99.13% | 87.79% | 981.9 | 10244.1 | 2500ms | 42/344 |
| ✅ | `useless_fact` | 99.42% | 99.13% | 585.0 | 10229.6 | 2500ms | 3/344 |
| ✅ | `catfact_random` | 99.42% | 99.71% | 250.0 | 10070.5 | 3000ms | 1/344 |
| ✅ | `agify_name` | 100.0% | 99.71% | 377.5 | 3237.1 | 2000ms | 1/344 |
| ✅ | `rest_countries` | 100.0% | 98.84% | 269.8 | 7269.1 | 2500ms | 4/344 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.71% | 238.9 | 2314.9 | 2000ms | 1/344 |
| ✅ | `coingecko_bitcoin` | 100.0% | 100.0% | 101.7 | 252.0 | 1500ms | 0/344 |

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
| `nasa_apod` | 10:00 | 4174.0 | 53.33% |
| `nasa_apod` | 14:00 | 4029.0 | 52.63% |
| `nasa_apod` | 00:00 | 3961.1 | 60.0% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
