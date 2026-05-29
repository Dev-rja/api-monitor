# API Reliability Monitor — SLA Report

> Last updated: **2026-05-29 22:16 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **79.4%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 71.64% | 3023.9 | 10206.7 | 1000ms | 266/938 |
| ❌ | `public_apis_list` | 0.0% | 99.57% | 126.9 | 4595.4 | 1500ms | 4/938 |
| ❌ | `ipapi_check` | 77.83% | 100.0% | 153.3 | 431.8 | 2500ms | 0/938 |
| ❌ | `nasa_apod` | 79.0% | 59.17% | 2784.8 | 10549.1 | 2000ms | 383/938 |
| ⚠️ | `rest_countries` | 98.61% | 98.29% | 346.1 | 10221.5 | 2500ms | 16/938 |
| ⚠️ | `open_meteo_weather` | 98.93% | 96.8% | 711.3 | 14877.1 | 2000ms | 30/938 |
| ✅ | `dog_ceo_random` | 99.47% | 95.52% | 595.8 | 10244.1 | 2500ms | 42/938 |
| ✅ | `catfact_random` | 99.68% | 99.25% | 264.5 | 10080.2 | 3000ms | 7/938 |
| ✅ | `coingecko_bitcoin` | 99.68% | 100.0% | 97.5 | 253.3 | 1500ms | 0/938 |
| ✅ | `useless_fact` | 99.79% | 99.57% | 617.2 | 10229.6 | 2500ms | 4/938 |
| ✅ | `agify_name` | 99.89% | 99.68% | 383.7 | 16112.2 | 2000ms | 3/938 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.79% | 225.9 | 3882.8 | 2000ms | 2/938 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `nasa_apod` | 03:00 | 4611.9 | 78.95% |
| `numbers_trivia` | 03:00 | 4408.7 | 42.11% |
| `numbers_trivia` | 05:00 | 3808.4 | 36.0% |
| `nasa_apod` | 17:00 | 3728.7 | 49.09% |
| `numbers_trivia` | 07:00 | 3664.8 | 34.48% |
| `nasa_apod` | 11:00 | 3663.7 | 47.17% |
| `nasa_apod` | 05:00 | 3555.0 | 60.0% |
| `numbers_trivia` | 10:00 | 3544.0 | 33.33% |
| `numbers_trivia` | 12:00 | 3477.0 | 32.5% |
| `numbers_trivia` | 14:00 | 3456.7 | 34.04% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
