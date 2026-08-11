# API Reliability Monitor — SLA Report

> Last updated: **2026-08-11 14:59 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **77.8%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 71.74% | 2965.6 | 10420.1 | 1000ms | 526/1861 |
| ❌ | `public_apis_list` | 0.0% | 99.62% | 132.2 | 5052.3 | 1500ms | 7/1861 |
| ❌ | `ipapi_check` | 63.03% | 99.95% | 147.8 | 4507.0 | 2500ms | 1/1861 |
| ❌ | `nasa_apod` | 77.0% | 53.04% | 3083.6 | 11152.5 | 2000ms | 874/1861 |
| ⚠️ | `dog_ceo_random` | 95.92% | 96.94% | 524.9 | 10244.1 | 2500ms | 57/1861 |
| ⚠️ | `open_meteo_weather` | 98.98% | 97.8% | 691.1 | 14877.1 | 2000ms | 41/1861 |
| ✅ | `rest_countries` | 99.19% | 98.87% | 287.6 | 10221.5 | 2500ms | 21/1861 |
| ✅ | `useless_fact` | 99.73% | 99.62% | 650.2 | 10229.6 | 2500ms | 7/1861 |
| ✅ | `coingecko_bitcoin` | 99.79% | 99.95% | 96.7 | 4328.4 | 1500ms | 1/1861 |
| ✅ | `catfact_random` | 99.84% | 99.46% | 256.9 | 10080.2 | 3000ms | 10/1861 |
| ✅ | `agify_name` | 99.89% | 99.73% | 391.9 | 16112.2 | 2000ms | 5/1861 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.89% | 195.8 | 3882.8 | 2000ms | 2/1861 |

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
