# API Reliability Monitor — SLA Report

> Last updated: **2026-04-04 16:28 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **82.8%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 100.0% | 308.5 | 517.6 | 1000ms | 0/63 |
| ❌ | `public_apis_list` | 0.0% | 100.0% | 116.8 | 234.1 | 1500ms | 0/63 |
| ⚠️ | `open_meteo_weather` | 96.83% | 100.0% | 575.2 | 1426.6 | 2000ms | 0/63 |
| ❌ | `nasa_apod` | 98.41% | 71.43% | 1179.5 | 10538.0 | 2000ms | 18/63 |
| ⚠️ | `ipapi_check` | 98.41% | 100.0% | 153.6 | 248.6 | 2500ms | 0/63 |
| ❌ | `dog_ceo_random` | 100.0% | 76.19% | 1617.6 | 4785.5 | 2500ms | 15/63 |
| ✅ | `useless_fact` | 100.0% | 100.0% | 583.6 | 1705.0 | 2500ms | 0/63 |
| ✅ | `agify_name` | 100.0% | 98.41% | 459.2 | 3237.1 | 2000ms | 1/63 |
| ✅ | `catfact_random` | 100.0% | 100.0% | 253.2 | 1218.5 | 3000ms | 0/63 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 100.0% | 233.6 | 1556.1 | 2000ms | 0/63 |
| ✅ | `rest_countries` | 100.0% | 100.0% | 209.3 | 363.3 | 2500ms | 0/63 |
| ✅ | `coingecko_bitcoin` | 100.0% | 100.0% | 101.0 | 252.0 | 1500ms | 0/63 |

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
