# API Reliability Monitor — SLA Report

> Last updated: **2026-04-05 14:21 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **82.8%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 100.0% | 302.5 | 517.6 | 1000ms | 0/89 |
| ❌ | `public_apis_list` | 0.0% | 100.0% | 115.7 | 234.1 | 1500ms | 0/89 |
| ❌ | `nasa_apod` | 97.75% | 68.54% | 1294.7 | 10538.0 | 2000ms | 28/89 |
| ⚠️ | `open_meteo_weather` | 97.75% | 98.88% | 586.0 | 2550.7 | 2000ms | 1/89 |
| ⚠️ | `ipapi_check` | 97.75% | 100.0% | 155.0 | 248.6 | 2500ms | 0/89 |
| ❌ | `dog_ceo_random` | 100.0% | 71.91% | 1785.5 | 5142.0 | 2500ms | 25/89 |
| ✅ | `useless_fact` | 100.0% | 100.0% | 594.0 | 2439.0 | 2500ms | 0/89 |
| ✅ | `agify_name` | 100.0% | 98.88% | 422.3 | 3237.1 | 2000ms | 1/89 |
| ✅ | `rest_countries` | 100.0% | 97.75% | 357.3 | 7269.1 | 2500ms | 2/89 |
| ✅ | `catfact_random` | 100.0% | 100.0% | 245.5 | 1218.5 | 3000ms | 0/89 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 100.0% | 241.9 | 1556.1 | 2000ms | 0/89 |
| ✅ | `coingecko_bitcoin` | 100.0% | 100.0% | 102.1 | 252.0 | 1500ms | 0/89 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `dog_ceo_random` | 13:00 | 3675.8 | 100.0% |
| `dog_ceo_random` | 17:00 | 3292.2 | 80.0% |
| `dog_ceo_random` | 03:00 | 3274.4 | 100.0% |
| `dog_ceo_random` | 14:00 | 2952.6 | 80.0% |
| `nasa_apod` | 10:00 | 2892.2 | 25.0% |
| `nasa_apod` | 03:00 | 2530.9 | 100.0% |
| `nasa_apod` | 22:00 | 2191.3 | 16.67% |
| `nasa_apod` | 07:00 | 2071.8 | 75.0% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
