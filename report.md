# API Reliability Monitor — SLA Report

> Last updated: **2026-05-09 08:16 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **5/12** &nbsp;|&nbsp; Avg uptime: **79.6%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 62.45% | 3952.3 | 10206.7 | 1000ms | 261/695 |
| ❌ | `public_apis_list` | 0.0% | 99.57% | 127.2 | 4595.4 | 1500ms | 3/695 |
| ❌ | `nasa_apod` | 73.38% | 53.67% | 3271.6 | 10549.1 | 2000ms | 322/695 |
| ❌ | `ipapi_check` | 86.19% | 100.0% | 156.4 | 363.0 | 2500ms | 0/695 |
| ⚠️ | `rest_countries` | 98.56% | 97.99% | 364.9 | 10221.5 | 2500ms | 14/695 |
| ⚠️ | `open_meteo_weather` | 98.85% | 96.98% | 714.2 | 14877.1 | 2000ms | 21/695 |
| ⚠️ | `dog_ceo_random` | 99.57% | 93.96% | 681.3 | 10244.1 | 2500ms | 42/695 |
| ✅ | `catfact_random` | 99.57% | 99.14% | 271.0 | 10080.2 | 3000ms | 6/695 |
| ✅ | `coingecko_bitcoin` | 99.57% | 100.0% | 98.8 | 252.0 | 1500ms | 0/695 |
| ✅ | `useless_fact` | 99.71% | 99.42% | 600.2 | 10229.6 | 2500ms | 4/695 |
| ✅ | `agify_name` | 99.86% | 99.71% | 392.7 | 16112.2 | 2000ms | 2/695 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.71% | 235.4 | 3882.8 | 2000ms | 2/695 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `numbers_trivia` | 12:00 | 4824.9 | 46.43% |
| `nasa_apod` | 03:00 | 4729.0 | 77.78% |
| `numbers_trivia` | 03:00 | 4635.3 | 44.44% |
| `numbers_trivia` | 07:00 | 4535.2 | 43.48% |
| `numbers_trivia` | 05:00 | 4499.3 | 42.86% |
| `nasa_apod` | 17:00 | 4497.7 | 55.0% |
| `numbers_trivia` | 00:00 | 4460.1 | 42.86% |
| `numbers_trivia` | 16:00 | 4357.4 | 41.94% |
| `numbers_trivia` | 10:00 | 4318.4 | 41.38% |
| `numbers_trivia` | 01:00 | 4309.0 | 41.67% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
