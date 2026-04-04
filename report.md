# API Reliability Monitor — SLA Report

> Last updated: **2026-04-04 11:03 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **82.7%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 100.0% | 305.6 | 517.6 | 1000ms | 0/55 |
| ❌ | `public_apis_list` | 0.0% | 100.0% | 115.8 | 234.1 | 1500ms | 0/55 |
| ⚠️ | `open_meteo_weather` | 96.36% | 100.0% | 547.5 | 804.5 | 2000ms | 0/55 |
| ❌ | `nasa_apod` | 98.18% | 67.27% | 1285.1 | 10538.0 | 2000ms | 18/55 |
| ⚠️ | `ipapi_check` | 98.18% | 100.0% | 150.9 | 248.6 | 2500ms | 0/55 |
| ⚠️ | `dog_ceo_random` | 100.0% | 81.82% | 1496.5 | 4785.5 | 2500ms | 10/55 |
| ✅ | `useless_fact` | 100.0% | 100.0% | 583.5 | 1705.0 | 2500ms | 0/55 |
| ✅ | `agify_name` | 100.0% | 98.18% | 457.4 | 3237.1 | 2000ms | 1/55 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 100.0% | 238.8 | 1556.1 | 2000ms | 0/55 |
| ✅ | `catfact_random` | 100.0% | 100.0% | 224.4 | 584.9 | 3000ms | 0/55 |
| ✅ | `rest_countries` | 100.0% | 100.0% | 207.8 | 363.3 | 2500ms | 0/55 |
| ✅ | `coingecko_bitcoin` | 100.0% | 100.0% | 97.9 | 252.0 | 1500ms | 0/55 |

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
