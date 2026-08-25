# API Reliability Monitor — SLA Report

> Last updated: **2026-08-25 01:01 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **7/12** &nbsp;|&nbsp; Avg uptime: **77.1%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 69.01% | 3230.8 | 10420.1 | 1000ms | 728/2349 |
| ❌ | `public_apis_list` | 0.0% | 99.45% | 139.3 | 5075.4 | 1500ms | 13/2349 |
| ❌ | `ipapi_check` | 50.92% | 99.96% | 144.5 | 4507.0 | 2500ms | 1/2349 |
| ❌ | `nasa_apod` | 80.03% | 57.73% | 2767.1 | 11152.5 | 2000ms | 993/2349 |
| ⚠️ | `dog_ceo_random` | 96.76% | 97.49% | 486.4 | 10244.1 | 2500ms | 59/2349 |
| ✅ | `open_meteo_weather` | 99.02% | 98.17% | 676.6 | 14877.1 | 2000ms | 43/2349 |
| ✅ | `rest_countries` | 99.36% | 99.11% | 268.1 | 10221.5 | 2500ms | 21/2349 |
| ✅ | `useless_fact` | 99.79% | 99.7% | 654.4 | 10229.6 | 2500ms | 7/2349 |
| ✅ | `catfact_random` | 99.79% | 99.45% | 262.2 | 10080.2 | 3000ms | 13/2349 |
| ✅ | `coingecko_bitcoin` | 99.83% | 99.91% | 96.6 | 4328.4 | 1500ms | 2/2349 |
| ✅ | `agify_name` | 99.91% | 99.53% | 401.8 | 16112.2 | 2000ms | 11/2349 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.91% | 185.3 | 3882.8 | 2000ms | 2/2349 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `numbers_trivia` | 03:00 | 4927.1 | 48.98% |
| `numbers_trivia` | 10:00 | 3834.8 | 36.56% |
| `numbers_trivia` | 02:00 | 3827.8 | 36.36% |
| `numbers_trivia` | 00:00 | 3645.0 | 34.92% |
| `numbers_trivia` | 14:00 | 3641.2 | 35.24% |
| `numbers_trivia` | 09:00 | 3560.2 | 34.34% |
| `nasa_apod` | 03:00 | 3476.6 | 51.02% |
| `nasa_apod` | 05:00 | 3462.4 | 49.23% |
| `numbers_trivia` | 17:00 | 3455.0 | 34.43% |
| `numbers_trivia` | 05:00 | 3445.2 | 33.85% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
