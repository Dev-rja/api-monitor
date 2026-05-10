# API Reliability Monitor — SLA Report

> Last updated: **2026-05-10 08:31 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **5/12** &nbsp;|&nbsp; Avg uptime: **79.6%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 63.39% | 3858.0 | 10206.7 | 1000ms | 261/713 |
| ❌ | `public_apis_list` | 0.0% | 99.58% | 127.1 | 4595.4 | 1500ms | 3/713 |
| ❌ | `nasa_apod` | 73.77% | 54.42% | 3231.4 | 10549.1 | 2000ms | 325/713 |
| ❌ | `ipapi_check` | 85.83% | 100.0% | 155.8 | 363.0 | 2500ms | 0/713 |
| ⚠️ | `rest_countries` | 98.6% | 98.04% | 360.8 | 10221.5 | 2500ms | 14/713 |
| ⚠️ | `open_meteo_weather` | 98.74% | 96.91% | 711.4 | 14877.1 | 2000ms | 22/713 |
| ⚠️ | `dog_ceo_random` | 99.58% | 94.11% | 674.3 | 10244.1 | 2500ms | 42/713 |
| ✅ | `catfact_random` | 99.58% | 99.02% | 275.4 | 10080.2 | 3000ms | 7/713 |
| ✅ | `coingecko_bitcoin` | 99.58% | 100.0% | 98.7 | 252.0 | 1500ms | 0/713 |
| ✅ | `useless_fact` | 99.72% | 99.44% | 600.2 | 10229.6 | 2500ms | 4/713 |
| ✅ | `agify_name` | 99.86% | 99.72% | 391.4 | 16112.2 | 2000ms | 2/713 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.72% | 236.0 | 3882.8 | 2000ms | 2/713 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `nasa_apod` | 03:00 | 4729.0 | 77.78% |
| `numbers_trivia` | 12:00 | 4674.2 | 44.83% |
| `numbers_trivia` | 03:00 | 4635.3 | 44.44% |
| `numbers_trivia` | 07:00 | 4535.2 | 43.48% |
| `numbers_trivia` | 05:00 | 4499.3 | 42.86% |
| `numbers_trivia` | 00:00 | 4460.1 | 42.86% |
| `nasa_apod` | 17:00 | 4398.4 | 53.66% |
| `numbers_trivia` | 01:00 | 4309.0 | 41.67% |
| `numbers_trivia` | 16:00 | 4228.5 | 40.63% |
| `numbers_trivia` | 10:00 | 4190.5 | 40.0% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
