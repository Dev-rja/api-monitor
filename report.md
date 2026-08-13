# API Reliability Monitor — SLA Report

> Last updated: **2026-08-13 09:50 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **7/12** &nbsp;|&nbsp; Avg uptime: **77.7%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 70.37% | 3100.5 | 10420.1 | 1000ms | 562/1897 |
| ❌ | `public_apis_list` | 0.0% | 99.63% | 132.0 | 5052.3 | 1500ms | 7/1897 |
| ❌ | `ipapi_check` | 61.94% | 99.95% | 147.2 | 4507.0 | 2500ms | 1/1897 |
| ❌ | `nasa_apod` | 76.81% | 52.66% | 3111.0 | 11152.5 | 2000ms | 898/1897 |
| ⚠️ | `dog_ceo_random` | 95.99% | 97.0% | 521.4 | 10244.1 | 2500ms | 57/1897 |
| ✅ | `open_meteo_weather` | 99.0% | 97.84% | 689.3 | 14877.1 | 2000ms | 41/1897 |
| ✅ | `rest_countries` | 99.21% | 98.89% | 285.9 | 10221.5 | 2500ms | 21/1897 |
| ✅ | `useless_fact` | 99.74% | 99.63% | 650.4 | 10229.6 | 2500ms | 7/1897 |
| ✅ | `coingecko_bitcoin` | 99.79% | 99.95% | 96.7 | 4328.4 | 1500ms | 1/1897 |
| ✅ | `catfact_random` | 99.84% | 99.47% | 256.0 | 10080.2 | 3000ms | 10/1897 |
| ✅ | `agify_name` | 99.89% | 99.74% | 392.0 | 16112.2 | 2000ms | 5/1897 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.89% | 194.8 | 3882.8 | 2000ms | 2/1897 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `numbers_trivia` | 03:00 | 5004.5 | 50.0% |
| `nasa_apod` | 02:00 | 4888.7 | 72.73% |
| `nasa_apod` | 05:00 | 4561.4 | 63.04% |
| `nasa_apod` | 03:00 | 4010.5 | 60.53% |
| `numbers_trivia` | 10:00 | 3999.2 | 38.03% |
| `nasa_apod` | 11:00 | 3799.2 | 52.43% |
| `nasa_apod` | 09:00 | 3760.9 | 53.16% |
| `numbers_trivia` | 14:00 | 3759.0 | 36.47% |
| `nasa_apod` | 17:00 | 3758.1 | 50.0% |
| `numbers_trivia` | 05:00 | 3452.1 | 32.61% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
