# API Reliability Monitor — SLA Report

> Last updated: **2026-04-04 10:34 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **82.7%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 100.0% | 307.4 | 517.6 | 1000ms | 0/54 |
| ❌ | `public_apis_list` | 0.0% | 100.0% | 114.8 | 234.1 | 1500ms | 0/54 |
| ⚠️ | `open_meteo_weather` | 96.3% | 100.0% | 548.1 | 804.5 | 2000ms | 0/54 |
| ❌ | `nasa_apod` | 98.15% | 66.67% | 1281.4 | 10538.0 | 2000ms | 18/54 |
| ⚠️ | `ipapi_check` | 98.15% | 100.0% | 150.8 | 248.6 | 2500ms | 0/54 |
| ⚠️ | `dog_ceo_random` | 100.0% | 81.48% | 1511.5 | 4785.5 | 2500ms | 10/54 |
| ✅ | `useless_fact` | 100.0% | 100.0% | 587.1 | 1705.0 | 2500ms | 0/54 |
| ✅ | `agify_name` | 100.0% | 98.15% | 461.2 | 3237.1 | 2000ms | 1/54 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 100.0% | 239.8 | 1556.1 | 2000ms | 0/54 |
| ✅ | `catfact_random` | 100.0% | 100.0% | 223.6 | 584.9 | 3000ms | 0/54 |
| ✅ | `rest_countries` | 100.0% | 100.0% | 208.7 | 363.3 | 2500ms | 0/54 |
| ✅ | `coingecko_bitcoin` | 100.0% | 100.0% | 98.2 | 252.0 | 1500ms | 0/54 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `nasa_apod` | 10:00 | 3753.5 | 33.33% |
| `dog_ceo_random` | 14:00 | 3607.4 | 100.0% |
| `dog_ceo_random` | 17:00 | 3075.1 | 66.67% |
| `dog_ceo_random` | 13:00 | 3033.8 | 100.0% |
| `dog_ceo_random` | 12:00 | 2811.7 | 100.0% |
| `nasa_apod` | 18:00 | 2476.7 | 100.0% |
| `nasa_apod` | 13:00 | 2052.3 | 100.0% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
