# API Reliability Monitor — SLA Report

> Last updated: **2026-04-04 20:48 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **82.9%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 100.0% | 307.5 | 517.6 | 1000ms | 0/70 |
| ❌ | `public_apis_list` | 0.0% | 100.0% | 112.7 | 234.1 | 1500ms | 0/70 |
| ⚠️ | `open_meteo_weather` | 97.14% | 100.0% | 571.6 | 1426.6 | 2000ms | 0/70 |
| ❌ | `nasa_apod` | 98.57% | 71.43% | 1165.8 | 10538.0 | 2000ms | 20/70 |
| ⚠️ | `ipapi_check` | 98.57% | 100.0% | 154.0 | 248.6 | 2500ms | 0/70 |
| ❌ | `dog_ceo_random` | 100.0% | 74.29% | 1682.8 | 4785.5 | 2500ms | 18/70 |
| ✅ | `useless_fact` | 100.0% | 100.0% | 576.5 | 1705.0 | 2500ms | 0/70 |
| ✅ | `agify_name` | 100.0% | 98.57% | 447.0 | 3237.1 | 2000ms | 1/70 |
| ✅ | `rest_countries` | 100.0% | 98.57% | 296.9 | 5081.4 | 2500ms | 1/70 |
| ✅ | `catfact_random` | 100.0% | 100.0% | 245.3 | 1218.5 | 3000ms | 0/70 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 100.0% | 238.4 | 1556.1 | 2000ms | 0/70 |
| ✅ | `coingecko_bitcoin` | 100.0% | 100.0% | 100.5 | 252.0 | 1500ms | 0/70 |

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
