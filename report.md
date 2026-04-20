# API Reliability Monitor — SLA Report

> Last updated: **2026-04-20 21:29 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **79.4%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 68.07% | 3426.5 | 10206.7 | 1000ms | 129/404 |
| ❌ | `public_apis_list` | 0.0% | 99.75% | 120.4 | 3806.8 | 1500ms | 1/404 |
| ❌ | `nasa_apod` | 62.87% | 38.61% | 4227.0 | 10538.0 | 2000ms | 248/404 |
| ❌ | `ipapi_check` | 94.06% | 100.0% | 159.3 | 353.0 | 2500ms | 0/404 |
| ⚠️ | `open_meteo_weather` | 98.02% | 96.78% | 752.2 | 14877.1 | 2000ms | 13/404 |
| ⚠️ | `dog_ceo_random` | 99.26% | 89.6% | 890.6 | 10244.1 | 2500ms | 42/404 |
| ✅ | `catfact_random` | 99.26% | 99.5% | 269.3 | 10080.2 | 3000ms | 2/404 |
| ✅ | `useless_fact` | 99.5% | 99.01% | 587.0 | 10229.6 | 2500ms | 4/404 |
| ✅ | `agify_name` | 100.0% | 99.75% | 373.0 | 3237.1 | 2000ms | 1/404 |
| ✅ | `rest_countries` | 100.0% | 99.01% | 260.5 | 7269.1 | 2500ms | 4/404 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.75% | 233.3 | 2314.9 | 2000ms | 1/404 |
| ✅ | `coingecko_bitcoin` | 100.0% | 100.0% | 100.8 | 252.0 | 1500ms | 0/404 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `nasa_apod` | 03:00 | 5952.4 | 90.91% |
| `numbers_trivia` | 00:00 | 5880.9 | 57.14% |
| `nasa_apod` | 17:00 | 5778.8 | 70.83% |
| `nasa_apod` | 18:00 | 5606.7 | 82.35% |
| `nasa_apod` | 11:00 | 4978.5 | 62.5% |
| `nasa_apod` | 00:00 | 4679.5 | 71.43% |
| `nasa_apod` | 14:00 | 4500.5 | 62.5% |
| `nasa_apod` | 19:00 | 4499.4 | 60.87% |
| `nasa_apod` | 21:00 | 4468.9 | 52.17% |
| `nasa_apod` | 20:00 | 4457.5 | 67.86% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
