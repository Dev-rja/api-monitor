# API Reliability Monitor — SLA Report

> Last updated: **2026-04-03 17:52 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **7/12** &nbsp;|&nbsp; Avg uptime: **82.9%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 100.0% | 288.5 | 506.9 | 1000ms | 0/36 |
| ❌ | `public_apis_list` | 0.0% | 100.0% | 112.2 | 234.1 | 1500ms | 0/36 |
| ❌ | `nasa_apod` | 97.22% | 63.89% | 1422.8 | 10538.0 | 2000ms | 13/36 |
| ⚠️ | `open_meteo_weather` | 97.22% | 100.0% | 534.8 | 804.5 | 2000ms | 0/36 |
| ❌ | `dog_ceo_random` | 100.0% | 72.22% | 1789.3 | 4785.5 | 2500ms | 10/36 |
| ✅ | `useless_fact` | 100.0% | 100.0% | 547.2 | 829.9 | 2500ms | 0/36 |
| ✅ | `agify_name` | 100.0% | 97.22% | 491.0 | 3237.1 | 2000ms | 1/36 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 100.0% | 224.7 | 737.9 | 2000ms | 0/36 |
| ✅ | `catfact_random` | 100.0% | 100.0% | 221.1 | 584.9 | 3000ms | 0/36 |
| ✅ | `rest_countries` | 100.0% | 100.0% | 203.4 | 363.3 | 2500ms | 0/36 |
| ✅ | `ipapi_check` | 100.0% | 100.0% | 159.3 | 248.6 | 2500ms | 0/36 |
| ✅ | `coingecko_bitcoin` | 100.0% | 100.0% | 104.3 | 252.0 | 1500ms | 0/36 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `nasa_apod` | 10:00 | 5513.9 | 50.0% |
| `dog_ceo_random` | 14:00 | 3607.4 | 100.0% |
| `agify_name` | 21:00 | 3237.1 | 100.0% |
| `dog_ceo_random` | 17:00 | 3075.1 | 66.67% |
| `dog_ceo_random` | 13:00 | 3033.8 | 100.0% |
| `dog_ceo_random` | 12:00 | 2811.7 | 100.0% |
| `nasa_apod` | 02:00 | 2697.2 | 100.0% |
| `nasa_apod` | 18:00 | 2630.6 | 100.0% |
| `nasa_apod` | 07:00 | 2536.7 | 100.0% |
| `nasa_apod` | 20:00 | 2344.2 | 100.0% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
