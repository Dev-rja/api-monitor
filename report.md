# API Reliability Monitor — SLA Report

> Last updated: **2026-04-17 12:42 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **79.5%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 83.59% | 1908.3 | 10206.7 | 1000ms | 54/329 |
| ❌ | `public_apis_list` | 0.0% | 99.7% | 126.9 | 3806.8 | 1500ms | 1/329 |
| ❌ | `nasa_apod` | 65.35% | 43.47% | 3893.2 | 10538.0 | 2000ms | 186/329 |
| ❌ | `ipapi_check` | 93.31% | 100.0% | 160.3 | 353.0 | 2500ms | 0/329 |
| ⚠️ | `open_meteo_weather` | 97.57% | 96.35% | 792.5 | 14877.1 | 2000ms | 12/329 |
| ⚠️ | `dog_ceo_random` | 99.39% | 87.54% | 980.8 | 5586.8 | 2500ms | 41/329 |
| ✅ | `useless_fact` | 99.39% | 99.09% | 589.0 | 10229.6 | 2500ms | 3/329 |
| ✅ | `catfact_random` | 99.39% | 99.7% | 254.0 | 10070.5 | 3000ms | 1/329 |
| ✅ | `agify_name` | 100.0% | 99.7% | 381.3 | 3237.1 | 2000ms | 1/329 |
| ✅ | `rest_countries` | 100.0% | 98.78% | 273.6 | 7269.1 | 2500ms | 4/329 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.7% | 239.8 | 2314.9 | 2000ms | 1/329 |
| ✅ | `coingecko_bitcoin` | 100.0% | 100.0% | 101.8 | 252.0 | 1500ms | 0/329 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `nasa_apod` | 03:00 | 5840.5 | 88.89% |
| `nasa_apod` | 20:00 | 4815.7 | 68.18% |
| `nasa_apod` | 18:00 | 4765.6 | 76.92% |
| `nasa_apod` | 11:00 | 4698.9 | 61.9% |
| `nasa_apod` | 17:00 | 4677.2 | 61.11% |
| `nasa_apod` | 14:00 | 4220.6 | 55.56% |
| `numbers_trivia` | 00:00 | 4205.1 | 40.0% |
| `nasa_apod` | 10:00 | 4174.0 | 53.33% |
| `nasa_apod` | 21:00 | 4054.0 | 42.11% |
| `nasa_apod` | 05:00 | 3989.9 | 66.67% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
