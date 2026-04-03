# API Reliability Monitor — SLA Report

> Last updated: **2026-04-03 11:55 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **7/12** &nbsp;|&nbsp; Avg uptime: **82.8%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 100.0% | 285.2 | 506.2 | 1000ms | 0/29 |
| ❌ | `public_apis_list` | 0.0% | 100.0% | 107.6 | 221.3 | 1500ms | 0/29 |
| ❌ | `nasa_apod` | 96.55% | 65.52% | 1465.5 | 10538.0 | 2000ms | 10/29 |
| ⚠️ | `open_meteo_weather` | 96.55% | 100.0% | 535.0 | 804.5 | 2000ms | 0/29 |
| ❌ | `dog_ceo_random` | 100.0% | 79.31% | 1675.1 | 4785.5 | 2500ms | 6/29 |
| ✅ | `useless_fact` | 100.0% | 100.0% | 541.7 | 829.9 | 2500ms | 0/29 |
| ✅ | `agify_name` | 100.0% | 96.55% | 488.7 | 3237.1 | 2000ms | 1/29 |
| ✅ | `catfact_random` | 100.0% | 100.0% | 248.0 | 584.9 | 3000ms | 0/29 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 100.0% | 232.7 | 737.9 | 2000ms | 0/29 |
| ✅ | `rest_countries` | 100.0% | 100.0% | 205.8 | 363.3 | 2500ms | 0/29 |
| ✅ | `ipapi_check` | 100.0% | 100.0% | 165.4 | 248.6 | 2500ms | 0/29 |
| ✅ | `coingecko_bitcoin` | 100.0% | 100.0% | 104.4 | 195.8 | 1500ms | 0/29 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `nasa_apod` | 10:00 | 5513.9 | 50.0% |
| `dog_ceo_random` | 17:00 | 4785.5 | 100.0% |
| `dog_ceo_random` | 14:00 | 4518.4 | 100.0% |
| `agify_name` | 21:00 | 3237.1 | 100.0% |
| `dog_ceo_random` | 16:00 | 3016.7 | 100.0% |
| `dog_ceo_random` | 12:00 | 2811.7 | 100.0% |
| `nasa_apod` | 02:00 | 2697.2 | 100.0% |
| `nasa_apod` | 18:00 | 2630.6 | 100.0% |
| `nasa_apod` | 07:00 | 2536.7 | 100.0% |
| `nasa_apod` | 20:00 | 2344.2 | 100.0% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
