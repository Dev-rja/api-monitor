# API Reliability Monitor — SLA Report

> Last updated: **2026-08-11 12:25 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **77.8%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 71.81% | 2957.9 | 10420.1 | 1000ms | 524/1859 |
| ❌ | `public_apis_list` | 0.0% | 99.62% | 132.1 | 5052.3 | 1500ms | 7/1859 |
| ❌ | `ipapi_check` | 63.1% | 99.95% | 147.8 | 4507.0 | 2500ms | 1/1859 |
| ❌ | `nasa_apod` | 77.03% | 53.09% | 3080.1 | 11152.5 | 2000ms | 872/1859 |
| ⚠️ | `dog_ceo_random` | 95.91% | 96.93% | 525.1 | 10244.1 | 2500ms | 57/1859 |
| ⚠️ | `open_meteo_weather` | 98.98% | 97.79% | 691.3 | 14877.1 | 2000ms | 41/1859 |
| ✅ | `rest_countries` | 99.19% | 98.87% | 287.7 | 10221.5 | 2500ms | 21/1859 |
| ✅ | `useless_fact` | 99.73% | 99.62% | 650.4 | 10229.6 | 2500ms | 7/1859 |
| ✅ | `coingecko_bitcoin` | 99.78% | 99.95% | 96.8 | 4328.4 | 1500ms | 1/1859 |
| ✅ | `catfact_random` | 99.84% | 99.46% | 257.0 | 10080.2 | 3000ms | 10/1859 |
| ✅ | `agify_name` | 99.89% | 99.73% | 392.0 | 16112.2 | 2000ms | 5/1859 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.89% | 195.8 | 3882.8 | 2000ms | 2/1859 |

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
| `numbers_trivia` | 14:00 | 3607.6 | 34.94% |
| `nasa_apod` | 12:00 | 3341.6 | 51.28% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
