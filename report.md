# API Reliability Monitor — SLA Report

> Last updated: **2026-05-27 23:04 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **79.4%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 71.15% | 3072.6 | 10206.7 | 1000ms | 266/922 |
| ❌ | `public_apis_list` | 0.0% | 99.57% | 127.0 | 4595.4 | 1500ms | 4/922 |
| ❌ | `ipapi_check` | 78.42% | 100.0% | 153.5 | 431.8 | 2500ms | 0/922 |
| ❌ | `nasa_apod` | 78.74% | 59.11% | 2803.6 | 10549.1 | 2000ms | 377/922 |
| ⚠️ | `rest_countries` | 98.81% | 98.37% | 337.5 | 10221.5 | 2500ms | 15/922 |
| ⚠️ | `open_meteo_weather` | 98.92% | 96.96% | 702.4 | 14877.1 | 2000ms | 28/922 |
| ✅ | `dog_ceo_random` | 99.46% | 95.44% | 600.9 | 10244.1 | 2500ms | 42/922 |
| ✅ | `catfact_random` | 99.67% | 99.24% | 263.9 | 10080.2 | 3000ms | 7/922 |
| ✅ | `coingecko_bitcoin` | 99.67% | 100.0% | 97.8 | 253.3 | 1500ms | 0/922 |
| ✅ | `useless_fact` | 99.78% | 99.57% | 616.7 | 10229.6 | 2500ms | 4/922 |
| ✅ | `agify_name` | 99.89% | 99.67% | 384.0 | 16112.2 | 2000ms | 3/922 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.78% | 226.8 | 3882.8 | 2000ms | 2/922 |

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
