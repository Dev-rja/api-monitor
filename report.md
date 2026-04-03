# API Reliability Monitor — SLA Report

> Last updated: **2026-04-03 16:29 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **7/12** &nbsp;|&nbsp; Avg uptime: **82.8%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 100.0% | 287.3 | 506.9 | 1000ms | 0/34 |
| ❌ | `public_apis_list` | 0.0% | 100.0% | 111.4 | 234.1 | 1500ms | 0/34 |
| ❌ | `nasa_apod` | 97.06% | 61.76% | 1486.8 | 10538.0 | 2000ms | 13/34 |
| ⚠️ | `open_meteo_weather` | 97.06% | 100.0% | 531.0 | 804.5 | 2000ms | 0/34 |
| ❌ | `dog_ceo_random` | 100.0% | 73.53% | 1764.0 | 4785.5 | 2500ms | 9/34 |
| ✅ | `useless_fact` | 100.0% | 100.0% | 546.5 | 829.9 | 2500ms | 0/34 |
| ✅ | `agify_name` | 100.0% | 97.06% | 500.5 | 3237.1 | 2000ms | 1/34 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 100.0% | 228.2 | 737.9 | 2000ms | 0/34 |
| ✅ | `catfact_random` | 100.0% | 100.0% | 227.4 | 584.9 | 3000ms | 0/34 |
| ✅ | `rest_countries` | 100.0% | 100.0% | 202.4 | 363.3 | 2500ms | 0/34 |
| ✅ | `ipapi_check` | 100.0% | 100.0% | 161.3 | 248.6 | 2500ms | 0/34 |
| ✅ | `coingecko_bitcoin` | 100.0% | 100.0% | 101.4 | 195.8 | 1500ms | 0/34 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `nasa_apod` | 10:00 | 5513.9 | 50.0% |
| `dog_ceo_random` | 17:00 | 4785.5 | 100.0% |
| `dog_ceo_random` | 14:00 | 3607.4 | 100.0% |
| `agify_name` | 21:00 | 3237.1 | 100.0% |
| `dog_ceo_random` | 13:00 | 3033.8 | 100.0% |
| `dog_ceo_random` | 12:00 | 2811.7 | 100.0% |
| `nasa_apod` | 02:00 | 2697.2 | 100.0% |
| `nasa_apod` | 18:00 | 2630.6 | 100.0% |
| `nasa_apod` | 07:00 | 2536.7 | 100.0% |
| `nasa_apod` | 20:00 | 2344.2 | 100.0% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
