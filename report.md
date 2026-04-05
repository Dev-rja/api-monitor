# API Reliability Monitor — SLA Report

> Last updated: **2026-04-05 16:58 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **82.5%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 100.0% | 298.6 | 517.6 | 1000ms | 0/93 |
| ❌ | `public_apis_list` | 0.0% | 100.0% | 116.1 | 234.1 | 1500ms | 0/93 |
| ⚠️ | `ipapi_check` | 96.77% | 100.0% | 155.3 | 248.6 | 2500ms | 0/93 |
| ❌ | `dog_ceo_random` | 97.85% | 70.97% | 1788.0 | 5142.0 | 2500ms | 27/93 |
| ❌ | `nasa_apod` | 97.85% | 68.82% | 1285.4 | 10538.0 | 2000ms | 29/93 |
| ⚠️ | `open_meteo_weather` | 97.85% | 98.92% | 580.0 | 2550.7 | 2000ms | 1/93 |
| ✅ | `useless_fact` | 100.0% | 100.0% | 585.4 | 2439.0 | 2500ms | 0/93 |
| ✅ | `agify_name` | 100.0% | 98.92% | 417.3 | 3237.1 | 2000ms | 1/93 |
| ✅ | `rest_countries` | 100.0% | 97.85% | 348.7 | 7269.1 | 2500ms | 2/93 |
| ✅ | `catfact_random` | 100.0% | 100.0% | 249.0 | 1218.5 | 3000ms | 0/93 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 100.0% | 239.9 | 1556.1 | 2000ms | 0/93 |
| ✅ | `coingecko_bitcoin` | 100.0% | 100.0% | 103.0 | 252.0 | 1500ms | 0/93 |

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
