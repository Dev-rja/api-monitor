# API Reliability Monitor — SLA Report

> Last updated: **2026-08-11 10:37 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **77.8%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 71.89% | 2950.3 | 10420.1 | 1000ms | 522/1857 |
| ❌ | `public_apis_list` | 0.0% | 99.62% | 132.1 | 5052.3 | 1500ms | 7/1857 |
| ❌ | `ipapi_check` | 63.17% | 99.95% | 147.8 | 4507.0 | 2500ms | 1/1857 |
| ❌ | `nasa_apod` | 77.06% | 53.15% | 3076.5 | 11152.5 | 2000ms | 870/1857 |
| ⚠️ | `dog_ceo_random` | 95.91% | 96.93% | 525.4 | 10244.1 | 2500ms | 57/1857 |
| ⚠️ | `open_meteo_weather` | 98.98% | 97.79% | 691.4 | 14877.1 | 2000ms | 41/1857 |
| ✅ | `rest_countries` | 99.19% | 98.87% | 287.8 | 10221.5 | 2500ms | 21/1857 |
| ✅ | `useless_fact` | 99.73% | 99.62% | 650.2 | 10229.6 | 2500ms | 7/1857 |
| ✅ | `coingecko_bitcoin` | 99.78% | 99.95% | 96.7 | 4328.4 | 1500ms | 1/1857 |
| ✅ | `catfact_random` | 99.84% | 99.46% | 257.0 | 10080.2 | 3000ms | 10/1857 |
| ✅ | `agify_name` | 99.89% | 99.73% | 391.7 | 16112.2 | 2000ms | 5/1857 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.89% | 195.8 | 3882.8 | 2000ms | 2/1857 |

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
| `nasa_apod` | 17:00 | 3726.4 | 50.0% |
| `nasa_apod` | 11:00 | 3673.0 | 51.49% |
| `numbers_trivia` | 14:00 | 3607.6 | 34.94% |
| `nasa_apod` | 12:00 | 3352.7 | 50.65% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
