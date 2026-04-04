# API Reliability Monitor — SLA Report

> Last updated: **2026-04-04 09:54 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **82.7%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 100.0% | 304.4 | 517.6 | 1000ms | 0/53 |
| ❌ | `public_apis_list` | 0.0% | 100.0% | 116.2 | 234.1 | 1500ms | 0/53 |
| ⚠️ | `open_meteo_weather` | 96.23% | 100.0% | 546.0 | 804.5 | 2000ms | 0/53 |
| ❌ | `nasa_apod` | 98.11% | 66.04% | 1301.2 | 10538.0 | 2000ms | 18/53 |
| ⚠️ | `ipapi_check` | 98.11% | 100.0% | 151.9 | 248.6 | 2500ms | 0/53 |
| ⚠️ | `dog_ceo_random` | 100.0% | 81.13% | 1515.1 | 4785.5 | 2500ms | 10/53 |
| ✅ | `useless_fact` | 100.0% | 100.0% | 585.0 | 1705.0 | 2500ms | 0/53 |
| ✅ | `agify_name` | 100.0% | 98.11% | 458.4 | 3237.1 | 2000ms | 1/53 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 100.0% | 242.2 | 1556.1 | 2000ms | 0/53 |
| ✅ | `catfact_random` | 100.0% | 100.0% | 225.1 | 584.9 | 3000ms | 0/53 |
| ✅ | `rest_countries` | 100.0% | 100.0% | 207.6 | 363.3 | 2500ms | 0/53 |
| ✅ | `coingecko_bitcoin` | 100.0% | 100.0% | 99.0 | 252.0 | 1500ms | 0/53 |

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
