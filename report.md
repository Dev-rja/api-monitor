# API Reliability Monitor — SLA Report

> Last updated: **2026-04-07 09:37 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **5/12** &nbsp;|&nbsp; Avg uptime: **81.3%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 100.0% | 303.5 | 524.7 | 1000ms | 0/130 |
| ❌ | `public_apis_list` | 0.0% | 100.0% | 115.7 | 234.1 | 1500ms | 0/130 |
| ❌ | `nasa_apod` | 90.77% | 67.69% | 1825.8 | 10538.0 | 2000ms | 42/130 |
| ❌ | `ipapi_check` | 93.85% | 100.0% | 156.8 | 252.2 | 2500ms | 0/130 |
| ❌ | `open_meteo_weather` | 94.62% | 96.15% | 912.7 | 14877.1 | 2000ms | 5/130 |
| ❌ | `dog_ceo_random` | 98.46% | 70.0% | 1823.0 | 5586.8 | 2500ms | 39/130 |
| ⚠️ | `useless_fact` | 98.46% | 99.23% | 636.0 | 10229.6 | 2500ms | 1/130 |
| ✅ | `catfact_random` | 99.23% | 100.0% | 237.2 | 1218.5 | 3000ms | 0/130 |
| ✅ | `agify_name` | 100.0% | 99.23% | 408.1 | 3237.1 | 2000ms | 1/130 |
| ✅ | `rest_countries` | 100.0% | 98.46% | 311.0 | 7269.1 | 2500ms | 2/130 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.23% | 254.8 | 2314.9 | 2000ms | 1/130 |
| ✅ | `coingecko_bitcoin` | 100.0% | 100.0% | 102.8 | 252.0 | 1500ms | 0/130 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `useless_fact` | 03:00 | 5454.5 | 50.0% |
| `open_meteo_weather` | 05:00 | 4216.1 | 25.0% |
| `dog_ceo_random` | 13:00 | 4153.6 | 100.0% |
| `nasa_apod` | 11:00 | 3500.1 | 55.56% |
| `nasa_apod` | 13:00 | 3279.6 | 50.0% |
| `open_meteo_weather` | 06:00 | 3112.1 | 20.0% |
| `nasa_apod` | 20:00 | 3095.4 | 44.44% |
| `nasa_apod` | 22:00 | 2952.7 | 33.33% |
| `dog_ceo_random` | 17:00 | 2937.7 | 71.43% |
| `nasa_apod` | 10:00 | 2892.2 | 25.0% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
