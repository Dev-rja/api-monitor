# API Reliability Monitor — SLA Report

> Last updated: **2026-08-21 22:28 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **77.3%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 67.22% | 3408.1 | 10420.1 | 1000ms | 728/2221 |
| ❌ | `public_apis_list` | 0.0% | 99.55% | 136.9 | 5075.4 | 1500ms | 10/2221 |
| ❌ | `ipapi_check` | 53.53% | 99.95% | 145.1 | 4507.0 | 2500ms | 1/2221 |
| ❌ | `nasa_apod` | 79.51% | 56.55% | 2841.3 | 11152.5 | 2000ms | 965/2221 |
| ⚠️ | `dog_ceo_random` | 96.58% | 97.39% | 492.0 | 10244.1 | 2500ms | 58/2221 |
| ⚠️ | `open_meteo_weather` | 98.96% | 98.06% | 682.1 | 14877.1 | 2000ms | 43/2221 |
| ✅ | `rest_countries` | 99.32% | 99.05% | 272.4 | 10221.5 | 2500ms | 21/2221 |
| ✅ | `useless_fact` | 99.77% | 99.68% | 652.2 | 10229.6 | 2500ms | 7/2221 |
| ✅ | `catfact_random` | 99.77% | 99.41% | 263.1 | 10080.2 | 3000ms | 13/2221 |
| ✅ | `coingecko_bitcoin` | 99.82% | 99.91% | 96.3 | 4328.4 | 1500ms | 2/2221 |
| ✅ | `agify_name` | 99.91% | 99.73% | 395.3 | 16112.2 | 2000ms | 6/2221 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.91% | 187.3 | 3882.8 | 2000ms | 2/2221 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `numbers_trivia` | 03:00 | 5127.8 | 51.06% |
| `numbers_trivia` | 02:00 | 4413.0 | 42.11% |
| `numbers_trivia` | 10:00 | 4179.5 | 40.0% |
| `numbers_trivia` | 14:00 | 3852.3 | 37.37% |
| `numbers_trivia` | 00:00 | 3759.2 | 36.07% |
| `numbers_trivia` | 09:00 | 3742.1 | 36.17% |
| `numbers_trivia` | 05:00 | 3664.7 | 36.07% |
| `nasa_apod` | 05:00 | 3662.9 | 52.46% |
| `numbers_trivia` | 17:00 | 3655.0 | 36.52% |
| `nasa_apod` | 09:00 | 3548.8 | 49.46% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
