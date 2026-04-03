# API Reliability Monitor — SLA Report

> Last updated: **2026-04-03 10:25 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **7/12** &nbsp;|&nbsp; Avg uptime: **82.7%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 100.0% | 283.1 | 506.2 | 1000ms | 0/27 |
| ❌ | `public_apis_list` | 0.0% | 100.0% | 111.5 | 221.3 | 1500ms | 0/27 |
| ❌ | `nasa_apod` | 96.3% | 66.67% | 1460.9 | 10538.0 | 2000ms | 9/27 |
| ⚠️ | `open_meteo_weather` | 96.3% | 100.0% | 530.9 | 804.5 | 2000ms | 0/27 |
| ⚠️ | `dog_ceo_random` | 100.0% | 81.48% | 1634.3 | 4785.5 | 2500ms | 5/27 |
| ✅ | `useless_fact` | 100.0% | 100.0% | 540.5 | 829.9 | 2500ms | 0/27 |
| ✅ | `agify_name` | 100.0% | 96.3% | 498.2 | 3237.1 | 2000ms | 1/27 |
| ✅ | `catfact_random` | 100.0% | 100.0% | 249.2 | 584.9 | 3000ms | 0/27 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 100.0% | 233.8 | 737.9 | 2000ms | 0/27 |
| ✅ | `rest_countries` | 100.0% | 100.0% | 203.2 | 363.3 | 2500ms | 0/27 |
| ✅ | `ipapi_check` | 100.0% | 100.0% | 165.1 | 248.6 | 2500ms | 0/27 |
| ✅ | `coingecko_bitcoin` | 100.0% | 100.0% | 105.4 | 195.8 | 1500ms | 0/27 |

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
| `nasa_apod` | 11:00 | 2644.3 | 100.0% |
| `nasa_apod` | 18:00 | 2630.6 | 100.0% |
| `nasa_apod` | 07:00 | 2536.7 | 100.0% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
