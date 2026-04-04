# API Reliability Monitor — SLA Report

> Last updated: **2026-04-04 08:24 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **82.7%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 100.0% | 306.3 | 517.6 | 1000ms | 0/51 |
| ❌ | `public_apis_list` | 0.0% | 100.0% | 113.4 | 234.1 | 1500ms | 0/51 |
| ⚠️ | `open_meteo_weather` | 96.08% | 100.0% | 549.7 | 804.5 | 2000ms | 0/51 |
| ❌ | `nasa_apod` | 98.04% | 66.67% | 1289.0 | 10538.0 | 2000ms | 17/51 |
| ⚠️ | `ipapi_check` | 98.04% | 100.0% | 151.8 | 248.6 | 2500ms | 0/51 |
| ⚠️ | `dog_ceo_random` | 100.0% | 80.39% | 1540.2 | 4785.5 | 2500ms | 10/51 |
| ✅ | `useless_fact` | 100.0% | 100.0% | 586.8 | 1705.0 | 2500ms | 0/51 |
| ✅ | `agify_name` | 100.0% | 98.04% | 466.6 | 3237.1 | 2000ms | 1/51 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 100.0% | 235.7 | 1556.1 | 2000ms | 0/51 |
| ✅ | `catfact_random` | 100.0% | 100.0% | 220.5 | 584.9 | 3000ms | 0/51 |
| ✅ | `rest_countries` | 100.0% | 100.0% | 210.4 | 363.3 | 2500ms | 0/51 |
| ✅ | `coingecko_bitcoin` | 100.0% | 100.0% | 100.4 | 252.0 | 1500ms | 0/51 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `nasa_apod` | 10:00 | 5513.9 | 50.0% |
| `dog_ceo_random` | 14:00 | 3607.4 | 100.0% |
| `dog_ceo_random` | 17:00 | 3075.1 | 66.67% |
| `dog_ceo_random` | 13:00 | 3033.8 | 100.0% |
| `dog_ceo_random` | 12:00 | 2811.7 | 100.0% |
| `nasa_apod` | 18:00 | 2476.7 | 100.0% |
| `nasa_apod` | 13:00 | 2052.3 | 100.0% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
