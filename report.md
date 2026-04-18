# API Reliability Monitor — SLA Report

> Last updated: **2026-04-18 23:28 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **79.5%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 75.34% | 2715.1 | 10206.7 | 1000ms | 90/365 |
| ❌ | `public_apis_list` | 0.0% | 99.73% | 122.7 | 3806.8 | 1500ms | 1/365 |
| ❌ | `nasa_apod` | 64.66% | 41.37% | 4016.0 | 10538.0 | 2000ms | 214/365 |
| ❌ | `ipapi_check` | 93.42% | 100.0% | 160.0 | 353.0 | 2500ms | 0/365 |
| ⚠️ | `open_meteo_weather` | 97.81% | 96.71% | 766.8 | 14877.1 | 2000ms | 12/365 |
| ⚠️ | `dog_ceo_random` | 99.18% | 88.49% | 945.7 | 10244.1 | 2500ms | 42/365 |
| ✅ | `useless_fact` | 99.45% | 99.18% | 582.1 | 10229.6 | 2500ms | 3/365 |
| ✅ | `catfact_random` | 99.45% | 99.73% | 246.7 | 10070.5 | 3000ms | 1/365 |
| ✅ | `agify_name` | 100.0% | 99.73% | 375.7 | 3237.1 | 2000ms | 1/365 |
| ✅ | `rest_countries` | 100.0% | 98.9% | 266.1 | 7269.1 | 2500ms | 4/365 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.73% | 236.4 | 2314.9 | 2000ms | 1/365 |
| ✅ | `coingecko_bitcoin` | 100.0% | 100.0% | 101.2 | 252.0 | 1500ms | 0/365 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `nasa_apod` | 03:00 | 5840.5 | 88.89% |
| `nasa_apod` | 17:00 | 5121.2 | 66.67% |
| `nasa_apod` | 18:00 | 4979.5 | 80.0% |
| `nasa_apod` | 20:00 | 4677.6 | 64.0% |
| `nasa_apod` | 11:00 | 4496.8 | 59.09% |
| `nasa_apod` | 21:00 | 4275.9 | 47.62% |
| `numbers_trivia` | 00:00 | 4205.1 | 40.0% |
| `nasa_apod` | 23:00 | 4115.2 | 51.85% |
| `nasa_apod` | 08:00 | 4055.4 | 57.14% |
| `nasa_apod` | 14:00 | 4031.8 | 57.14% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
