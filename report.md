# API Reliability Monitor — SLA Report

> Last updated: **2026-04-20 20:31 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **79.4%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 68.24% | 3410.0 | 10206.7 | 1000ms | 128/403 |
| ❌ | `public_apis_list` | 0.0% | 99.75% | 120.3 | 3806.8 | 1500ms | 1/403 |
| ❌ | `nasa_apod` | 62.78% | 38.71% | 4231.2 | 10538.0 | 2000ms | 247/403 |
| ❌ | `ipapi_check` | 94.04% | 100.0% | 159.3 | 353.0 | 2500ms | 0/403 |
| ⚠️ | `open_meteo_weather` | 98.01% | 96.77% | 752.7 | 14877.1 | 2000ms | 13/403 |
| ⚠️ | `dog_ceo_random` | 99.26% | 89.58% | 891.7 | 10244.1 | 2500ms | 42/403 |
| ✅ | `catfact_random` | 99.26% | 99.5% | 269.0 | 10080.2 | 3000ms | 2/403 |
| ✅ | `useless_fact` | 99.5% | 99.01% | 587.2 | 10229.6 | 2500ms | 4/403 |
| ✅ | `agify_name` | 100.0% | 99.75% | 373.3 | 3237.1 | 2000ms | 1/403 |
| ✅ | `rest_countries` | 100.0% | 99.01% | 260.6 | 7269.1 | 2500ms | 4/403 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.75% | 232.8 | 2314.9 | 2000ms | 1/403 |
| ✅ | `coingecko_bitcoin` | 100.0% | 100.0% | 100.9 | 252.0 | 1500ms | 0/403 |

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
| `nasa_apod` | 21:00 | 4556.5 | 50.0% |
| `nasa_apod` | 14:00 | 4500.5 | 62.5% |
| `nasa_apod` | 19:00 | 4499.4 | 60.87% |
| `nasa_apod` | 20:00 | 4457.5 | 67.86% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
