# API Reliability Monitor — SLA Report

> Last updated: **2026-08-13 10:50 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **7/12** &nbsp;|&nbsp; Avg uptime: **77.7%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 70.34% | 3104.2 | 10420.1 | 1000ms | 563/1898 |
| ❌ | `public_apis_list` | 0.0% | 99.63% | 132.1 | 5052.3 | 1500ms | 7/1898 |
| ❌ | `ipapi_check` | 61.91% | 99.95% | 147.1 | 4507.0 | 2500ms | 1/1898 |
| ❌ | `nasa_apod` | 76.82% | 52.69% | 3109.5 | 11152.5 | 2000ms | 898/1898 |
| ⚠️ | `dog_ceo_random` | 96.0% | 97.0% | 521.4 | 10244.1 | 2500ms | 57/1898 |
| ✅ | `open_meteo_weather` | 99.0% | 97.84% | 689.3 | 14877.1 | 2000ms | 41/1898 |
| ✅ | `rest_countries` | 99.21% | 98.89% | 285.9 | 10221.5 | 2500ms | 21/1898 |
| ✅ | `useless_fact` | 99.74% | 99.63% | 650.5 | 10229.6 | 2500ms | 7/1898 |
| ✅ | `coingecko_bitcoin` | 99.79% | 99.95% | 96.7 | 4328.4 | 1500ms | 1/1898 |
| ✅ | `catfact_random` | 99.84% | 99.47% | 255.9 | 10080.2 | 3000ms | 10/1898 |
| ✅ | `agify_name` | 99.89% | 99.74% | 392.1 | 16112.2 | 2000ms | 5/1898 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.89% | 194.8 | 3882.8 | 2000ms | 2/1898 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `numbers_trivia` | 03:00 | 5004.5 | 50.0% |
| `nasa_apod` | 02:00 | 4888.7 | 72.73% |
| `nasa_apod` | 05:00 | 4561.4 | 63.04% |
| `numbers_trivia` | 10:00 | 4083.3 | 38.89% |
| `nasa_apod` | 03:00 | 4010.5 | 60.53% |
| `nasa_apod` | 11:00 | 3799.2 | 52.43% |
| `nasa_apod` | 09:00 | 3760.9 | 53.16% |
| `numbers_trivia` | 14:00 | 3759.0 | 36.47% |
| `nasa_apod` | 17:00 | 3758.1 | 50.0% |
| `numbers_trivia` | 05:00 | 3452.1 | 32.61% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
