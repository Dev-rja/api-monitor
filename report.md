# API Reliability Monitor — SLA Report

> Last updated: **2026-05-09 14:07 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **5/12** &nbsp;|&nbsp; Avg uptime: **79.6%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 62.71% | 3926.3 | 10206.7 | 1000ms | 261/700 |
| ❌ | `public_apis_list` | 0.0% | 99.57% | 126.8 | 4595.4 | 1500ms | 3/700 |
| ❌ | `nasa_apod` | 73.29% | 53.57% | 3282.0 | 10549.1 | 2000ms | 325/700 |
| ❌ | `ipapi_check` | 86.14% | 100.0% | 156.0 | 363.0 | 2500ms | 0/700 |
| ⚠️ | `rest_countries` | 98.57% | 98.0% | 364.1 | 10221.5 | 2500ms | 14/700 |
| ⚠️ | `open_meteo_weather` | 98.86% | 97.0% | 713.3 | 14877.1 | 2000ms | 21/700 |
| ⚠️ | `dog_ceo_random` | 99.57% | 94.0% | 680.4 | 10244.1 | 2500ms | 42/700 |
| ✅ | `catfact_random` | 99.57% | 99.14% | 270.3 | 10080.2 | 3000ms | 6/700 |
| ✅ | `coingecko_bitcoin` | 99.57% | 100.0% | 98.8 | 252.0 | 1500ms | 0/700 |
| ✅ | `useless_fact` | 99.71% | 99.43% | 600.9 | 10229.6 | 2500ms | 4/700 |
| ✅ | `agify_name` | 99.86% | 99.71% | 392.5 | 16112.2 | 2000ms | 2/700 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.71% | 235.3 | 3882.8 | 2000ms | 2/700 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `nasa_apod` | 03:00 | 4729.0 | 77.78% |
| `numbers_trivia` | 12:00 | 4674.2 | 44.83% |
| `numbers_trivia` | 03:00 | 4635.3 | 44.44% |
| `numbers_trivia` | 07:00 | 4535.2 | 43.48% |
| `numbers_trivia` | 05:00 | 4499.3 | 42.86% |
| `nasa_apod` | 17:00 | 4497.7 | 55.0% |
| `numbers_trivia` | 00:00 | 4460.1 | 42.86% |
| `numbers_trivia` | 16:00 | 4357.4 | 41.94% |
| `numbers_trivia` | 01:00 | 4309.0 | 41.67% |
| `numbers_trivia` | 18:00 | 4263.5 | 40.63% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
