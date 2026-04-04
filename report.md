# API Reliability Monitor — SLA Report

> Last updated: **2026-04-04 19:06 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **82.8%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 100.0% | 305.6 | 517.6 | 1000ms | 0/67 |
| ❌ | `public_apis_list` | 0.0% | 100.0% | 112.5 | 234.1 | 1500ms | 0/67 |
| ⚠️ | `open_meteo_weather` | 97.01% | 100.0% | 571.1 | 1426.6 | 2000ms | 0/67 |
| ❌ | `nasa_apod` | 98.51% | 71.64% | 1166.4 | 10538.0 | 2000ms | 19/67 |
| ⚠️ | `ipapi_check` | 98.51% | 100.0% | 152.5 | 248.6 | 2500ms | 0/67 |
| ❌ | `dog_ceo_random` | 100.0% | 73.13% | 1696.7 | 4785.5 | 2500ms | 18/67 |
| ✅ | `useless_fact` | 100.0% | 100.0% | 580.1 | 1705.0 | 2500ms | 0/67 |
| ✅ | `agify_name` | 100.0% | 98.51% | 450.2 | 3237.1 | 2000ms | 1/67 |
| ✅ | `rest_countries` | 100.0% | 98.51% | 280.1 | 5081.4 | 2500ms | 1/67 |
| ✅ | `catfact_random` | 100.0% | 100.0% | 246.1 | 1218.5 | 3000ms | 0/67 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 100.0% | 238.4 | 1556.1 | 2000ms | 0/67 |
| ✅ | `coingecko_bitcoin` | 100.0% | 100.0% | 99.5 | 252.0 | 1500ms | 0/67 |

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
