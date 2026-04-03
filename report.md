# API Reliability Monitor — SLA Report

> Last updated: **2026-04-03 22:48 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **7/12** &nbsp;|&nbsp; Avg uptime: **82.8%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 100.0% | 301.5 | 506.9 | 1000ms | 0/43 |
| ❌ | `public_apis_list` | 0.0% | 100.0% | 116.6 | 234.1 | 1500ms | 0/43 |
| ⚠️ | `open_meteo_weather` | 95.35% | 100.0% | 543.2 | 804.5 | 2000ms | 0/43 |
| ❌ | `nasa_apod` | 97.67% | 65.12% | 1351.3 | 10538.0 | 2000ms | 15/43 |
| ❌ | `dog_ceo_random` | 100.0% | 76.74% | 1608.0 | 4785.5 | 2500ms | 10/43 |
| ✅ | `useless_fact` | 100.0% | 100.0% | 564.8 | 849.5 | 2500ms | 0/43 |
| ✅ | `agify_name` | 100.0% | 97.67% | 482.0 | 3237.1 | 2000ms | 1/43 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 100.0% | 244.3 | 1556.1 | 2000ms | 0/43 |
| ✅ | `catfact_random` | 100.0% | 100.0% | 223.9 | 584.9 | 3000ms | 0/43 |
| ✅ | `rest_countries` | 100.0% | 100.0% | 208.5 | 363.3 | 2500ms | 0/43 |
| ✅ | `ipapi_check` | 100.0% | 100.0% | 155.3 | 248.6 | 2500ms | 0/43 |
| ✅ | `coingecko_bitcoin` | 100.0% | 100.0% | 100.4 | 252.0 | 1500ms | 0/43 |

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
