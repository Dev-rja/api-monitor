# API Reliability Monitor — SLA Report

> Last updated: **2026-08-11 06:31 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **77.8%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 72.05% | 2934.8 | 10420.1 | 1000ms | 518/1853 |
| ❌ | `public_apis_list` | 0.0% | 99.62% | 131.9 | 5052.3 | 1500ms | 7/1853 |
| ❌ | `ipapi_check` | 63.3% | 99.95% | 148.0 | 4507.0 | 2500ms | 1/1853 |
| ❌ | `nasa_apod` | 77.06% | 53.21% | 3075.0 | 11152.5 | 2000ms | 867/1853 |
| ⚠️ | `dog_ceo_random` | 95.9% | 96.92% | 525.7 | 10244.1 | 2500ms | 57/1853 |
| ⚠️ | `open_meteo_weather` | 98.97% | 97.79% | 691.2 | 14877.1 | 2000ms | 41/1853 |
| ✅ | `rest_countries` | 99.19% | 98.87% | 288.0 | 10221.5 | 2500ms | 21/1853 |
| ✅ | `useless_fact` | 99.73% | 99.62% | 649.9 | 10229.6 | 2500ms | 7/1853 |
| ✅ | `coingecko_bitcoin` | 99.78% | 99.95% | 96.8 | 4328.4 | 1500ms | 1/1853 |
| ✅ | `catfact_random` | 99.84% | 99.46% | 257.1 | 10080.2 | 3000ms | 10/1853 |
| ✅ | `agify_name` | 99.89% | 99.73% | 391.4 | 16112.2 | 2000ms | 5/1853 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.89% | 196.0 | 3882.8 | 2000ms | 2/1853 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `nasa_apod` | 02:00 | 4888.7 | 72.73% |
| `numbers_trivia` | 03:00 | 4867.8 | 48.65% |
| `nasa_apod` | 05:00 | 4478.0 | 61.36% |
| `nasa_apod` | 03:00 | 4105.3 | 62.16% |
| `numbers_trivia` | 10:00 | 3824.0 | 36.23% |
| `nasa_apod` | 17:00 | 3726.4 | 50.0% |
| `nasa_apod` | 09:00 | 3705.3 | 51.32% |
| `nasa_apod` | 11:00 | 3673.0 | 51.49% |
| `numbers_trivia` | 14:00 | 3607.6 | 34.94% |
| `nasa_apod` | 12:00 | 3352.7 | 50.65% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
