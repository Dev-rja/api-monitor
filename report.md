# API Reliability Monitor — SLA Report

> Last updated: **2026-04-04 21:18 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **82.9%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 100.0% | 307.7 | 517.6 | 1000ms | 0/71 |
| ❌ | `public_apis_list` | 0.0% | 100.0% | 113.6 | 234.1 | 1500ms | 0/71 |
| ⚠️ | `open_meteo_weather` | 97.18% | 100.0% | 572.4 | 1426.6 | 2000ms | 0/71 |
| ❌ | `nasa_apod` | 98.59% | 71.83% | 1156.2 | 10538.0 | 2000ms | 20/71 |
| ⚠️ | `ipapi_check` | 98.59% | 100.0% | 154.6 | 248.6 | 2500ms | 0/71 |
| ❌ | `dog_ceo_random` | 100.0% | 74.65% | 1666.9 | 4785.5 | 2500ms | 18/71 |
| ✅ | `useless_fact` | 100.0% | 100.0% | 575.0 | 1705.0 | 2500ms | 0/71 |
| ✅ | `agify_name` | 100.0% | 98.59% | 445.5 | 3237.1 | 2000ms | 1/71 |
| ✅ | `rest_countries` | 100.0% | 98.59% | 297.0 | 5081.4 | 2500ms | 1/71 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 100.0% | 252.4 | 1556.1 | 2000ms | 0/71 |
| ✅ | `catfact_random` | 100.0% | 100.0% | 244.0 | 1218.5 | 3000ms | 0/71 |
| ✅ | `coingecko_bitcoin` | 100.0% | 100.0% | 100.8 | 252.0 | 1500ms | 0/71 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `nasa_apod` | 10:00 | 3753.5 | 33.33% |
| `dog_ceo_random` | 17:00 | 3292.2 | 80.0% |
| `dog_ceo_random` | 14:00 | 3011.8 | 75.0% |
| `dog_ceo_random` | 13:00 | 2942.8 | 100.0% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
