# API Reliability Monitor — SLA Report

> Last updated: **2026-04-21 09:14 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **79.4%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 66.91% | 3539.8 | 10206.7 | 1000ms | 136/411 |
| ❌ | `public_apis_list` | 0.0% | 99.51% | 130.0 | 4088.9 | 1500ms | 2/411 |
| ❌ | `nasa_apod` | 62.29% | 38.2% | 4285.1 | 10538.0 | 2000ms | 254/411 |
| ❌ | `ipapi_check` | 94.16% | 100.0% | 159.3 | 353.0 | 2500ms | 0/411 |
| ⚠️ | `open_meteo_weather` | 98.05% | 96.84% | 749.2 | 14877.1 | 2000ms | 13/411 |
| ⚠️ | `dog_ceo_random` | 99.27% | 89.78% | 882.8 | 10244.1 | 2500ms | 42/411 |
| ✅ | `catfact_random` | 99.27% | 99.27% | 277.4 | 10080.2 | 3000ms | 3/411 |
| ✅ | `useless_fact` | 99.51% | 99.03% | 586.9 | 10229.6 | 2500ms | 4/411 |
| ✅ | `agify_name` | 100.0% | 99.76% | 373.2 | 3237.1 | 2000ms | 1/411 |
| ✅ | `rest_countries` | 100.0% | 99.03% | 260.2 | 7269.1 | 2500ms | 4/411 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.76% | 233.1 | 2314.9 | 2000ms | 1/411 |
| ✅ | `coingecko_bitcoin` | 100.0% | 100.0% | 100.9 | 252.0 | 1500ms | 0/411 |

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
| `numbers_trivia` | 07:00 | 4515.1 | 42.86% |
| `nasa_apod` | 14:00 | 4500.5 | 62.5% |
| `nasa_apod` | 19:00 | 4499.4 | 60.87% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
