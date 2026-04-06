# API Reliability Monitor — SLA Report

> Last updated: **2026-04-06 22:54 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **81.7%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 100.0% | 304.2 | 524.7 | 1000ms | 0/123 |
| ❌ | `public_apis_list` | 0.0% | 100.0% | 113.7 | 234.1 | 1500ms | 0/123 |
| ❌ | `nasa_apod` | 90.24% | 66.67% | 1886.3 | 10538.0 | 2000ms | 41/123 |
| ❌ | `ipapi_check` | 94.31% | 100.0% | 155.8 | 251.4 | 2500ms | 0/123 |
| ⚠️ | `open_meteo_weather` | 97.56% | 99.19% | 571.7 | 2550.7 | 2000ms | 1/123 |
| ❌ | `dog_ceo_random` | 98.37% | 68.29% | 1875.4 | 5586.8 | 2500ms | 39/123 |
| ✅ | `useless_fact` | 100.0% | 100.0% | 565.2 | 2439.0 | 2500ms | 0/123 |
| ✅ | `agify_name` | 100.0% | 99.19% | 412.4 | 3237.1 | 2000ms | 1/123 |
| ✅ | `rest_countries` | 100.0% | 98.37% | 317.0 | 7269.1 | 2500ms | 2/123 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.19% | 255.0 | 2314.9 | 2000ms | 1/123 |
| ✅ | `catfact_random` | 100.0% | 100.0% | 240.5 | 1218.5 | 3000ms | 0/123 |
| ✅ | `coingecko_bitcoin` | 100.0% | 100.0% | 102.0 | 252.0 | 1500ms | 0/123 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `dog_ceo_random` | 13:00 | 4153.6 | 100.0% |
| `nasa_apod` | 11:00 | 3500.1 | 55.56% |
| `nasa_apod` | 13:00 | 3279.6 | 50.0% |
| `dog_ceo_random` | 03:00 | 3274.4 | 100.0% |
| `nasa_apod` | 20:00 | 3095.4 | 44.44% |
| `nasa_apod` | 22:00 | 2952.7 | 33.33% |
| `dog_ceo_random` | 17:00 | 2937.7 | 71.43% |
| `nasa_apod` | 10:00 | 2892.2 | 25.0% |
| `dog_ceo_random` | 11:00 | 2626.8 | 66.67% |
| `dog_ceo_random` | 14:00 | 2625.3 | 71.43% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
