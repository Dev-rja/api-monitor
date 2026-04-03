# API Reliability Monitor — SLA Report

> Last updated: **2026-04-03 07:40 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **7/12** &nbsp;|&nbsp; Avg uptime: **83.0%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 100.0% | 292.4 | 506.2 | 1000ms | 0/24 |
| ❌ | `public_apis_list` | 0.0% | 100.0% | 99.5 | 202.3 | 1500ms | 0/24 |
| ⚠️ | `open_meteo_weather` | 95.83% | 100.0% | 535.4 | 804.5 | 2000ms | 0/24 |
| ❌ | `dog_ceo_random` | 100.0% | 79.17% | 1656.0 | 4785.5 | 2500ms | 5/24 |
| ❌ | `nasa_apod` | 100.0% | 70.83% | 1069.7 | 2697.2 | 2000ms | 7/24 |
| ✅ | `useless_fact` | 100.0% | 100.0% | 549.2 | 829.9 | 2500ms | 0/24 |
| ✅ | `agify_name` | 100.0% | 95.83% | 524.0 | 3237.1 | 2000ms | 1/24 |
| ✅ | `catfact_random` | 100.0% | 100.0% | 241.1 | 474.2 | 3000ms | 0/24 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 100.0% | 235.6 | 737.9 | 2000ms | 0/24 |
| ✅ | `rest_countries` | 100.0% | 100.0% | 208.4 | 363.3 | 2500ms | 0/24 |
| ✅ | `ipapi_check` | 100.0% | 100.0% | 163.1 | 248.6 | 2500ms | 0/24 |
| ✅ | `coingecko_bitcoin` | 100.0% | 100.0% | 103.5 | 195.8 | 1500ms | 0/24 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `dog_ceo_random` | 17:00 | 4785.5 | 100.0% |
| `dog_ceo_random` | 14:00 | 4518.4 | 100.0% |
| `agify_name` | 21:00 | 3237.1 | 100.0% |
| `dog_ceo_random` | 16:00 | 3016.7 | 100.0% |
| `dog_ceo_random` | 12:00 | 2811.7 | 100.0% |
| `dog_ceo_random` | 08:00 | 2743.5 | 100.0% |
| `nasa_apod` | 02:00 | 2697.2 | 100.0% |
| `nasa_apod` | 11:00 | 2644.3 | 100.0% |
| `nasa_apod` | 18:00 | 2630.6 | 100.0% |
| `nasa_apod` | 07:00 | 2536.7 | 100.0% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
