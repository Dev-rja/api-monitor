# API Reliability Monitor — SLA Report

> Last updated: **2026-04-02 11:32 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **8/12** &nbsp;|&nbsp; Avg uptime: **83.3%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 100.0% | 314.3 | 498.3 | 1000ms | 0/6 |
| ❌ | `public_apis_list` | 0.0% | 100.0% | 95.9 | 196.1 | 1500ms | 0/6 |
| ⚠️ | `dog_ceo_random` | 100.0% | 83.33% | 1902.8 | 2743.5 | 2500ms | 1/6 |
| ❌ | `nasa_apod` | 100.0% | 66.67% | 1086.2 | 2644.3 | 2000ms | 2/6 |
| ✅ | `open_meteo_weather` | 100.0% | 100.0% | 593.1 | 804.5 | 2000ms | 0/6 |
| ✅ | `useless_fact` | 100.0% | 100.0% | 549.1 | 683.8 | 2500ms | 0/6 |
| ✅ | `agify_name` | 100.0% | 100.0% | 499.3 | 733.3 | 2000ms | 0/6 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 100.0% | 317.6 | 737.9 | 2000ms | 0/6 |
| ✅ | `catfact_random` | 100.0% | 100.0% | 243.7 | 386.9 | 3000ms | 0/6 |
| ✅ | `rest_countries` | 100.0% | 100.0% | 201.7 | 281.3 | 2500ms | 0/6 |
| ✅ | `ipapi_check` | 100.0% | 100.0% | 151.3 | 188.1 | 2500ms | 0/6 |
| ✅ | `coingecko_bitcoin` | 100.0% | 100.0% | 94.1 | 124.5 | 1500ms | 0/6 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `dog_ceo_random` | 08:00 | 2743.5 | 100.0% |
| `nasa_apod` | 11:00 | 2644.3 | 100.0% |
| `nasa_apod` | 07:00 | 2530.3 | 100.0% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
