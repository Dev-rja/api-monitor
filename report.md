# API Reliability Monitor — SLA Report

> Last updated: **2026-04-21 03:39 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **79.4%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 67.4% | 3491.6 | 10206.7 | 1000ms | 133/408 |
| ❌ | `public_apis_list` | 0.0% | 99.51% | 129.8 | 4088.9 | 1500ms | 2/408 |
| ❌ | `nasa_apod` | 62.5% | 38.48% | 4259.2 | 10538.0 | 2000ms | 251/408 |
| ❌ | `ipapi_check` | 94.12% | 100.0% | 159.3 | 353.0 | 2500ms | 0/408 |
| ⚠️ | `open_meteo_weather` | 98.04% | 96.81% | 750.9 | 14877.1 | 2000ms | 13/408 |
| ⚠️ | `dog_ceo_random` | 99.26% | 89.71% | 886.4 | 10244.1 | 2500ms | 42/408 |
| ✅ | `catfact_random` | 99.26% | 99.26% | 278.0 | 10080.2 | 3000ms | 3/408 |
| ✅ | `useless_fact` | 99.51% | 99.02% | 587.2 | 10229.6 | 2500ms | 4/408 |
| ✅ | `agify_name` | 100.0% | 99.75% | 373.6 | 3237.1 | 2000ms | 1/408 |
| ✅ | `rest_countries` | 100.0% | 99.02% | 260.8 | 7269.1 | 2500ms | 4/408 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.75% | 232.9 | 2314.9 | 2000ms | 1/408 |
| ✅ | `coingecko_bitcoin` | 100.0% | 100.0% | 100.9 | 252.0 | 1500ms | 0/408 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `numbers_trivia` | 00:00 | 6402.8 | 62.5% |
| `nasa_apod` | 03:00 | 6314.9 | 91.67% |
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
