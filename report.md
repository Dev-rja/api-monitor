# API Reliability Monitor — SLA Report

> Last updated: **2026-08-17 09:55 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **77.5%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 65.31% | 3599.1 | 10420.1 | 1000ms | 709/2044 |
| ❌ | `public_apis_list` | 0.0% | 99.56% | 136.4 | 5075.4 | 1500ms | 9/2044 |
| ❌ | `ipapi_check` | 57.88% | 99.95% | 145.5 | 4507.0 | 2500ms | 1/2044 |
| ❌ | `nasa_apod` | 78.13% | 54.26% | 2986.3 | 11152.5 | 2000ms | 935/2044 |
| ⚠️ | `dog_ceo_random` | 96.28% | 97.16% | 506.9 | 10244.1 | 2500ms | 58/2044 |
| ⚠️ | `open_meteo_weather` | 98.92% | 97.9% | 690.9 | 14877.1 | 2000ms | 43/2044 |
| ✅ | `rest_countries` | 99.27% | 98.97% | 278.9 | 10221.5 | 2500ms | 21/2044 |
| ✅ | `useless_fact` | 99.76% | 99.66% | 651.1 | 10229.6 | 2500ms | 7/2044 |
| ✅ | `catfact_random` | 99.76% | 99.41% | 264.5 | 10080.2 | 3000ms | 12/2044 |
| ✅ | `coingecko_bitcoin` | 99.8% | 99.9% | 96.7 | 4328.4 | 1500ms | 2/2044 |
| ✅ | `agify_name` | 99.9% | 99.76% | 391.7 | 16112.2 | 2000ms | 5/2044 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.9% | 191.0 | 3882.8 | 2000ms | 2/2044 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `numbers_trivia` | 03:00 | 5376.8 | 53.66% |
| `numbers_trivia` | 02:00 | 4898.3 | 46.67% |
| `numbers_trivia` | 10:00 | 4472.8 | 42.86% |
| `numbers_trivia` | 05:00 | 4198.9 | 41.51% |
| `numbers_trivia` | 14:00 | 4176.1 | 40.66% |
| `nasa_apod` | 05:00 | 4091.3 | 58.49% |
| `numbers_trivia` | 09:00 | 3988.1 | 38.64% |
| `numbers_trivia` | 07:00 | 3807.8 | 36.07% |
| `numbers_trivia` | 17:00 | 3801.2 | 38.1% |
| `numbers_trivia` | 00:00 | 3774.1 | 36.21% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
