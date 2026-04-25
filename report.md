# API Reliability Monitor — SLA Report

> Last updated: **2026-04-25 01:56 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **5/12** &nbsp;|&nbsp; Avg uptime: **79.1%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 58.02% | 4409.6 | 10206.7 | 1000ms | 199/474 |
| ❌ | `public_apis_list` | 0.0% | 99.58% | 128.4 | 4088.9 | 1500ms | 2/474 |
| ❌ | `nasa_apod` | 61.81% | 36.92% | 4412.7 | 10549.1 | 2000ms | 299/474 |
| ❌ | `ipapi_check` | 92.41% | 100.0% | 158.2 | 353.0 | 2500ms | 0/474 |
| ⚠️ | `open_meteo_weather` | 98.31% | 97.05% | 731.4 | 14877.1 | 2000ms | 14/474 |
| ⚠️ | `rest_countries` | 98.52% | 98.1% | 355.4 | 10221.5 | 2500ms | 9/474 |
| ⚠️ | `dog_ceo_random` | 99.37% | 91.14% | 817.8 | 10244.1 | 2500ms | 42/474 |
| ✅ | `catfact_random` | 99.37% | 99.37% | 264.7 | 10080.2 | 3000ms | 3/474 |
| ✅ | `useless_fact` | 99.58% | 99.16% | 584.2 | 10229.6 | 2500ms | 4/474 |
| ✅ | `agify_name` | 100.0% | 99.79% | 372.9 | 3237.1 | 2000ms | 1/474 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.79% | 235.4 | 2314.9 | 2000ms | 1/474 |
| ✅ | `coingecko_bitcoin` | 100.0% | 100.0% | 100.7 | 252.0 | 1500ms | 0/474 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `numbers_trivia` | 00:00 | 6402.8 | 62.5% |
| `nasa_apod` | 01:00 | 5838.7 | 66.67% |
| `nasa_apod` | 17:00 | 5806.4 | 71.43% |
| `nasa_apod` | 18:00 | 5779.3 | 85.71% |
| `nasa_apod` | 03:00 | 5600.9 | 85.71% |
| `nasa_apod` | 11:00 | 5359.7 | 64.29% |
| `numbers_trivia` | 12:00 | 5201.9 | 50.0% |
| `numbers_trivia` | 03:00 | 5200.2 | 50.0% |
| `nasa_apod` | 00:00 | 5195.1 | 75.0% |
| `numbers_trivia` | 01:00 | 5154.4 | 50.0% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
