# API Reliability Monitor — SLA Report

> Last updated: **2026-08-11 02:55 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **77.8%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 72.16% | 2923.3 | 10420.1 | 1000ms | 515/1850 |
| ❌ | `public_apis_list` | 0.0% | 99.62% | 131.8 | 5052.3 | 1500ms | 7/1850 |
| ❌ | `ipapi_check` | 63.41% | 99.95% | 147.9 | 4507.0 | 2500ms | 1/1850 |
| ❌ | `nasa_apod` | 77.03% | 53.24% | 3077.0 | 11152.5 | 2000ms | 865/1850 |
| ⚠️ | `dog_ceo_random` | 95.89% | 96.92% | 526.1 | 10244.1 | 2500ms | 57/1850 |
| ⚠️ | `open_meteo_weather` | 98.97% | 97.78% | 691.4 | 14877.1 | 2000ms | 41/1850 |
| ✅ | `rest_countries` | 99.19% | 98.86% | 288.1 | 10221.5 | 2500ms | 21/1850 |
| ✅ | `useless_fact` | 99.73% | 99.62% | 649.8 | 10229.6 | 2500ms | 7/1850 |
| ✅ | `coingecko_bitcoin` | 99.78% | 99.95% | 96.8 | 4328.4 | 1500ms | 1/1850 |
| ✅ | `catfact_random` | 99.84% | 99.46% | 257.1 | 10080.2 | 3000ms | 10/1850 |
| ✅ | `agify_name` | 99.89% | 99.73% | 391.3 | 16112.2 | 2000ms | 5/1850 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.89% | 196.0 | 3882.8 | 2000ms | 2/1850 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `nasa_apod` | 02:00 | 4888.7 | 72.73% |
| `numbers_trivia` | 03:00 | 4867.8 | 48.65% |
| `nasa_apod` | 05:00 | 4572.2 | 62.79% |
| `nasa_apod` | 03:00 | 4105.3 | 62.16% |
| `numbers_trivia` | 10:00 | 3824.0 | 36.23% |
| `nasa_apod` | 17:00 | 3726.4 | 50.0% |
| `nasa_apod` | 09:00 | 3705.3 | 51.32% |
| `nasa_apod` | 11:00 | 3673.0 | 51.49% |
| `numbers_trivia` | 14:00 | 3607.6 | 34.94% |
| `nasa_apod` | 12:00 | 3352.7 | 50.65% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
