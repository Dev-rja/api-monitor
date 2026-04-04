# API Reliability Monitor — SLA Report

> Last updated: **2026-04-04 06:42 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **7/12** &nbsp;|&nbsp; Avg uptime: **82.8%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 100.0% | 306.9 | 517.6 | 1000ms | 0/49 |
| ❌ | `public_apis_list` | 0.0% | 100.0% | 112.5 | 234.1 | 1500ms | 0/49 |
| ⚠️ | `open_meteo_weather` | 95.92% | 100.0% | 551.6 | 804.5 | 2000ms | 0/49 |
| ❌ | `nasa_apod` | 97.96% | 67.35% | 1277.6 | 10538.0 | 2000ms | 16/49 |
| ❌ | `dog_ceo_random` | 100.0% | 79.59% | 1537.2 | 4785.5 | 2500ms | 10/49 |
| ✅ | `useless_fact` | 100.0% | 100.0% | 568.9 | 849.5 | 2500ms | 0/49 |
| ✅ | `agify_name` | 100.0% | 97.96% | 472.1 | 3237.1 | 2000ms | 1/49 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 100.0% | 233.6 | 1556.1 | 2000ms | 0/49 |
| ✅ | `catfact_random` | 100.0% | 100.0% | 212.3 | 584.9 | 3000ms | 0/49 |
| ✅ | `rest_countries` | 100.0% | 100.0% | 210.8 | 363.3 | 2500ms | 0/49 |
| ✅ | `ipapi_check` | 100.0% | 100.0% | 152.5 | 248.6 | 2500ms | 0/49 |
| ✅ | `coingecko_bitcoin` | 100.0% | 100.0% | 99.9 | 252.0 | 1500ms | 0/49 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `nasa_apod` | 10:00 | 5513.9 | 50.0% |
| `dog_ceo_random` | 14:00 | 3607.4 | 100.0% |
| `dog_ceo_random` | 17:00 | 3075.1 | 66.67% |
| `dog_ceo_random` | 13:00 | 3033.8 | 100.0% |
| `dog_ceo_random` | 12:00 | 2811.7 | 100.0% |
| `nasa_apod` | 07:00 | 2536.7 | 100.0% |
| `nasa_apod` | 18:00 | 2476.7 | 100.0% |
| `nasa_apod` | 13:00 | 2052.3 | 100.0% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
