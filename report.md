# API Reliability Monitor — SLA Report

> Last updated: **2026-04-06 13:25 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **82.1%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 100.0% | 301.6 | 524.7 | 1000ms | 0/112 |
| ❌ | `public_apis_list` | 0.0% | 100.0% | 116.0 | 234.1 | 1500ms | 0/112 |
| ❌ | `ipapi_check` | 94.64% | 100.0% | 156.4 | 248.6 | 2500ms | 0/112 |
| ❌ | `nasa_apod` | 95.54% | 69.64% | 1448.6 | 10538.0 | 2000ms | 34/112 |
| ⚠️ | `open_meteo_weather` | 97.32% | 99.11% | 574.2 | 2550.7 | 2000ms | 1/112 |
| ❌ | `dog_ceo_random` | 98.21% | 66.07% | 1955.9 | 5586.8 | 2500ms | 38/112 |
| ✅ | `useless_fact` | 100.0% | 100.0% | 570.0 | 2439.0 | 2500ms | 0/112 |
| ✅ | `agify_name` | 100.0% | 99.11% | 411.6 | 3237.1 | 2000ms | 1/112 |
| ✅ | `rest_countries` | 100.0% | 98.21% | 326.0 | 7269.1 | 2500ms | 2/112 |
| ✅ | `catfact_random` | 100.0% | 100.0% | 244.9 | 1218.5 | 3000ms | 0/112 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 100.0% | 237.3 | 1556.1 | 2000ms | 0/112 |
| ✅ | `coingecko_bitcoin` | 100.0% | 100.0% | 101.9 | 252.0 | 1500ms | 0/112 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `dog_ceo_random` | 13:00 | 4153.6 | 100.0% |
| `nasa_apod` | 11:00 | 3500.1 | 55.56% |
| `dog_ceo_random` | 17:00 | 3338.8 | 83.33% |
| `nasa_apod` | 13:00 | 3279.6 | 50.0% |
| `dog_ceo_random` | 03:00 | 3274.4 | 100.0% |
| `nasa_apod` | 10:00 | 2892.2 | 25.0% |
| `dog_ceo_random` | 11:00 | 2626.8 | 66.67% |
| `nasa_apod` | 03:00 | 2530.9 | 100.0% |
| `dog_ceo_random` | 14:00 | 2501.6 | 66.67% |
| `nasa_apod` | 22:00 | 2253.1 | 28.57% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
