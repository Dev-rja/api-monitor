# API Reliability Monitor — SLA Report

> Last updated: **2026-04-06 02:31 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **82.5%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 100.0% | 299.4 | 524.7 | 1000ms | 0/105 |
| ❌ | `public_apis_list` | 0.0% | 100.0% | 115.7 | 234.1 | 1500ms | 0/105 |
| ⚠️ | `ipapi_check` | 96.19% | 100.0% | 157.0 | 248.6 | 2500ms | 0/105 |
| ⚠️ | `open_meteo_weather` | 97.14% | 99.05% | 574.0 | 2550.7 | 2000ms | 1/105 |
| ❌ | `dog_ceo_random` | 98.1% | 67.62% | 1865.2 | 5142.0 | 2500ms | 34/105 |
| ❌ | `nasa_apod` | 98.1% | 71.43% | 1215.9 | 10538.0 | 2000ms | 30/105 |
| ✅ | `useless_fact` | 100.0% | 100.0% | 574.3 | 2439.0 | 2500ms | 0/105 |
| ✅ | `agify_name` | 100.0% | 99.05% | 405.0 | 3237.1 | 2000ms | 1/105 |
| ✅ | `rest_countries` | 100.0% | 98.1% | 331.8 | 7269.1 | 2500ms | 2/105 |
| ✅ | `catfact_random` | 100.0% | 100.0% | 247.7 | 1218.5 | 3000ms | 0/105 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 100.0% | 241.4 | 1556.1 | 2000ms | 0/105 |
| ✅ | `coingecko_bitcoin` | 100.0% | 100.0% | 102.2 | 252.0 | 1500ms | 0/105 |

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
| `nasa_apod` | 07:00 | 2071.8 | 75.0% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
