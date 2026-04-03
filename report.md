# API Reliability Monitor — SLA Report

> Last updated: **2026-04-03 22:00 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **7/12** &nbsp;|&nbsp; Avg uptime: **82.7%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 100.0% | 304.7 | 506.9 | 1000ms | 0/42 |
| ❌ | `public_apis_list` | 0.0% | 100.0% | 114.8 | 234.1 | 1500ms | 0/42 |
| ⚠️ | `open_meteo_weather` | 95.24% | 100.0% | 544.2 | 804.5 | 2000ms | 0/42 |
| ❌ | `nasa_apod` | 97.62% | 64.29% | 1370.7 | 10538.0 | 2000ms | 15/42 |
| ❌ | `dog_ceo_random` | 100.0% | 76.19% | 1636.0 | 4785.5 | 2500ms | 10/42 |
| ✅ | `useless_fact` | 100.0% | 100.0% | 564.8 | 849.5 | 2500ms | 0/42 |
| ✅ | `agify_name` | 100.0% | 97.62% | 486.2 | 3237.1 | 2000ms | 1/42 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 100.0% | 247.3 | 1556.1 | 2000ms | 0/42 |
| ✅ | `catfact_random` | 100.0% | 100.0% | 222.5 | 584.9 | 3000ms | 0/42 |
| ✅ | `rest_countries` | 100.0% | 100.0% | 211.8 | 363.3 | 2500ms | 0/42 |
| ✅ | `ipapi_check` | 100.0% | 100.0% | 155.2 | 248.6 | 2500ms | 0/42 |
| ✅ | `coingecko_bitcoin` | 100.0% | 100.0% | 101.3 | 252.0 | 1500ms | 0/42 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `nasa_apod` | 10:00 | 5513.9 | 50.0% |
| `dog_ceo_random` | 14:00 | 3607.4 | 100.0% |
| `dog_ceo_random` | 17:00 | 3075.1 | 66.67% |
| `dog_ceo_random` | 13:00 | 3033.8 | 100.0% |
| `dog_ceo_random` | 12:00 | 2811.7 | 100.0% |
| `nasa_apod` | 02:00 | 2697.2 | 100.0% |
| `nasa_apod` | 07:00 | 2536.7 | 100.0% |
| `nasa_apod` | 18:00 | 2476.7 | 100.0% |
| `nasa_apod` | 13:00 | 2052.3 | 100.0% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
