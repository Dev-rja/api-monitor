# API Reliability Monitor — SLA Report

> Last updated: **2026-04-03 11:12 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **7/12** &nbsp;|&nbsp; Avg uptime: **82.7%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 100.0% | 286.2 | 506.2 | 1000ms | 0/28 |
| ❌ | `public_apis_list` | 0.0% | 100.0% | 109.9 | 221.3 | 1500ms | 0/28 |
| ❌ | `nasa_apod` | 96.43% | 64.29% | 1498.6 | 10538.0 | 2000ms | 10/28 |
| ⚠️ | `open_meteo_weather` | 96.43% | 100.0% | 532.1 | 804.5 | 2000ms | 0/28 |
| ⚠️ | `dog_ceo_random` | 100.0% | 82.14% | 1621.0 | 4785.5 | 2500ms | 5/28 |
| ✅ | `useless_fact` | 100.0% | 100.0% | 542.7 | 829.9 | 2500ms | 0/28 |
| ✅ | `agify_name` | 100.0% | 96.43% | 492.6 | 3237.1 | 2000ms | 1/28 |
| ✅ | `catfact_random` | 100.0% | 100.0% | 253.2 | 584.9 | 3000ms | 0/28 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 100.0% | 235.9 | 737.9 | 2000ms | 0/28 |
| ✅ | `rest_countries` | 100.0% | 100.0% | 206.7 | 363.3 | 2500ms | 0/28 |
| ✅ | `ipapi_check` | 100.0% | 100.0% | 165.9 | 248.6 | 2500ms | 0/28 |
| ✅ | `coingecko_bitcoin` | 100.0% | 100.0% | 106.4 | 195.8 | 1500ms | 0/28 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `nasa_apod` | 10:00 | 5513.9 | 50.0% |
| `dog_ceo_random` | 17:00 | 4785.5 | 100.0% |
| `dog_ceo_random` | 14:00 | 4518.4 | 100.0% |
| `agify_name` | 21:00 | 3237.1 | 100.0% |
| `dog_ceo_random` | 16:00 | 3016.7 | 100.0% |
| `dog_ceo_random` | 12:00 | 2811.7 | 100.0% |
| `nasa_apod` | 02:00 | 2697.2 | 100.0% |
| `nasa_apod` | 18:00 | 2630.6 | 100.0% |
| `nasa_apod` | 11:00 | 2580.7 | 100.0% |
| `nasa_apod` | 07:00 | 2536.7 | 100.0% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
