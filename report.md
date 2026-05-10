# API Reliability Monitor — SLA Report

> Last updated: **2026-05-10 15:39 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **5/12** &nbsp;|&nbsp; Avg uptime: **79.6%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 63.56% | 3829.8 | 10206.7 | 1000ms | 262/719 |
| ❌ | `public_apis_list` | 0.0% | 99.58% | 126.7 | 4595.4 | 1500ms | 3/719 |
| ❌ | `nasa_apod` | 73.71% | 54.52% | 3235.5 | 10549.1 | 2000ms | 327/719 |
| ❌ | `ipapi_check` | 85.81% | 100.0% | 155.9 | 363.0 | 2500ms | 0/719 |
| ⚠️ | `rest_countries` | 98.61% | 98.05% | 359.6 | 10221.5 | 2500ms | 14/719 |
| ⚠️ | `open_meteo_weather` | 98.75% | 96.94% | 710.6 | 14877.1 | 2000ms | 22/719 |
| ⚠️ | `dog_ceo_random` | 99.58% | 94.16% | 671.0 | 10244.1 | 2500ms | 42/719 |
| ✅ | `catfact_random` | 99.58% | 99.03% | 275.2 | 10080.2 | 3000ms | 7/719 |
| ✅ | `coingecko_bitcoin` | 99.58% | 100.0% | 98.7 | 252.0 | 1500ms | 0/719 |
| ✅ | `useless_fact` | 99.72% | 99.44% | 601.0 | 10229.6 | 2500ms | 4/719 |
| ✅ | `agify_name` | 99.86% | 99.72% | 391.5 | 16112.2 | 2000ms | 2/719 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.72% | 235.6 | 3882.8 | 2000ms | 2/719 |

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
| `numbers_trivia` | 16:00 | 4228.5 | 40.63% |
| `numbers_trivia` | 10:00 | 4190.5 | 40.0% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
