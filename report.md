# API Reliability Monitor — SLA Report

> Last updated: **2026-08-12 13:50 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **77.7%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 71.01% | 3037.5 | 10420.1 | 1000ms | 545/1880 |
| ❌ | `public_apis_list` | 0.0% | 99.63% | 132.4 | 5052.3 | 1500ms | 7/1880 |
| ❌ | `ipapi_check` | 62.45% | 99.95% | 147.4 | 4507.0 | 2500ms | 1/1880 |
| ❌ | `nasa_apod` | 76.65% | 52.66% | 3123.5 | 11152.5 | 2000ms | 890/1880 |
| ⚠️ | `dog_ceo_random` | 95.96% | 96.97% | 523.4 | 10244.1 | 2500ms | 57/1880 |
| ⚠️ | `open_meteo_weather` | 98.99% | 97.82% | 690.4 | 14877.1 | 2000ms | 41/1880 |
| ✅ | `rest_countries` | 99.2% | 98.88% | 286.7 | 10221.5 | 2500ms | 21/1880 |
| ✅ | `useless_fact` | 99.73% | 99.63% | 650.3 | 10229.6 | 2500ms | 7/1880 |
| ✅ | `coingecko_bitcoin` | 99.79% | 99.95% | 96.6 | 4328.4 | 1500ms | 1/1880 |
| ✅ | `catfact_random` | 99.84% | 99.47% | 256.5 | 10080.2 | 3000ms | 10/1880 |
| ✅ | `agify_name` | 99.89% | 99.73% | 392.4 | 16112.2 | 2000ms | 5/1880 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.89% | 195.3 | 3882.8 | 2000ms | 2/1880 |

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
| `numbers_trivia` | 14:00 | 3684.0 | 35.71% |
| `nasa_apod` | 12:00 | 3428.2 | 51.9% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
