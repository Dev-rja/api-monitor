# API Reliability Monitor — SLA Report

> Last updated: **2026-08-17 21:43 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **77.4%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 65.54% | 3576.5 | 10420.1 | 1000ms | 712/2066 |
| ❌ | `public_apis_list` | 0.0% | 99.56% | 136.1 | 5075.4 | 1500ms | 9/2066 |
| ❌ | `ipapi_check` | 57.36% | 99.95% | 145.4 | 4507.0 | 2500ms | 1/2066 |
| ❌ | `nasa_apod` | 78.17% | 54.36% | 2985.0 | 11152.5 | 2000ms | 943/2066 |
| ⚠️ | `dog_ceo_random` | 96.32% | 97.19% | 504.6 | 10244.1 | 2500ms | 58/2066 |
| ⚠️ | `open_meteo_weather` | 98.94% | 97.92% | 689.6 | 14877.1 | 2000ms | 43/2066 |
| ✅ | `rest_countries` | 99.27% | 98.98% | 277.9 | 10221.5 | 2500ms | 21/2066 |
| ✅ | `useless_fact` | 99.76% | 99.66% | 651.4 | 10229.6 | 2500ms | 7/2066 |
| ✅ | `catfact_random` | 99.76% | 99.42% | 264.7 | 10080.2 | 3000ms | 12/2066 |
| ✅ | `coingecko_bitcoin` | 99.81% | 99.9% | 96.7 | 4328.4 | 1500ms | 2/2066 |
| ✅ | `agify_name` | 99.9% | 99.76% | 391.1 | 16112.2 | 2000ms | 5/2066 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.9% | 190.5 | 3882.8 | 2000ms | 2/2066 |

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
