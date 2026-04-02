# API Reliability Monitor — SLA Report

> Last updated: **2026-04-02 20:48 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **8/12** &nbsp;|&nbsp; Avg uptime: **83.3%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 100.0% | 288.2 | 498.3 | 1000ms | 0/15 |
| ❌ | `public_apis_list` | 0.0% | 100.0% | 98.3 | 202.3 | 1500ms | 0/15 |
| ❌ | `dog_ceo_random` | 100.0% | 66.67% | 2120.1 | 4785.5 | 2500ms | 5/15 |
| ❌ | `nasa_apod` | 100.0% | 66.67% | 1128.3 | 2649.0 | 2000ms | 5/15 |
| ✅ | `open_meteo_weather` | 100.0% | 100.0% | 556.0 | 804.5 | 2000ms | 0/15 |
| ✅ | `useless_fact` | 100.0% | 100.0% | 555.1 | 829.9 | 2500ms | 0/15 |
| ✅ | `agify_name` | 100.0% | 100.0% | 403.1 | 733.3 | 2000ms | 0/15 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 100.0% | 262.2 | 737.9 | 2000ms | 0/15 |
| ✅ | `catfact_random` | 100.0% | 100.0% | 242.3 | 417.8 | 3000ms | 0/15 |
| ✅ | `rest_countries` | 100.0% | 100.0% | 196.3 | 320.8 | 2500ms | 0/15 |
| ✅ | `ipapi_check` | 100.0% | 100.0% | 159.6 | 248.6 | 2500ms | 0/15 |
| ✅ | `coingecko_bitcoin` | 100.0% | 100.0% | 94.7 | 195.8 | 1500ms | 0/15 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `dog_ceo_random` | 17:00 | 4785.5 | 100.0% |
| `dog_ceo_random` | 14:00 | 4518.4 | 100.0% |
| `dog_ceo_random` | 16:00 | 3016.7 | 100.0% |
| `dog_ceo_random` | 12:00 | 2811.7 | 100.0% |
| `dog_ceo_random` | 08:00 | 2743.5 | 100.0% |
| `nasa_apod` | 11:00 | 2644.3 | 100.0% |
| `nasa_apod` | 18:00 | 2630.6 | 100.0% |
| `nasa_apod` | 07:00 | 2530.3 | 100.0% |
| `nasa_apod` | 20:00 | 2344.2 | 100.0% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
