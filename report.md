# API Reliability Monitor — SLA Report

> Last updated: **2026-05-28 22:50 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **79.4%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 71.4% | 3047.8 | 10206.7 | 1000ms | 266/930 |
| ❌ | `public_apis_list` | 0.0% | 99.57% | 127.2 | 4595.4 | 1500ms | 4/930 |
| ❌ | `ipapi_check` | 78.17% | 100.0% | 153.4 | 431.8 | 2500ms | 0/930 |
| ❌ | `nasa_apod` | 78.92% | 59.25% | 2788.0 | 10549.1 | 2000ms | 379/930 |
| ⚠️ | `rest_countries` | 98.82% | 98.39% | 336.6 | 10221.5 | 2500ms | 15/930 |
| ⚠️ | `open_meteo_weather` | 98.92% | 96.77% | 711.9 | 14877.1 | 2000ms | 30/930 |
| ✅ | `dog_ceo_random` | 99.46% | 95.48% | 598.6 | 10244.1 | 2500ms | 42/930 |
| ✅ | `catfact_random` | 99.68% | 99.25% | 265.8 | 10080.2 | 3000ms | 7/930 |
| ✅ | `coingecko_bitcoin` | 99.68% | 100.0% | 97.6 | 253.3 | 1500ms | 0/930 |
| ✅ | `useless_fact` | 99.78% | 99.57% | 617.1 | 10229.6 | 2500ms | 4/930 |
| ✅ | `agify_name` | 99.89% | 99.68% | 383.9 | 16112.2 | 2000ms | 3/930 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.78% | 226.5 | 3882.8 | 2000ms | 2/930 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `nasa_apod` | 03:00 | 4611.9 | 78.95% |
| `numbers_trivia` | 03:00 | 4408.7 | 42.11% |
| `numbers_trivia` | 05:00 | 3808.4 | 36.0% |
| `nasa_apod` | 11:00 | 3686.9 | 46.15% |
| `numbers_trivia` | 07:00 | 3664.8 | 34.48% |
| `nasa_apod` | 17:00 | 3605.4 | 48.15% |
| `nasa_apod` | 05:00 | 3555.0 | 60.0% |
| `numbers_trivia` | 10:00 | 3544.0 | 33.33% |
| `numbers_trivia` | 14:00 | 3524.3 | 34.78% |
| `numbers_trivia` | 12:00 | 3477.0 | 32.5% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
