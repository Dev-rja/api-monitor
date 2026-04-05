# API Reliability Monitor — SLA Report

> Last updated: **2026-04-05 06:46 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **82.8%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 100.0% | 306.5 | 517.6 | 1000ms | 0/79 |
| ❌ | `public_apis_list` | 0.0% | 100.0% | 114.1 | 234.1 | 1500ms | 0/79 |
| ❌ | `nasa_apod` | 97.47% | 69.62% | 1293.6 | 10538.0 | 2000ms | 24/79 |
| ⚠️ | `open_meteo_weather` | 97.47% | 100.0% | 568.1 | 1426.6 | 2000ms | 0/79 |
| ⚠️ | `ipapi_check` | 98.73% | 100.0% | 154.7 | 248.6 | 2500ms | 0/79 |
| ❌ | `dog_ceo_random` | 100.0% | 75.95% | 1645.8 | 4785.5 | 2500ms | 19/79 |
| ✅ | `useless_fact` | 100.0% | 100.0% | 577.2 | 1705.0 | 2500ms | 0/79 |
| ✅ | `agify_name` | 100.0% | 98.73% | 435.9 | 3237.1 | 2000ms | 1/79 |
| ✅ | `rest_countries` | 100.0% | 98.73% | 289.4 | 5081.4 | 2500ms | 1/79 |
| ✅ | `catfact_random` | 100.0% | 100.0% | 251.1 | 1218.5 | 3000ms | 0/79 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 100.0% | 247.9 | 1556.1 | 2000ms | 0/79 |
| ✅ | `coingecko_bitcoin` | 100.0% | 100.0% | 102.5 | 252.0 | 1500ms | 0/79 |

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
