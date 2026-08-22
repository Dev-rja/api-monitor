# API Reliability Monitor — SLA Report

> Last updated: **2026-08-22 15:18 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **77.2%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 67.66% | 3364.6 | 10420.1 | 1000ms | 728/2251 |
| ❌ | `public_apis_list` | 0.0% | 99.51% | 137.4 | 5075.4 | 1500ms | 11/2251 |
| ❌ | `ipapi_check` | 52.87% | 99.96% | 144.9 | 4507.0 | 2500ms | 1/2251 |
| ❌ | `nasa_apod` | 79.56% | 56.82% | 2819.1 | 11152.5 | 2000ms | 972/2251 |
| ⚠️ | `dog_ceo_random` | 96.62% | 97.42% | 489.8 | 10244.1 | 2500ms | 58/2251 |
| ⚠️ | `open_meteo_weather` | 98.98% | 98.09% | 680.7 | 14877.1 | 2000ms | 43/2251 |
| ✅ | `rest_countries` | 99.33% | 99.07% | 271.2 | 10221.5 | 2500ms | 21/2251 |
| ✅ | `useless_fact` | 99.78% | 99.69% | 652.4 | 10229.6 | 2500ms | 7/2251 |
| ✅ | `catfact_random` | 99.78% | 99.42% | 262.4 | 10080.2 | 3000ms | 13/2251 |
| ✅ | `coingecko_bitcoin` | 99.82% | 99.91% | 96.9 | 4328.4 | 1500ms | 2/2251 |
| ✅ | `agify_name` | 99.91% | 99.64% | 397.4 | 16112.2 | 2000ms | 8/2251 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.91% | 186.8 | 3882.8 | 2000ms | 2/2251 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `numbers_trivia` | 03:00 | 5024.8 | 50.0% |
| `numbers_trivia` | 02:00 | 4199.6 | 40.0% |
| `numbers_trivia` | 10:00 | 4043.1 | 38.64% |
| `numbers_trivia` | 14:00 | 3780.0 | 36.63% |
| `numbers_trivia` | 00:00 | 3701.8 | 35.48% |
| `numbers_trivia` | 09:00 | 3667.1 | 35.42% |
| `numbers_trivia` | 17:00 | 3655.0 | 36.52% |
| `nasa_apod` | 05:00 | 3561.5 | 50.79% |
| `numbers_trivia` | 05:00 | 3550.7 | 34.92% |
| `nasa_apod` | 09:00 | 3483.5 | 48.42% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
