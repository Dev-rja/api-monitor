# API Reliability Monitor — SLA Report

> Last updated: **2026-05-29 17:57 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **79.4%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 71.58% | 3030.0 | 10206.7 | 1000ms | 266/936 |
| ❌ | `public_apis_list` | 0.0% | 99.57% | 127.0 | 4595.4 | 1500ms | 4/936 |
| ❌ | `ipapi_check` | 77.88% | 100.0% | 153.3 | 431.8 | 2500ms | 0/936 |
| ❌ | `nasa_apod` | 78.95% | 59.19% | 2787.3 | 10549.1 | 2000ms | 382/936 |
| ⚠️ | `rest_countries` | 98.82% | 98.4% | 335.9 | 10221.5 | 2500ms | 15/936 |
| ⚠️ | `open_meteo_weather` | 98.93% | 96.79% | 712.0 | 14877.1 | 2000ms | 30/936 |
| ✅ | `dog_ceo_random` | 99.47% | 95.51% | 596.4 | 10244.1 | 2500ms | 42/936 |
| ✅ | `catfact_random` | 99.68% | 99.25% | 264.9 | 10080.2 | 3000ms | 7/936 |
| ✅ | `coingecko_bitcoin` | 99.68% | 100.0% | 97.5 | 253.3 | 1500ms | 0/936 |
| ✅ | `useless_fact` | 99.79% | 99.57% | 617.4 | 10229.6 | 2500ms | 4/936 |
| ✅ | `agify_name` | 99.89% | 99.68% | 384.0 | 16112.2 | 2000ms | 3/936 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.79% | 226.2 | 3882.8 | 2000ms | 2/936 |

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
