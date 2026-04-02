# API Reliability Monitor — SLA Report

> Last updated: **2026-04-02 17:12 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **8/12** &nbsp;|&nbsp; Avg uptime: **83.3%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 100.0% | 306.2 | 498.3 | 1000ms | 0/11 |
| ❌ | `public_apis_list` | 0.0% | 100.0% | 103.5 | 202.3 | 1500ms | 0/11 |
| ❌ | `dog_ceo_random` | 100.0% | 54.55% | 2465.5 | 4785.5 | 2500ms | 5/11 |
| ⚠️ | `nasa_apod` | 100.0% | 81.82% | 798.1 | 2644.3 | 2000ms | 2/11 |
| ✅ | `open_meteo_weather` | 100.0% | 100.0% | 575.4 | 804.5 | 2000ms | 0/11 |
| ✅ | `useless_fact` | 100.0% | 100.0% | 569.9 | 829.9 | 2500ms | 0/11 |
| ✅ | `agify_name` | 100.0% | 100.0% | 450.8 | 733.3 | 2000ms | 0/11 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 100.0% | 287.3 | 737.9 | 2000ms | 0/11 |
| ✅ | `catfact_random` | 100.0% | 100.0% | 222.7 | 411.7 | 3000ms | 0/11 |
| ✅ | `rest_countries` | 100.0% | 100.0% | 198.1 | 300.4 | 2500ms | 0/11 |
| ✅ | `ipapi_check` | 100.0% | 100.0% | 157.0 | 248.6 | 2500ms | 0/11 |
| ✅ | `coingecko_bitcoin` | 100.0% | 100.0% | 92.5 | 195.8 | 1500ms | 0/11 |

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
| `nasa_apod` | 07:00 | 2530.3 | 100.0% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
