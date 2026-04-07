# API Reliability Monitor — SLA Report

> Last updated: **2026-04-07 10:41 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **5/12** &nbsp;|&nbsp; Avg uptime: **81.3%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 100.0% | 304.2 | 524.7 | 1000ms | 0/131 |
| ❌ | `public_apis_list` | 0.0% | 100.0% | 116.2 | 234.1 | 1500ms | 0/131 |
| ❌ | `nasa_apod` | 90.84% | 67.94% | 1815.8 | 10538.0 | 2000ms | 42/131 |
| ❌ | `ipapi_check` | 93.89% | 100.0% | 157.1 | 252.2 | 2500ms | 0/131 |
| ❌ | `open_meteo_weather` | 94.66% | 95.42% | 949.5 | 14877.1 | 2000ms | 6/131 |
| ❌ | `dog_ceo_random` | 98.47% | 70.23% | 1824.9 | 5586.8 | 2500ms | 39/131 |
| ⚠️ | `useless_fact` | 98.47% | 99.24% | 635.1 | 10229.6 | 2500ms | 1/131 |
| ✅ | `catfact_random` | 99.24% | 100.0% | 237.8 | 1218.5 | 3000ms | 0/131 |
| ✅ | `agify_name` | 100.0% | 99.24% | 409.2 | 3237.1 | 2000ms | 1/131 |
| ✅ | `rest_countries` | 100.0% | 98.47% | 311.3 | 7269.1 | 2500ms | 2/131 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.24% | 255.0 | 2314.9 | 2000ms | 1/131 |
| ✅ | `coingecko_bitcoin` | 100.0% | 100.0% | 103.2 | 252.0 | 1500ms | 0/131 |

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
| `dog_ceo_random` | 11:00 | 2626.8 | 66.67% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
