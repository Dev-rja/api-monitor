# API Reliability Monitor — SLA Report

> Last updated: **2026-08-12 21:23 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **77.7%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 70.71% | 3067.3 | 10420.1 | 1000ms | 553/1888 |
| ❌ | `public_apis_list` | 0.0% | 99.63% | 132.1 | 5052.3 | 1500ms | 7/1888 |
| ❌ | `ipapi_check` | 62.24% | 99.95% | 147.2 | 4507.0 | 2500ms | 1/1888 |
| ❌ | `nasa_apod` | 76.75% | 52.75% | 3116.5 | 11152.5 | 2000ms | 892/1888 |
| ⚠️ | `dog_ceo_random` | 95.97% | 96.98% | 522.5 | 10244.1 | 2500ms | 57/1888 |
| ⚠️ | `open_meteo_weather` | 98.99% | 97.83% | 690.0 | 14877.1 | 2000ms | 41/1888 |
| ✅ | `rest_countries` | 99.21% | 98.89% | 286.3 | 10221.5 | 2500ms | 21/1888 |
| ✅ | `useless_fact` | 99.74% | 99.63% | 650.2 | 10229.6 | 2500ms | 7/1888 |
| ✅ | `coingecko_bitcoin` | 99.79% | 99.95% | 96.7 | 4328.4 | 1500ms | 1/1888 |
| ✅ | `catfact_random` | 99.84% | 99.47% | 256.2 | 10080.2 | 3000ms | 10/1888 |
| ✅ | `agify_name` | 99.89% | 99.74% | 392.4 | 16112.2 | 2000ms | 5/1888 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.89% | 195.1 | 3882.8 | 2000ms | 2/1888 |

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
| `nasa_apod` | 09:00 | 3774.0 | 52.56% |
| `numbers_trivia` | 14:00 | 3759.0 | 36.47% |
| `nasa_apod` | 17:00 | 3758.1 | 50.0% |
| `nasa_apod` | 12:00 | 3428.2 | 51.9% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
