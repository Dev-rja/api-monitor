# API Reliability Monitor — SLA Report

> Last updated: **2026-05-27 21:46 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **79.4%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 71.12% | 3075.5 | 10206.7 | 1000ms | 266/921 |
| ❌ | `public_apis_list` | 0.0% | 99.57% | 127.1 | 4595.4 | 1500ms | 4/921 |
| ❌ | `ipapi_check` | 78.39% | 100.0% | 153.4 | 431.8 | 2500ms | 0/921 |
| ❌ | `nasa_apod` | 78.72% | 59.17% | 2804.0 | 10549.1 | 2000ms | 376/921 |
| ⚠️ | `rest_countries` | 98.81% | 98.37% | 337.5 | 10221.5 | 2500ms | 15/921 |
| ⚠️ | `open_meteo_weather` | 98.91% | 96.96% | 702.5 | 14877.1 | 2000ms | 28/921 |
| ✅ | `dog_ceo_random` | 99.46% | 95.44% | 601.0 | 10244.1 | 2500ms | 42/921 |
| ✅ | `catfact_random` | 99.67% | 99.24% | 263.9 | 10080.2 | 3000ms | 7/921 |
| ✅ | `coingecko_bitcoin` | 99.67% | 100.0% | 97.8 | 253.3 | 1500ms | 0/921 |
| ✅ | `useless_fact` | 99.78% | 99.57% | 616.6 | 10229.6 | 2500ms | 4/921 |
| ✅ | `agify_name` | 99.89% | 99.67% | 383.9 | 16112.2 | 2000ms | 3/921 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.78% | 226.9 | 3882.8 | 2000ms | 2/921 |

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
| `numbers_trivia` | 12:00 | 3562.7 | 33.33% |
| `nasa_apod` | 05:00 | 3555.0 | 60.0% |
| `numbers_trivia` | 10:00 | 3544.0 | 33.33% |
| `numbers_trivia` | 14:00 | 3524.3 | 34.78% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
