# API Reliability Monitor — SLA Report

> Last updated: **2026-04-18 17:53 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **79.5%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 77.03% | 2549.8 | 10206.7 | 1000ms | 82/357 |
| ❌ | `public_apis_list` | 0.0% | 99.72% | 124.0 | 3806.8 | 1500ms | 1/357 |
| ❌ | `nasa_apod` | 64.99% | 41.46% | 3979.6 | 10538.0 | 2000ms | 209/357 |
| ❌ | `ipapi_check` | 93.28% | 100.0% | 160.2 | 353.0 | 2500ms | 0/357 |
| ⚠️ | `open_meteo_weather` | 97.76% | 96.64% | 772.2 | 14877.1 | 2000ms | 12/357 |
| ⚠️ | `dog_ceo_random` | 99.16% | 88.24% | 957.7 | 10244.1 | 2500ms | 42/357 |
| ✅ | `useless_fact` | 99.44% | 99.16% | 583.4 | 10229.6 | 2500ms | 3/357 |
| ✅ | `catfact_random` | 99.44% | 99.72% | 248.5 | 10070.5 | 3000ms | 1/357 |
| ✅ | `agify_name` | 100.0% | 99.72% | 377.0 | 3237.1 | 2000ms | 1/357 |
| ✅ | `rest_countries` | 100.0% | 98.88% | 267.3 | 7269.1 | 2500ms | 4/357 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.72% | 237.0 | 2314.9 | 2000ms | 1/357 |
| ✅ | `coingecko_bitcoin` | 100.0% | 100.0% | 101.2 | 252.0 | 1500ms | 0/357 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `nasa_apod` | 03:00 | 5840.5 | 88.89% |
| `nasa_apod` | 17:00 | 5121.2 | 66.67% |
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
