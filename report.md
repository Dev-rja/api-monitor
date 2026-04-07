# API Reliability Monitor — SLA Report

> Last updated: **2026-04-07 14:21 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **5/12** &nbsp;|&nbsp; Avg uptime: **81.2%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 100.0% | 305.5 | 524.7 | 1000ms | 0/134 |
| ❌ | `public_apis_list` | 0.0% | 100.0% | 116.5 | 234.1 | 1500ms | 0/134 |
| ❌ | `nasa_apod` | 91.04% | 67.91% | 1799.2 | 10538.0 | 2000ms | 43/134 |
| ❌ | `ipapi_check` | 92.54% | 100.0% | 156.6 | 252.2 | 2500ms | 0/134 |
| ❌ | `open_meteo_weather` | 94.03% | 94.78% | 1042.9 | 14877.1 | 2000ms | 7/134 |
| ❌ | `dog_ceo_random` | 98.51% | 70.15% | 1841.5 | 5586.8 | 2500ms | 40/134 |
| ⚠️ | `useless_fact` | 98.51% | 99.25% | 634.3 | 10229.6 | 2500ms | 1/134 |
| ✅ | `catfact_random` | 99.25% | 100.0% | 239.4 | 1218.5 | 3000ms | 0/134 |
| ✅ | `agify_name` | 100.0% | 99.25% | 409.0 | 3237.1 | 2000ms | 1/134 |
| ✅ | `rest_countries` | 100.0% | 98.51% | 309.5 | 7269.1 | 2500ms | 2/134 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.25% | 253.2 | 2314.9 | 2000ms | 1/134 |
| ✅ | `coingecko_bitcoin` | 100.0% | 100.0% | 102.5 | 252.0 | 1500ms | 0/134 |

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
