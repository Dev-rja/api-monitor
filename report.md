# API Reliability Monitor — SLA Report

> Last updated: **2026-04-04 12:00 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **82.7%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 100.0% | 304.8 | 517.6 | 1000ms | 0/57 |
| ❌ | `public_apis_list` | 0.0% | 100.0% | 113.9 | 234.1 | 1500ms | 0/57 |
| ⚠️ | `open_meteo_weather` | 96.49% | 100.0% | 577.5 | 1426.6 | 2000ms | 0/57 |
| ❌ | `nasa_apod` | 98.25% | 68.42% | 1255.6 | 10538.0 | 2000ms | 18/57 |
| ⚠️ | `ipapi_check` | 98.25% | 100.0% | 152.4 | 248.6 | 2500ms | 0/57 |
| ⚠️ | `dog_ceo_random` | 100.0% | 80.7% | 1525.8 | 4785.5 | 2500ms | 11/57 |
| ✅ | `useless_fact` | 100.0% | 100.0% | 583.0 | 1705.0 | 2500ms | 0/57 |
| ✅ | `agify_name` | 100.0% | 98.25% | 452.2 | 3237.1 | 2000ms | 1/57 |
| ✅ | `catfact_random` | 100.0% | 100.0% | 243.6 | 1218.5 | 3000ms | 0/57 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 100.0% | 238.8 | 1556.1 | 2000ms | 0/57 |
| ✅ | `rest_countries` | 100.0% | 100.0% | 206.5 | 363.3 | 2500ms | 0/57 |
| ✅ | `coingecko_bitcoin` | 100.0% | 100.0% | 100.8 | 252.0 | 1500ms | 0/57 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `nasa_apod` | 10:00 | 3753.5 | 33.33% |
| `dog_ceo_random` | 14:00 | 3607.4 | 100.0% |
| `dog_ceo_random` | 17:00 | 3075.1 | 66.67% |
| `dog_ceo_random` | 13:00 | 3033.8 | 100.0% |
| `nasa_apod` | 18:00 | 2476.7 | 100.0% |
| `nasa_apod` | 13:00 | 2052.3 | 100.0% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
