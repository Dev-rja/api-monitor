# API Reliability Monitor — SLA Report

> Last updated: **2026-04-04 22:54 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **82.8%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 100.0% | 303.4 | 517.6 | 1000ms | 0/74 |
| ❌ | `public_apis_list` | 0.0% | 100.0% | 115.3 | 234.1 | 1500ms | 0/74 |
| ❌ | `nasa_apod` | 97.3% | 71.62% | 1264.8 | 10538.0 | 2000ms | 21/74 |
| ⚠️ | `open_meteo_weather` | 97.3% | 100.0% | 567.3 | 1426.6 | 2000ms | 0/74 |
| ⚠️ | `ipapi_check` | 98.65% | 100.0% | 154.7 | 248.6 | 2500ms | 0/74 |
| ❌ | `dog_ceo_random` | 100.0% | 75.68% | 1638.3 | 4785.5 | 2500ms | 18/74 |
| ✅ | `useless_fact` | 100.0% | 100.0% | 574.1 | 1705.0 | 2500ms | 0/74 |
| ✅ | `agify_name` | 100.0% | 98.65% | 437.5 | 3237.1 | 2000ms | 1/74 |
| ✅ | `rest_countries` | 100.0% | 98.65% | 292.2 | 5081.4 | 2500ms | 1/74 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 100.0% | 248.8 | 1556.1 | 2000ms | 0/74 |
| ✅ | `catfact_random` | 100.0% | 100.0% | 247.3 | 1218.5 | 3000ms | 0/74 |
| ✅ | `coingecko_bitcoin` | 100.0% | 100.0% | 102.5 | 252.0 | 1500ms | 0/74 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `nasa_apod` | 10:00 | 3753.5 | 33.33% |
| `dog_ceo_random` | 17:00 | 3292.2 | 80.0% |
| `dog_ceo_random` | 14:00 | 3011.8 | 75.0% |
| `dog_ceo_random` | 13:00 | 2942.8 | 100.0% |
| `nasa_apod` | 22:00 | 2191.3 | 16.67% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
