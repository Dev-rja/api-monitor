# API Reliability Monitor — SLA Report

> Last updated: **2026-04-03 15:01 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **7/12** &nbsp;|&nbsp; Avg uptime: **82.8%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 100.0% | 284.2 | 506.2 | 1000ms | 0/32 |
| ❌ | `public_apis_list` | 0.0% | 100.0% | 112.2 | 234.1 | 1500ms | 0/32 |
| ❌ | `nasa_apod` | 96.88% | 65.63% | 1421.8 | 10538.0 | 2000ms | 11/32 |
| ⚠️ | `open_meteo_weather` | 96.88% | 100.0% | 530.6 | 804.5 | 2000ms | 0/32 |
| ❌ | `dog_ceo_random` | 100.0% | 71.88% | 1804.8 | 4785.5 | 2500ms | 9/32 |
| ✅ | `useless_fact` | 100.0% | 100.0% | 544.6 | 829.9 | 2500ms | 0/32 |
| ✅ | `agify_name` | 100.0% | 96.88% | 508.0 | 3237.1 | 2000ms | 1/32 |
| ✅ | `catfact_random` | 100.0% | 100.0% | 235.0 | 584.9 | 3000ms | 0/32 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 100.0% | 230.5 | 737.9 | 2000ms | 0/32 |
| ✅ | `rest_countries` | 100.0% | 100.0% | 201.4 | 363.3 | 2500ms | 0/32 |
| ✅ | `ipapi_check` | 100.0% | 100.0% | 163.2 | 248.6 | 2500ms | 0/32 |
| ✅ | `coingecko_bitcoin` | 100.0% | 100.0% | 104.1 | 195.8 | 1500ms | 0/32 |

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
