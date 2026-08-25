# API Reliability Monitor — SLA Report

> Last updated: **2026-08-25 04:08 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **7/12** &nbsp;|&nbsp; Avg uptime: **77.1%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 69.05% | 3226.8 | 10420.1 | 1000ms | 728/2352 |
| ❌ | `public_apis_list` | 0.0% | 99.45% | 139.3 | 5075.4 | 1500ms | 13/2352 |
| ❌ | `ipapi_check` | 50.85% | 99.96% | 144.5 | 4507.0 | 2500ms | 1/2352 |
| ❌ | `nasa_apod` | 80.06% | 57.78% | 2764.2 | 11152.5 | 2000ms | 993/2352 |
| ⚠️ | `dog_ceo_random` | 96.77% | 97.49% | 486.3 | 10244.1 | 2500ms | 59/2352 |
| ✅ | `open_meteo_weather` | 99.02% | 98.17% | 676.4 | 14877.1 | 2000ms | 43/2352 |
| ✅ | `rest_countries` | 99.36% | 99.11% | 268.0 | 10221.5 | 2500ms | 21/2352 |
| ✅ | `useless_fact` | 99.79% | 99.7% | 654.4 | 10229.6 | 2500ms | 7/2352 |
| ✅ | `catfact_random` | 99.79% | 99.45% | 262.3 | 10080.2 | 3000ms | 13/2352 |
| ✅ | `coingecko_bitcoin` | 99.83% | 99.91% | 96.6 | 4328.4 | 1500ms | 2/2352 |
| ✅ | `agify_name` | 99.91% | 99.53% | 401.8 | 16112.2 | 2000ms | 11/2352 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.91% | 185.3 | 3882.8 | 2000ms | 2/2352 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `numbers_trivia` | 03:00 | 4832.5 | 48.0% |
| `numbers_trivia` | 10:00 | 3834.8 | 36.56% |
| `numbers_trivia` | 02:00 | 3664.7 | 34.78% |
| `numbers_trivia` | 00:00 | 3645.0 | 34.92% |
| `numbers_trivia` | 14:00 | 3641.2 | 35.24% |
| `numbers_trivia` | 09:00 | 3560.2 | 34.34% |
| `nasa_apod` | 05:00 | 3462.4 | 49.23% |
| `numbers_trivia` | 17:00 | 3455.0 | 34.43% |
| `numbers_trivia` | 05:00 | 3445.2 | 33.85% |
| `nasa_apod` | 03:00 | 3414.9 | 50.0% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
