# API Reliability Monitor — SLA Report

> Last updated: **2026-05-10 19:45 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **5/12** &nbsp;|&nbsp; Avg uptime: **79.6%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 63.76% | 3810.0 | 10206.7 | 1000ms | 262/723 |
| ❌ | `public_apis_list` | 0.0% | 99.59% | 126.2 | 4595.4 | 1500ms | 3/723 |
| ❌ | `nasa_apod` | 73.86% | 54.63% | 3222.9 | 10549.1 | 2000ms | 328/723 |
| ❌ | `ipapi_check` | 85.89% | 100.0% | 155.7 | 363.0 | 2500ms | 0/723 |
| ⚠️ | `rest_countries` | 98.62% | 98.06% | 358.8 | 10221.5 | 2500ms | 14/723 |
| ⚠️ | `open_meteo_weather` | 98.76% | 96.96% | 709.8 | 14877.1 | 2000ms | 22/723 |
| ⚠️ | `dog_ceo_random` | 99.59% | 94.19% | 669.5 | 10244.1 | 2500ms | 42/723 |
| ✅ | `catfact_random` | 99.59% | 99.03% | 275.0 | 10080.2 | 3000ms | 7/723 |
| ✅ | `coingecko_bitcoin` | 99.59% | 100.0% | 98.8 | 252.0 | 1500ms | 0/723 |
| ✅ | `useless_fact` | 99.72% | 99.45% | 601.2 | 10229.6 | 2500ms | 4/723 |
| ✅ | `agify_name` | 99.86% | 99.72% | 391.5 | 16112.2 | 2000ms | 2/723 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.72% | 235.3 | 3882.8 | 2000ms | 2/723 |

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
