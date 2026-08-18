# API Reliability Monitor — SLA Report

> Last updated: **2026-08-18 06:19 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **77.4%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 65.75% | 3554.8 | 10420.1 | 1000ms | 712/2079 |
| ❌ | `public_apis_list` | 0.0% | 99.57% | 136.1 | 5075.4 | 1500ms | 9/2079 |
| ❌ | `ipapi_check` | 57.05% | 99.95% | 145.4 | 4507.0 | 2500ms | 1/2079 |
| ❌ | `nasa_apod` | 78.31% | 54.5% | 2971.9 | 11152.5 | 2000ms | 946/2079 |
| ⚠️ | `dog_ceo_random` | 96.34% | 97.21% | 503.7 | 10244.1 | 2500ms | 58/2079 |
| ⚠️ | `open_meteo_weather` | 98.94% | 97.93% | 688.9 | 14877.1 | 2000ms | 43/2079 |
| ✅ | `rest_countries` | 99.28% | 98.99% | 277.6 | 10221.5 | 2500ms | 21/2079 |
| ✅ | `useless_fact` | 99.76% | 99.66% | 651.5 | 10229.6 | 2500ms | 7/2079 |
| ✅ | `catfact_random` | 99.76% | 99.42% | 264.6 | 10080.2 | 3000ms | 12/2079 |
| ✅ | `coingecko_bitcoin` | 99.81% | 99.9% | 96.8 | 4328.4 | 1500ms | 2/2079 |
| ✅ | `agify_name` | 99.9% | 99.76% | 391.1 | 16112.2 | 2000ms | 5/2079 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.9% | 190.3 | 3882.8 | 2000ms | 2/2079 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `numbers_trivia` | 03:00 | 5132.1 | 51.16% |
| `numbers_trivia` | 02:00 | 4598.2 | 43.75% |
| `numbers_trivia` | 10:00 | 4544.4 | 43.59% |
| `numbers_trivia` | 14:00 | 4090.2 | 39.78% |
| `numbers_trivia` | 05:00 | 4051.3 | 40.0% |
| `nasa_apod` | 05:00 | 3992.2 | 58.18% |
| `numbers_trivia` | 09:00 | 3988.1 | 38.64% |
| `numbers_trivia` | 07:00 | 3807.8 | 36.07% |
| `numbers_trivia` | 17:00 | 3731.6 | 37.38% |
| `numbers_trivia` | 00:00 | 3712.5 | 35.59% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
