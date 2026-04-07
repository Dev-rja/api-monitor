# API Reliability Monitor — SLA Report

> Last updated: **2026-04-07 03:29 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **81.6%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 100.0% | 303.0 | 524.7 | 1000ms | 0/126 |
| ❌ | `public_apis_list` | 0.0% | 100.0% | 114.6 | 234.1 | 1500ms | 0/126 |
| ❌ | `nasa_apod` | 90.48% | 66.67% | 1868.0 | 10538.0 | 2000ms | 42/126 |
| ❌ | `ipapi_check` | 94.44% | 100.0% | 156.4 | 252.2 | 2500ms | 0/126 |
| ⚠️ | `open_meteo_weather` | 97.62% | 99.21% | 570.2 | 2550.7 | 2000ms | 1/126 |
| ❌ | `dog_ceo_random` | 98.41% | 69.05% | 1842.4 | 5586.8 | 2500ms | 39/126 |
| ✅ | `useless_fact` | 99.21% | 99.21% | 640.4 | 10229.6 | 2500ms | 1/126 |
| ✅ | `catfact_random` | 99.21% | 100.0% | 237.7 | 1218.5 | 3000ms | 0/126 |
| ✅ | `agify_name` | 100.0% | 99.21% | 409.3 | 3237.1 | 2000ms | 1/126 |
| ✅ | `rest_countries` | 100.0% | 98.41% | 313.0 | 7269.1 | 2500ms | 2/126 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.21% | 254.7 | 2314.9 | 2000ms | 1/126 |
| ✅ | `coingecko_bitcoin` | 100.0% | 100.0% | 102.4 | 252.0 | 1500ms | 0/126 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `useless_fact` | 03:00 | 5454.5 | 50.0% |
| `dog_ceo_random` | 13:00 | 4153.6 | 100.0% |
| `nasa_apod` | 11:00 | 3500.1 | 55.56% |
| `nasa_apod` | 13:00 | 3279.6 | 50.0% |
| `nasa_apod` | 20:00 | 3095.4 | 44.44% |
| `nasa_apod` | 22:00 | 2952.7 | 33.33% |
| `dog_ceo_random` | 17:00 | 2937.7 | 71.43% |
| `nasa_apod` | 10:00 | 2892.2 | 25.0% |
| `dog_ceo_random` | 11:00 | 2626.8 | 66.67% |
| `dog_ceo_random` | 14:00 | 2625.3 | 71.43% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
