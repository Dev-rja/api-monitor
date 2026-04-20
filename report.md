# API Reliability Monitor — SLA Report

> Last updated: **2026-04-20 23:10 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **79.4%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 67.73% | 3459.2 | 10206.7 | 1000ms | 131/406 |
| ❌ | `public_apis_list` | 0.0% | 99.51% | 130.1 | 4088.9 | 1500ms | 2/406 |
| ❌ | `nasa_apod` | 62.81% | 38.67% | 4233.1 | 10538.0 | 2000ms | 249/406 |
| ❌ | `ipapi_check` | 94.09% | 100.0% | 159.2 | 353.0 | 2500ms | 0/406 |
| ⚠️ | `open_meteo_weather` | 98.03% | 96.8% | 751.7 | 14877.1 | 2000ms | 13/406 |
| ⚠️ | `dog_ceo_random` | 99.26% | 89.66% | 888.1 | 10244.1 | 2500ms | 42/406 |
| ✅ | `catfact_random` | 99.26% | 99.51% | 268.7 | 10080.2 | 3000ms | 2/406 |
| ✅ | `useless_fact` | 99.51% | 99.01% | 586.8 | 10229.6 | 2500ms | 4/406 |
| ✅ | `agify_name` | 100.0% | 99.75% | 373.5 | 3237.1 | 2000ms | 1/406 |
| ✅ | `rest_countries` | 100.0% | 99.01% | 260.5 | 7269.1 | 2500ms | 4/406 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.75% | 233.1 | 2314.9 | 2000ms | 1/406 |
| ✅ | `coingecko_bitcoin` | 100.0% | 100.0% | 100.8 | 252.0 | 1500ms | 0/406 |

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
| `nasa_apod` | 23:00 | 4535.5 | 55.17% |
| `nasa_apod` | 14:00 | 4500.5 | 62.5% |
| `nasa_apod` | 19:00 | 4499.4 | 60.87% |
| `nasa_apod` | 21:00 | 4468.9 | 52.17% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
