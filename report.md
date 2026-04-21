# API Reliability Monitor — SLA Report

> Last updated: **2026-04-21 00:00 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **79.4%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 67.57% | 3475.4 | 10206.7 | 1000ms | 132/407 |
| ❌ | `public_apis_list` | 0.0% | 99.51% | 129.9 | 4088.9 | 1500ms | 2/407 |
| ❌ | `nasa_apod` | 62.65% | 38.57% | 4244.3 | 10538.0 | 2000ms | 250/407 |
| ❌ | `ipapi_check` | 94.1% | 100.0% | 159.1 | 353.0 | 2500ms | 0/407 |
| ⚠️ | `open_meteo_weather` | 98.03% | 96.81% | 751.4 | 14877.1 | 2000ms | 13/407 |
| ⚠️ | `dog_ceo_random` | 99.26% | 89.68% | 887.5 | 10244.1 | 2500ms | 42/407 |
| ✅ | `catfact_random` | 99.26% | 99.26% | 277.1 | 10080.2 | 3000ms | 3/407 |
| ✅ | `useless_fact` | 99.51% | 99.02% | 587.1 | 10229.6 | 2500ms | 4/407 |
| ✅ | `agify_name` | 100.0% | 99.75% | 373.7 | 3237.1 | 2000ms | 1/407 |
| ✅ | `rest_countries` | 100.0% | 99.02% | 261.0 | 7269.1 | 2500ms | 4/407 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.75% | 232.9 | 2314.9 | 2000ms | 1/407 |
| ✅ | `coingecko_bitcoin` | 100.0% | 100.0% | 100.8 | 252.0 | 1500ms | 0/407 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `numbers_trivia` | 00:00 | 6402.8 | 62.5% |
| `nasa_apod` | 03:00 | 5952.4 | 90.91% |
| `nasa_apod` | 17:00 | 5778.8 | 70.83% |
| `nasa_apod` | 18:00 | 5606.7 | 82.35% |
| `nasa_apod` | 00:00 | 5195.1 | 75.0% |
| `nasa_apod` | 11:00 | 4978.5 | 62.5% |
| `nasa_apod` | 23:00 | 4535.5 | 55.17% |
| `nasa_apod` | 14:00 | 4500.5 | 62.5% |
| `nasa_apod` | 19:00 | 4499.4 | 60.87% |
| `nasa_apod` | 21:00 | 4468.9 | 52.17% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
