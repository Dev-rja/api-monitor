# API Reliability Monitor — SLA Report

> Last updated: **2026-04-04 11:40 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **82.7%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 100.0% | 303.6 | 517.6 | 1000ms | 0/56 |
| ❌ | `public_apis_list` | 0.0% | 100.0% | 114.3 | 234.1 | 1500ms | 0/56 |
| ⚠️ | `open_meteo_weather` | 96.43% | 100.0% | 563.2 | 1426.6 | 2000ms | 0/56 |
| ❌ | `nasa_apod` | 98.21% | 67.86% | 1270.8 | 10538.0 | 2000ms | 18/56 |
| ⚠️ | `ipapi_check` | 98.21% | 100.0% | 151.1 | 248.6 | 2500ms | 0/56 |
| ⚠️ | `dog_ceo_random` | 100.0% | 80.36% | 1520.7 | 4785.5 | 2500ms | 11/56 |
| ✅ | `useless_fact` | 100.0% | 100.0% | 581.3 | 1705.0 | 2500ms | 0/56 |
| ✅ | `agify_name` | 100.0% | 98.21% | 454.7 | 3237.1 | 2000ms | 1/56 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 100.0% | 238.4 | 1556.1 | 2000ms | 0/56 |
| ✅ | `catfact_random` | 100.0% | 100.0% | 226.2 | 584.9 | 3000ms | 0/56 |
| ✅ | `rest_countries` | 100.0% | 100.0% | 206.6 | 363.3 | 2500ms | 0/56 |
| ✅ | `coingecko_bitcoin` | 100.0% | 100.0% | 98.5 | 252.0 | 1500ms | 0/56 |

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
