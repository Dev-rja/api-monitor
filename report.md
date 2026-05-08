# API Reliability Monitor — SLA Report

> Last updated: **2026-05-08 03:54 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **5/12** &nbsp;|&nbsp; Avg uptime: **79.6%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 61.5% | 4044.8 | 10206.7 | 1000ms | 261/678 |
| ❌ | `public_apis_list` | 0.0% | 99.56% | 128.2 | 4595.4 | 1500ms | 3/678 |
| ❌ | `nasa_apod` | 72.71% | 52.8% | 3333.2 | 10549.1 | 2000ms | 320/678 |
| ❌ | `ipapi_check` | 86.58% | 100.0% | 156.6 | 363.0 | 2500ms | 0/678 |
| ⚠️ | `rest_countries` | 98.67% | 98.38% | 336.6 | 10221.5 | 2500ms | 11/678 |
| ⚠️ | `open_meteo_weather` | 98.82% | 96.9% | 717.2 | 14877.1 | 2000ms | 21/678 |
| ⚠️ | `dog_ceo_random` | 99.56% | 93.81% | 688.5 | 10244.1 | 2500ms | 42/678 |
| ✅ | `catfact_random` | 99.56% | 99.41% | 262.2 | 10080.2 | 3000ms | 4/678 |
| ✅ | `coingecko_bitcoin` | 99.56% | 100.0% | 98.9 | 252.0 | 1500ms | 0/678 |
| ✅ | `useless_fact` | 99.71% | 99.41% | 596.8 | 10229.6 | 2500ms | 4/678 |
| ✅ | `agify_name` | 100.0% | 99.85% | 368.4 | 3237.1 | 2000ms | 1/678 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.71% | 235.4 | 3882.8 | 2000ms | 2/678 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `numbers_trivia` | 12:00 | 5000.0 | 48.15% |
| `numbers_trivia` | 03:00 | 4902.0 | 47.06% |
| `nasa_apod` | 03:00 | 4821.6 | 76.47% |
| `numbers_trivia` | 00:00 | 4778.2 | 46.15% |
| `numbers_trivia` | 07:00 | 4734.0 | 45.45% |
| `numbers_trivia` | 05:00 | 4708.1 | 45.0% |
| `nasa_apod` | 17:00 | 4607.0 | 56.41% |
| `numbers_trivia` | 10:00 | 4461.5 | 42.86% |
| `numbers_trivia` | 18:00 | 4390.9 | 41.94% |
| `numbers_trivia` | 14:00 | 4365.7 | 41.67% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
