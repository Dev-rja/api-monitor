# API Reliability Monitor — SLA Report

> Last updated: **2026-04-04 19:45 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **82.8%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 100.0% | 306.8 | 517.6 | 1000ms | 0/68 |
| ❌ | `public_apis_list` | 0.0% | 100.0% | 111.8 | 234.1 | 1500ms | 0/68 |
| ⚠️ | `open_meteo_weather` | 97.06% | 100.0% | 572.1 | 1426.6 | 2000ms | 0/68 |
| ❌ | `nasa_apod` | 98.53% | 72.06% | 1156.1 | 10538.0 | 2000ms | 19/68 |
| ⚠️ | `ipapi_check` | 98.53% | 100.0% | 153.8 | 248.6 | 2500ms | 0/68 |
| ❌ | `dog_ceo_random` | 100.0% | 73.53% | 1695.9 | 4785.5 | 2500ms | 18/68 |
| ✅ | `useless_fact` | 100.0% | 100.0% | 578.8 | 1705.0 | 2500ms | 0/68 |
| ✅ | `agify_name` | 100.0% | 98.53% | 448.4 | 3237.1 | 2000ms | 1/68 |
| ✅ | `rest_countries` | 100.0% | 98.53% | 299.2 | 5081.4 | 2500ms | 1/68 |
| ✅ | `catfact_random` | 100.0% | 100.0% | 247.0 | 1218.5 | 3000ms | 0/68 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 100.0% | 237.9 | 1556.1 | 2000ms | 0/68 |
| ✅ | `coingecko_bitcoin` | 100.0% | 100.0% | 99.1 | 252.0 | 1500ms | 0/68 |

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
