# API Reliability Monitor — SLA Report

> Last updated: **2026-04-03 15:50 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **7/12** &nbsp;|&nbsp; Avg uptime: **82.8%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 100.0% | 290.9 | 506.9 | 1000ms | 0/33 |
| ❌ | `public_apis_list` | 0.0% | 100.0% | 110.0 | 234.1 | 1500ms | 0/33 |
| ❌ | `nasa_apod` | 96.97% | 63.64% | 1449.8 | 10538.0 | 2000ms | 12/33 |
| ⚠️ | `open_meteo_weather` | 96.97% | 100.0% | 534.4 | 804.5 | 2000ms | 0/33 |
| ❌ | `dog_ceo_random` | 100.0% | 72.73% | 1799.0 | 4785.5 | 2500ms | 9/33 |
| ✅ | `useless_fact` | 100.0% | 100.0% | 549.8 | 829.9 | 2500ms | 0/33 |
| ✅ | `agify_name` | 100.0% | 96.97% | 510.7 | 3237.1 | 2000ms | 1/33 |
| ✅ | `catfact_random` | 100.0% | 100.0% | 232.0 | 584.9 | 3000ms | 0/33 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 100.0% | 229.8 | 737.9 | 2000ms | 0/33 |
| ✅ | `rest_countries` | 100.0% | 100.0% | 205.6 | 363.3 | 2500ms | 0/33 |
| ✅ | `ipapi_check` | 100.0% | 100.0% | 160.9 | 248.6 | 2500ms | 0/33 |
| ✅ | `coingecko_bitcoin` | 100.0% | 100.0% | 102.7 | 195.8 | 1500ms | 0/33 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `nasa_apod` | 10:00 | 5513.9 | 50.0% |
| `dog_ceo_random` | 17:00 | 4785.5 | 100.0% |
| `dog_ceo_random` | 14:00 | 3607.4 | 100.0% |
| `agify_name` | 21:00 | 3237.1 | 100.0% |
| `dog_ceo_random` | 13:00 | 3033.8 | 100.0% |
| `dog_ceo_random` | 16:00 | 3016.7 | 100.0% |
| `dog_ceo_random` | 12:00 | 2811.7 | 100.0% |
| `nasa_apod` | 02:00 | 2697.2 | 100.0% |
| `nasa_apod` | 18:00 | 2630.6 | 100.0% |
| `nasa_apod` | 07:00 | 2536.7 | 100.0% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
