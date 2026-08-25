# API Reliability Monitor — SLA Report

> Last updated: **2026-08-25 11:05 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **77.1%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 69.18% | 3213.7 | 10420.1 | 1000ms | 728/2362 |
| ❌ | `public_apis_list` | 0.0% | 99.45% | 139.3 | 5075.4 | 1500ms | 13/2362 |
| ❌ | `ipapi_check` | 50.68% | 99.96% | 144.3 | 4507.0 | 2500ms | 1/2362 |
| ❌ | `nasa_apod` | 80.14% | 57.92% | 2757.0 | 11152.5 | 2000ms | 994/2362 |
| ⚠️ | `dog_ceo_random` | 96.78% | 97.5% | 486.1 | 10244.1 | 2500ms | 59/2362 |
| ⚠️ | `open_meteo_weather` | 98.98% | 98.18% | 676.1 | 14877.1 | 2000ms | 43/2362 |
| ✅ | `rest_countries` | 99.36% | 99.11% | 267.4 | 10221.5 | 2500ms | 21/2362 |
| ✅ | `useless_fact` | 99.79% | 99.7% | 654.6 | 10229.6 | 2500ms | 7/2362 |
| ✅ | `catfact_random` | 99.79% | 99.45% | 261.8 | 10080.2 | 3000ms | 13/2362 |
| ✅ | `coingecko_bitcoin` | 99.83% | 99.92% | 96.4 | 4328.4 | 1500ms | 2/2362 |
| ✅ | `agify_name` | 99.92% | 99.53% | 402.2 | 16112.2 | 2000ms | 11/2362 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.92% | 185.0 | 3882.8 | 2000ms | 2/2362 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `numbers_trivia` | 03:00 | 4832.5 | 48.0% |
| `numbers_trivia` | 10:00 | 3795.8 | 36.17% |
| `numbers_trivia` | 02:00 | 3664.7 | 34.78% |
| `numbers_trivia` | 00:00 | 3645.0 | 34.92% |
| `numbers_trivia` | 14:00 | 3641.2 | 35.24% |
| `numbers_trivia` | 09:00 | 3491.9 | 33.66% |
| `numbers_trivia` | 17:00 | 3455.0 | 34.43% |
| `nasa_apod` | 03:00 | 3414.9 | 50.0% |
| `nasa_apod` | 05:00 | 3413.5 | 48.48% |
| `numbers_trivia` | 05:00 | 3396.0 | 33.33% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
