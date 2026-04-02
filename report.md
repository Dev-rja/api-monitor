# API Reliability Monitor — SLA Report

> Last updated: **2026-04-02 18:04 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **8/12** &nbsp;|&nbsp; Avg uptime: **83.3%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 100.0% | 293.7 | 498.3 | 1000ms | 0/12 |
| ❌ | `public_apis_list` | 0.0% | 100.0% | 98.6 | 202.3 | 1500ms | 0/12 |
| ❌ | `dog_ceo_random` | 100.0% | 58.33% | 2423.7 | 4785.5 | 2500ms | 5/12 |
| ❌ | `nasa_apod` | 100.0% | 75.0% | 950.8 | 2644.3 | 2000ms | 3/12 |
| ✅ | `useless_fact` | 100.0% | 100.0% | 571.8 | 829.9 | 2500ms | 0/12 |
| ✅ | `open_meteo_weather` | 100.0% | 100.0% | 561.4 | 804.5 | 2000ms | 0/12 |
| ✅ | `agify_name` | 100.0% | 100.0% | 427.5 | 733.3 | 2000ms | 0/12 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 100.0% | 277.6 | 737.9 | 2000ms | 0/12 |
| ✅ | `catfact_random` | 100.0% | 100.0% | 231.4 | 411.7 | 3000ms | 0/12 |
| ✅ | `rest_countries` | 100.0% | 100.0% | 196.0 | 300.4 | 2500ms | 0/12 |
| ✅ | `ipapi_check` | 100.0% | 100.0% | 161.4 | 248.6 | 2500ms | 0/12 |
| ✅ | `coingecko_bitcoin` | 100.0% | 100.0% | 98.1 | 195.8 | 1500ms | 0/12 |

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

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
