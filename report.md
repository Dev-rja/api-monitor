# API Reliability Monitor — SLA Report

> Last updated: **2026-08-17 14:04 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **77.5%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 65.29% | 3601.8 | 10420.1 | 1000ms | 712/2051 |
| ❌ | `public_apis_list` | 0.0% | 99.56% | 136.4 | 5075.4 | 1500ms | 9/2051 |
| ❌ | `ipapi_check` | 57.68% | 99.95% | 145.7 | 4507.0 | 2500ms | 1/2051 |
| ❌ | `nasa_apod` | 78.11% | 54.12% | 2994.0 | 11152.5 | 2000ms | 941/2051 |
| ⚠️ | `dog_ceo_random` | 96.29% | 97.17% | 506.2 | 10244.1 | 2500ms | 58/2051 |
| ⚠️ | `open_meteo_weather` | 98.93% | 97.9% | 690.4 | 14877.1 | 2000ms | 43/2051 |
| ✅ | `rest_countries` | 99.27% | 98.98% | 278.8 | 10221.5 | 2500ms | 21/2051 |
| ✅ | `useless_fact` | 99.76% | 99.66% | 651.1 | 10229.6 | 2500ms | 7/2051 |
| ✅ | `catfact_random` | 99.76% | 99.41% | 264.3 | 10080.2 | 3000ms | 12/2051 |
| ✅ | `coingecko_bitcoin` | 99.8% | 99.9% | 96.7 | 4328.4 | 1500ms | 2/2051 |
| ✅ | `agify_name` | 99.9% | 99.76% | 391.5 | 16112.2 | 2000ms | 5/2051 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.9% | 191.0 | 3882.8 | 2000ms | 2/2051 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `numbers_trivia` | 03:00 | 5376.8 | 53.66% |
| `numbers_trivia` | 02:00 | 4898.3 | 46.67% |
| `numbers_trivia` | 10:00 | 4544.4 | 43.59% |
| `numbers_trivia` | 05:00 | 4198.9 | 41.51% |
| `numbers_trivia` | 14:00 | 4132.6 | 40.22% |
| `nasa_apod` | 05:00 | 4091.3 | 58.49% |
| `numbers_trivia` | 09:00 | 3988.1 | 38.64% |
| `numbers_trivia` | 07:00 | 3807.8 | 36.07% |
| `numbers_trivia` | 17:00 | 3801.2 | 38.1% |
| `numbers_trivia` | 00:00 | 3774.1 | 36.21% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
