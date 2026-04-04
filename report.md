# API Reliability Monitor — SLA Report

> Last updated: **2026-04-04 14:49 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **82.8%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 100.0% | 305.2 | 517.6 | 1000ms | 0/60 |
| ❌ | `public_apis_list` | 0.0% | 100.0% | 116.3 | 234.1 | 1500ms | 0/60 |
| ⚠️ | `open_meteo_weather` | 96.67% | 100.0% | 575.3 | 1426.6 | 2000ms | 0/60 |
| ❌ | `nasa_apod` | 98.33% | 70.0% | 1217.8 | 10538.0 | 2000ms | 18/60 |
| ⚠️ | `ipapi_check` | 98.33% | 100.0% | 155.0 | 248.6 | 2500ms | 0/60 |
| ❌ | `dog_ceo_random` | 100.0% | 78.33% | 1577.5 | 4785.5 | 2500ms | 13/60 |
| ✅ | `useless_fact` | 100.0% | 100.0% | 585.0 | 1705.0 | 2500ms | 0/60 |
| ✅ | `agify_name` | 100.0% | 98.33% | 454.0 | 3237.1 | 2000ms | 1/60 |
| ✅ | `catfact_random` | 100.0% | 100.0% | 254.6 | 1218.5 | 3000ms | 0/60 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 100.0% | 237.3 | 1556.1 | 2000ms | 0/60 |
| ✅ | `rest_countries` | 100.0% | 100.0% | 208.0 | 363.3 | 2500ms | 0/60 |
| ✅ | `coingecko_bitcoin` | 100.0% | 100.0% | 102.5 | 252.0 | 1500ms | 0/60 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `nasa_apod` | 10:00 | 3753.5 | 33.33% |
| `dog_ceo_random` | 17:00 | 3075.1 | 66.67% |
| `dog_ceo_random` | 14:00 | 3011.8 | 75.0% |
| `dog_ceo_random` | 13:00 | 2942.8 | 100.0% |
| `nasa_apod` | 18:00 | 2476.7 | 100.0% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
