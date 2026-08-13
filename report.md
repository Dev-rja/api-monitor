# API Reliability Monitor — SLA Report

> Last updated: **2026-08-13 05:52 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **7/12** &nbsp;|&nbsp; Avg uptime: **77.7%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 70.49% | 3089.5 | 10420.1 | 1000ms | 559/1894 |
| ❌ | `public_apis_list` | 0.0% | 99.63% | 132.0 | 5052.3 | 1500ms | 7/1894 |
| ❌ | `ipapi_check` | 62.04% | 99.95% | 147.3 | 4507.0 | 2500ms | 1/1894 |
| ❌ | `nasa_apod` | 76.77% | 52.69% | 3112.5 | 11152.5 | 2000ms | 896/1894 |
| ⚠️ | `dog_ceo_random` | 95.99% | 96.99% | 521.8 | 10244.1 | 2500ms | 57/1894 |
| ✅ | `open_meteo_weather` | 99.0% | 97.84% | 689.6 | 14877.1 | 2000ms | 41/1894 |
| ✅ | `rest_countries` | 99.21% | 98.89% | 286.2 | 10221.5 | 2500ms | 21/1894 |
| ✅ | `useless_fact` | 99.74% | 99.63% | 650.4 | 10229.6 | 2500ms | 7/1894 |
| ✅ | `coingecko_bitcoin` | 99.79% | 99.95% | 96.7 | 4328.4 | 1500ms | 1/1894 |
| ✅ | `catfact_random` | 99.84% | 99.47% | 256.2 | 10080.2 | 3000ms | 10/1894 |
| ✅ | `agify_name` | 99.89% | 99.74% | 392.2 | 16112.2 | 2000ms | 5/1894 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.89% | 195.0 | 3882.8 | 2000ms | 2/1894 |

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
| `nasa_apod` | 09:00 | 3774.0 | 52.56% |
| `numbers_trivia` | 14:00 | 3759.0 | 36.47% |
| `nasa_apod` | 17:00 | 3758.1 | 50.0% |
| `numbers_trivia` | 05:00 | 3452.1 | 32.61% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
