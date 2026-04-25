# API Reliability Monitor — SLA Report

> Last updated: **2026-04-25 04:39 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **5/12** &nbsp;|&nbsp; Avg uptime: **79.1%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 57.89% | 4421.5 | 10206.7 | 1000ms | 200/475 |
| ❌ | `public_apis_list` | 0.0% | 99.58% | 128.3 | 4088.9 | 1500ms | 2/475 |
| ❌ | `nasa_apod` | 61.89% | 37.05% | 4404.3 | 10549.1 | 2000ms | 299/475 |
| ❌ | `ipapi_check` | 92.42% | 100.0% | 158.3 | 353.0 | 2500ms | 0/475 |
| ⚠️ | `open_meteo_weather` | 98.32% | 97.05% | 731.1 | 14877.1 | 2000ms | 14/475 |
| ⚠️ | `rest_countries` | 98.53% | 98.11% | 355.2 | 10221.5 | 2500ms | 9/475 |
| ⚠️ | `dog_ceo_random` | 99.37% | 91.16% | 817.1 | 10244.1 | 2500ms | 42/475 |
| ✅ | `catfact_random` | 99.37% | 99.37% | 265.0 | 10080.2 | 3000ms | 3/475 |
| ✅ | `useless_fact` | 99.58% | 99.16% | 584.4 | 10229.6 | 2500ms | 4/475 |
| ✅ | `agify_name` | 100.0% | 99.79% | 372.9 | 3237.1 | 2000ms | 1/475 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.79% | 235.3 | 2314.9 | 2000ms | 1/475 |
| ✅ | `coingecko_bitcoin` | 100.0% | 100.0% | 100.8 | 252.0 | 1500ms | 0/475 |

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
