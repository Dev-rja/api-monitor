# API Reliability Monitor — SLA Report

> Last updated: **2026-05-08 15:55 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **5/12** &nbsp;|&nbsp; Avg uptime: **79.6%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 61.9% | 4005.8 | 10206.7 | 1000ms | 261/685 |
| ❌ | `public_apis_list` | 0.0% | 99.56% | 128.0 | 4595.4 | 1500ms | 3/685 |
| ❌ | `nasa_apod` | 72.99% | 53.14% | 3310.1 | 10549.1 | 2000ms | 321/685 |
| ❌ | `ipapi_check` | 85.99% | 100.0% | 156.5 | 363.0 | 2500ms | 0/685 |
| ⚠️ | `rest_countries` | 98.54% | 97.96% | 366.3 | 10221.5 | 2500ms | 14/685 |
| ⚠️ | `open_meteo_weather` | 98.83% | 96.93% | 715.3 | 14877.1 | 2000ms | 21/685 |
| ⚠️ | `dog_ceo_random` | 99.56% | 93.87% | 685.4 | 10244.1 | 2500ms | 42/685 |
| ✅ | `catfact_random` | 99.56% | 99.27% | 267.2 | 10080.2 | 3000ms | 5/685 |
| ✅ | `coingecko_bitcoin` | 99.56% | 100.0% | 98.8 | 252.0 | 1500ms | 0/685 |
| ✅ | `useless_fact` | 99.71% | 99.42% | 597.6 | 10229.6 | 2500ms | 4/685 |
| ✅ | `agify_name` | 100.0% | 99.85% | 368.5 | 3237.1 | 2000ms | 1/685 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.71% | 236.0 | 3882.8 | 2000ms | 2/685 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `numbers_trivia` | 03:00 | 4902.0 | 47.06% |
| `numbers_trivia` | 12:00 | 4824.9 | 46.43% |
| `nasa_apod` | 03:00 | 4821.6 | 76.47% |
| `numbers_trivia` | 00:00 | 4778.2 | 46.15% |
| `nasa_apod` | 17:00 | 4607.0 | 56.41% |
| `numbers_trivia` | 07:00 | 4535.2 | 43.48% |
| `numbers_trivia` | 05:00 | 4499.3 | 42.86% |
| `numbers_trivia` | 18:00 | 4390.9 | 41.94% |
| `numbers_trivia` | 16:00 | 4357.4 | 41.94% |
| `numbers_trivia` | 10:00 | 4318.4 | 41.38% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
