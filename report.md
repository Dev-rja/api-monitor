# API Reliability Monitor — SLA Report

> Last updated: **2026-04-04 14:03 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **82.8%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 100.0% | 303.6 | 517.6 | 1000ms | 0/59 |
| ❌ | `public_apis_list` | 0.0% | 100.0% | 114.9 | 234.1 | 1500ms | 0/59 |
| ⚠️ | `open_meteo_weather` | 96.61% | 100.0% | 575.6 | 1426.6 | 2000ms | 0/59 |
| ❌ | `nasa_apod` | 98.31% | 69.49% | 1231.0 | 10538.0 | 2000ms | 18/59 |
| ⚠️ | `ipapi_check` | 98.31% | 100.0% | 153.9 | 248.6 | 2500ms | 0/59 |
| ❌ | `dog_ceo_random` | 100.0% | 79.66% | 1550.5 | 4785.5 | 2500ms | 12/59 |
| ✅ | `useless_fact` | 100.0% | 100.0% | 584.0 | 1705.0 | 2500ms | 0/59 |
| ✅ | `agify_name` | 100.0% | 98.31% | 452.5 | 3237.1 | 2000ms | 1/59 |
| ✅ | `catfact_random` | 100.0% | 100.0% | 253.2 | 1218.5 | 3000ms | 0/59 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 100.0% | 237.1 | 1556.1 | 2000ms | 0/59 |
| ✅ | `rest_countries` | 100.0% | 100.0% | 206.3 | 363.3 | 2500ms | 0/59 |
| ✅ | `coingecko_bitcoin` | 100.0% | 100.0% | 101.4 | 252.0 | 1500ms | 0/59 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `nasa_apod` | 10:00 | 3753.5 | 33.33% |
| `dog_ceo_random` | 17:00 | 3075.1 | 66.67% |
| `dog_ceo_random` | 14:00 | 2958.2 | 66.67% |
| `dog_ceo_random` | 13:00 | 2942.8 | 100.0% |
| `nasa_apod` | 18:00 | 2476.7 | 100.0% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
