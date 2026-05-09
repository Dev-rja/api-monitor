# API Reliability Monitor — SLA Report

> Last updated: **2026-05-09 16:10 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **5/12** &nbsp;|&nbsp; Avg uptime: **79.6%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 62.82% | 3915.6 | 10206.7 | 1000ms | 261/702 |
| ❌ | `public_apis_list` | 0.0% | 99.57% | 126.8 | 4595.4 | 1500ms | 3/702 |
| ❌ | `nasa_apod` | 73.36% | 53.7% | 3274.2 | 10549.1 | 2000ms | 325/702 |
| ❌ | `ipapi_check` | 85.9% | 100.0% | 156.0 | 363.0 | 2500ms | 0/702 |
| ⚠️ | `rest_countries` | 98.58% | 98.01% | 363.6 | 10221.5 | 2500ms | 14/702 |
| ⚠️ | `open_meteo_weather` | 98.86% | 97.01% | 712.5 | 14877.1 | 2000ms | 21/702 |
| ⚠️ | `dog_ceo_random` | 99.57% | 94.02% | 679.7 | 10244.1 | 2500ms | 42/702 |
| ✅ | `catfact_random` | 99.57% | 99.15% | 270.8 | 10080.2 | 3000ms | 6/702 |
| ✅ | `coingecko_bitcoin` | 99.57% | 100.0% | 98.8 | 252.0 | 1500ms | 0/702 |
| ✅ | `useless_fact` | 99.72% | 99.43% | 600.8 | 10229.6 | 2500ms | 4/702 |
| ✅ | `agify_name` | 99.86% | 99.72% | 392.3 | 16112.2 | 2000ms | 2/702 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.72% | 236.0 | 3882.8 | 2000ms | 2/702 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `nasa_apod` | 03:00 | 4729.0 | 77.78% |
| `numbers_trivia` | 12:00 | 4674.2 | 44.83% |
| `numbers_trivia` | 03:00 | 4635.3 | 44.44% |
| `numbers_trivia` | 07:00 | 4535.2 | 43.48% |
| `numbers_trivia` | 05:00 | 4499.3 | 42.86% |
| `nasa_apod` | 17:00 | 4497.7 | 55.0% |
| `numbers_trivia` | 00:00 | 4460.1 | 42.86% |
| `numbers_trivia` | 01:00 | 4309.0 | 41.67% |
| `numbers_trivia` | 18:00 | 4263.5 | 40.63% |
| `numbers_trivia` | 16:00 | 4228.5 | 40.63% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
