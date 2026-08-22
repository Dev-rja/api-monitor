# API Reliability Monitor — SLA Report

> Last updated: **2026-08-22 09:10 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **77.2%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 67.47% | 3383.2 | 10420.1 | 1000ms | 728/2238 |
| ❌ | `public_apis_list` | 0.0% | 99.51% | 137.5 | 5075.4 | 1500ms | 11/2238 |
| ❌ | `ipapi_check` | 53.13% | 99.96% | 145.0 | 4507.0 | 2500ms | 1/2238 |
| ❌ | `nasa_apod` | 79.49% | 56.75% | 2825.8 | 11152.5 | 2000ms | 968/2238 |
| ⚠️ | `dog_ceo_random` | 96.6% | 97.41% | 490.8 | 10244.1 | 2500ms | 58/2238 |
| ⚠️ | `open_meteo_weather` | 98.97% | 98.08% | 681.2 | 14877.1 | 2000ms | 43/2238 |
| ✅ | `rest_countries` | 99.33% | 99.06% | 271.7 | 10221.5 | 2500ms | 21/2238 |
| ✅ | `useless_fact` | 99.78% | 99.69% | 652.2 | 10229.6 | 2500ms | 7/2238 |
| ✅ | `catfact_random` | 99.78% | 99.42% | 262.6 | 10080.2 | 3000ms | 13/2238 |
| ✅ | `coingecko_bitcoin` | 99.82% | 99.91% | 96.4 | 4328.4 | 1500ms | 2/2238 |
| ✅ | `agify_name` | 99.91% | 99.69% | 396.1 | 16112.2 | 2000ms | 7/2238 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.91% | 186.9 | 3882.8 | 2000ms | 2/2238 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `numbers_trivia` | 03:00 | 5024.8 | 50.0% |
| `numbers_trivia` | 02:00 | 4199.6 | 40.0% |
| `numbers_trivia` | 10:00 | 4179.5 | 40.0% |
| `numbers_trivia` | 14:00 | 3852.3 | 37.37% |
| `numbers_trivia` | 09:00 | 3703.8 | 35.79% |
| `numbers_trivia` | 00:00 | 3701.8 | 35.48% |
| `numbers_trivia` | 17:00 | 3655.0 | 36.52% |
| `nasa_apod` | 05:00 | 3561.5 | 50.79% |
| `numbers_trivia` | 05:00 | 3550.7 | 34.92% |
| `nasa_apod` | 09:00 | 3515.3 | 48.94% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
