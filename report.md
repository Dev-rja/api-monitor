# API Reliability Monitor — SLA Report

> Last updated: **2026-04-03 08:33 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **7/12** &nbsp;|&nbsp; Avg uptime: **83.0%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 100.0% | 289.3 | 506.2 | 1000ms | 0/25 |
| ❌ | `public_apis_list` | 0.0% | 100.0% | 104.3 | 221.3 | 1500ms | 0/25 |
| ⚠️ | `open_meteo_weather` | 96.0% | 100.0% | 530.9 | 804.5 | 2000ms | 0/25 |
| ⚠️ | `dog_ceo_random` | 100.0% | 80.0% | 1632.0 | 4785.5 | 2500ms | 5/25 |
| ❌ | `nasa_apod` | 100.0% | 68.0% | 1138.1 | 2779.4 | 2000ms | 8/25 |
| ✅ | `useless_fact` | 100.0% | 100.0% | 542.3 | 829.9 | 2500ms | 0/25 |
| ✅ | `agify_name` | 100.0% | 96.0% | 516.0 | 3237.1 | 2000ms | 1/25 |
| ✅ | `catfact_random` | 100.0% | 100.0% | 254.9 | 584.9 | 3000ms | 0/25 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 100.0% | 234.6 | 737.9 | 2000ms | 0/25 |
| ✅ | `rest_countries` | 100.0% | 100.0% | 204.4 | 363.3 | 2500ms | 0/25 |
| ✅ | `ipapi_check` | 100.0% | 100.0% | 163.3 | 248.6 | 2500ms | 0/25 |
| ✅ | `coingecko_bitcoin` | 100.0% | 100.0% | 105.7 | 195.8 | 1500ms | 0/25 |

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
