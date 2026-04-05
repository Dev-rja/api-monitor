# API Reliability Monitor — SLA Report

> Last updated: **2026-04-05 16:18 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **82.5%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 100.0% | 300.4 | 517.6 | 1000ms | 0/92 |
| ❌ | `public_apis_list` | 0.0% | 100.0% | 116.9 | 234.1 | 1500ms | 0/92 |
| ⚠️ | `ipapi_check` | 96.74% | 100.0% | 155.0 | 248.6 | 2500ms | 0/92 |
| ❌ | `dog_ceo_random` | 97.83% | 71.74% | 1772.8 | 5142.0 | 2500ms | 26/92 |
| ❌ | `nasa_apod` | 97.83% | 68.48% | 1292.9 | 10538.0 | 2000ms | 29/92 |
| ⚠️ | `open_meteo_weather` | 97.83% | 98.91% | 581.9 | 2550.7 | 2000ms | 1/92 |
| ✅ | `useless_fact` | 100.0% | 100.0% | 587.8 | 2439.0 | 2500ms | 0/92 |
| ✅ | `agify_name` | 100.0% | 98.91% | 418.6 | 3237.1 | 2000ms | 1/92 |
| ✅ | `rest_countries` | 100.0% | 97.83% | 351.4 | 7269.1 | 2500ms | 2/92 |
| ✅ | `catfact_random` | 100.0% | 100.0% | 249.2 | 1218.5 | 3000ms | 0/92 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 100.0% | 240.3 | 1556.1 | 2000ms | 0/92 |
| ✅ | `coingecko_bitcoin` | 100.0% | 100.0% | 103.2 | 252.0 | 1500ms | 0/92 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `dog_ceo_random` | 13:00 | 3675.8 | 100.0% |
| `dog_ceo_random` | 17:00 | 3292.2 | 80.0% |
| `dog_ceo_random` | 03:00 | 3274.4 | 100.0% |
| `nasa_apod` | 10:00 | 2892.2 | 25.0% |
| `nasa_apod` | 03:00 | 2530.9 | 100.0% |
| `dog_ceo_random` | 14:00 | 2501.6 | 66.67% |
| `nasa_apod` | 22:00 | 2191.3 | 16.67% |
| `nasa_apod` | 07:00 | 2071.8 | 75.0% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
