# API Reliability Monitor — SLA Report

> Last updated: **2026-04-04 07:38 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **82.7%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 100.0% | 305.0 | 517.6 | 1000ms | 0/50 |
| ❌ | `public_apis_list` | 0.0% | 100.0% | 114.4 | 234.1 | 1500ms | 0/50 |
| ⚠️ | `open_meteo_weather` | 96.0% | 100.0% | 548.7 | 804.5 | 2000ms | 0/50 |
| ❌ | `nasa_apod` | 98.0% | 68.0% | 1263.6 | 10538.0 | 2000ms | 16/50 |
| ⚠️ | `ipapi_check` | 98.0% | 100.0% | 150.8 | 248.6 | 2500ms | 0/50 |
| ⚠️ | `dog_ceo_random` | 100.0% | 80.0% | 1538.0 | 4785.5 | 2500ms | 10/50 |
| ✅ | `useless_fact` | 100.0% | 100.0% | 564.5 | 849.5 | 2500ms | 0/50 |
| ✅ | `agify_name` | 100.0% | 98.0% | 469.2 | 3237.1 | 2000ms | 1/50 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 100.0% | 236.7 | 1556.1 | 2000ms | 0/50 |
| ✅ | `catfact_random` | 100.0% | 100.0% | 219.5 | 584.9 | 3000ms | 0/50 |
| ✅ | `rest_countries` | 100.0% | 100.0% | 209.6 | 363.3 | 2500ms | 0/50 |
| ✅ | `coingecko_bitcoin` | 100.0% | 100.0% | 99.9 | 252.0 | 1500ms | 0/50 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `nasa_apod` | 10:00 | 5513.9 | 50.0% |
| `dog_ceo_random` | 14:00 | 3607.4 | 100.0% |
| `dog_ceo_random` | 17:00 | 3075.1 | 66.67% |
| `dog_ceo_random` | 13:00 | 3033.8 | 100.0% |
| `dog_ceo_random` | 12:00 | 2811.7 | 100.0% |
| `nasa_apod` | 18:00 | 2476.7 | 100.0% |
| `nasa_apod` | 13:00 | 2052.3 | 100.0% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
