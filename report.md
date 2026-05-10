# API Reliability Monitor — SLA Report

> Last updated: **2026-05-10 16:36 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **5/12** &nbsp;|&nbsp; Avg uptime: **79.6%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 63.61% | 3825.0 | 10206.7 | 1000ms | 262/720 |
| ❌ | `public_apis_list` | 0.0% | 99.58% | 126.5 | 4595.4 | 1500ms | 3/720 |
| ❌ | `nasa_apod` | 73.75% | 54.58% | 3231.7 | 10549.1 | 2000ms | 327/720 |
| ❌ | `ipapi_check` | 85.83% | 100.0% | 155.8 | 363.0 | 2500ms | 0/720 |
| ⚠️ | `rest_countries` | 98.61% | 98.06% | 359.6 | 10221.5 | 2500ms | 14/720 |
| ⚠️ | `open_meteo_weather` | 98.75% | 96.94% | 710.5 | 14877.1 | 2000ms | 22/720 |
| ⚠️ | `dog_ceo_random` | 99.58% | 94.17% | 670.7 | 10244.1 | 2500ms | 42/720 |
| ✅ | `catfact_random` | 99.58% | 99.03% | 275.0 | 10080.2 | 3000ms | 7/720 |
| ✅ | `coingecko_bitcoin` | 99.58% | 100.0% | 98.6 | 252.0 | 1500ms | 0/720 |
| ✅ | `useless_fact` | 99.72% | 99.44% | 601.2 | 10229.6 | 2500ms | 4/720 |
| ✅ | `agify_name` | 99.86% | 99.72% | 391.9 | 16112.2 | 2000ms | 2/720 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.72% | 235.5 | 3882.8 | 2000ms | 2/720 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `nasa_apod` | 03:00 | 4729.0 | 77.78% |
| `numbers_trivia` | 03:00 | 4635.3 | 44.44% |
| `numbers_trivia` | 07:00 | 4535.2 | 43.48% |
| `numbers_trivia` | 12:00 | 4533.3 | 43.33% |
| `numbers_trivia` | 05:00 | 4499.3 | 42.86% |
| `numbers_trivia` | 00:00 | 4460.1 | 42.86% |
| `nasa_apod` | 17:00 | 4398.4 | 53.66% |
| `numbers_trivia` | 01:00 | 4309.0 | 41.67% |
| `numbers_trivia` | 10:00 | 4190.5 | 40.0% |
| `numbers_trivia` | 18:00 | 4136.2 | 39.39% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
