# API Reliability Monitor — SLA Report

> Last updated: **2026-05-30 20:39 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **79.3%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 72.03% | 2985.9 | 10206.7 | 1000ms | 266/951 |
| ❌ | `public_apis_list` | 0.0% | 99.58% | 126.3 | 4595.4 | 1500ms | 4/951 |
| ❌ | `ipapi_check` | 77.08% | 100.0% | 152.7 | 431.8 | 2500ms | 0/951 |
| ❌ | `nasa_apod` | 78.97% | 58.99% | 2783.7 | 10549.1 | 2000ms | 390/951 |
| ⚠️ | `rest_countries` | 98.42% | 98.11% | 365.3 | 10221.5 | 2500ms | 18/951 |
| ⚠️ | `open_meteo_weather` | 98.95% | 96.85% | 709.2 | 14877.1 | 2000ms | 30/951 |
| ✅ | `dog_ceo_random` | 99.47% | 95.58% | 592.3 | 10244.1 | 2500ms | 42/951 |
| ✅ | `catfact_random` | 99.68% | 99.26% | 263.8 | 10080.2 | 3000ms | 7/951 |
| ✅ | `coingecko_bitcoin` | 99.68% | 100.0% | 97.1 | 253.3 | 1500ms | 0/951 |
| ✅ | `useless_fact` | 99.79% | 99.58% | 617.7 | 10229.6 | 2500ms | 4/951 |
| ✅ | `agify_name` | 99.89% | 99.68% | 383.2 | 16112.2 | 2000ms | 3/951 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.79% | 225.1 | 3882.8 | 2000ms | 2/951 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `nasa_apod` | 03:00 | 4611.9 | 78.95% |
| `numbers_trivia` | 03:00 | 4408.7 | 42.11% |
| `nasa_apod` | 17:00 | 3728.7 | 49.09% |
| `numbers_trivia` | 05:00 | 3674.1 | 34.62% |
| `numbers_trivia` | 07:00 | 3664.8 | 34.48% |
| `nasa_apod` | 11:00 | 3605.9 | 46.3% |
| `nasa_apod` | 05:00 | 3511.6 | 61.54% |
| `numbers_trivia` | 10:00 | 3454.8 | 32.43% |
| `numbers_trivia` | 12:00 | 3394.7 | 31.71% |
| `numbers_trivia` | 14:00 | 3388.1 | 33.33% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
