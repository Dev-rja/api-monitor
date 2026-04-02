# API Reliability Monitor — SLA Report

> Last updated: **2026-04-02 19:13 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **8/12** &nbsp;|&nbsp; Avg uptime: **83.3%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 100.0% | 282.3 | 498.3 | 1000ms | 0/13 |
| ❌ | `public_apis_list` | 0.0% | 100.0% | 94.8 | 202.3 | 1500ms | 0/13 |
| ❌ | `dog_ceo_random` | 100.0% | 61.54% | 2380.2 | 4785.5 | 2500ms | 5/13 |
| ❌ | `nasa_apod` | 100.0% | 69.23% | 1081.4 | 2649.0 | 2000ms | 4/13 |
| ✅ | `useless_fact` | 100.0% | 100.0% | 553.0 | 829.9 | 2500ms | 0/13 |
| ✅ | `open_meteo_weather` | 100.0% | 100.0% | 549.4 | 804.5 | 2000ms | 0/13 |
| ✅ | `agify_name` | 100.0% | 100.0% | 409.6 | 733.3 | 2000ms | 0/13 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 100.0% | 273.4 | 737.9 | 2000ms | 0/13 |
| ✅ | `catfact_random` | 100.0% | 100.0% | 237.2 | 411.7 | 3000ms | 0/13 |
| ✅ | `rest_countries` | 100.0% | 100.0% | 193.4 | 300.4 | 2500ms | 0/13 |
| ✅ | `ipapi_check` | 100.0% | 100.0% | 164.2 | 248.6 | 2500ms | 0/13 |
| ✅ | `coingecko_bitcoin` | 100.0% | 100.0% | 97.2 | 195.8 | 1500ms | 0/13 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `dog_ceo_random` | 17:00 | 4785.5 | 100.0% |
| `dog_ceo_random` | 14:00 | 4518.4 | 100.0% |
| `dog_ceo_random` | 16:00 | 3016.7 | 100.0% |
| `dog_ceo_random` | 12:00 | 2811.7 | 100.0% |
| `dog_ceo_random` | 08:00 | 2743.5 | 100.0% |
| `nasa_apod` | 19:00 | 2649.0 | 100.0% |
| `nasa_apod` | 11:00 | 2644.3 | 100.0% |
| `nasa_apod` | 18:00 | 2630.6 | 100.0% |
| `nasa_apod` | 07:00 | 2530.3 | 100.0% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
