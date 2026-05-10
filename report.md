# API Reliability Monitor — SLA Report

> Last updated: **2026-05-10 21:30 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **5/12** &nbsp;|&nbsp; Avg uptime: **79.6%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 63.72% | 3803.1 | 10206.7 | 1000ms | 263/725 |
| ❌ | `public_apis_list` | 0.0% | 99.59% | 126.2 | 4595.4 | 1500ms | 3/725 |
| ❌ | `nasa_apod` | 73.93% | 54.62% | 3218.1 | 10549.1 | 2000ms | 329/725 |
| ❌ | `ipapi_check` | 85.93% | 100.0% | 155.6 | 363.0 | 2500ms | 0/725 |
| ⚠️ | `rest_countries` | 98.62% | 98.07% | 358.3 | 10221.5 | 2500ms | 14/725 |
| ⚠️ | `open_meteo_weather` | 98.76% | 96.97% | 710.6 | 14877.1 | 2000ms | 22/725 |
| ⚠️ | `dog_ceo_random` | 99.59% | 94.21% | 668.8 | 10244.1 | 2500ms | 42/725 |
| ✅ | `catfact_random` | 99.59% | 99.03% | 275.6 | 10080.2 | 3000ms | 7/725 |
| ✅ | `coingecko_bitcoin` | 99.59% | 100.0% | 98.6 | 252.0 | 1500ms | 0/725 |
| ✅ | `useless_fact` | 99.72% | 99.45% | 601.9 | 10229.6 | 2500ms | 4/725 |
| ✅ | `agify_name` | 99.86% | 99.72% | 391.6 | 16112.2 | 2000ms | 2/725 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.72% | 235.2 | 3882.8 | 2000ms | 2/725 |

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
