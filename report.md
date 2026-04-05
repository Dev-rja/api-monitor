# API Reliability Monitor — SLA Report

> Last updated: **2026-04-05 07:44 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **82.8%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 100.0% | 306.6 | 517.6 | 1000ms | 0/80 |
| ❌ | `public_apis_list` | 0.0% | 100.0% | 115.1 | 234.1 | 1500ms | 0/80 |
| ❌ | `nasa_apod` | 97.5% | 68.75% | 1310.4 | 10538.0 | 2000ms | 25/80 |
| ⚠️ | `open_meteo_weather` | 97.5% | 100.0% | 568.0 | 1426.6 | 2000ms | 0/80 |
| ⚠️ | `ipapi_check` | 98.75% | 100.0% | 155.2 | 248.6 | 2500ms | 0/80 |
| ❌ | `dog_ceo_random` | 100.0% | 76.25% | 1656.1 | 4785.5 | 2500ms | 19/80 |
| ✅ | `useless_fact` | 100.0% | 100.0% | 579.1 | 1705.0 | 2500ms | 0/80 |
| ✅ | `agify_name` | 100.0% | 98.75% | 436.1 | 3237.1 | 2000ms | 1/80 |
| ✅ | `rest_countries` | 100.0% | 98.75% | 288.4 | 5081.4 | 2500ms | 1/80 |
| ✅ | `catfact_random` | 100.0% | 100.0% | 250.2 | 1218.5 | 3000ms | 0/80 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 100.0% | 248.1 | 1556.1 | 2000ms | 0/80 |
| ✅ | `coingecko_bitcoin` | 100.0% | 100.0% | 102.4 | 252.0 | 1500ms | 0/80 |

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
