# API Reliability Monitor — SLA Report

> Last updated: **2026-08-18 17:21 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **77.4%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 66.0% | 3530.1 | 10420.1 | 1000ms | 713/2097 |
| ❌ | `public_apis_list` | 0.0% | 99.52% | 137.1 | 5075.4 | 1500ms | 10/2097 |
| ❌ | `ipapi_check` | 56.6% | 99.95% | 145.4 | 4507.0 | 2500ms | 1/2097 |
| ❌ | `nasa_apod` | 78.4% | 54.74% | 2960.1 | 11152.5 | 2000ms | 949/2097 |
| ⚠️ | `dog_ceo_random` | 96.38% | 97.23% | 502.2 | 10244.1 | 2500ms | 58/2097 |
| ⚠️ | `open_meteo_weather` | 98.95% | 97.95% | 687.8 | 14877.1 | 2000ms | 43/2097 |
| ✅ | `rest_countries` | 99.28% | 99.0% | 277.0 | 10221.5 | 2500ms | 21/2097 |
| ✅ | `useless_fact` | 99.76% | 99.67% | 651.3 | 10229.6 | 2500ms | 7/2097 |
| ✅ | `catfact_random` | 99.76% | 99.43% | 264.3 | 10080.2 | 3000ms | 12/2097 |
| ✅ | `coingecko_bitcoin` | 99.81% | 99.9% | 96.8 | 4328.4 | 1500ms | 2/2097 |
| ✅ | `agify_name` | 99.9% | 99.71% | 393.3 | 16112.2 | 2000ms | 6/2097 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.9% | 190.1 | 3882.8 | 2000ms | 2/2097 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `numbers_trivia` | 03:00 | 5132.1 | 51.16% |
| `numbers_trivia` | 02:00 | 4598.2 | 43.75% |
| `numbers_trivia` | 10:00 | 4433.0 | 42.5% |
| `numbers_trivia` | 05:00 | 4051.3 | 40.0% |
| `numbers_trivia` | 14:00 | 4048.7 | 39.36% |
| `nasa_apod` | 05:00 | 3992.2 | 58.18% |
| `numbers_trivia` | 09:00 | 3902.6 | 37.78% |
| `numbers_trivia` | 00:00 | 3712.5 | 35.59% |
| `numbers_trivia` | 17:00 | 3698.4 | 37.04% |
| `nasa_apod` | 09:00 | 3696.1 | 51.69% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
