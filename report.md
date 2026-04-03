# API Reliability Monitor — SLA Report

> Last updated: **2026-04-03 04:56 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **8/12** &nbsp;|&nbsp; Avg uptime: **83.3%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 100.0% | 288.0 | 498.3 | 1000ms | 0/22 |
| ❌ | `public_apis_list` | 0.0% | 100.0% | 97.6 | 202.3 | 1500ms | 0/22 |
| ❌ | `dog_ceo_random` | 100.0% | 77.27% | 1649.4 | 4785.5 | 2500ms | 5/22 |
| ❌ | `nasa_apod` | 100.0% | 72.73% | 1025.7 | 2697.2 | 2000ms | 6/22 |
| ✅ | `useless_fact` | 100.0% | 100.0% | 554.9 | 829.9 | 2500ms | 0/22 |
| ✅ | `open_meteo_weather` | 100.0% | 100.0% | 545.1 | 804.5 | 2000ms | 0/22 |
| ✅ | `agify_name` | 100.0% | 95.45% | 536.0 | 3237.1 | 2000ms | 1/22 |
| ✅ | `catfact_random` | 100.0% | 100.0% | 247.7 | 474.2 | 3000ms | 0/22 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 100.0% | 241.4 | 737.9 | 2000ms | 0/22 |
| ✅ | `rest_countries` | 100.0% | 100.0% | 199.0 | 363.3 | 2500ms | 0/22 |
| ✅ | `ipapi_check` | 100.0% | 100.0% | 166.7 | 248.6 | 2500ms | 0/22 |
| ✅ | `coingecko_bitcoin` | 100.0% | 100.0% | 102.1 | 195.8 | 1500ms | 0/22 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `dog_ceo_random` | 17:00 | 4785.5 | 100.0% |
| `dog_ceo_random` | 14:00 | 4518.4 | 100.0% |
| `agify_name` | 21:00 | 3237.1 | 100.0% |
| `dog_ceo_random` | 16:00 | 3016.7 | 100.0% |
| `dog_ceo_random` | 12:00 | 2811.7 | 100.0% |
| `dog_ceo_random` | 08:00 | 2743.5 | 100.0% |
| `nasa_apod` | 02:00 | 2697.2 | 100.0% |
| `nasa_apod` | 11:00 | 2644.3 | 100.0% |
| `nasa_apod` | 18:00 | 2630.6 | 100.0% |
| `nasa_apod` | 07:00 | 2530.3 | 100.0% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
