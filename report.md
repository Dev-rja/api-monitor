# API Reliability Monitor — SLA Report

> Last updated: **2026-04-03 19:28 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **7/12** &nbsp;|&nbsp; Avg uptime: **82.9%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 100.0% | 295.7 | 506.9 | 1000ms | 0/38 |
| ❌ | `public_apis_list` | 0.0% | 100.0% | 109.2 | 234.1 | 1500ms | 0/38 |
| ❌ | `nasa_apod` | 97.37% | 60.53% | 1479.3 | 10538.0 | 2000ms | 15/38 |
| ⚠️ | `open_meteo_weather` | 97.37% | 100.0% | 539.0 | 804.5 | 2000ms | 0/38 |
| ❌ | `dog_ceo_random` | 100.0% | 73.68% | 1744.4 | 4785.5 | 2500ms | 10/38 |
| ✅ | `useless_fact` | 100.0% | 100.0% | 555.9 | 849.5 | 2500ms | 0/38 |
| ✅ | `agify_name` | 100.0% | 97.37% | 487.9 | 3237.1 | 2000ms | 1/38 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 100.0% | 223.4 | 737.9 | 2000ms | 0/38 |
| ✅ | `catfact_random` | 100.0% | 100.0% | 217.0 | 584.9 | 3000ms | 0/38 |
| ✅ | `rest_countries` | 100.0% | 100.0% | 209.2 | 363.3 | 2500ms | 0/38 |
| ✅ | `ipapi_check` | 100.0% | 100.0% | 157.9 | 248.6 | 2500ms | 0/38 |
| ✅ | `coingecko_bitcoin` | 100.0% | 100.0% | 103.7 | 252.0 | 1500ms | 0/38 |

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
| `nasa_apod` | 07:00 | 2536.7 | 100.0% |
| `nasa_apod` | 18:00 | 2476.7 | 100.0% |
| `nasa_apod` | 20:00 | 2344.2 | 100.0% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
