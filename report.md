# API Reliability Monitor — SLA Report

> Last updated: **2026-04-18 13:24 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **79.5%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 78.35% | 2421.3 | 10206.7 | 1000ms | 76/351 |
| ❌ | `public_apis_list` | 0.0% | 99.72% | 124.4 | 3806.8 | 1500ms | 1/351 |
| ❌ | `nasa_apod` | 65.53% | 42.17% | 3929.9 | 10538.0 | 2000ms | 203/351 |
| ❌ | `ipapi_check` | 93.16% | 100.0% | 160.5 | 353.0 | 2500ms | 0/351 |
| ⚠️ | `open_meteo_weather` | 97.72% | 96.58% | 775.7 | 14877.1 | 2000ms | 12/351 |
| ⚠️ | `dog_ceo_random` | 99.15% | 88.03% | 968.6 | 10244.1 | 2500ms | 42/351 |
| ✅ | `useless_fact` | 99.43% | 99.15% | 584.1 | 10229.6 | 2500ms | 3/351 |
| ✅ | `catfact_random` | 99.43% | 99.72% | 248.8 | 10070.5 | 3000ms | 1/351 |
| ✅ | `agify_name` | 100.0% | 99.72% | 377.8 | 3237.1 | 2000ms | 1/351 |
| ✅ | `rest_countries` | 100.0% | 98.86% | 268.0 | 7269.1 | 2500ms | 4/351 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.72% | 237.9 | 2314.9 | 2000ms | 1/351 |
| ✅ | `coingecko_bitcoin` | 100.0% | 100.0% | 101.6 | 252.0 | 1500ms | 0/351 |

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
