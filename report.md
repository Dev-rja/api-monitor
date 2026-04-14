# API Reliability Monitor — SLA Report

> Last updated: **2026-04-14 10:24 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **80.0%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 99.64% | 336.5 | 10117.1 | 1000ms | 1/276 |
| ❌ | `public_apis_list` | 0.0% | 99.64% | 126.8 | 3806.8 | 1500ms | 1/276 |
| ❌ | `nasa_apod` | 69.93% | 49.64% | 3340.1 | 10538.0 | 2000ms | 139/276 |
| ❌ | `ipapi_check` | 94.57% | 100.0% | 158.4 | 353.0 | 2500ms | 0/276 |
| ⚠️ | `open_meteo_weather` | 97.1% | 96.01% | 832.5 | 14877.1 | 2000ms | 11/276 |
| ⚠️ | `dog_ceo_random` | 99.28% | 85.14% | 1098.4 | 5586.8 | 2500ms | 41/276 |
| ✅ | `useless_fact` | 99.28% | 99.64% | 577.2 | 10229.6 | 2500ms | 1/276 |
| ✅ | `catfact_random` | 99.28% | 99.64% | 260.2 | 10070.5 | 3000ms | 1/276 |
| ✅ | `agify_name` | 100.0% | 99.64% | 386.4 | 3237.1 | 2000ms | 1/276 |
| ✅ | `rest_countries` | 100.0% | 98.91% | 276.5 | 7269.1 | 2500ms | 3/276 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.64% | 238.0 | 2314.9 | 2000ms | 1/276 |
| ✅ | `coingecko_bitcoin` | 100.0% | 100.0% | 100.7 | 252.0 | 1500ms | 0/276 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `nasa_apod` | 03:00 | 5624.1 | 85.71% |
| `nasa_apod` | 20:00 | 4763.5 | 63.16% |
| `nasa_apod` | 18:00 | 4464.9 | 72.73% |
| `nasa_apod` | 17:00 | 4072.6 | 53.33% |
| `nasa_apod` | 14:00 | 4050.6 | 46.67% |
| `nasa_apod` | 08:00 | 3821.0 | 58.33% |
| `nasa_apod` | 13:00 | 3734.4 | 57.14% |
| `nasa_apod` | 23:00 | 3531.7 | 42.86% |
| `nasa_apod` | 19:00 | 3524.3 | 50.0% |
| `catfact_random` | 00:00 | 3471.7 | 33.33% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
