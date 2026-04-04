# API Reliability Monitor — SLA Report

> Last updated: **2026-04-04 13:18 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **82.8%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 100.0% | 306.1 | 517.6 | 1000ms | 0/58 |
| ❌ | `public_apis_list` | 0.0% | 100.0% | 113.4 | 234.1 | 1500ms | 0/58 |
| ⚠️ | `open_meteo_weather` | 96.55% | 100.0% | 578.3 | 1426.6 | 2000ms | 0/58 |
| ❌ | `nasa_apod` | 98.28% | 68.97% | 1241.1 | 10538.0 | 2000ms | 18/58 |
| ⚠️ | `ipapi_check` | 98.28% | 100.0% | 153.8 | 248.6 | 2500ms | 0/58 |
| ❌ | `dog_ceo_random` | 100.0% | 79.31% | 1548.6 | 4785.5 | 2500ms | 12/58 |
| ✅ | `useless_fact` | 100.0% | 100.0% | 584.9 | 1705.0 | 2500ms | 0/58 |
| ✅ | `agify_name` | 100.0% | 98.28% | 454.2 | 3237.1 | 2000ms | 1/58 |
| ✅ | `catfact_random` | 100.0% | 100.0% | 247.0 | 1218.5 | 3000ms | 0/58 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 100.0% | 239.0 | 1556.1 | 2000ms | 0/58 |
| ✅ | `rest_countries` | 100.0% | 100.0% | 208.3 | 363.3 | 2500ms | 0/58 |
| ✅ | `coingecko_bitcoin` | 100.0% | 100.0% | 101.9 | 252.0 | 1500ms | 0/58 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `nasa_apod` | 10:00 | 3753.5 | 33.33% |
| `dog_ceo_random` | 14:00 | 3607.4 | 100.0% |
| `dog_ceo_random` | 17:00 | 3075.1 | 66.67% |
| `dog_ceo_random` | 13:00 | 2942.8 | 100.0% |
| `nasa_apod` | 18:00 | 2476.7 | 100.0% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
