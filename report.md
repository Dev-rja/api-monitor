# API Reliability Monitor — SLA Report

> Last updated: **2026-04-21 05:53 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **79.4%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 67.24% | 3507.9 | 10206.7 | 1000ms | 134/409 |
| ❌ | `public_apis_list` | 0.0% | 99.51% | 129.7 | 4088.9 | 1500ms | 2/409 |
| ❌ | `nasa_apod` | 62.35% | 38.39% | 4274.3 | 10538.0 | 2000ms | 252/409 |
| ❌ | `ipapi_check` | 94.13% | 100.0% | 159.4 | 353.0 | 2500ms | 0/409 |
| ⚠️ | `open_meteo_weather` | 98.04% | 96.82% | 750.5 | 14877.1 | 2000ms | 13/409 |
| ⚠️ | `dog_ceo_random` | 99.27% | 89.73% | 885.3 | 10244.1 | 2500ms | 42/409 |
| ✅ | `catfact_random` | 99.27% | 99.27% | 278.3 | 10080.2 | 3000ms | 3/409 |
| ✅ | `useless_fact` | 99.51% | 99.02% | 587.3 | 10229.6 | 2500ms | 4/409 |
| ✅ | `agify_name` | 100.0% | 99.76% | 373.5 | 3237.1 | 2000ms | 1/409 |
| ✅ | `rest_countries` | 100.0% | 99.02% | 260.7 | 7269.1 | 2500ms | 4/409 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.76% | 232.9 | 2314.9 | 2000ms | 1/409 |
| ✅ | `coingecko_bitcoin` | 100.0% | 100.0% | 101.0 | 252.0 | 1500ms | 0/409 |

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
| `nasa_apod` | 05:00 | 4497.7 | 73.33% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
