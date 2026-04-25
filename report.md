# API Reliability Monitor — SLA Report

> Last updated: **2026-04-25 06:11 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **5/12** &nbsp;|&nbsp; Avg uptime: **79.1%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 57.77% | 4433.3 | 10206.7 | 1000ms | 201/476 |
| ❌ | `public_apis_list` | 0.0% | 99.58% | 128.1 | 4088.9 | 1500ms | 2/476 |
| ❌ | `nasa_apod` | 61.97% | 37.18% | 4395.5 | 10549.1 | 2000ms | 299/476 |
| ❌ | `ipapi_check` | 92.44% | 100.0% | 158.1 | 353.0 | 2500ms | 0/476 |
| ⚠️ | `open_meteo_weather` | 98.32% | 97.06% | 730.9 | 14877.1 | 2000ms | 14/476 |
| ⚠️ | `rest_countries` | 98.53% | 98.11% | 355.0 | 10221.5 | 2500ms | 9/476 |
| ⚠️ | `dog_ceo_random` | 99.37% | 91.18% | 816.5 | 10244.1 | 2500ms | 42/476 |
| ✅ | `catfact_random` | 99.37% | 99.37% | 264.7 | 10080.2 | 3000ms | 3/476 |
| ✅ | `useless_fact` | 99.58% | 99.16% | 584.2 | 10229.6 | 2500ms | 4/476 |
| ✅ | `agify_name` | 100.0% | 99.79% | 373.2 | 3237.1 | 2000ms | 1/476 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.79% | 235.3 | 2314.9 | 2000ms | 1/476 |
| ✅ | `coingecko_bitcoin` | 100.0% | 100.0% | 100.7 | 252.0 | 1500ms | 0/476 |

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
