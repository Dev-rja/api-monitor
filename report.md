# API Reliability Monitor — SLA Report

> Last updated: **2026-05-08 17:21 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **5/12** &nbsp;|&nbsp; Avg uptime: **79.6%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 61.95% | 4000.5 | 10206.7 | 1000ms | 261/686 |
| ❌ | `public_apis_list` | 0.0% | 99.56% | 127.9 | 4595.4 | 1500ms | 3/686 |
| ❌ | `nasa_apod` | 73.03% | 53.21% | 3305.6 | 10549.1 | 2000ms | 321/686 |
| ❌ | `ipapi_check` | 86.01% | 100.0% | 156.4 | 363.0 | 2500ms | 0/686 |
| ⚠️ | `rest_countries` | 98.54% | 97.96% | 366.1 | 10221.5 | 2500ms | 14/686 |
| ⚠️ | `open_meteo_weather` | 98.83% | 96.94% | 715.3 | 14877.1 | 2000ms | 21/686 |
| ⚠️ | `dog_ceo_random` | 99.56% | 93.88% | 685.1 | 10244.1 | 2500ms | 42/686 |
| ✅ | `catfact_random` | 99.56% | 99.27% | 267.0 | 10080.2 | 3000ms | 5/686 |
| ✅ | `coingecko_bitcoin` | 99.56% | 100.0% | 98.8 | 252.0 | 1500ms | 0/686 |
| ✅ | `useless_fact` | 99.71% | 99.42% | 597.8 | 10229.6 | 2500ms | 4/686 |
| ✅ | `agify_name` | 100.0% | 99.85% | 368.9 | 3237.1 | 2000ms | 1/686 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.71% | 235.9 | 3882.8 | 2000ms | 2/686 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `numbers_trivia` | 03:00 | 4902.0 | 47.06% |
| `numbers_trivia` | 12:00 | 4824.9 | 46.43% |
| `nasa_apod` | 03:00 | 4821.6 | 76.47% |
| `numbers_trivia` | 00:00 | 4778.2 | 46.15% |
| `numbers_trivia` | 07:00 | 4535.2 | 43.48% |
| `numbers_trivia` | 05:00 | 4499.3 | 42.86% |
| `nasa_apod` | 17:00 | 4497.7 | 55.0% |
| `numbers_trivia` | 18:00 | 4390.9 | 41.94% |
| `numbers_trivia` | 16:00 | 4357.4 | 41.94% |
| `numbers_trivia` | 10:00 | 4318.4 | 41.38% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
