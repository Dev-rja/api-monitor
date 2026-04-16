# API Reliability Monitor — SLA Report

> Last updated: **2026-04-16 11:37 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **79.6%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 88.42% | 1434.4 | 10206.7 | 1000ms | 36/311 |
| ❌ | `public_apis_list` | 0.0% | 99.68% | 127.1 | 3806.8 | 1500ms | 1/311 |
| ❌ | `nasa_apod` | 66.56% | 45.34% | 3735.8 | 10538.0 | 2000ms | 170/311 |
| ❌ | `ipapi_check` | 93.57% | 100.0% | 159.6 | 353.0 | 2500ms | 0/311 |
| ⚠️ | `open_meteo_weather` | 97.43% | 96.46% | 799.6 | 14877.1 | 2000ms | 11/311 |
| ⚠️ | `dog_ceo_random` | 99.36% | 86.82% | 1016.2 | 5586.8 | 2500ms | 41/311 |
| ✅ | `useless_fact` | 99.36% | 99.68% | 565.7 | 10229.6 | 2500ms | 1/311 |
| ✅ | `catfact_random` | 99.36% | 99.68% | 255.2 | 10070.5 | 3000ms | 1/311 |
| ✅ | `agify_name` | 100.0% | 99.68% | 382.6 | 3237.1 | 2000ms | 1/311 |
| ✅ | `rest_countries` | 100.0% | 98.71% | 277.9 | 7269.1 | 2500ms | 4/311 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.68% | 239.8 | 2314.9 | 2000ms | 1/311 |
| ✅ | `coingecko_bitcoin` | 100.0% | 100.0% | 101.0 | 252.0 | 1500ms | 0/311 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `nasa_apod` | 03:00 | 5273.5 | 87.5% |
| `nasa_apod` | 18:00 | 4952.5 | 75.0% |
| `nasa_apod` | 20:00 | 4550.4 | 66.67% |
| `nasa_apod` | 10:00 | 4445.3 | 57.14% |
| `nasa_apod` | 11:00 | 4414.7 | 60.0% |
| `nasa_apod` | 17:00 | 4370.4 | 58.82% |
| `nasa_apod` | 14:00 | 4321.9 | 52.94% |
| `nasa_apod` | 13:00 | 3734.4 | 57.14% |
| `nasa_apod` | 21:00 | 3704.5 | 38.89% |
| `nasa_apod` | 15:00 | 3689.4 | 62.5% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
