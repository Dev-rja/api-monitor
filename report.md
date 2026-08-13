# API Reliability Monitor — SLA Report

> Last updated: **2026-08-13 19:25 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **7/12** &nbsp;|&nbsp; Avg uptime: **77.7%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 70.04% | 3133.5 | 10420.1 | 1000ms | 571/1906 |
| ❌ | `public_apis_list` | 0.0% | 99.63% | 132.2 | 5052.3 | 1500ms | 7/1906 |
| ❌ | `ipapi_check` | 61.7% | 99.95% | 147.0 | 4507.0 | 2500ms | 1/1906 |
| ❌ | `nasa_apod` | 76.86% | 52.78% | 3104.2 | 11152.5 | 2000ms | 900/1906 |
| ⚠️ | `dog_ceo_random` | 96.01% | 97.01% | 520.7 | 10244.1 | 2500ms | 57/1906 |
| ✅ | `open_meteo_weather` | 99.0% | 97.85% | 689.2 | 14877.1 | 2000ms | 41/1906 |
| ✅ | `rest_countries` | 99.21% | 98.9% | 285.5 | 10221.5 | 2500ms | 21/1906 |
| ✅ | `useless_fact` | 99.74% | 99.63% | 650.8 | 10229.6 | 2500ms | 7/1906 |
| ✅ | `coingecko_bitcoin` | 99.79% | 99.95% | 96.6 | 4328.4 | 1500ms | 1/1906 |
| ✅ | `catfact_random` | 99.84% | 99.48% | 255.6 | 10080.2 | 3000ms | 10/1906 |
| ✅ | `agify_name` | 99.9% | 99.74% | 392.3 | 16112.2 | 2000ms | 5/1906 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.9% | 194.5 | 3882.8 | 2000ms | 2/1906 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `numbers_trivia` | 03:00 | 5004.5 | 50.0% |
| `nasa_apod` | 02:00 | 4888.7 | 72.73% |
| `nasa_apod` | 05:00 | 4561.4 | 63.04% |
| `numbers_trivia` | 10:00 | 4083.3 | 38.89% |
| `nasa_apod` | 03:00 | 4010.5 | 60.53% |
| `numbers_trivia` | 14:00 | 3833.3 | 37.21% |
| `nasa_apod` | 11:00 | 3765.4 | 51.92% |
| `nasa_apod` | 09:00 | 3760.9 | 53.16% |
| `nasa_apod` | 17:00 | 3722.4 | 49.48% |
| `numbers_trivia` | 05:00 | 3452.1 | 32.61% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
