# API Reliability Monitor — SLA Report

> Last updated: **2026-04-06 08:44 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **82.4%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 100.0% | 303.2 | 524.7 | 1000ms | 0/108 |
| ❌ | `public_apis_list` | 0.0% | 100.0% | 115.2 | 234.1 | 1500ms | 0/108 |
| ⚠️ | `ipapi_check` | 95.37% | 100.0% | 156.9 | 248.6 | 2500ms | 0/108 |
| ⚠️ | `open_meteo_weather` | 97.22% | 99.07% | 575.8 | 2550.7 | 2000ms | 1/108 |
| ❌ | `dog_ceo_random` | 98.15% | 67.59% | 1879.2 | 5142.0 | 2500ms | 35/108 |
| ❌ | `nasa_apod` | 98.15% | 71.3% | 1212.3 | 10538.0 | 2000ms | 31/108 |
| ✅ | `useless_fact` | 100.0% | 100.0% | 572.8 | 2439.0 | 2500ms | 0/108 |
| ✅ | `agify_name` | 100.0% | 99.07% | 414.6 | 3237.1 | 2000ms | 1/108 |
| ✅ | `rest_countries` | 100.0% | 98.15% | 331.1 | 7269.1 | 2500ms | 2/108 |
| ✅ | `catfact_random` | 100.0% | 100.0% | 246.3 | 1218.5 | 3000ms | 0/108 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 100.0% | 241.0 | 1556.1 | 2000ms | 0/108 |
| ✅ | `coingecko_bitcoin` | 100.0% | 100.0% | 102.8 | 252.0 | 1500ms | 0/108 |

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
