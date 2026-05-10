# API Reliability Monitor — SLA Report

> Last updated: **2026-05-10 23:29 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **5/12** &nbsp;|&nbsp; Avg uptime: **79.6%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 63.69% | 3795.5 | 10206.7 | 1000ms | 264/727 |
| ❌ | `public_apis_list` | 0.0% | 99.59% | 126.3 | 4595.4 | 1500ms | 3/727 |
| ❌ | `nasa_apod` | 74.0% | 54.75% | 3210.9 | 10549.1 | 2000ms | 329/727 |
| ❌ | `ipapi_check` | 85.83% | 100.0% | 155.7 | 363.0 | 2500ms | 0/727 |
| ⚠️ | `rest_countries` | 98.62% | 98.07% | 357.9 | 10221.5 | 2500ms | 14/727 |
| ⚠️ | `open_meteo_weather` | 98.76% | 96.97% | 710.1 | 14877.1 | 2000ms | 22/727 |
| ⚠️ | `dog_ceo_random` | 99.59% | 94.22% | 668.4 | 10244.1 | 2500ms | 42/727 |
| ✅ | `catfact_random` | 99.59% | 99.04% | 275.7 | 10080.2 | 3000ms | 7/727 |
| ✅ | `coingecko_bitcoin` | 99.59% | 100.0% | 98.6 | 252.0 | 1500ms | 0/727 |
| ✅ | `useless_fact` | 99.72% | 99.45% | 602.3 | 10229.6 | 2500ms | 4/727 |
| ✅ | `agify_name` | 99.86% | 99.72% | 391.5 | 16112.2 | 2000ms | 2/727 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.72% | 235.1 | 3882.8 | 2000ms | 2/727 |

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
| `nasa_apod` | 17:00 | 4350.3 | 54.76% |
| `numbers_trivia` | 01:00 | 4309.0 | 41.67% |
| `numbers_trivia` | 10:00 | 4190.5 | 40.0% |
| `numbers_trivia` | 16:00 | 4111.4 | 39.39% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
