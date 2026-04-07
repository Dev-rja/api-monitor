# API Reliability Monitor — SLA Report

> Last updated: **2026-04-07 15:52 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **5/12** &nbsp;|&nbsp; Avg uptime: **81.2%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 100.0% | 306.6 | 524.7 | 1000ms | 0/135 |
| ❌ | `public_apis_list` | 0.0% | 100.0% | 117.1 | 234.1 | 1500ms | 0/135 |
| ❌ | `nasa_apod` | 91.11% | 68.15% | 1787.7 | 10538.0 | 2000ms | 43/135 |
| ❌ | `ipapi_check` | 92.59% | 100.0% | 156.1 | 252.2 | 2500ms | 0/135 |
| ❌ | `open_meteo_weather` | 94.07% | 94.81% | 1040.3 | 14877.1 | 2000ms | 7/135 |
| ❌ | `dog_ceo_random` | 98.52% | 70.37% | 1830.5 | 5586.8 | 2500ms | 40/135 |
| ⚠️ | `useless_fact` | 98.52% | 99.26% | 634.8 | 10229.6 | 2500ms | 1/135 |
| ✅ | `catfact_random` | 99.26% | 100.0% | 239.4 | 1218.5 | 3000ms | 0/135 |
| ✅ | `agify_name` | 100.0% | 99.26% | 409.7 | 3237.1 | 2000ms | 1/135 |
| ✅ | `rest_countries` | 100.0% | 98.52% | 309.4 | 7269.1 | 2500ms | 2/135 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.26% | 252.2 | 2314.9 | 2000ms | 1/135 |
| ✅ | `coingecko_bitcoin` | 100.0% | 100.0% | 102.2 | 252.0 | 1500ms | 0/135 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `useless_fact` | 03:00 | 5454.5 | 50.0% |
| `open_meteo_weather` | 05:00 | 4216.1 | 25.0% |
| `dog_ceo_random` | 13:00 | 4153.6 | 100.0% |
| `nasa_apod` | 13:00 | 3279.6 | 50.0% |
| `nasa_apod` | 11:00 | 3203.4 | 50.0% |
| `open_meteo_weather` | 06:00 | 3112.1 | 20.0% |
| `nasa_apod` | 20:00 | 3095.4 | 44.44% |
| `dog_ceo_random` | 12:00 | 3057.6 | 50.0% |
| `nasa_apod` | 22:00 | 2952.7 | 33.33% |
| `dog_ceo_random` | 17:00 | 2937.7 | 71.43% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
