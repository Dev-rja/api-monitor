# API Reliability Monitor — SLA Report

> Last updated: **2026-04-04 22:19 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **82.9%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 100.0% | 304.5 | 517.6 | 1000ms | 0/73 |
| ❌ | `public_apis_list` | 0.0% | 100.0% | 114.0 | 234.1 | 1500ms | 0/73 |
| ⚠️ | `open_meteo_weather` | 97.26% | 100.0% | 569.6 | 1426.6 | 2000ms | 0/73 |
| ❌ | `nasa_apod` | 98.63% | 72.6% | 1138.8 | 10538.0 | 2000ms | 20/73 |
| ⚠️ | `ipapi_check` | 98.63% | 100.0% | 154.4 | 248.6 | 2500ms | 0/73 |
| ❌ | `dog_ceo_random` | 100.0% | 75.34% | 1638.3 | 4785.5 | 2500ms | 18/73 |
| ✅ | `useless_fact` | 100.0% | 100.0% | 574.2 | 1705.0 | 2500ms | 0/73 |
| ✅ | `agify_name` | 100.0% | 98.63% | 439.0 | 3237.1 | 2000ms | 1/73 |
| ✅ | `rest_countries` | 100.0% | 98.63% | 293.0 | 5081.4 | 2500ms | 1/73 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 100.0% | 249.4 | 1556.1 | 2000ms | 0/73 |
| ✅ | `catfact_random` | 100.0% | 100.0% | 245.8 | 1218.5 | 3000ms | 0/73 |
| ✅ | `coingecko_bitcoin` | 100.0% | 100.0% | 100.6 | 252.0 | 1500ms | 0/73 |

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
