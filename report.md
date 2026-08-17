# API Reliability Monitor — SLA Report

> Last updated: **2026-08-17 19:52 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **77.4%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 65.47% | 3583.2 | 10420.1 | 1000ms | 712/2062 |
| ❌ | `public_apis_list` | 0.0% | 99.56% | 136.1 | 5075.4 | 1500ms | 9/2062 |
| ❌ | `ipapi_check` | 57.47% | 99.95% | 145.5 | 4507.0 | 2500ms | 1/2062 |
| ❌ | `nasa_apod` | 78.13% | 54.27% | 2990.1 | 11152.5 | 2000ms | 943/2062 |
| ⚠️ | `dog_ceo_random` | 96.31% | 97.19% | 505.1 | 10244.1 | 2500ms | 58/2062 |
| ⚠️ | `open_meteo_weather` | 98.93% | 97.91% | 689.9 | 14877.1 | 2000ms | 43/2062 |
| ✅ | `rest_countries` | 99.27% | 98.98% | 278.2 | 10221.5 | 2500ms | 21/2062 |
| ✅ | `useless_fact` | 99.76% | 99.66% | 651.2 | 10229.6 | 2500ms | 7/2062 |
| ✅ | `catfact_random` | 99.76% | 99.42% | 264.7 | 10080.2 | 3000ms | 12/2062 |
| ✅ | `coingecko_bitcoin` | 99.81% | 99.9% | 96.7 | 4328.4 | 1500ms | 2/2062 |
| ✅ | `agify_name` | 99.9% | 99.76% | 391.2 | 16112.2 | 2000ms | 5/2062 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.9% | 190.7 | 3882.8 | 2000ms | 2/2062 |

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
| `numbers_trivia` | 00:00 | 3774.1 | 36.21% |
| `nasa_apod` | 03:00 | 3758.3 | 56.1% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
