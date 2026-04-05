# API Reliability Monitor — SLA Report

> Last updated: **2026-04-05 19:46 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **82.6%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 100.0% | 299.1 | 524.7 | 1000ms | 0/97 |
| ❌ | `public_apis_list` | 0.0% | 100.0% | 116.0 | 234.1 | 1500ms | 0/97 |
| ⚠️ | `ipapi_check` | 96.91% | 100.0% | 156.4 | 248.6 | 2500ms | 0/97 |
| ❌ | `dog_ceo_random` | 97.94% | 68.04% | 1854.5 | 5142.0 | 2500ms | 31/97 |
| ❌ | `nasa_apod` | 97.94% | 70.1% | 1252.9 | 10538.0 | 2000ms | 29/97 |
| ⚠️ | `open_meteo_weather` | 97.94% | 98.97% | 579.4 | 2550.7 | 2000ms | 1/97 |
| ✅ | `useless_fact` | 100.0% | 100.0% | 580.9 | 2439.0 | 2500ms | 0/97 |
| ✅ | `agify_name` | 100.0% | 98.97% | 414.7 | 3237.1 | 2000ms | 1/97 |
| ✅ | `rest_countries` | 100.0% | 97.94% | 343.3 | 7269.1 | 2500ms | 2/97 |
| ✅ | `catfact_random` | 100.0% | 100.0% | 249.0 | 1218.5 | 3000ms | 0/97 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 100.0% | 238.8 | 1556.1 | 2000ms | 0/97 |
| ✅ | `coingecko_bitcoin` | 100.0% | 100.0% | 103.4 | 252.0 | 1500ms | 0/97 |

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
| `nasa_apod` | 22:00 | 2191.3 | 16.67% |
| `nasa_apod` | 07:00 | 2071.8 | 75.0% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
