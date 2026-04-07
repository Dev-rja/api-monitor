# API Reliability Monitor — SLA Report

> Last updated: **2026-04-07 21:54 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **5/12** &nbsp;|&nbsp; Avg uptime: **81.3%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 100.0% | 306.5 | 588.9 | 1000ms | 0/141 |
| ❌ | `public_apis_list` | 0.0% | 100.0% | 115.3 | 234.1 | 1500ms | 0/141 |
| ❌ | `nasa_apod` | 91.49% | 69.5% | 1730.6 | 10538.0 | 2000ms | 43/141 |
| ❌ | `ipapi_check` | 92.91% | 100.0% | 156.2 | 252.2 | 2500ms | 0/141 |
| ❌ | `open_meteo_weather` | 94.33% | 95.04% | 1018.4 | 14877.1 | 2000ms | 7/141 |
| ❌ | `dog_ceo_random` | 98.58% | 71.63% | 1766.4 | 5586.8 | 2500ms | 40/141 |
| ⚠️ | `useless_fact` | 98.58% | 99.29% | 629.2 | 10229.6 | 2500ms | 1/141 |
| ✅ | `catfact_random` | 99.29% | 100.0% | 238.2 | 1218.5 | 3000ms | 0/141 |
| ✅ | `agify_name` | 100.0% | 99.29% | 407.8 | 3237.1 | 2000ms | 1/141 |
| ✅ | `rest_countries` | 100.0% | 98.58% | 304.7 | 7269.1 | 2500ms | 2/141 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.29% | 251.9 | 2314.9 | 2000ms | 1/141 |
| ✅ | `coingecko_bitcoin` | 100.0% | 100.0% | 101.9 | 252.0 | 1500ms | 0/141 |

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
| `dog_ceo_random` | 12:00 | 3057.6 | 50.0% |
| `nasa_apod` | 22:00 | 2952.7 | 33.33% |
| `nasa_apod` | 20:00 | 2829.3 | 40.0% |
| `dog_ceo_random` | 17:00 | 2591.7 | 62.5% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
