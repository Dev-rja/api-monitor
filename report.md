# API Reliability Monitor — SLA Report

> Last updated: **2026-09-25 20:36 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **7/12** &nbsp;|&nbsp; Avg uptime: **76.8%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 71.95% | 2939.8 | 10420.1 | 1000ms | 728/2595 |
| ❌ | `public_apis_list` | 0.0% | 99.42% | 142.5 | 5075.4 | 1500ms | 15/2595 |
| ❌ | `ipapi_check` | 46.44% | 99.96% | 144.7 | 4507.0 | 2500ms | 1/2595 |
| ❌ | `nasa_apod` | 81.19% | 60.0% | 2627.0 | 11152.5 | 2000ms | 1038/2595 |
| ⚠️ | `dog_ceo_random` | 97.07% | 97.73% | 477.9 | 10244.1 | 2500ms | 59/2595 |
| ✅ | `open_meteo_weather` | 99.04% | 98.27% | 670.4 | 14877.1 | 2000ms | 45/2595 |
| ✅ | `useless_fact` | 99.11% | 99.5% | 669.6 | 10229.6 | 2500ms | 13/2595 |
| ✅ | `rest_countries` | 99.42% | 99.15% | 268.3 | 10221.5 | 2500ms | 22/2595 |
| ✅ | `catfact_random` | 99.81% | 99.5% | 262.6 | 10080.2 | 3000ms | 13/2595 |
| ✅ | `coingecko_bitcoin` | 99.85% | 99.92% | 96.7 | 4328.4 | 1500ms | 2/2595 |
| ✅ | `agify_name` | 99.92% | 99.54% | 402.7 | 16112.2 | 2000ms | 12/2595 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.88% | 182.6 | 3882.8 | 2000ms | 3/2595 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `numbers_trivia` | 03:00 | 4566.7 | 45.28% |
| `numbers_trivia` | 10:00 | 3544.5 | 33.66% |
| `numbers_trivia` | 02:00 | 3519.9 | 33.33% |
| `numbers_trivia` | 14:00 | 3255.8 | 31.36% |
| `nasa_apod` | 03:00 | 3254.9 | 47.17% |
| `numbers_trivia` | 09:00 | 3165.1 | 30.36% |
| `numbers_trivia` | 00:00 | 3126.9 | 29.73% |
| `nasa_apod` | 11:00 | 3115.1 | 43.38% |
| `nasa_apod` | 17:00 | 3111.5 | 38.69% |
| `nasa_apod` | 12:00 | 3089.2 | 48.0% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
