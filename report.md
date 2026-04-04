# API Reliability Monitor — SLA Report

> Last updated: **2026-04-04 20:03 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **82.9%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 100.0% | 305.7 | 517.6 | 1000ms | 0/69 |
| ❌ | `public_apis_list` | 0.0% | 100.0% | 113.2 | 234.1 | 1500ms | 0/69 |
| ⚠️ | `open_meteo_weather` | 97.1% | 100.0% | 571.0 | 1426.6 | 2000ms | 0/69 |
| ❌ | `nasa_apod` | 98.55% | 72.46% | 1147.2 | 10538.0 | 2000ms | 19/69 |
| ⚠️ | `ipapi_check` | 98.55% | 100.0% | 154.0 | 248.6 | 2500ms | 0/69 |
| ❌ | `dog_ceo_random` | 100.0% | 73.91% | 1688.0 | 4785.5 | 2500ms | 18/69 |
| ✅ | `useless_fact` | 100.0% | 100.0% | 575.5 | 1705.0 | 2500ms | 0/69 |
| ✅ | `agify_name` | 100.0% | 98.55% | 446.0 | 3237.1 | 2000ms | 1/69 |
| ✅ | `rest_countries` | 100.0% | 98.55% | 297.4 | 5081.4 | 2500ms | 1/69 |
| ✅ | `catfact_random` | 100.0% | 100.0% | 244.8 | 1218.5 | 3000ms | 0/69 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 100.0% | 238.6 | 1556.1 | 2000ms | 0/69 |
| ✅ | `coingecko_bitcoin` | 100.0% | 100.0% | 99.9 | 252.0 | 1500ms | 0/69 |

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
