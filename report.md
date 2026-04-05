# API Reliability Monitor — SLA Report

> Last updated: **2026-04-05 09:57 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **82.7%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 100.0% | 305.7 | 517.6 | 1000ms | 0/83 |
| ❌ | `public_apis_list` | 0.0% | 100.0% | 117.2 | 234.1 | 1500ms | 0/83 |
| ❌ | `nasa_apod` | 97.59% | 68.67% | 1303.6 | 10538.0 | 2000ms | 26/83 |
| ⚠️ | `open_meteo_weather` | 97.59% | 98.8% | 590.9 | 2550.7 | 2000ms | 1/83 |
| ⚠️ | `ipapi_check` | 97.59% | 100.0% | 153.9 | 248.6 | 2500ms | 0/83 |
| ❌ | `dog_ceo_random` | 100.0% | 75.9% | 1677.4 | 4785.5 | 2500ms | 20/83 |
| ✅ | `useless_fact` | 100.0% | 100.0% | 577.0 | 1705.0 | 2500ms | 0/83 |
| ✅ | `agify_name` | 100.0% | 98.8% | 429.9 | 3237.1 | 2000ms | 1/83 |
| ✅ | `rest_countries` | 100.0% | 98.8% | 285.5 | 5081.4 | 2500ms | 1/83 |
| ✅ | `catfact_random` | 100.0% | 100.0% | 246.7 | 1218.5 | 3000ms | 0/83 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 100.0% | 245.5 | 1556.1 | 2000ms | 0/83 |
| ✅ | `coingecko_bitcoin` | 100.0% | 100.0% | 101.0 | 252.0 | 1500ms | 0/83 |

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
