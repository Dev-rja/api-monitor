# API Reliability Monitor — SLA Report

> Last updated: **2026-08-18 02:17 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **77.4%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 65.65% | 3564.8 | 10420.1 | 1000ms | 712/2073 |
| ❌ | `public_apis_list` | 0.0% | 99.57% | 136.0 | 5075.4 | 1500ms | 9/2073 |
| ❌ | `ipapi_check` | 57.21% | 99.95% | 145.4 | 4507.0 | 2500ms | 1/2073 |
| ❌ | `nasa_apod` | 78.24% | 54.51% | 2976.3 | 11152.5 | 2000ms | 943/2073 |
| ⚠️ | `dog_ceo_random` | 96.33% | 97.2% | 504.1 | 10244.1 | 2500ms | 58/2073 |
| ⚠️ | `open_meteo_weather` | 98.94% | 97.93% | 689.2 | 14877.1 | 2000ms | 43/2073 |
| ✅ | `rest_countries` | 99.28% | 98.99% | 277.6 | 10221.5 | 2500ms | 21/2073 |
| ✅ | `useless_fact` | 99.76% | 99.66% | 651.4 | 10229.6 | 2500ms | 7/2073 |
| ✅ | `catfact_random` | 99.76% | 99.42% | 264.6 | 10080.2 | 3000ms | 12/2073 |
| ✅ | `coingecko_bitcoin` | 99.81% | 99.9% | 96.7 | 4328.4 | 1500ms | 2/2073 |
| ✅ | `agify_name` | 99.9% | 99.76% | 391.1 | 16112.2 | 2000ms | 5/2073 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.9% | 190.4 | 3882.8 | 2000ms | 2/2073 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `numbers_trivia` | 03:00 | 5376.8 | 53.66% |
| `numbers_trivia` | 02:00 | 4598.2 | 43.75% |
| `numbers_trivia` | 10:00 | 4544.4 | 43.59% |
| `numbers_trivia` | 05:00 | 4198.9 | 41.51% |
| `nasa_apod` | 05:00 | 4091.3 | 58.49% |
| `numbers_trivia` | 14:00 | 4090.2 | 39.78% |
| `numbers_trivia` | 09:00 | 3988.1 | 38.64% |
| `numbers_trivia` | 07:00 | 3807.8 | 36.07% |
| `nasa_apod` | 03:00 | 3758.3 | 56.1% |
| `numbers_trivia` | 17:00 | 3731.6 | 37.38% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
