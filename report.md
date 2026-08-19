# API Reliability Monitor — SLA Report

> Last updated: **2026-08-19 04:09 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **77.4%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 66.29% | 3501.0 | 10420.1 | 1000ms | 713/2115 |
| ❌ | `public_apis_list` | 0.0% | 99.53% | 136.9 | 5075.4 | 1500ms | 10/2115 |
| ❌ | `ipapi_check` | 56.17% | 99.95% | 145.2 | 4507.0 | 2500ms | 1/2115 |
| ❌ | `nasa_apod` | 78.53% | 54.94% | 2947.0 | 11152.5 | 2000ms | 953/2115 |
| ⚠️ | `dog_ceo_random` | 96.41% | 97.26% | 500.2 | 10244.1 | 2500ms | 58/2115 |
| ⚠️ | `open_meteo_weather` | 98.96% | 97.97% | 686.8 | 14877.1 | 2000ms | 43/2115 |
| ✅ | `rest_countries` | 99.29% | 99.01% | 276.2 | 10221.5 | 2500ms | 21/2115 |
| ✅ | `useless_fact` | 99.76% | 99.67% | 651.3 | 10229.6 | 2500ms | 7/2115 |
| ✅ | `catfact_random` | 99.76% | 99.39% | 265.7 | 10080.2 | 3000ms | 13/2115 |
| ✅ | `coingecko_bitcoin` | 99.81% | 99.91% | 96.6 | 4328.4 | 1500ms | 2/2115 |
| ✅ | `agify_name` | 99.91% | 99.72% | 393.7 | 16112.2 | 2000ms | 6/2115 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.91% | 189.6 | 3882.8 | 2000ms | 2/2115 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `numbers_trivia` | 03:00 | 5018.2 | 50.0% |
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
