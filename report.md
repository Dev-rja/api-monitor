# API Reliability Monitor — SLA Report

> Last updated: **2026-04-02 08:35 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **8/12** &nbsp;|&nbsp; Avg uptime: **83.3%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 100.0% | 404.9 | 498.3 | 1000ms | 0/3 |
| ❌ | `public_apis_list` | 0.0% | 100.0% | 42.9 | 59.9 | 1500ms | 0/3 |
| ❌ | `dog_ceo_random` | 100.0% | 66.67% | 2052.2 | 2743.5 | 2500ms | 1/3 |
| ❌ | `nasa_apod` | 100.0% | 66.67% | 1032.8 | 2530.3 | 2000ms | 1/3 |
| ✅ | `open_meteo_weather` | 100.0% | 100.0% | 679.9 | 804.5 | 2000ms | 0/3 |
| ✅ | `agify_name` | 100.0% | 100.0% | 599.6 | 733.3 | 2000ms | 0/3 |
| ✅ | `useless_fact` | 100.0% | 100.0% | 580.4 | 660.7 | 2500ms | 0/3 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 100.0% | 420.0 | 737.9 | 2000ms | 0/3 |
| ✅ | `rest_countries` | 100.0% | 100.0% | 260.8 | 281.3 | 2500ms | 0/3 |
| ✅ | `catfact_random` | 100.0% | 100.0% | 253.2 | 292.6 | 3000ms | 0/3 |
| ✅ | `ipapi_check` | 100.0% | 100.0% | 144.4 | 188.1 | 2500ms | 0/3 |
| ✅ | `coingecko_bitcoin` | 100.0% | 100.0% | 102.0 | 124.5 | 1500ms | 0/3 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `dog_ceo_random` | 08:00 | 2743.5 | 100.0% |
| `nasa_apod` | 07:00 | 2530.3 | 100.0% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
