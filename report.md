# API Reliability Monitor — SLA Report

> Last updated: **2026-05-10 18:38 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **5/12** &nbsp;|&nbsp; Avg uptime: **79.6%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 63.71% | 3815.1 | 10206.7 | 1000ms | 262/722 |
| ❌ | `public_apis_list` | 0.0% | 99.58% | 126.4 | 4595.4 | 1500ms | 3/722 |
| ❌ | `nasa_apod` | 73.82% | 54.57% | 3226.7 | 10549.1 | 2000ms | 328/722 |
| ❌ | `ipapi_check` | 85.87% | 100.0% | 155.7 | 363.0 | 2500ms | 0/722 |
| ⚠️ | `rest_countries` | 98.61% | 98.06% | 359.2 | 10221.5 | 2500ms | 14/722 |
| ⚠️ | `open_meteo_weather` | 98.75% | 96.95% | 710.1 | 14877.1 | 2000ms | 22/722 |
| ⚠️ | `dog_ceo_random` | 99.58% | 94.18% | 670.0 | 10244.1 | 2500ms | 42/722 |
| ✅ | `catfact_random` | 99.58% | 99.03% | 275.3 | 10080.2 | 3000ms | 7/722 |
| ✅ | `coingecko_bitcoin` | 99.58% | 100.0% | 98.7 | 252.0 | 1500ms | 0/722 |
| ✅ | `useless_fact` | 99.72% | 99.45% | 601.2 | 10229.6 | 2500ms | 4/722 |
| ✅ | `agify_name` | 99.86% | 99.72% | 391.8 | 16112.2 | 2000ms | 2/722 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.72% | 235.5 | 3882.8 | 2000ms | 2/722 |

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
