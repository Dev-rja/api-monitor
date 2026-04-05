# API Reliability Monitor — SLA Report

> Last updated: **2026-04-05 09:10 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **82.8%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 100.0% | 304.0 | 517.6 | 1000ms | 0/82 |
| ❌ | `public_apis_list` | 0.0% | 100.0% | 117.0 | 234.1 | 1500ms | 0/82 |
| ❌ | `nasa_apod` | 97.56% | 69.51% | 1291.5 | 10538.0 | 2000ms | 25/82 |
| ⚠️ | `open_meteo_weather` | 97.56% | 98.78% | 590.2 | 2550.7 | 2000ms | 1/82 |
| ⚠️ | `ipapi_check` | 98.78% | 100.0% | 154.9 | 248.6 | 2500ms | 0/82 |
| ❌ | `dog_ceo_random` | 100.0% | 76.83% | 1660.3 | 4785.5 | 2500ms | 19/82 |
| ✅ | `useless_fact` | 100.0% | 100.0% | 577.6 | 1705.0 | 2500ms | 0/82 |
| ✅ | `agify_name` | 100.0% | 98.78% | 429.2 | 3237.1 | 2000ms | 1/82 |
| ✅ | `rest_countries` | 100.0% | 98.78% | 284.9 | 5081.4 | 2500ms | 1/82 |
| ✅ | `catfact_random` | 100.0% | 100.0% | 247.9 | 1218.5 | 3000ms | 0/82 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 100.0% | 246.3 | 1556.1 | 2000ms | 0/82 |
| ✅ | `coingecko_bitcoin` | 100.0% | 100.0% | 101.4 | 252.0 | 1500ms | 0/82 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `nasa_apod` | 10:00 | 3753.5 | 33.33% |
| `dog_ceo_random` | 17:00 | 3292.2 | 80.0% |
| `dog_ceo_random` | 03:00 | 3274.4 | 100.0% |
| `dog_ceo_random` | 14:00 | 3011.8 | 75.0% |
| `dog_ceo_random` | 13:00 | 2942.8 | 100.0% |
| `nasa_apod` | 03:00 | 2530.9 | 100.0% |
| `nasa_apod` | 22:00 | 2191.3 | 16.67% |
| `nasa_apod` | 07:00 | 2071.8 | 75.0% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
