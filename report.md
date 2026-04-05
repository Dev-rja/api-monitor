# API Reliability Monitor — SLA Report

> Last updated: **2026-04-05 05:28 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **82.8%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 100.0% | 306.1 | 517.6 | 1000ms | 0/78 |
| ❌ | `public_apis_list` | 0.0% | 100.0% | 115.0 | 234.1 | 1500ms | 0/78 |
| ❌ | `nasa_apod` | 97.44% | 69.23% | 1304.8 | 10538.0 | 2000ms | 24/78 |
| ⚠️ | `open_meteo_weather` | 97.44% | 100.0% | 568.8 | 1426.6 | 2000ms | 0/78 |
| ⚠️ | `ipapi_check` | 98.72% | 100.0% | 155.0 | 248.6 | 2500ms | 0/78 |
| ❌ | `dog_ceo_random` | 100.0% | 75.64% | 1645.3 | 4785.5 | 2500ms | 19/78 |
| ✅ | `useless_fact` | 100.0% | 100.0% | 577.4 | 1705.0 | 2500ms | 0/78 |
| ✅ | `agify_name` | 100.0% | 98.72% | 438.3 | 3237.1 | 2000ms | 1/78 |
| ✅ | `rest_countries` | 100.0% | 98.72% | 291.1 | 5081.4 | 2500ms | 1/78 |
| ✅ | `catfact_random` | 100.0% | 100.0% | 252.9 | 1218.5 | 3000ms | 0/78 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 100.0% | 247.9 | 1556.1 | 2000ms | 0/78 |
| ✅ | `coingecko_bitcoin` | 100.0% | 100.0% | 101.9 | 252.0 | 1500ms | 0/78 |

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

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
