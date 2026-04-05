# API Reliability Monitor — SLA Report

> Last updated: **2026-04-05 08:27 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **82.8%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 100.0% | 305.7 | 517.6 | 1000ms | 0/81 |
| ❌ | `public_apis_list` | 0.0% | 100.0% | 116.0 | 234.1 | 1500ms | 0/81 |
| ❌ | `nasa_apod` | 97.53% | 69.14% | 1301.1 | 10538.0 | 2000ms | 25/81 |
| ⚠️ | `open_meteo_weather` | 97.53% | 100.0% | 566.0 | 1426.6 | 2000ms | 0/81 |
| ⚠️ | `ipapi_check` | 98.77% | 100.0% | 155.1 | 248.6 | 2500ms | 0/81 |
| ❌ | `dog_ceo_random` | 100.0% | 76.54% | 1651.3 | 4785.5 | 2500ms | 19/81 |
| ✅ | `useless_fact` | 100.0% | 100.0% | 579.2 | 1705.0 | 2500ms | 0/81 |
| ✅ | `agify_name` | 100.0% | 98.77% | 432.6 | 3237.1 | 2000ms | 1/81 |
| ✅ | `rest_countries` | 100.0% | 98.77% | 286.6 | 5081.4 | 2500ms | 1/81 |
| ✅ | `catfact_random` | 100.0% | 100.0% | 248.2 | 1218.5 | 3000ms | 0/81 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 100.0% | 247.2 | 1556.1 | 2000ms | 0/81 |
| ✅ | `coingecko_bitcoin` | 100.0% | 100.0% | 102.1 | 252.0 | 1500ms | 0/81 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `nasa_apod` | 10:00 | 3753.5 | 33.33% |
| `dog_ceo_random` | 17:00 | 3292.2 | 80.0% |
| `dog_ceo_random` | 03:00 | 3274.4 | 100.0% |
| `dog_ceo_random` | 14:00 | 3011.8 | 75.0% |
| `dog_ceo_random` | 13:00 | 2942.8 | 100.0% |
| `nasa_apod` | 03:00 | 2530.9 | 100.0% |
| `nasa_apod` | 22:00 | 2191.3 | 16.67% |
| `nasa_apod` | 07:00 | 2071.8 | 75.0% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
