# API Reliability Monitor — SLA Report

> Last updated: **2026-08-19 02:32 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **77.4%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 66.26% | 3504.2 | 10420.1 | 1000ms | 713/2113 |
| ❌ | `public_apis_list` | 0.0% | 99.53% | 137.0 | 5075.4 | 1500ms | 10/2113 |
| ❌ | `ipapi_check` | 56.22% | 99.95% | 145.2 | 4507.0 | 2500ms | 1/2113 |
| ❌ | `nasa_apod` | 78.51% | 54.9% | 2949.3 | 11152.5 | 2000ms | 953/2113 |
| ⚠️ | `dog_ceo_random` | 96.4% | 97.26% | 500.5 | 10244.1 | 2500ms | 58/2113 |
| ⚠️ | `open_meteo_weather` | 98.96% | 97.96% | 687.0 | 14877.1 | 2000ms | 43/2113 |
| ✅ | `rest_countries` | 99.29% | 99.01% | 276.3 | 10221.5 | 2500ms | 21/2113 |
| ✅ | `useless_fact` | 99.76% | 99.67% | 651.4 | 10229.6 | 2500ms | 7/2113 |
| ✅ | `catfact_random` | 99.76% | 99.43% | 263.9 | 10080.2 | 3000ms | 12/2113 |
| ✅ | `coingecko_bitcoin` | 99.81% | 99.91% | 96.6 | 4328.4 | 1500ms | 2/2113 |
| ✅ | `agify_name` | 99.91% | 99.72% | 393.7 | 16112.2 | 2000ms | 6/2113 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.91% | 189.7 | 3882.8 | 2000ms | 2/2113 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `numbers_trivia` | 03:00 | 5132.1 | 51.16% |
| `numbers_trivia` | 10:00 | 4433.0 | 42.5% |
| `numbers_trivia` | 02:00 | 4334.9 | 41.18% |
| `numbers_trivia` | 05:00 | 4051.3 | 40.0% |
| `numbers_trivia` | 14:00 | 4048.7 | 39.36% |
| `nasa_apod` | 05:00 | 3992.2 | 58.18% |
| `numbers_trivia` | 09:00 | 3902.6 | 37.78% |
| `numbers_trivia` | 00:00 | 3712.5 | 35.59% |
| `nasa_apod` | 09:00 | 3696.1 | 51.69% |
| `numbers_trivia` | 07:00 | 3690.3 | 34.92% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
