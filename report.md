# API Reliability Monitor — SLA Report

> Last updated: **2026-04-07 12:45 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **5/12** &nbsp;|&nbsp; Avg uptime: **81.2%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 100.0% | 304.5 | 524.7 | 1000ms | 0/133 |
| ❌ | `public_apis_list` | 0.0% | 100.0% | 116.4 | 234.1 | 1500ms | 0/133 |
| ❌ | `nasa_apod` | 90.98% | 68.42% | 1795.8 | 10538.0 | 2000ms | 42/133 |
| ❌ | `ipapi_check` | 93.23% | 100.0% | 157.2 | 252.2 | 2500ms | 0/133 |
| ❌ | `open_meteo_weather` | 93.98% | 94.74% | 1045.6 | 14877.1 | 2000ms | 7/133 |
| ❌ | `dog_ceo_random` | 98.5% | 69.92% | 1851.1 | 5586.8 | 2500ms | 40/133 |
| ⚠️ | `useless_fact` | 98.5% | 99.25% | 634.9 | 10229.6 | 2500ms | 1/133 |
| ✅ | `catfact_random` | 99.25% | 100.0% | 238.9 | 1218.5 | 3000ms | 0/133 |
| ✅ | `agify_name` | 100.0% | 99.25% | 408.2 | 3237.1 | 2000ms | 1/133 |
| ✅ | `rest_countries` | 100.0% | 98.5% | 309.8 | 7269.1 | 2500ms | 2/133 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.25% | 253.5 | 2314.9 | 2000ms | 1/133 |
| ✅ | `coingecko_bitcoin` | 100.0% | 100.0% | 102.9 | 252.0 | 1500ms | 0/133 |

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
