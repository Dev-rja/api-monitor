# API Reliability Monitor — SLA Report

> Last updated: **2026-08-11 16:07 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **77.8%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 71.7% | 2969.4 | 10420.1 | 1000ms | 527/1862 |
| ❌ | `public_apis_list` | 0.0% | 99.62% | 132.2 | 5052.3 | 1500ms | 7/1862 |
| ❌ | `ipapi_check` | 63.0% | 99.95% | 147.7 | 4507.0 | 2500ms | 1/1862 |
| ❌ | `nasa_apod` | 77.01% | 53.01% | 3083.2 | 11152.5 | 2000ms | 875/1862 |
| ⚠️ | `dog_ceo_random` | 95.92% | 96.94% | 524.9 | 10244.1 | 2500ms | 57/1862 |
| ⚠️ | `open_meteo_weather` | 98.98% | 97.8% | 691.1 | 14877.1 | 2000ms | 41/1862 |
| ✅ | `rest_countries` | 99.19% | 98.87% | 287.5 | 10221.5 | 2500ms | 21/1862 |
| ✅ | `useless_fact` | 99.73% | 99.62% | 650.3 | 10229.6 | 2500ms | 7/1862 |
| ✅ | `coingecko_bitcoin` | 99.79% | 99.95% | 96.7 | 4328.4 | 1500ms | 1/1862 |
| ✅ | `catfact_random` | 99.84% | 99.46% | 256.8 | 10080.2 | 3000ms | 10/1862 |
| ✅ | `agify_name` | 99.89% | 99.73% | 392.1 | 16112.2 | 2000ms | 5/1862 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.89% | 195.8 | 3882.8 | 2000ms | 2/1862 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `nasa_apod` | 02:00 | 4888.7 | 72.73% |
| `numbers_trivia` | 03:00 | 4867.8 | 48.65% |
| `nasa_apod` | 05:00 | 4478.0 | 61.36% |
| `nasa_apod` | 03:00 | 4105.3 | 62.16% |
| `numbers_trivia` | 10:00 | 3912.8 | 37.14% |
| `nasa_apod` | 09:00 | 3789.3 | 51.95% |
| `nasa_apod` | 11:00 | 3737.3 | 51.96% |
| `nasa_apod` | 17:00 | 3726.4 | 50.0% |
| `numbers_trivia` | 14:00 | 3684.0 | 35.71% |
| `nasa_apod` | 12:00 | 3341.6 | 51.28% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
