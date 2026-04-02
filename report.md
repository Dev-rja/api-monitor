# API Reliability Monitor — SLA Report

> Last updated: **2026-04-02 12:36 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **8/12** &nbsp;|&nbsp; Avg uptime: **83.3%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 100.0% | 299.1 | 498.3 | 1000ms | 0/7 |
| ❌ | `public_apis_list` | 0.0% | 100.0% | 110.3 | 197.0 | 1500ms | 0/7 |
| ❌ | `dog_ceo_random` | 100.0% | 71.43% | 2032.7 | 2811.7 | 2500ms | 2/7 |
| ❌ | `nasa_apod` | 100.0% | 71.43% | 1014.4 | 2644.3 | 2000ms | 2/7 |
| ✅ | `open_meteo_weather` | 100.0% | 100.0% | 577.6 | 804.5 | 2000ms | 0/7 |
| ✅ | `useless_fact` | 100.0% | 100.0% | 534.8 | 683.8 | 2500ms | 0/7 |
| ✅ | `agify_name` | 100.0% | 100.0% | 475.2 | 733.3 | 2000ms | 0/7 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 100.0% | 299.2 | 737.9 | 2000ms | 0/7 |
| ✅ | `catfact_random` | 100.0% | 100.0% | 222.4 | 386.9 | 3000ms | 0/7 |
| ✅ | `rest_countries` | 100.0% | 100.0% | 184.7 | 281.3 | 2500ms | 0/7 |
| ✅ | `ipapi_check` | 100.0% | 100.0% | 155.1 | 188.1 | 2500ms | 0/7 |
| ✅ | `coingecko_bitcoin` | 100.0% | 100.0% | 91.8 | 124.5 | 1500ms | 0/7 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `dog_ceo_random` | 12:00 | 2811.7 | 100.0% |
| `dog_ceo_random` | 08:00 | 2743.5 | 100.0% |
| `nasa_apod` | 11:00 | 2644.3 | 100.0% |
| `nasa_apod` | 07:00 | 2530.3 | 100.0% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
