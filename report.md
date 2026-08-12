# API Reliability Monitor — SLA Report

> Last updated: **2026-08-12 09:21 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **77.7%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 71.16% | 3022.5 | 10420.1 | 1000ms | 541/1876 |
| ❌ | `public_apis_list` | 0.0% | 99.63% | 132.3 | 5052.3 | 1500ms | 7/1876 |
| ❌ | `ipapi_check` | 62.58% | 99.95% | 147.6 | 4507.0 | 2500ms | 1/1876 |
| ❌ | `nasa_apod` | 76.76% | 52.77% | 3108.9 | 11152.5 | 2000ms | 886/1876 |
| ⚠️ | `dog_ceo_random` | 95.95% | 96.96% | 523.6 | 10244.1 | 2500ms | 57/1876 |
| ⚠️ | `open_meteo_weather` | 98.99% | 97.81% | 690.3 | 14877.1 | 2000ms | 41/1876 |
| ✅ | `rest_countries` | 99.2% | 98.88% | 287.0 | 10221.5 | 2500ms | 21/1876 |
| ✅ | `useless_fact` | 99.73% | 99.63% | 650.1 | 10229.6 | 2500ms | 7/1876 |
| ✅ | `coingecko_bitcoin` | 99.79% | 99.95% | 96.7 | 4328.4 | 1500ms | 1/1876 |
| ✅ | `catfact_random` | 99.84% | 99.47% | 256.7 | 10080.2 | 3000ms | 10/1876 |
| ✅ | `agify_name` | 99.89% | 99.73% | 392.0 | 16112.2 | 2000ms | 5/1876 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.89% | 195.4 | 3882.8 | 2000ms | 2/1876 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `numbers_trivia` | 03:00 | 5004.5 | 50.0% |
| `nasa_apod` | 02:00 | 4888.7 | 72.73% |
| `nasa_apod` | 05:00 | 4607.9 | 62.22% |
| `nasa_apod` | 03:00 | 4010.5 | 60.53% |
| `numbers_trivia` | 10:00 | 3912.8 | 37.14% |
| `nasa_apod` | 17:00 | 3793.7 | 50.53% |
| `nasa_apod` | 09:00 | 3774.0 | 52.56% |
| `nasa_apod` | 11:00 | 3737.3 | 51.96% |
| `numbers_trivia` | 14:00 | 3684.0 | 35.71% |
| `nasa_apod` | 12:00 | 3341.6 | 51.28% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
