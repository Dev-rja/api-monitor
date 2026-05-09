# API Reliability Monitor — SLA Report

> Last updated: **2026-05-09 10:42 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **5/12** &nbsp;|&nbsp; Avg uptime: **79.6%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 62.55% | 3941.9 | 10206.7 | 1000ms | 261/697 |
| ❌ | `public_apis_list` | 0.0% | 99.57% | 127.2 | 4595.4 | 1500ms | 3/697 |
| ❌ | `nasa_apod` | 73.31% | 53.52% | 3280.5 | 10549.1 | 2000ms | 324/697 |
| ❌ | `ipapi_check` | 86.23% | 100.0% | 156.3 | 363.0 | 2500ms | 0/697 |
| ⚠️ | `rest_countries` | 98.57% | 97.99% | 364.6 | 10221.5 | 2500ms | 14/697 |
| ⚠️ | `open_meteo_weather` | 98.85% | 96.99% | 713.8 | 14877.1 | 2000ms | 21/697 |
| ⚠️ | `dog_ceo_random` | 99.57% | 93.97% | 680.5 | 10244.1 | 2500ms | 42/697 |
| ✅ | `catfact_random` | 99.57% | 99.14% | 271.0 | 10080.2 | 3000ms | 6/697 |
| ✅ | `coingecko_bitcoin` | 99.57% | 100.0% | 98.8 | 252.0 | 1500ms | 0/697 |
| ✅ | `useless_fact` | 99.71% | 99.43% | 600.6 | 10229.6 | 2500ms | 4/697 |
| ✅ | `agify_name` | 99.86% | 99.71% | 392.5 | 16112.2 | 2000ms | 2/697 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.71% | 235.7 | 3882.8 | 2000ms | 2/697 |

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
| `numbers_trivia` | 01:00 | 4309.0 | 41.67% |
| `numbers_trivia` | 18:00 | 4263.5 | 40.63% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
