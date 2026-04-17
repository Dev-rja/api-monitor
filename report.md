# API Reliability Monitor — SLA Report

> Last updated: **2026-04-17 22:01 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **79.5%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 81.36% | 2126.1 | 10206.7 | 1000ms | 63/338 |
| ❌ | `public_apis_list` | 0.0% | 99.7% | 125.0 | 3806.8 | 1500ms | 1/338 |
| ❌ | `nasa_apod` | 65.38% | 43.2% | 3902.8 | 10538.0 | 2000ms | 192/338 |
| ❌ | `ipapi_check` | 92.9% | 100.0% | 160.5 | 353.0 | 2500ms | 0/338 |
| ⚠️ | `open_meteo_weather` | 97.63% | 96.45% | 785.5 | 14877.1 | 2000ms | 12/338 |
| ⚠️ | `dog_ceo_random` | 99.11% | 87.57% | 992.4 | 10244.1 | 2500ms | 42/338 |
| ✅ | `useless_fact` | 99.41% | 99.11% | 586.3 | 10229.6 | 2500ms | 3/338 |
| ✅ | `catfact_random` | 99.41% | 99.7% | 252.0 | 10070.5 | 3000ms | 1/338 |
| ✅ | `agify_name` | 100.0% | 99.7% | 378.7 | 3237.1 | 2000ms | 1/338 |
| ✅ | `rest_countries` | 100.0% | 98.82% | 271.0 | 7269.1 | 2500ms | 4/338 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.7% | 239.1 | 2314.9 | 2000ms | 1/338 |
| ✅ | `coingecko_bitcoin` | 100.0% | 100.0% | 101.9 | 252.0 | 1500ms | 0/338 |

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
| `nasa_apod` | 05:00 | 3989.9 | 66.67% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
