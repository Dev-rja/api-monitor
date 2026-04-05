# API Reliability Monitor — SLA Report

> Last updated: **2026-04-05 20:16 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **82.5%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 100.0% | 299.4 | 524.7 | 1000ms | 0/98 |
| ❌ | `public_apis_list` | 0.0% | 100.0% | 115.3 | 234.1 | 1500ms | 0/98 |
| ⚠️ | `ipapi_check` | 95.92% | 100.0% | 155.5 | 248.6 | 2500ms | 0/98 |
| ❌ | `dog_ceo_random` | 97.96% | 67.35% | 1869.4 | 5142.0 | 2500ms | 32/98 |
| ❌ | `nasa_apod` | 97.96% | 70.41% | 1245.0 | 10538.0 | 2000ms | 29/98 |
| ⚠️ | `open_meteo_weather` | 97.96% | 98.98% | 578.8 | 2550.7 | 2000ms | 1/98 |
| ✅ | `useless_fact` | 100.0% | 100.0% | 579.3 | 2439.0 | 2500ms | 0/98 |
| ✅ | `agify_name` | 100.0% | 98.98% | 413.3 | 3237.1 | 2000ms | 1/98 |
| ✅ | `rest_countries` | 100.0% | 97.96% | 342.0 | 7269.1 | 2500ms | 2/98 |
| ✅ | `catfact_random` | 100.0% | 100.0% | 248.7 | 1218.5 | 3000ms | 0/98 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 100.0% | 239.1 | 1556.1 | 2000ms | 0/98 |
| ✅ | `coingecko_bitcoin` | 100.0% | 100.0% | 102.9 | 252.0 | 1500ms | 0/98 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `dog_ceo_random` | 13:00 | 3675.8 | 100.0% |
| `dog_ceo_random` | 17:00 | 3338.8 | 83.33% |
| `dog_ceo_random` | 03:00 | 3274.4 | 100.0% |
| `nasa_apod` | 10:00 | 2892.2 | 25.0% |
| `nasa_apod` | 03:00 | 2530.9 | 100.0% |
| `dog_ceo_random` | 14:00 | 2501.6 | 66.67% |
| `nasa_apod` | 22:00 | 2191.3 | 16.67% |
| `nasa_apod` | 07:00 | 2071.8 | 75.0% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
