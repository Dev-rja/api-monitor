# API Reliability Monitor — SLA Report

> Last updated: **2026-08-17 14:41 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **77.5%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 65.3% | 3600.2 | 10420.1 | 1000ms | 712/2052 |
| ❌ | `public_apis_list` | 0.0% | 99.56% | 136.3 | 5075.4 | 1500ms | 9/2052 |
| ❌ | `ipapi_check` | 57.65% | 99.95% | 145.7 | 4507.0 | 2500ms | 1/2052 |
| ❌ | `nasa_apod` | 78.07% | 54.09% | 2997.6 | 11152.5 | 2000ms | 942/2052 |
| ⚠️ | `dog_ceo_random` | 96.3% | 97.17% | 506.1 | 10244.1 | 2500ms | 58/2052 |
| ⚠️ | `open_meteo_weather` | 98.93% | 97.9% | 690.4 | 14877.1 | 2000ms | 43/2052 |
| ✅ | `rest_countries` | 99.27% | 98.98% | 278.7 | 10221.5 | 2500ms | 21/2052 |
| ✅ | `useless_fact` | 99.76% | 99.66% | 651.1 | 10229.6 | 2500ms | 7/2052 |
| ✅ | `catfact_random` | 99.76% | 99.42% | 264.4 | 10080.2 | 3000ms | 12/2052 |
| ✅ | `coingecko_bitcoin` | 99.81% | 99.9% | 96.8 | 4328.4 | 1500ms | 2/2052 |
| ✅ | `agify_name` | 99.9% | 99.76% | 391.5 | 16112.2 | 2000ms | 5/2052 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.9% | 191.0 | 3882.8 | 2000ms | 2/2052 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `numbers_trivia` | 03:00 | 5376.8 | 53.66% |
| `numbers_trivia` | 02:00 | 4898.3 | 46.67% |
| `numbers_trivia` | 10:00 | 4544.4 | 43.59% |
| `numbers_trivia` | 05:00 | 4198.9 | 41.51% |
| `nasa_apod` | 05:00 | 4091.3 | 58.49% |
| `numbers_trivia` | 14:00 | 4090.2 | 39.78% |
| `numbers_trivia` | 09:00 | 3988.1 | 38.64% |
| `numbers_trivia` | 07:00 | 3807.8 | 36.07% |
| `numbers_trivia` | 17:00 | 3801.2 | 38.1% |
| `numbers_trivia` | 00:00 | 3774.1 | 36.21% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
