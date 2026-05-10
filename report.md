# API Reliability Monitor — SLA Report

> Last updated: **2026-05-10 20:33 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **5/12** &nbsp;|&nbsp; Avg uptime: **79.6%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 63.67% | 3807.2 | 10206.7 | 1000ms | 263/724 |
| ❌ | `public_apis_list` | 0.0% | 99.59% | 126.1 | 4595.4 | 1500ms | 3/724 |
| ❌ | `nasa_apod` | 73.9% | 54.7% | 3218.8 | 10549.1 | 2000ms | 328/724 |
| ❌ | `ipapi_check` | 85.91% | 100.0% | 155.6 | 363.0 | 2500ms | 0/724 |
| ⚠️ | `rest_countries` | 98.62% | 98.07% | 358.7 | 10221.5 | 2500ms | 14/724 |
| ⚠️ | `open_meteo_weather` | 98.76% | 96.96% | 709.8 | 14877.1 | 2000ms | 22/724 |
| ⚠️ | `dog_ceo_random` | 99.59% | 94.2% | 669.2 | 10244.1 | 2500ms | 42/724 |
| ✅ | `catfact_random` | 99.59% | 99.03% | 275.0 | 10080.2 | 3000ms | 7/724 |
| ✅ | `coingecko_bitcoin` | 99.59% | 100.0% | 98.7 | 252.0 | 1500ms | 0/724 |
| ✅ | `useless_fact` | 99.72% | 99.45% | 601.9 | 10229.6 | 2500ms | 4/724 |
| ✅ | `agify_name` | 99.86% | 99.72% | 391.7 | 16112.2 | 2000ms | 2/724 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.72% | 235.2 | 3882.8 | 2000ms | 2/724 |

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
