# API Reliability Monitor — SLA Report

> Last updated: **2026-08-22 00:02 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **77.3%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 67.28% | 3402.2 | 10420.1 | 1000ms | 728/2225 |
| ❌ | `public_apis_list` | 0.0% | 99.55% | 136.7 | 5075.4 | 1500ms | 10/2225 |
| ❌ | `ipapi_check` | 53.44% | 99.96% | 145.0 | 4507.0 | 2500ms | 1/2225 |
| ❌ | `nasa_apod` | 79.51% | 56.58% | 2838.0 | 11152.5 | 2000ms | 966/2225 |
| ⚠️ | `dog_ceo_random` | 96.58% | 97.39% | 491.6 | 10244.1 | 2500ms | 58/2225 |
| ⚠️ | `open_meteo_weather` | 98.97% | 98.07% | 682.0 | 14877.1 | 2000ms | 43/2225 |
| ✅ | `rest_countries` | 99.33% | 99.06% | 272.2 | 10221.5 | 2500ms | 21/2225 |
| ✅ | `useless_fact` | 99.78% | 99.69% | 652.2 | 10229.6 | 2500ms | 7/2225 |
| ✅ | `catfact_random` | 99.78% | 99.42% | 262.9 | 10080.2 | 3000ms | 13/2225 |
| ✅ | `coingecko_bitcoin` | 99.82% | 99.91% | 96.4 | 4328.4 | 1500ms | 2/2225 |
| ✅ | `agify_name` | 99.91% | 99.73% | 395.2 | 16112.2 | 2000ms | 6/2225 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.91% | 187.2 | 3882.8 | 2000ms | 2/2225 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `numbers_trivia` | 03:00 | 5127.8 | 51.06% |
| `numbers_trivia` | 02:00 | 4413.0 | 42.11% |
| `numbers_trivia` | 10:00 | 4179.5 | 40.0% |
| `numbers_trivia` | 14:00 | 3852.3 | 37.37% |
| `numbers_trivia` | 09:00 | 3742.1 | 36.17% |
| `numbers_trivia` | 00:00 | 3701.8 | 35.48% |
| `numbers_trivia` | 05:00 | 3664.7 | 36.07% |
| `nasa_apod` | 05:00 | 3662.9 | 52.46% |
| `numbers_trivia` | 17:00 | 3655.0 | 36.52% |
| `nasa_apod` | 09:00 | 3548.8 | 49.46% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
