# API Reliability Monitor — SLA Report

> Last updated: **2026-04-18 21:28 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **79.5%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 75.97% | 2653.8 | 10206.7 | 1000ms | 87/362 |
| ❌ | `public_apis_list` | 0.0% | 99.72% | 123.0 | 3806.8 | 1500ms | 1/362 |
| ❌ | `nasa_apod` | 64.64% | 41.16% | 4017.4 | 10538.0 | 2000ms | 213/362 |
| ❌ | `ipapi_check` | 93.37% | 100.0% | 159.9 | 353.0 | 2500ms | 0/362 |
| ⚠️ | `open_meteo_weather` | 97.79% | 96.69% | 769.3 | 14877.1 | 2000ms | 12/362 |
| ⚠️ | `dog_ceo_random` | 99.17% | 88.4% | 951.2 | 10244.1 | 2500ms | 42/362 |
| ✅ | `useless_fact` | 99.45% | 99.17% | 581.8 | 10229.6 | 2500ms | 3/362 |
| ✅ | `catfact_random` | 99.45% | 99.72% | 247.9 | 10070.5 | 3000ms | 1/362 |
| ✅ | `agify_name` | 100.0% | 99.72% | 376.7 | 3237.1 | 2000ms | 1/362 |
| ✅ | `rest_countries` | 100.0% | 98.9% | 267.1 | 7269.1 | 2500ms | 4/362 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.72% | 236.9 | 2314.9 | 2000ms | 1/362 |
| ✅ | `coingecko_bitcoin` | 100.0% | 100.0% | 101.0 | 252.0 | 1500ms | 0/362 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `nasa_apod` | 03:00 | 5840.5 | 88.89% |
| `nasa_apod` | 17:00 | 5121.2 | 66.67% |
| `nasa_apod` | 18:00 | 4979.5 | 80.0% |
| `nasa_apod` | 20:00 | 4677.6 | 64.0% |
| `nasa_apod` | 11:00 | 4496.8 | 59.09% |
| `nasa_apod` | 21:00 | 4275.9 | 47.62% |
| `numbers_trivia` | 00:00 | 4205.1 | 40.0% |
| `nasa_apod` | 08:00 | 4055.4 | 57.14% |
| `nasa_apod` | 14:00 | 4031.8 | 57.14% |
| `nasa_apod` | 12:00 | 3997.0 | 60.0% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
