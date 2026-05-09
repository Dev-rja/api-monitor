# API Reliability Monitor — SLA Report

> Last updated: **2026-05-09 06:24 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **5/12** &nbsp;|&nbsp; Avg uptime: **79.6%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 62.39% | 3957.5 | 10206.7 | 1000ms | 261/694 |
| ❌ | `public_apis_list` | 0.0% | 99.57% | 127.3 | 4595.4 | 1500ms | 3/694 |
| ❌ | `nasa_apod` | 73.34% | 53.6% | 3276.0 | 10549.1 | 2000ms | 322/694 |
| ❌ | `ipapi_check` | 86.17% | 100.0% | 156.5 | 363.0 | 2500ms | 0/694 |
| ⚠️ | `rest_countries` | 98.56% | 97.98% | 365.0 | 10221.5 | 2500ms | 14/694 |
| ⚠️ | `open_meteo_weather` | 98.85% | 96.97% | 714.3 | 14877.1 | 2000ms | 21/694 |
| ⚠️ | `dog_ceo_random` | 99.57% | 93.95% | 681.7 | 10244.1 | 2500ms | 42/694 |
| ✅ | `catfact_random` | 99.57% | 99.14% | 271.2 | 10080.2 | 3000ms | 6/694 |
| ✅ | `coingecko_bitcoin` | 99.57% | 100.0% | 98.9 | 252.0 | 1500ms | 0/694 |
| ✅ | `useless_fact` | 99.71% | 99.42% | 598.8 | 10229.6 | 2500ms | 4/694 |
| ✅ | `agify_name` | 99.86% | 99.71% | 392.5 | 16112.2 | 2000ms | 2/694 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.71% | 235.4 | 3882.8 | 2000ms | 2/694 |

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
