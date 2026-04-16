# API Reliability Monitor — SLA Report

> Last updated: **2026-04-16 18:52 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **79.6%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 87.03% | 1571.4 | 10206.7 | 1000ms | 41/316 |
| ❌ | `public_apis_list` | 0.0% | 99.68% | 126.6 | 3806.8 | 1500ms | 1/316 |
| ❌ | `nasa_apod` | 66.46% | 44.62% | 3765.3 | 10538.0 | 2000ms | 175/316 |
| ❌ | `ipapi_check` | 93.04% | 100.0% | 159.6 | 353.0 | 2500ms | 0/316 |
| ⚠️ | `open_meteo_weather` | 97.47% | 96.2% | 803.1 | 14877.1 | 2000ms | 12/316 |
| ⚠️ | `dog_ceo_random` | 99.37% | 87.03% | 1007.0 | 5586.8 | 2500ms | 41/316 |
| ✅ | `useless_fact` | 99.37% | 99.68% | 569.1 | 10229.6 | 2500ms | 1/316 |
| ✅ | `catfact_random` | 99.37% | 99.68% | 254.8 | 10070.5 | 3000ms | 1/316 |
| ✅ | `agify_name` | 100.0% | 99.68% | 381.8 | 3237.1 | 2000ms | 1/316 |
| ✅ | `rest_countries` | 100.0% | 98.73% | 276.9 | 7269.1 | 2500ms | 4/316 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.68% | 239.7 | 2314.9 | 2000ms | 1/316 |
| ✅ | `coingecko_bitcoin` | 100.0% | 100.0% | 101.2 | 252.0 | 1500ms | 0/316 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `nasa_apod` | 03:00 | 5273.5 | 87.5% |
| `nasa_apod` | 18:00 | 4765.6 | 76.92% |
| `nasa_apod` | 17:00 | 4677.2 | 61.11% |
| `nasa_apod` | 20:00 | 4550.4 | 66.67% |
| `nasa_apod` | 10:00 | 4445.3 | 57.14% |
| `nasa_apod` | 11:00 | 4414.7 | 60.0% |
| `nasa_apod` | 14:00 | 4220.6 | 55.56% |
| `nasa_apod` | 13:00 | 3734.4 | 57.14% |
| `nasa_apod` | 21:00 | 3704.5 | 38.89% |
| `nasa_apod` | 15:00 | 3689.4 | 62.5% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
