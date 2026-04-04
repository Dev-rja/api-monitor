# API Reliability Monitor — SLA Report

> Last updated: **2026-04-04 04:31 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **7/12** &nbsp;|&nbsp; Avg uptime: **82.8%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 100.0% | 309.6 | 517.6 | 1000ms | 0/47 |
| ❌ | `public_apis_list` | 0.0% | 100.0% | 110.1 | 234.1 | 1500ms | 0/47 |
| ⚠️ | `open_meteo_weather` | 95.74% | 100.0% | 550.3 | 804.5 | 2000ms | 0/47 |
| ❌ | `nasa_apod` | 97.87% | 68.09% | 1265.2 | 10538.0 | 2000ms | 15/47 |
| ❌ | `dog_ceo_random` | 100.0% | 78.72% | 1555.4 | 4785.5 | 2500ms | 10/47 |
| ✅ | `useless_fact` | 100.0% | 100.0% | 568.9 | 849.5 | 2500ms | 0/47 |
| ✅ | `agify_name` | 100.0% | 97.87% | 479.4 | 3237.1 | 2000ms | 1/47 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 100.0% | 234.9 | 1556.1 | 2000ms | 0/47 |
| ✅ | `catfact_random` | 100.0% | 100.0% | 215.9 | 584.9 | 3000ms | 0/47 |
| ✅ | `rest_countries` | 100.0% | 100.0% | 212.7 | 363.3 | 2500ms | 0/47 |
| ✅ | `ipapi_check` | 100.0% | 100.0% | 150.9 | 248.6 | 2500ms | 0/47 |
| ✅ | `coingecko_bitcoin` | 100.0% | 100.0% | 97.8 | 252.0 | 1500ms | 0/47 |

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
