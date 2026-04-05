# API Reliability Monitor — SLA Report

> Last updated: **2026-04-05 15:44 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **82.5%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 100.0% | 301.9 | 517.6 | 1000ms | 0/91 |
| ❌ | `public_apis_list` | 0.0% | 100.0% | 116.0 | 234.1 | 1500ms | 0/91 |
| ⚠️ | `ipapi_check` | 96.7% | 100.0% | 155.0 | 248.6 | 2500ms | 0/91 |
| ❌ | `dog_ceo_random` | 97.8% | 72.53% | 1753.1 | 5142.0 | 2500ms | 25/91 |
| ❌ | `nasa_apod` | 97.8% | 68.13% | 1301.2 | 10538.0 | 2000ms | 29/91 |
| ⚠️ | `open_meteo_weather` | 97.8% | 98.9% | 583.4 | 2550.7 | 2000ms | 1/91 |
| ✅ | `useless_fact` | 100.0% | 100.0% | 590.5 | 2439.0 | 2500ms | 0/91 |
| ✅ | `agify_name` | 100.0% | 98.9% | 421.6 | 3237.1 | 2000ms | 1/91 |
| ✅ | `rest_countries` | 100.0% | 97.8% | 353.7 | 7269.1 | 2500ms | 2/91 |
| ✅ | `catfact_random` | 100.0% | 100.0% | 249.8 | 1218.5 | 3000ms | 0/91 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 100.0% | 239.9 | 1556.1 | 2000ms | 0/91 |
| ✅ | `coingecko_bitcoin` | 100.0% | 100.0% | 103.3 | 252.0 | 1500ms | 0/91 |

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
