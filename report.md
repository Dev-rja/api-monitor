# API Reliability Monitor — SLA Report

> Last updated: **2026-04-14 00:08 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **80.0%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 100.0% | 301.6 | 588.9 | 1000ms | 0/271 |
| ❌ | `public_apis_list` | 0.0% | 99.63% | 126.7 | 3806.8 | 1500ms | 1/271 |
| ❌ | `nasa_apod` | 70.11% | 50.55% | 3286.4 | 10538.0 | 2000ms | 134/271 |
| ❌ | `ipapi_check` | 94.83% | 100.0% | 158.3 | 353.0 | 2500ms | 0/271 |
| ⚠️ | `open_meteo_weather` | 97.05% | 95.94% | 838.2 | 14877.1 | 2000ms | 11/271 |
| ⚠️ | `dog_ceo_random` | 99.26% | 84.87% | 1111.7 | 5586.8 | 2500ms | 41/271 |
| ✅ | `useless_fact` | 99.26% | 99.63% | 578.4 | 10229.6 | 2500ms | 1/271 |
| ✅ | `catfact_random` | 99.26% | 99.63% | 262.2 | 10070.5 | 3000ms | 1/271 |
| ✅ | `agify_name` | 100.0% | 99.63% | 388.3 | 3237.1 | 2000ms | 1/271 |
| ✅ | `rest_countries` | 100.0% | 98.89% | 278.3 | 7269.1 | 2500ms | 3/271 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.63% | 239.1 | 2314.9 | 2000ms | 1/271 |
| ✅ | `coingecko_bitcoin` | 100.0% | 100.0% | 100.1 | 252.0 | 1500ms | 0/271 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `nasa_apod` | 03:00 | 4838.2 | 83.33% |
| `nasa_apod` | 20:00 | 4763.5 | 63.16% |
| `nasa_apod` | 18:00 | 4464.9 | 72.73% |
| `nasa_apod` | 17:00 | 4072.6 | 53.33% |
| `nasa_apod` | 14:00 | 4050.6 | 46.67% |
| `nasa_apod` | 13:00 | 3734.4 | 57.14% |
| `nasa_apod` | 10:00 | 3532.9 | 45.45% |
| `nasa_apod` | 23:00 | 3531.7 | 42.86% |
| `nasa_apod` | 19:00 | 3524.3 | 50.0% |
| `catfact_random` | 00:00 | 3471.7 | 33.33% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
