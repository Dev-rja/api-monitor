# API Reliability Monitor — SLA Report

> Last updated: **2026-04-18 16:24 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **79.5%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 77.46% | 2507.6 | 10206.7 | 1000ms | 80/355 |
| ❌ | `public_apis_list` | 0.0% | 99.72% | 124.4 | 3806.8 | 1500ms | 1/355 |
| ❌ | `nasa_apod` | 65.35% | 41.69% | 3944.3 | 10538.0 | 2000ms | 207/355 |
| ❌ | `ipapi_check` | 93.24% | 100.0% | 160.4 | 353.0 | 2500ms | 0/355 |
| ⚠️ | `open_meteo_weather` | 97.75% | 96.62% | 773.3 | 14877.1 | 2000ms | 12/355 |
| ⚠️ | `dog_ceo_random` | 99.15% | 88.17% | 960.8 | 10244.1 | 2500ms | 42/355 |
| ✅ | `useless_fact` | 99.44% | 99.15% | 583.6 | 10229.6 | 2500ms | 3/355 |
| ✅ | `catfact_random` | 99.44% | 99.72% | 248.3 | 10070.5 | 3000ms | 1/355 |
| ✅ | `agify_name` | 100.0% | 99.72% | 376.9 | 3237.1 | 2000ms | 1/355 |
| ✅ | `rest_countries` | 100.0% | 98.87% | 267.4 | 7269.1 | 2500ms | 4/355 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.72% | 237.3 | 2314.9 | 2000ms | 1/355 |
| ✅ | `coingecko_bitcoin` | 100.0% | 100.0% | 101.5 | 252.0 | 1500ms | 0/355 |

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
| `nasa_apod` | 14:00 | 4031.8 | 57.14% |
| `nasa_apod` | 12:00 | 3997.0 | 60.0% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
