# API Reliability Monitor — SLA Report

> Last updated: **2026-04-04 23:59 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **82.8%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 100.0% | 303.4 | 517.6 | 1000ms | 0/76 |
| ❌ | `public_apis_list` | 0.0% | 100.0% | 114.8 | 234.1 | 1500ms | 0/76 |
| ❌ | `nasa_apod` | 97.37% | 71.05% | 1271.9 | 10538.0 | 2000ms | 22/76 |
| ⚠️ | `open_meteo_weather` | 97.37% | 100.0% | 567.4 | 1426.6 | 2000ms | 0/76 |
| ⚠️ | `ipapi_check` | 98.68% | 100.0% | 154.0 | 248.6 | 2500ms | 0/76 |
| ❌ | `dog_ceo_random` | 100.0% | 76.32% | 1618.3 | 4785.5 | 2500ms | 18/76 |
| ✅ | `useless_fact` | 100.0% | 100.0% | 576.4 | 1705.0 | 2500ms | 0/76 |
| ✅ | `agify_name` | 100.0% | 98.68% | 437.4 | 3237.1 | 2000ms | 1/76 |
| ✅ | `rest_countries` | 100.0% | 98.68% | 291.0 | 5081.4 | 2500ms | 1/76 |
| ✅ | `catfact_random` | 100.0% | 100.0% | 249.5 | 1218.5 | 3000ms | 0/76 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 100.0% | 246.5 | 1556.1 | 2000ms | 0/76 |
| ✅ | `coingecko_bitcoin` | 100.0% | 100.0% | 101.1 | 252.0 | 1500ms | 0/76 |

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
