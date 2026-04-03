# API Reliability Monitor — SLA Report

> Last updated: **2026-04-03 09:35 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **7/12** &nbsp;|&nbsp; Avg uptime: **83.0%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 100.0% | 289.3 | 506.2 | 1000ms | 0/26 |
| ❌ | `public_apis_list` | 0.0% | 100.0% | 107.5 | 221.3 | 1500ms | 0/26 |
| ⚠️ | `open_meteo_weather` | 96.15% | 100.0% | 532.3 | 804.5 | 2000ms | 0/26 |
| ⚠️ | `dog_ceo_random` | 100.0% | 80.77% | 1625.4 | 4785.5 | 2500ms | 5/26 |
| ❌ | `nasa_apod` | 100.0% | 69.23% | 1111.8 | 2779.4 | 2000ms | 8/26 |
| ✅ | `useless_fact` | 100.0% | 100.0% | 544.5 | 829.9 | 2500ms | 0/26 |
| ✅ | `agify_name` | 100.0% | 96.15% | 507.3 | 3237.1 | 2000ms | 1/26 |
| ✅ | `catfact_random` | 100.0% | 100.0% | 256.2 | 584.9 | 3000ms | 0/26 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 100.0% | 235.5 | 737.9 | 2000ms | 0/26 |
| ✅ | `rest_countries` | 100.0% | 100.0% | 205.3 | 363.3 | 2500ms | 0/26 |
| ✅ | `ipapi_check` | 100.0% | 100.0% | 165.9 | 248.6 | 2500ms | 0/26 |
| ✅ | `coingecko_bitcoin` | 100.0% | 100.0% | 106.5 | 195.8 | 1500ms | 0/26 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `dog_ceo_random` | 17:00 | 4785.5 | 100.0% |
| `dog_ceo_random` | 14:00 | 4518.4 | 100.0% |
| `agify_name` | 21:00 | 3237.1 | 100.0% |
| `dog_ceo_random` | 16:00 | 3016.7 | 100.0% |
| `dog_ceo_random` | 12:00 | 2811.7 | 100.0% |
| `nasa_apod` | 02:00 | 2697.2 | 100.0% |
| `nasa_apod` | 11:00 | 2644.3 | 100.0% |
| `nasa_apod` | 18:00 | 2630.6 | 100.0% |
| `nasa_apod` | 07:00 | 2536.7 | 100.0% |
| `nasa_apod` | 20:00 | 2344.2 | 100.0% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
