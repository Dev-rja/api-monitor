# API Reliability Monitor — SLA Report

> Last updated: **2026-04-07 11:40 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **5/12** &nbsp;|&nbsp; Avg uptime: **81.2%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 100.0% | 304.9 | 524.7 | 1000ms | 0/132 |
| ❌ | `public_apis_list` | 0.0% | 100.0% | 115.8 | 234.1 | 1500ms | 0/132 |
| ❌ | `nasa_apod` | 90.91% | 68.18% | 1806.1 | 10538.0 | 2000ms | 42/132 |
| ❌ | `ipapi_check` | 93.18% | 100.0% | 157.2 | 252.2 | 2500ms | 0/132 |
| ❌ | `open_meteo_weather` | 93.94% | 94.7% | 1050.3 | 14877.1 | 2000ms | 7/132 |
| ❌ | `dog_ceo_random` | 98.48% | 70.45% | 1825.9 | 5586.8 | 2500ms | 39/132 |
| ⚠️ | `useless_fact` | 98.48% | 99.24% | 636.6 | 10229.6 | 2500ms | 1/132 |
| ✅ | `catfact_random` | 99.24% | 100.0% | 240.1 | 1218.5 | 3000ms | 0/132 |
| ✅ | `agify_name` | 100.0% | 99.24% | 410.2 | 3237.1 | 2000ms | 1/132 |
| ✅ | `rest_countries` | 100.0% | 98.48% | 311.0 | 7269.1 | 2500ms | 2/132 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.24% | 254.5 | 2314.9 | 2000ms | 1/132 |
| ✅ | `coingecko_bitcoin` | 100.0% | 100.0% | 103.3 | 252.0 | 1500ms | 0/132 |

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
| `nasa_apod` | 22:00 | 2952.7 | 33.33% |
| `dog_ceo_random` | 17:00 | 2937.7 | 71.43% |
| `dog_ceo_random` | 14:00 | 2625.3 | 71.43% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
