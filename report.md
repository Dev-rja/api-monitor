# API Reliability Monitor — SLA Report

> Last updated: **2026-09-27 00:30 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **7/12** &nbsp;|&nbsp; Avg uptime: **76.8%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 72.03% | 2931.2 | 10420.1 | 1000ms | 728/2603 |
| ❌ | `public_apis_list` | 0.0% | 99.42% | 142.5 | 5075.4 | 1500ms | 15/2603 |
| ❌ | `ipapi_check` | 46.33% | 99.96% | 144.6 | 4507.0 | 2500ms | 1/2603 |
| ❌ | `nasa_apod` | 81.25% | 60.08% | 2621.0 | 11152.5 | 2000ms | 1039/2603 |
| ⚠️ | `dog_ceo_random` | 97.08% | 97.73% | 477.6 | 10244.1 | 2500ms | 59/2603 |
| ✅ | `open_meteo_weather` | 99.04% | 98.27% | 669.6 | 14877.1 | 2000ms | 45/2603 |
| ✅ | `useless_fact` | 99.12% | 99.5% | 669.3 | 10229.6 | 2500ms | 13/2603 |
| ✅ | `rest_countries` | 99.42% | 99.15% | 268.0 | 10221.5 | 2500ms | 22/2603 |
| ✅ | `catfact_random` | 99.81% | 99.5% | 262.7 | 10080.2 | 3000ms | 13/2603 |
| ✅ | `coingecko_bitcoin` | 99.85% | 99.92% | 96.7 | 4328.4 | 1500ms | 2/2603 |
| ✅ | `agify_name` | 99.92% | 99.54% | 402.6 | 16112.2 | 2000ms | 12/2603 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.88% | 182.3 | 3882.8 | 2000ms | 3/2603 |

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
| `nasa_apod` | 11:00 | 3115.1 | 43.38% |
| `nasa_apod` | 17:00 | 3111.5 | 38.69% |
| `numbers_trivia` | 00:00 | 3086.1 | 29.33% |
| `nasa_apod` | 12:00 | 3083.5 | 48.51% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
