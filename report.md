# API Reliability Monitor — SLA Report

> Last updated: **2026-04-04 21:50 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **82.9%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 100.0% | 306.7 | 517.6 | 1000ms | 0/72 |
| ❌ | `public_apis_list` | 0.0% | 100.0% | 112.7 | 234.1 | 1500ms | 0/72 |
| ⚠️ | `open_meteo_weather` | 97.22% | 100.0% | 571.3 | 1426.6 | 2000ms | 0/72 |
| ❌ | `nasa_apod` | 98.61% | 72.22% | 1146.5 | 10538.0 | 2000ms | 20/72 |
| ⚠️ | `ipapi_check` | 98.61% | 100.0% | 154.4 | 248.6 | 2500ms | 0/72 |
| ❌ | `dog_ceo_random` | 100.0% | 75.0% | 1656.1 | 4785.5 | 2500ms | 18/72 |
| ✅ | `useless_fact` | 100.0% | 100.0% | 573.0 | 1705.0 | 2500ms | 0/72 |
| ✅ | `agify_name` | 100.0% | 98.61% | 442.9 | 3237.1 | 2000ms | 1/72 |
| ✅ | `rest_countries` | 100.0% | 98.61% | 295.9 | 5081.4 | 2500ms | 1/72 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 100.0% | 250.4 | 1556.1 | 2000ms | 0/72 |
| ✅ | `catfact_random` | 100.0% | 100.0% | 248.2 | 1218.5 | 3000ms | 0/72 |
| ✅ | `coingecko_bitcoin` | 100.0% | 100.0% | 100.2 | 252.0 | 1500ms | 0/72 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `nasa_apod` | 10:00 | 3753.5 | 33.33% |
| `dog_ceo_random` | 17:00 | 3292.2 | 80.0% |
| `dog_ceo_random` | 14:00 | 3011.8 | 75.0% |
| `dog_ceo_random` | 13:00 | 2942.8 | 100.0% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
