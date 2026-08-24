# API Reliability Monitor — SLA Report

> Last updated: **2026-08-24 14:44 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **7/12** &nbsp;|&nbsp; Avg uptime: **77.1%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 68.78% | 3253.2 | 10420.1 | 1000ms | 728/2332 |
| ❌ | `public_apis_list` | 0.0% | 99.44% | 139.3 | 5075.4 | 1500ms | 13/2332 |
| ❌ | `ipapi_check` | 51.2% | 99.96% | 144.4 | 4507.0 | 2500ms | 1/2332 |
| ❌ | `nasa_apod` | 79.93% | 57.59% | 2777.6 | 11152.5 | 2000ms | 989/2332 |
| ⚠️ | `dog_ceo_random` | 96.74% | 97.47% | 487.3 | 10244.1 | 2500ms | 59/2332 |
| ✅ | `open_meteo_weather` | 99.01% | 98.16% | 677.3 | 14877.1 | 2000ms | 43/2332 |
| ✅ | `rest_countries` | 99.36% | 99.1% | 268.2 | 10221.5 | 2500ms | 21/2332 |
| ✅ | `useless_fact` | 99.79% | 99.7% | 654.3 | 10229.6 | 2500ms | 7/2332 |
| ✅ | `catfact_random` | 99.79% | 99.44% | 261.6 | 10080.2 | 3000ms | 13/2332 |
| ✅ | `coingecko_bitcoin` | 99.83% | 99.91% | 96.6 | 4328.4 | 1500ms | 2/2332 |
| ✅ | `agify_name` | 99.91% | 99.53% | 401.6 | 16112.2 | 2000ms | 11/2332 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.91% | 185.5 | 3882.8 | 2000ms | 2/2332 |

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
| `numbers_trivia` | 17:00 | 3510.1 | 35.0% |
| `nasa_apod` | 03:00 | 3476.6 | 51.02% |
| `nasa_apod` | 05:00 | 3462.4 | 49.23% |
| `numbers_trivia` | 05:00 | 3445.2 | 33.85% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
