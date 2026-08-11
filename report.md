# API Reliability Monitor — SLA Report

> Last updated: **2026-08-11 21:59 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **77.7%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 71.47% | 2992.3 | 10420.1 | 1000ms | 533/1868 |
| ❌ | `public_apis_list` | 0.0% | 99.63% | 132.4 | 5052.3 | 1500ms | 7/1868 |
| ❌ | `ipapi_check` | 62.79% | 99.95% | 147.7 | 4507.0 | 2500ms | 1/1868 |
| ❌ | `nasa_apod` | 76.82% | 52.89% | 3101.0 | 11152.5 | 2000ms | 880/1868 |
| ⚠️ | `dog_ceo_random` | 95.93% | 96.95% | 524.5 | 10244.1 | 2500ms | 57/1868 |
| ⚠️ | `open_meteo_weather` | 98.98% | 97.81% | 690.7 | 14877.1 | 2000ms | 41/1868 |
| ✅ | `rest_countries` | 99.2% | 98.88% | 287.3 | 10221.5 | 2500ms | 21/1868 |
| ✅ | `useless_fact` | 99.73% | 99.63% | 650.3 | 10229.6 | 2500ms | 7/1868 |
| ✅ | `coingecko_bitcoin` | 99.79% | 99.95% | 96.8 | 4328.4 | 1500ms | 1/1868 |
| ✅ | `catfact_random` | 99.84% | 99.46% | 257.0 | 10080.2 | 3000ms | 10/1868 |
| ✅ | `agify_name` | 99.89% | 99.73% | 392.1 | 16112.2 | 2000ms | 5/1868 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.89% | 195.6 | 3882.8 | 2000ms | 2/1868 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `nasa_apod` | 02:00 | 4888.7 | 72.73% |
| `numbers_trivia` | 03:00 | 4867.8 | 48.65% |
| `nasa_apod` | 05:00 | 4478.0 | 61.36% |
| `nasa_apod` | 03:00 | 4105.3 | 62.16% |
| `numbers_trivia` | 10:00 | 3912.8 | 37.14% |
| `nasa_apod` | 17:00 | 3793.7 | 50.53% |
| `nasa_apod` | 09:00 | 3789.3 | 51.95% |
| `nasa_apod` | 11:00 | 3737.3 | 51.96% |
| `numbers_trivia` | 14:00 | 3684.0 | 35.71% |
| `nasa_apod` | 12:00 | 3341.6 | 51.28% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
