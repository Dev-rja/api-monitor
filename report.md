# API Reliability Monitor — SLA Report

> Last updated: **2026-08-21 06:37 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **7/12** &nbsp;|&nbsp; Avg uptime: **77.3%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 66.82% | 3447.8 | 10420.1 | 1000ms | 728/2194 |
| ❌ | `public_apis_list` | 0.0% | 99.54% | 136.9 | 5075.4 | 1500ms | 10/2194 |
| ❌ | `ipapi_check` | 54.19% | 99.95% | 145.2 | 4507.0 | 2500ms | 1/2194 |
| ❌ | `nasa_apod` | 79.26% | 56.06% | 2871.0 | 11152.5 | 2000ms | 964/2194 |
| ⚠️ | `dog_ceo_random` | 96.54% | 97.36% | 493.8 | 10244.1 | 2500ms | 58/2194 |
| ✅ | `open_meteo_weather` | 99.0% | 98.04% | 682.9 | 14877.1 | 2000ms | 43/2194 |
| ✅ | `rest_countries` | 99.32% | 99.04% | 272.9 | 10221.5 | 2500ms | 21/2194 |
| ✅ | `useless_fact` | 99.77% | 99.68% | 652.0 | 10229.6 | 2500ms | 7/2194 |
| ✅ | `catfact_random` | 99.77% | 99.41% | 263.6 | 10080.2 | 3000ms | 13/2194 |
| ✅ | `coingecko_bitcoin` | 99.82% | 99.91% | 96.4 | 4328.4 | 1500ms | 2/2194 |
| ✅ | `agify_name` | 99.91% | 99.73% | 394.6 | 16112.2 | 2000ms | 6/2194 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.91% | 187.9 | 3882.8 | 2000ms | 2/2194 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `numbers_trivia` | 03:00 | 5127.8 | 51.06% |
| `numbers_trivia` | 02:00 | 4413.0 | 42.11% |
| `numbers_trivia` | 10:00 | 4275.8 | 40.96% |
| `numbers_trivia` | 14:00 | 3926.9 | 38.14% |
| `numbers_trivia` | 09:00 | 3780.7 | 36.56% |
| `numbers_trivia` | 00:00 | 3759.2 | 36.07% |
| `numbers_trivia` | 17:00 | 3716.8 | 37.17% |
| `numbers_trivia` | 05:00 | 3664.7 | 36.07% |
| `nasa_apod` | 05:00 | 3662.9 | 52.46% |
| `nasa_apod` | 09:00 | 3582.8 | 50.0% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
