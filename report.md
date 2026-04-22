# API Reliability Monitor — SLA Report

> Last updated: **2026-04-22 16:44 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **79.3%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 63.36% | 3886.6 | 10206.7 | 1000ms | 159/434 |
| ❌ | `public_apis_list` | 0.0% | 99.54% | 129.6 | 4088.9 | 1500ms | 2/434 |
| ❌ | `nasa_apod` | 61.29% | 37.1% | 4398.5 | 10549.1 | 2000ms | 273/434 |
| ❌ | `ipapi_check` | 93.55% | 100.0% | 158.3 | 353.0 | 2500ms | 0/434 |
| ⚠️ | `open_meteo_weather` | 98.16% | 96.77% | 748.4 | 14877.1 | 2000ms | 14/434 |
| ⚠️ | `dog_ceo_random` | 99.31% | 90.32% | 856.7 | 10244.1 | 2500ms | 42/434 |
| ✅ | `catfact_random` | 99.31% | 99.31% | 272.6 | 10080.2 | 3000ms | 3/434 |
| ✅ | `useless_fact` | 99.54% | 99.08% | 585.2 | 10229.6 | 2500ms | 4/434 |
| ✅ | `agify_name` | 100.0% | 99.77% | 374.0 | 3237.1 | 2000ms | 1/434 |
| ✅ | `rest_countries` | 100.0% | 99.08% | 257.9 | 7269.1 | 2500ms | 4/434 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.77% | 231.0 | 2314.9 | 2000ms | 1/434 |
| ✅ | `coingecko_bitcoin` | 100.0% | 100.0% | 100.3 | 252.0 | 1500ms | 0/434 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `numbers_trivia` | 00:00 | 6402.8 | 62.5% |
| `nasa_apod` | 03:00 | 6314.9 | 91.67% |
| `nasa_apod` | 17:00 | 5959.2 | 72.0% |
| `nasa_apod` | 18:00 | 5870.5 | 83.33% |
| `nasa_apod` | 00:00 | 5195.1 | 75.0% |
| `nasa_apod` | 11:00 | 4979.2 | 61.54% |
| `nasa_apod` | 01:00 | 4971.7 | 60.0% |
| `numbers_trivia` | 12:00 | 4944.8 | 47.37% |
| `nasa_apod` | 19:00 | 4739.6 | 62.5% |
| `nasa_apod` | 21:00 | 4705.1 | 54.17% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
