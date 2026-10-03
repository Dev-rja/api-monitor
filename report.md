# API Reliability Monitor — SLA Report

> Last updated: **2026-10-03 21:10 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **7/12** &nbsp;|&nbsp; Avg uptime: **76.7%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 72.39% | 2895.4 | 10420.1 | 1000ms | 728/2637 |
| ❌ | `public_apis_list` | 0.0% | 99.43% | 142.8 | 5075.4 | 1500ms | 15/2637 |
| ❌ | `ipapi_check` | 45.81% | 99.96% | 144.9 | 4507.0 | 2500ms | 1/2637 |
| ❌ | `nasa_apod` | 80.81% | 59.84% | 2642.9 | 11152.5 | 2000ms | 1059/2637 |
| ⚠️ | `dog_ceo_random` | 97.12% | 97.76% | 477.2 | 10244.1 | 2500ms | 59/2637 |
| ✅ | `open_meteo_weather` | 99.05% | 98.29% | 668.1 | 14877.1 | 2000ms | 45/2637 |
| ✅ | `useless_fact` | 99.13% | 99.51% | 669.1 | 10229.6 | 2500ms | 13/2637 |
| ✅ | `rest_countries` | 99.43% | 99.13% | 271.8 | 10221.5 | 2500ms | 23/2637 |
| ✅ | `coingecko_bitcoin` | 99.7% | 99.92% | 96.9 | 4328.4 | 1500ms | 2/2637 |
| ✅ | `catfact_random` | 99.81% | 99.51% | 262.3 | 10080.2 | 3000ms | 13/2637 |
| ✅ | `agify_name` | 99.92% | 99.54% | 402.4 | 16112.2 | 2000ms | 12/2637 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.89% | 181.8 | 3882.8 | 2000ms | 3/2637 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `numbers_trivia` | 03:00 | 4483.7 | 44.44% |
| `numbers_trivia` | 10:00 | 3511.2 | 33.33% |
| `numbers_trivia` | 02:00 | 3385.1 | 32.0% |
| `nasa_apod` | 03:00 | 3208.5 | 46.3% |
| `numbers_trivia` | 14:00 | 3204.1 | 30.83% |
| `nasa_apod` | 11:00 | 3115.1 | 43.38% |
| `numbers_trivia` | 09:00 | 3113.5 | 29.82% |
| `nasa_apod` | 17:00 | 3111.5 | 38.69% |
| `nasa_apod` | 09:00 | 3089.5 | 44.25% |
| `numbers_trivia` | 17:00 | 3071.9 | 30.43% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
