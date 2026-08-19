# API Reliability Monitor — SLA Report

> Last updated: **2026-08-19 08:51 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **77.4%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 66.4% | 3489.8 | 10420.1 | 1000ms | 713/2122 |
| ❌ | `public_apis_list` | 0.0% | 99.53% | 136.9 | 5075.4 | 1500ms | 10/2122 |
| ❌ | `ipapi_check` | 56.03% | 99.95% | 145.3 | 4507.0 | 2500ms | 1/2122 |
| ❌ | `nasa_apod` | 78.61% | 55.04% | 2939.9 | 11152.5 | 2000ms | 954/2122 |
| ⚠️ | `dog_ceo_random` | 96.42% | 97.27% | 499.7 | 10244.1 | 2500ms | 58/2122 |
| ⚠️ | `open_meteo_weather` | 98.96% | 97.97% | 686.5 | 14877.1 | 2000ms | 43/2122 |
| ✅ | `rest_countries` | 99.29% | 99.01% | 275.9 | 10221.5 | 2500ms | 21/2122 |
| ✅ | `useless_fact` | 99.76% | 99.67% | 651.5 | 10229.6 | 2500ms | 7/2122 |
| ✅ | `catfact_random` | 99.76% | 99.39% | 265.6 | 10080.2 | 3000ms | 13/2122 |
| ✅ | `coingecko_bitcoin` | 99.81% | 99.91% | 96.7 | 4328.4 | 1500ms | 2/2122 |
| ✅ | `agify_name` | 99.91% | 99.72% | 393.6 | 16112.2 | 2000ms | 6/2122 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.91% | 189.5 | 3882.8 | 2000ms | 2/2122 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `numbers_trivia` | 03:00 | 5018.2 | 50.0% |
| `numbers_trivia` | 10:00 | 4433.0 | 42.5% |
| `numbers_trivia` | 02:00 | 4334.9 | 41.18% |
| `numbers_trivia` | 14:00 | 4048.7 | 39.36% |
| `numbers_trivia` | 05:00 | 3912.1 | 38.6% |
| `numbers_trivia` | 09:00 | 3902.6 | 37.78% |
| `nasa_apod` | 05:00 | 3869.5 | 56.14% |
| `numbers_trivia` | 00:00 | 3712.5 | 35.59% |
| `nasa_apod` | 09:00 | 3696.1 | 51.69% |
| `numbers_trivia` | 17:00 | 3665.8 | 36.7% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
