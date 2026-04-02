# API Reliability Monitor — SLA Report

> Last updated: **2026-04-02 10:37 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **8/12** &nbsp;|&nbsp; Avg uptime: **83.3%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 100.0% | 354.3 | 498.3 | 1000ms | 0/5 |
| ❌ | `public_apis_list` | 0.0% | 100.0% | 76.2 | 196.1 | 1500ms | 0/5 |
| ⚠️ | `dog_ceo_random` | 100.0% | 80.0% | 2079.6 | 2743.5 | 2500ms | 1/5 |
| ⚠️ | `nasa_apod` | 100.0% | 80.0% | 774.5 | 2530.3 | 2000ms | 1/5 |
| ✅ | `open_meteo_weather` | 100.0% | 100.0% | 628.2 | 804.5 | 2000ms | 0/5 |
| ✅ | `useless_fact` | 100.0% | 100.0% | 591.3 | 683.8 | 2500ms | 0/5 |
| ✅ | `agify_name` | 100.0% | 100.0% | 544.0 | 733.3 | 2000ms | 0/5 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 100.0% | 338.8 | 737.9 | 2000ms | 0/5 |
| ✅ | `catfact_random` | 100.0% | 100.0% | 276.7 | 386.9 | 3000ms | 0/5 |
| ✅ | `rest_countries` | 100.0% | 100.0% | 224.0 | 281.3 | 2500ms | 0/5 |
| ✅ | `ipapi_check` | 100.0% | 100.0% | 148.2 | 188.1 | 2500ms | 0/5 |
| ✅ | `coingecko_bitcoin` | 100.0% | 100.0% | 102.5 | 124.5 | 1500ms | 0/5 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `dog_ceo_random` | 08:00 | 2743.5 | 100.0% |
| `nasa_apod` | 07:00 | 2530.3 | 100.0% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
