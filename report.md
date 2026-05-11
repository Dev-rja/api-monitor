# API Reliability Monitor — SLA Report

> Last updated: **2026-05-11 05:37 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **5/12** &nbsp;|&nbsp; Avg uptime: **79.6%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 63.79% | 3786.3 | 10206.7 | 1000ms | 264/729 |
| ❌ | `public_apis_list` | 0.0% | 99.59% | 126.3 | 4595.4 | 1500ms | 3/729 |
| ❌ | `nasa_apod` | 74.07% | 54.73% | 3206.3 | 10549.1 | 2000ms | 330/729 |
| ❌ | `ipapi_check` | 85.87% | 100.0% | 155.8 | 363.0 | 2500ms | 0/729 |
| ⚠️ | `rest_countries` | 98.63% | 98.08% | 357.4 | 10221.5 | 2500ms | 14/729 |
| ⚠️ | `open_meteo_weather` | 98.77% | 96.98% | 709.7 | 14877.1 | 2000ms | 22/729 |
| ⚠️ | `dog_ceo_random` | 99.59% | 94.24% | 667.7 | 10244.1 | 2500ms | 42/729 |
| ✅ | `catfact_random` | 99.59% | 99.04% | 275.5 | 10080.2 | 3000ms | 7/729 |
| ✅ | `coingecko_bitcoin` | 99.59% | 100.0% | 98.7 | 252.0 | 1500ms | 0/729 |
| ✅ | `useless_fact` | 99.73% | 99.45% | 602.5 | 10229.6 | 2500ms | 4/729 |
| ✅ | `agify_name` | 99.86% | 99.73% | 391.4 | 16112.2 | 2000ms | 2/729 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.73% | 235.0 | 3882.8 | 2000ms | 2/729 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `nasa_apod` | 03:00 | 4729.0 | 77.78% |
| `numbers_trivia` | 03:00 | 4635.3 | 44.44% |
| `numbers_trivia` | 07:00 | 4535.2 | 43.48% |
| `numbers_trivia` | 12:00 | 4533.3 | 43.33% |
| `numbers_trivia` | 00:00 | 4460.1 | 42.86% |
| `nasa_apod` | 17:00 | 4350.3 | 54.76% |
| `numbers_trivia` | 05:00 | 4297.7 | 40.91% |
| `numbers_trivia` | 10:00 | 4190.5 | 40.0% |
| `numbers_trivia` | 16:00 | 4111.4 | 39.39% |
| `nasa_apod` | 11:00 | 4102.8 | 46.51% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
