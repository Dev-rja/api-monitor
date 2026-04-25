# API Reliability Monitor — SLA Report

> Last updated: **2026-04-25 07:46 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **5/12** &nbsp;|&nbsp; Avg uptime: **79.1%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 57.65% | 4445.1 | 10206.7 | 1000ms | 202/477 |
| ❌ | `public_apis_list` | 0.0% | 99.58% | 128.0 | 4088.9 | 1500ms | 2/477 |
| ❌ | `nasa_apod` | 62.05% | 37.11% | 4391.9 | 10549.1 | 2000ms | 300/477 |
| ❌ | `ipapi_check` | 92.45% | 100.0% | 158.3 | 353.0 | 2500ms | 0/477 |
| ⚠️ | `open_meteo_weather` | 98.32% | 97.06% | 730.7 | 14877.1 | 2000ms | 14/477 |
| ⚠️ | `rest_countries` | 98.53% | 98.11% | 354.8 | 10221.5 | 2500ms | 9/477 |
| ⚠️ | `dog_ceo_random` | 99.37% | 91.19% | 815.6 | 10244.1 | 2500ms | 42/477 |
| ✅ | `catfact_random` | 99.37% | 99.37% | 264.9 | 10080.2 | 3000ms | 3/477 |
| ✅ | `useless_fact` | 99.58% | 99.16% | 584.0 | 10229.6 | 2500ms | 4/477 |
| ✅ | `agify_name` | 100.0% | 99.79% | 373.3 | 3237.1 | 2000ms | 1/477 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.79% | 235.3 | 2314.9 | 2000ms | 1/477 |
| ✅ | `coingecko_bitcoin` | 100.0% | 100.0% | 100.8 | 252.0 | 1500ms | 0/477 |

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
| `numbers_trivia` | 07:00 | 5211.4 | 50.0% |
| `numbers_trivia` | 12:00 | 5201.9 | 50.0% |
| `numbers_trivia` | 03:00 | 5200.2 | 50.0% |
| `nasa_apod` | 00:00 | 5195.1 | 75.0% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
