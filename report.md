# API Reliability Monitor — SLA Report

> Last updated: **2026-04-05 11:49 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **82.8%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 100.0% | 304.4 | 517.6 | 1000ms | 0/86 |
| ❌ | `public_apis_list` | 0.0% | 100.0% | 117.8 | 234.1 | 1500ms | 0/86 |
| ❌ | `nasa_apod` | 97.67% | 68.6% | 1298.0 | 10538.0 | 2000ms | 27/86 |
| ⚠️ | `open_meteo_weather` | 97.67% | 98.84% | 588.3 | 2550.7 | 2000ms | 1/86 |
| ⚠️ | `ipapi_check` | 97.67% | 100.0% | 154.0 | 248.6 | 2500ms | 0/86 |
| ❌ | `dog_ceo_random` | 100.0% | 73.26% | 1728.1 | 4785.5 | 2500ms | 23/86 |
| ✅ | `useless_fact` | 100.0% | 100.0% | 595.2 | 2439.0 | 2500ms | 0/86 |
| ✅ | `agify_name` | 100.0% | 98.84% | 425.1 | 3237.1 | 2000ms | 1/86 |
| ✅ | `rest_countries` | 100.0% | 98.84% | 281.5 | 5081.4 | 2500ms | 1/86 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 100.0% | 243.7 | 1556.1 | 2000ms | 0/86 |
| ✅ | `catfact_random` | 100.0% | 100.0% | 243.6 | 1218.5 | 3000ms | 0/86 |
| ✅ | `coingecko_bitcoin` | 100.0% | 100.0% | 101.9 | 252.0 | 1500ms | 0/86 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `dog_ceo_random` | 17:00 | 3292.2 | 80.0% |
| `dog_ceo_random` | 03:00 | 3274.4 | 100.0% |
| `dog_ceo_random` | 14:00 | 3011.8 | 75.0% |
| `dog_ceo_random` | 13:00 | 2942.8 | 100.0% |
| `nasa_apod` | 10:00 | 2892.2 | 25.0% |
| `nasa_apod` | 03:00 | 2530.9 | 100.0% |
| `nasa_apod` | 22:00 | 2191.3 | 16.67% |
| `nasa_apod` | 07:00 | 2071.8 | 75.0% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
