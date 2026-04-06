# API Reliability Monitor — SLA Report

> Last updated: **2026-04-06 09:55 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **82.4%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 100.0% | 302.9 | 524.7 | 1000ms | 0/109 |
| ❌ | `public_apis_list` | 0.0% | 100.0% | 115.7 | 234.1 | 1500ms | 0/109 |
| ⚠️ | `ipapi_check` | 95.41% | 100.0% | 156.6 | 248.6 | 2500ms | 0/109 |
| ⚠️ | `open_meteo_weather` | 97.25% | 99.08% | 575.9 | 2550.7 | 2000ms | 1/109 |
| ❌ | `dog_ceo_random` | 98.17% | 67.89% | 1880.9 | 5142.0 | 2500ms | 35/109 |
| ❌ | `nasa_apod` | 98.17% | 71.56% | 1205.4 | 10538.0 | 2000ms | 31/109 |
| ✅ | `useless_fact` | 100.0% | 100.0% | 572.1 | 2439.0 | 2500ms | 0/109 |
| ✅ | `agify_name` | 100.0% | 99.08% | 413.1 | 3237.1 | 2000ms | 1/109 |
| ✅ | `rest_countries` | 100.0% | 98.17% | 330.1 | 7269.1 | 2500ms | 2/109 |
| ✅ | `catfact_random` | 100.0% | 100.0% | 248.2 | 1218.5 | 3000ms | 0/109 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 100.0% | 240.7 | 1556.1 | 2000ms | 0/109 |
| ✅ | `coingecko_bitcoin` | 100.0% | 100.0% | 103.2 | 252.0 | 1500ms | 0/109 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `dog_ceo_random` | 13:00 | 3675.8 | 100.0% |
| `dog_ceo_random` | 17:00 | 3338.8 | 83.33% |
| `dog_ceo_random` | 03:00 | 3274.4 | 100.0% |
| `nasa_apod` | 10:00 | 2892.2 | 25.0% |
| `nasa_apod` | 03:00 | 2530.9 | 100.0% |
| `dog_ceo_random` | 14:00 | 2501.6 | 66.67% |
| `nasa_apod` | 22:00 | 2253.1 | 28.57% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
