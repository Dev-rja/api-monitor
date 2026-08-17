# API Reliability Monitor — SLA Report

> Last updated: **2026-08-17 07:31 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **77.5%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 65.41% | 3589.6 | 10420.1 | 1000ms | 706/2041 |
| ❌ | `public_apis_list` | 0.0% | 99.56% | 136.3 | 5075.4 | 1500ms | 9/2041 |
| ❌ | `ipapi_check` | 57.96% | 99.95% | 145.5 | 4507.0 | 2500ms | 1/2041 |
| ❌ | `nasa_apod` | 78.2% | 54.29% | 2980.4 | 11152.5 | 2000ms | 933/2041 |
| ⚠️ | `dog_ceo_random` | 96.28% | 97.16% | 507.3 | 10244.1 | 2500ms | 58/2041 |
| ⚠️ | `open_meteo_weather` | 98.92% | 97.89% | 691.2 | 14877.1 | 2000ms | 43/2041 |
| ✅ | `rest_countries` | 99.27% | 98.97% | 279.0 | 10221.5 | 2500ms | 21/2041 |
| ✅ | `useless_fact` | 99.76% | 99.66% | 650.6 | 10229.6 | 2500ms | 7/2041 |
| ✅ | `catfact_random` | 99.76% | 99.41% | 264.5 | 10080.2 | 3000ms | 12/2041 |
| ✅ | `coingecko_bitcoin` | 99.8% | 99.9% | 96.7 | 4328.4 | 1500ms | 2/2041 |
| ✅ | `agify_name` | 99.9% | 99.76% | 391.8 | 16112.2 | 2000ms | 5/2041 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.9% | 191.1 | 3882.8 | 2000ms | 2/2041 |

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
| `numbers_trivia` | 09:00 | 3846.3 | 37.21% |
| `numbers_trivia` | 07:00 | 3807.8 | 36.07% |
| `numbers_trivia` | 17:00 | 3801.2 | 38.1% |
| `numbers_trivia` | 00:00 | 3774.1 | 36.21% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
