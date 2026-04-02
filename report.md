# API Reliability Monitor — SLA Report

> Last updated: **2026-04-02 09:41 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **8/12** &nbsp;|&nbsp; Avg uptime: **83.3%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 100.0% | 411.6 | 498.3 | 1000ms | 0/4 |
| ❌ | `public_apis_list` | 0.0% | 100.0% | 46.2 | 59.9 | 1500ms | 0/4 |
| ❌ | `dog_ceo_random` | 100.0% | 75.0% | 2137.9 | 2743.5 | 2500ms | 1/4 |
| ❌ | `nasa_apod` | 100.0% | 75.0% | 845.7 | 2530.3 | 2000ms | 1/4 |
| ✅ | `open_meteo_weather` | 100.0% | 100.0% | 674.8 | 804.5 | 2000ms | 0/4 |
| ✅ | `useless_fact` | 100.0% | 100.0% | 606.3 | 683.8 | 2500ms | 0/4 |
| ✅ | `agify_name` | 100.0% | 100.0% | 604.3 | 733.3 | 2000ms | 0/4 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 100.0% | 369.4 | 737.9 | 2000ms | 0/4 |
| ✅ | `catfact_random` | 100.0% | 100.0% | 286.6 | 386.9 | 3000ms | 0/4 |
| ✅ | `rest_countries` | 100.0% | 100.0% | 258.9 | 281.3 | 2500ms | 0/4 |
| ✅ | `ipapi_check` | 100.0% | 100.0% | 147.9 | 188.1 | 2500ms | 0/4 |
| ✅ | `coingecko_bitcoin` | 100.0% | 100.0% | 107.5 | 124.5 | 1500ms | 0/4 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `dog_ceo_random` | 08:00 | 2743.5 | 100.0% |
| `nasa_apod` | 07:00 | 2530.3 | 100.0% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
