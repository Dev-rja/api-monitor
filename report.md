# API Reliability Monitor — SLA Report

> Last updated: **2026-05-11 01:26 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **5/12** &nbsp;|&nbsp; Avg uptime: **79.6%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 63.74% | 3791.4 | 10206.7 | 1000ms | 264/728 |
| ❌ | `public_apis_list` | 0.0% | 99.59% | 126.3 | 4595.4 | 1500ms | 3/728 |
| ❌ | `nasa_apod` | 74.04% | 54.67% | 3210.0 | 10549.1 | 2000ms | 330/728 |
| ❌ | `ipapi_check` | 85.85% | 100.0% | 155.8 | 363.0 | 2500ms | 0/728 |
| ⚠️ | `rest_countries` | 98.63% | 98.08% | 357.8 | 10221.5 | 2500ms | 14/728 |
| ⚠️ | `open_meteo_weather` | 98.76% | 96.98% | 710.0 | 14877.1 | 2000ms | 22/728 |
| ⚠️ | `dog_ceo_random` | 99.59% | 94.23% | 668.1 | 10244.1 | 2500ms | 42/728 |
| ✅ | `catfact_random` | 99.59% | 99.04% | 275.8 | 10080.2 | 3000ms | 7/728 |
| ✅ | `coingecko_bitcoin` | 99.59% | 100.0% | 98.7 | 252.0 | 1500ms | 0/728 |
| ✅ | `useless_fact` | 99.73% | 99.45% | 602.6 | 10229.6 | 2500ms | 4/728 |
| ✅ | `agify_name` | 99.86% | 99.73% | 391.6 | 16112.2 | 2000ms | 2/728 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.73% | 235.1 | 3882.8 | 2000ms | 2/728 |

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
| `numbers_trivia` | 10:00 | 4190.5 | 40.0% |
| `numbers_trivia` | 16:00 | 4111.4 | 39.39% |
| `nasa_apod` | 11:00 | 4102.8 | 46.51% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
