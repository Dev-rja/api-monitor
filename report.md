# API Reliability Monitor — SLA Report

> Last updated: **2026-04-19 00:03 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **79.5%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 75.14% | 2735.2 | 10206.7 | 1000ms | 91/366 |
| ❌ | `public_apis_list` | 0.0% | 99.73% | 122.9 | 3806.8 | 1500ms | 1/366 |
| ❌ | `nasa_apod` | 64.75% | 41.26% | 4012.1 | 10538.0 | 2000ms | 215/366 |
| ❌ | `ipapi_check` | 93.44% | 100.0% | 159.9 | 353.0 | 2500ms | 0/366 |
| ⚠️ | `open_meteo_weather` | 97.81% | 96.72% | 765.9 | 14877.1 | 2000ms | 12/366 |
| ⚠️ | `dog_ceo_random` | 99.18% | 88.52% | 944.2 | 10244.1 | 2500ms | 42/366 |
| ✅ | `useless_fact` | 99.45% | 98.91% | 593.1 | 10229.6 | 2500ms | 4/366 |
| ✅ | `catfact_random` | 99.45% | 99.73% | 246.2 | 10070.5 | 3000ms | 1/366 |
| ✅ | `agify_name` | 100.0% | 99.73% | 375.6 | 3237.1 | 2000ms | 1/366 |
| ✅ | `rest_countries` | 100.0% | 98.91% | 265.7 | 7269.1 | 2500ms | 4/366 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.73% | 236.1 | 2314.9 | 2000ms | 1/366 |
| ✅ | `coingecko_bitcoin` | 100.0% | 100.0% | 101.3 | 252.0 | 1500ms | 0/366 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `nasa_apod` | 03:00 | 5840.5 | 88.89% |
| `numbers_trivia` | 00:00 | 5183.1 | 50.0% |
| `nasa_apod` | 17:00 | 5121.2 | 66.67% |
| `nasa_apod` | 18:00 | 4979.5 | 80.0% |
| `nasa_apod` | 20:00 | 4677.6 | 64.0% |
| `nasa_apod` | 11:00 | 4496.8 | 59.09% |
| `nasa_apod` | 21:00 | 4275.9 | 47.62% |
| `nasa_apod` | 23:00 | 4115.2 | 51.85% |
| `nasa_apod` | 08:00 | 4055.4 | 57.14% |
| `nasa_apod` | 14:00 | 4031.8 | 57.14% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
