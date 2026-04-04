# API Reliability Monitor — SLA Report

> Last updated: **2026-04-04 09:06 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **82.7%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 100.0% | 306.1 | 517.6 | 1000ms | 0/52 |
| ❌ | `public_apis_list` | 0.0% | 100.0% | 115.1 | 234.1 | 1500ms | 0/52 |
| ⚠️ | `open_meteo_weather` | 96.15% | 100.0% | 547.1 | 804.5 | 2000ms | 0/52 |
| ❌ | `nasa_apod` | 98.08% | 67.31% | 1275.7 | 10538.0 | 2000ms | 17/52 |
| ⚠️ | `ipapi_check` | 98.08% | 100.0% | 152.2 | 248.6 | 2500ms | 0/52 |
| ⚠️ | `dog_ceo_random` | 100.0% | 80.77% | 1522.4 | 4785.5 | 2500ms | 10/52 |
| ✅ | `useless_fact` | 100.0% | 100.0% | 588.6 | 1705.0 | 2500ms | 0/52 |
| ✅ | `agify_name` | 100.0% | 98.08% | 462.1 | 3237.1 | 2000ms | 1/52 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 100.0% | 243.6 | 1556.1 | 2000ms | 0/52 |
| ✅ | `catfact_random` | 100.0% | 100.0% | 227.5 | 584.9 | 3000ms | 0/52 |
| ✅ | `rest_countries` | 100.0% | 100.0% | 208.3 | 363.3 | 2500ms | 0/52 |
| ✅ | `coingecko_bitcoin` | 100.0% | 100.0% | 99.8 | 252.0 | 1500ms | 0/52 |

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
