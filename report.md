# API Reliability Monitor — SLA Report

> Last updated: **2026-04-25 15:11 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **5/12** &nbsp;|&nbsp; Avg uptime: **79.1%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 56.7% | 4537.9 | 10206.7 | 1000ms | 210/485 |
| ❌ | `public_apis_list` | 0.0% | 99.59% | 127.2 | 4088.9 | 1500ms | 2/485 |
| ❌ | `nasa_apod` | 62.68% | 37.94% | 4331.9 | 10549.1 | 2000ms | 301/485 |
| ❌ | `ipapi_check` | 91.55% | 100.0% | 157.9 | 353.0 | 2500ms | 0/485 |
| ⚠️ | `open_meteo_weather` | 98.35% | 97.11% | 728.5 | 14877.1 | 2000ms | 14/485 |
| ⚠️ | `rest_countries` | 98.56% | 98.14% | 352.8 | 10221.5 | 2500ms | 9/485 |
| ⚠️ | `dog_ceo_random` | 99.38% | 91.34% | 808.2 | 10244.1 | 2500ms | 42/485 |
| ✅ | `catfact_random` | 99.38% | 99.38% | 263.7 | 10080.2 | 3000ms | 3/485 |
| ✅ | `useless_fact` | 99.59% | 99.18% | 582.9 | 10229.6 | 2500ms | 4/485 |
| ✅ | `agify_name` | 100.0% | 99.79% | 372.8 | 3237.1 | 2000ms | 1/485 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.79% | 234.8 | 2314.9 | 2000ms | 1/485 |
| ✅ | `coingecko_bitcoin` | 100.0% | 100.0% | 100.6 | 252.0 | 1500ms | 0/485 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `numbers_trivia` | 00:00 | 6402.8 | 62.5% |
| `nasa_apod` | 01:00 | 5838.7 | 66.67% |
| `nasa_apod` | 17:00 | 5806.4 | 71.43% |
| `nasa_apod` | 18:00 | 5779.3 | 85.71% |
| `nasa_apod` | 03:00 | 5600.9 | 85.71% |
| `numbers_trivia` | 12:00 | 5436.1 | 52.38% |
| `numbers_trivia` | 07:00 | 5211.4 | 50.0% |
| `numbers_trivia` | 03:00 | 5200.2 | 50.0% |
| `nasa_apod` | 00:00 | 5195.1 | 75.0% |
| `nasa_apod` | 11:00 | 5182.1 | 62.07% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
