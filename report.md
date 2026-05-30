# API Reliability Monitor — SLA Report

> Last updated: **2026-05-30 12:54 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **79.4%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 71.85% | 3003.0 | 10206.7 | 1000ms | 266/945 |
| ❌ | `public_apis_list` | 0.0% | 99.58% | 126.5 | 4595.4 | 1500ms | 4/945 |
| ❌ | `ipapi_check` | 77.46% | 100.0% | 153.1 | 431.8 | 2500ms | 0/945 |
| ❌ | `nasa_apod` | 79.15% | 59.05% | 2776.3 | 10549.1 | 2000ms | 387/945 |
| ⚠️ | `rest_countries` | 98.41% | 98.1% | 365.9 | 10221.5 | 2500ms | 18/945 |
| ⚠️ | `open_meteo_weather` | 98.94% | 96.83% | 709.9 | 14877.1 | 2000ms | 30/945 |
| ✅ | `dog_ceo_random` | 99.47% | 95.56% | 593.9 | 10244.1 | 2500ms | 42/945 |
| ✅ | `catfact_random` | 99.68% | 99.26% | 264.3 | 10080.2 | 3000ms | 7/945 |
| ✅ | `coingecko_bitcoin` | 99.68% | 100.0% | 97.3 | 253.3 | 1500ms | 0/945 |
| ✅ | `useless_fact` | 99.79% | 99.58% | 617.6 | 10229.6 | 2500ms | 4/945 |
| ✅ | `agify_name` | 99.89% | 99.68% | 383.1 | 16112.2 | 2000ms | 3/945 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.79% | 225.7 | 3882.8 | 2000ms | 2/945 |

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
| `numbers_trivia` | 14:00 | 3456.7 | 34.04% |
| `numbers_trivia` | 10:00 | 3454.8 | 32.43% |
| `numbers_trivia` | 12:00 | 3394.7 | 31.71% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
