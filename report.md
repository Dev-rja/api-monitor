# API Reliability Monitor — SLA Report

> Last updated: **2026-05-08 05:59 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **5/12** &nbsp;|&nbsp; Avg uptime: **79.6%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 61.56% | 4039.3 | 10206.7 | 1000ms | 261/679 |
| ❌ | `public_apis_list` | 0.0% | 99.56% | 128.1 | 4595.4 | 1500ms | 3/679 |
| ❌ | `nasa_apod` | 72.75% | 52.87% | 3328.8 | 10549.1 | 2000ms | 320/679 |
| ❌ | `ipapi_check` | 86.45% | 100.0% | 156.6 | 363.0 | 2500ms | 0/679 |
| ⚠️ | `rest_countries` | 98.67% | 98.38% | 336.5 | 10221.5 | 2500ms | 11/679 |
| ⚠️ | `open_meteo_weather` | 98.82% | 96.91% | 717.1 | 14877.1 | 2000ms | 21/679 |
| ⚠️ | `dog_ceo_random` | 99.56% | 93.81% | 688.0 | 10244.1 | 2500ms | 42/679 |
| ✅ | `catfact_random` | 99.56% | 99.41% | 262.6 | 10080.2 | 3000ms | 4/679 |
| ✅ | `coingecko_bitcoin` | 99.56% | 100.0% | 99.0 | 252.0 | 1500ms | 0/679 |
| ✅ | `useless_fact` | 99.71% | 99.41% | 597.1 | 10229.6 | 2500ms | 4/679 |
| ✅ | `agify_name` | 100.0% | 99.85% | 368.5 | 3237.1 | 2000ms | 1/679 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.71% | 235.3 | 3882.8 | 2000ms | 2/679 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `numbers_trivia` | 12:00 | 5000.0 | 48.15% |
| `numbers_trivia` | 03:00 | 4902.0 | 47.06% |
| `nasa_apod` | 03:00 | 4821.6 | 76.47% |
| `numbers_trivia` | 00:00 | 4778.2 | 46.15% |
| `numbers_trivia` | 07:00 | 4734.0 | 45.45% |
| `nasa_apod` | 17:00 | 4607.0 | 56.41% |
| `numbers_trivia` | 05:00 | 4499.3 | 42.86% |
| `numbers_trivia` | 10:00 | 4461.5 | 42.86% |
| `numbers_trivia` | 18:00 | 4390.9 | 41.94% |
| `numbers_trivia` | 14:00 | 4365.7 | 41.67% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
