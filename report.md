# API Reliability Monitor — SLA Report

> Last updated: **2026-08-18 20:32 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **77.4%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 66.1% | 3520.4 | 10420.1 | 1000ms | 713/2103 |
| ❌ | `public_apis_list` | 0.0% | 99.52% | 137.1 | 5075.4 | 1500ms | 10/2103 |
| ❌ | `ipapi_check` | 56.44% | 99.95% | 145.3 | 4507.0 | 2500ms | 1/2103 |
| ❌ | `nasa_apod` | 78.46% | 54.83% | 2953.8 | 11152.5 | 2000ms | 950/2103 |
| ⚠️ | `dog_ceo_random` | 96.39% | 97.24% | 501.4 | 10244.1 | 2500ms | 58/2103 |
| ⚠️ | `open_meteo_weather` | 98.95% | 97.96% | 687.5 | 14877.1 | 2000ms | 43/2103 |
| ✅ | `rest_countries` | 99.29% | 99.0% | 276.7 | 10221.5 | 2500ms | 21/2103 |
| ✅ | `useless_fact` | 99.76% | 99.67% | 651.4 | 10229.6 | 2500ms | 7/2103 |
| ✅ | `catfact_random` | 99.76% | 99.43% | 264.1 | 10080.2 | 3000ms | 12/2103 |
| ✅ | `coingecko_bitcoin` | 99.81% | 99.9% | 96.7 | 4328.4 | 1500ms | 2/2103 |
| ✅ | `agify_name` | 99.9% | 99.71% | 393.4 | 16112.2 | 2000ms | 6/2103 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.9% | 190.0 | 3882.8 | 2000ms | 2/2103 |

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
| `nasa_apod` | 09:00 | 3696.1 | 51.69% |
| `numbers_trivia` | 07:00 | 3690.3 | 34.92% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
