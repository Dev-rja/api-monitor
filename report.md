# API Reliability Monitor — SLA Report

> Last updated: **2026-04-04 18:21 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **82.8%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 100.0% | 307.9 | 517.6 | 1000ms | 0/66 |
| ❌ | `public_apis_list` | 0.0% | 100.0% | 113.4 | 234.1 | 1500ms | 0/66 |
| ⚠️ | `open_meteo_weather` | 96.97% | 100.0% | 572.4 | 1426.6 | 2000ms | 0/66 |
| ❌ | `nasa_apod` | 98.48% | 71.21% | 1176.0 | 10538.0 | 2000ms | 19/66 |
| ⚠️ | `ipapi_check` | 98.48% | 100.0% | 152.5 | 248.6 | 2500ms | 0/66 |
| ❌ | `dog_ceo_random` | 100.0% | 74.24% | 1683.7 | 4785.5 | 2500ms | 17/66 |
| ✅ | `useless_fact` | 100.0% | 100.0% | 582.8 | 1705.0 | 2500ms | 0/66 |
| ✅ | `agify_name` | 100.0% | 98.48% | 454.5 | 3237.1 | 2000ms | 1/66 |
| ✅ | `rest_countries` | 100.0% | 98.48% | 283.3 | 5081.4 | 2500ms | 1/66 |
| ✅ | `catfact_random` | 100.0% | 100.0% | 248.5 | 1218.5 | 3000ms | 0/66 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 100.0% | 240.4 | 1556.1 | 2000ms | 0/66 |
| ✅ | `coingecko_bitcoin` | 100.0% | 100.0% | 99.0 | 252.0 | 1500ms | 0/66 |

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
