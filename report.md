# API Reliability Monitor — SLA Report

> Last updated: **2026-08-22 18:48 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **77.2%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 67.77% | 3353.3 | 10420.1 | 1000ms | 728/2259 |
| ❌ | `public_apis_list` | 0.0% | 99.51% | 137.5 | 5075.4 | 1500ms | 11/2259 |
| ❌ | `ipapi_check` | 52.68% | 99.96% | 145.0 | 4507.0 | 2500ms | 1/2259 |
| ❌ | `nasa_apod` | 79.59% | 56.88% | 2815.9 | 11152.5 | 2000ms | 974/2259 |
| ⚠️ | `dog_ceo_random` | 96.64% | 97.43% | 489.4 | 10244.1 | 2500ms | 58/2259 |
| ⚠️ | `open_meteo_weather` | 98.98% | 98.1% | 680.5 | 14877.1 | 2000ms | 43/2259 |
| ✅ | `rest_countries` | 99.34% | 99.07% | 271.1 | 10221.5 | 2500ms | 21/2259 |
| ✅ | `useless_fact` | 99.78% | 99.69% | 652.7 | 10229.6 | 2500ms | 7/2259 |
| ✅ | `catfact_random` | 99.78% | 99.42% | 262.3 | 10080.2 | 3000ms | 13/2259 |
| ✅ | `coingecko_bitcoin` | 99.82% | 99.91% | 97.0 | 4328.4 | 1500ms | 2/2259 |
| ✅ | `agify_name` | 99.91% | 99.6% | 398.7 | 16112.2 | 2000ms | 9/2259 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.91% | 186.7 | 3882.8 | 2000ms | 2/2259 |

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
| `numbers_trivia` | 17:00 | 3595.1 | 35.9% |
| `nasa_apod` | 05:00 | 3561.5 | 50.79% |
| `numbers_trivia` | 05:00 | 3550.7 | 34.92% |
| `nasa_apod` | 09:00 | 3483.5 | 48.42% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
