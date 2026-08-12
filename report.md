# API Reliability Monitor — SLA Report

> Last updated: **2026-08-12 14:49 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **77.7%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 70.97% | 3041.2 | 10420.1 | 1000ms | 546/1881 |
| ❌ | `public_apis_list` | 0.0% | 99.63% | 132.4 | 5052.3 | 1500ms | 7/1881 |
| ❌ | `ipapi_check` | 62.41% | 99.95% | 147.4 | 4507.0 | 2500ms | 1/1881 |
| ❌ | `nasa_apod` | 76.66% | 52.68% | 3122.0 | 11152.5 | 2000ms | 890/1881 |
| ⚠️ | `dog_ceo_random` | 95.96% | 96.97% | 523.3 | 10244.1 | 2500ms | 57/1881 |
| ⚠️ | `open_meteo_weather` | 98.99% | 97.82% | 690.3 | 14877.1 | 2000ms | 41/1881 |
| ✅ | `rest_countries` | 99.2% | 98.88% | 286.6 | 10221.5 | 2500ms | 21/1881 |
| ✅ | `useless_fact` | 99.73% | 99.63% | 650.3 | 10229.6 | 2500ms | 7/1881 |
| ✅ | `coingecko_bitcoin` | 99.79% | 99.95% | 96.7 | 4328.4 | 1500ms | 1/1881 |
| ✅ | `catfact_random` | 99.84% | 99.47% | 256.5 | 10080.2 | 3000ms | 10/1881 |
| ✅ | `agify_name` | 99.89% | 99.73% | 392.5 | 16112.2 | 2000ms | 5/1881 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.89% | 195.3 | 3882.8 | 2000ms | 2/1881 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `numbers_trivia` | 03:00 | 5004.5 | 50.0% |
| `nasa_apod` | 02:00 | 4888.7 | 72.73% |
| `nasa_apod` | 05:00 | 4607.9 | 62.22% |
| `nasa_apod` | 03:00 | 4010.5 | 60.53% |
| `numbers_trivia` | 10:00 | 3999.2 | 38.03% |
| `nasa_apod` | 11:00 | 3799.2 | 52.43% |
| `nasa_apod` | 17:00 | 3793.7 | 50.53% |
| `nasa_apod` | 09:00 | 3774.0 | 52.56% |
| `numbers_trivia` | 14:00 | 3759.0 | 36.47% |
| `nasa_apod` | 12:00 | 3428.2 | 51.9% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
