# API Reliability Monitor — SLA Report

> Last updated: **2026-04-02 23:20 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **7/12** &nbsp;|&nbsp; Avg uptime: **83.3%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 100.0% | 294.2 | 498.3 | 1000ms | 0/19 |
| ❌ | `public_apis_list` | 0.0% | 100.0% | 104.8 | 202.3 | 1500ms | 0/19 |
| ❌ | `dog_ceo_random` | 100.0% | 73.68% | 1779.0 | 4785.5 | 2500ms | 5/19 |
| ❌ | `nasa_apod` | 100.0% | 73.68% | 992.7 | 2649.0 | 2000ms | 5/19 |
| ⚠️ | `agify_name` | 100.0% | 94.74% | 564.7 | 3237.1 | 2000ms | 1/19 |
| ✅ | `useless_fact` | 100.0% | 100.0% | 564.1 | 829.9 | 2500ms | 0/19 |
| ✅ | `open_meteo_weather` | 100.0% | 100.0% | 548.4 | 804.5 | 2000ms | 0/19 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 100.0% | 248.5 | 737.9 | 2000ms | 0/19 |
| ✅ | `catfact_random` | 100.0% | 100.0% | 230.5 | 417.8 | 3000ms | 0/19 |
| ✅ | `rest_countries` | 100.0% | 100.0% | 203.4 | 363.3 | 2500ms | 0/19 |
| ✅ | `ipapi_check` | 100.0% | 100.0% | 163.7 | 248.6 | 2500ms | 0/19 |
| ✅ | `coingecko_bitcoin` | 100.0% | 100.0% | 102.4 | 195.8 | 1500ms | 0/19 |

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
| `nasa_apod` | 11:00 | 2644.3 | 100.0% |
| `nasa_apod` | 18:00 | 2630.6 | 100.0% |
| `nasa_apod` | 07:00 | 2530.3 | 100.0% |
| `nasa_apod` | 20:00 | 2344.2 | 100.0% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
