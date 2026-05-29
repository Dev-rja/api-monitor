# API Reliability Monitor — SLA Report

> Last updated: **2026-05-29 08:29 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **79.4%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 71.49% | 3038.9 | 10206.7 | 1000ms | 266/933 |
| ❌ | `public_apis_list` | 0.0% | 99.57% | 127.2 | 4595.4 | 1500ms | 4/933 |
| ❌ | `ipapi_check` | 77.92% | 100.0% | 153.3 | 431.8 | 2500ms | 0/933 |
| ❌ | `nasa_apod` | 78.99% | 59.27% | 2782.2 | 10549.1 | 2000ms | 380/933 |
| ⚠️ | `rest_countries` | 98.82% | 98.39% | 336.3 | 10221.5 | 2500ms | 15/933 |
| ⚠️ | `open_meteo_weather` | 98.93% | 96.78% | 712.5 | 14877.1 | 2000ms | 30/933 |
| ✅ | `dog_ceo_random` | 99.46% | 95.5% | 597.7 | 10244.1 | 2500ms | 42/933 |
| ✅ | `catfact_random` | 99.68% | 99.25% | 265.4 | 10080.2 | 3000ms | 7/933 |
| ✅ | `coingecko_bitcoin` | 99.68% | 100.0% | 97.6 | 253.3 | 1500ms | 0/933 |
| ✅ | `useless_fact` | 99.79% | 99.57% | 617.0 | 10229.6 | 2500ms | 4/933 |
| ✅ | `agify_name` | 99.89% | 99.68% | 384.2 | 16112.2 | 2000ms | 3/933 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.79% | 226.3 | 3882.8 | 2000ms | 2/933 |

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
