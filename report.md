# API Reliability Monitor — SLA Report

> Last updated: **2026-08-17 11:34 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **77.5%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 65.27% | 3603.7 | 10420.1 | 1000ms | 711/2047 |
| ❌ | `public_apis_list` | 0.0% | 99.56% | 136.4 | 5075.4 | 1500ms | 9/2047 |
| ❌ | `ipapi_check` | 57.79% | 99.95% | 145.5 | 4507.0 | 2500ms | 1/2047 |
| ❌ | `nasa_apod` | 78.11% | 54.23% | 2991.2 | 11152.5 | 2000ms | 937/2047 |
| ⚠️ | `dog_ceo_random` | 96.29% | 97.17% | 506.4 | 10244.1 | 2500ms | 58/2047 |
| ⚠️ | `open_meteo_weather` | 98.93% | 97.9% | 690.5 | 14877.1 | 2000ms | 43/2047 |
| ✅ | `rest_countries` | 99.27% | 98.97% | 278.7 | 10221.5 | 2500ms | 21/2047 |
| ✅ | `useless_fact` | 99.76% | 99.66% | 651.0 | 10229.6 | 2500ms | 7/2047 |
| ✅ | `catfact_random` | 99.76% | 99.41% | 264.3 | 10080.2 | 3000ms | 12/2047 |
| ✅ | `coingecko_bitcoin` | 99.8% | 99.9% | 96.6 | 4328.4 | 1500ms | 2/2047 |
| ✅ | `agify_name` | 99.9% | 99.76% | 391.5 | 16112.2 | 2000ms | 5/2047 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.9% | 191.0 | 3882.8 | 2000ms | 2/2047 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `numbers_trivia` | 03:00 | 5376.8 | 53.66% |
| `numbers_trivia` | 02:00 | 4898.3 | 46.67% |
| `numbers_trivia` | 10:00 | 4544.4 | 43.59% |
| `numbers_trivia` | 05:00 | 4198.9 | 41.51% |
| `numbers_trivia` | 14:00 | 4176.1 | 40.66% |
| `nasa_apod` | 05:00 | 4091.3 | 58.49% |
| `numbers_trivia` | 09:00 | 3988.1 | 38.64% |
| `numbers_trivia` | 07:00 | 3807.8 | 36.07% |
| `numbers_trivia` | 17:00 | 3801.2 | 38.1% |
| `numbers_trivia` | 00:00 | 3774.1 | 36.21% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
