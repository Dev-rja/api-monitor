# API Reliability Monitor — SLA Report

> Last updated: **2026-04-16 21:54 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **79.6%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 86.21% | 1651.6 | 10206.7 | 1000ms | 44/319 |
| ❌ | `public_apis_list` | 0.0% | 99.69% | 127.0 | 3806.8 | 1500ms | 1/319 |
| ❌ | `nasa_apod` | 66.14% | 44.51% | 3796.0 | 10538.0 | 2000ms | 177/319 |
| ❌ | `ipapi_check` | 93.1% | 100.0% | 159.8 | 353.0 | 2500ms | 0/319 |
| ⚠️ | `open_meteo_weather` | 97.49% | 96.24% | 800.5 | 14877.1 | 2000ms | 12/319 |
| ⚠️ | `dog_ceo_random` | 99.37% | 87.15% | 1000.2 | 5586.8 | 2500ms | 41/319 |
| ✅ | `useless_fact` | 99.37% | 99.69% | 567.8 | 10229.6 | 2500ms | 1/319 |
| ✅ | `catfact_random` | 99.37% | 99.69% | 255.4 | 10070.5 | 3000ms | 1/319 |
| ✅ | `agify_name` | 100.0% | 99.69% | 381.2 | 3237.1 | 2000ms | 1/319 |
| ✅ | `rest_countries` | 100.0% | 98.75% | 276.2 | 7269.1 | 2500ms | 4/319 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.69% | 240.1 | 2314.9 | 2000ms | 1/319 |
| ✅ | `coingecko_bitcoin` | 100.0% | 100.0% | 101.1 | 252.0 | 1500ms | 0/319 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `nasa_apod` | 03:00 | 5273.5 | 87.5% |
| `nasa_apod` | 20:00 | 4815.7 | 68.18% |
| `nasa_apod` | 18:00 | 4765.6 | 76.92% |
| `nasa_apod` | 17:00 | 4677.2 | 61.11% |
| `nasa_apod` | 10:00 | 4445.3 | 57.14% |
| `nasa_apod` | 11:00 | 4414.7 | 60.0% |
| `nasa_apod` | 14:00 | 4220.6 | 55.56% |
| `nasa_apod` | 21:00 | 4054.0 | 42.11% |
| `nasa_apod` | 13:00 | 3734.4 | 57.14% |
| `nasa_apod` | 15:00 | 3689.4 | 62.5% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
