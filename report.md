# API Reliability Monitor — SLA Report

> Last updated: **2026-09-28 05:58 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **7/12** &nbsp;|&nbsp; Avg uptime: **76.8%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 72.11% | 2923.7 | 10420.1 | 1000ms | 728/2610 |
| ❌ | `public_apis_list` | 0.0% | 99.43% | 142.6 | 5075.4 | 1500ms | 15/2610 |
| ❌ | `ipapi_check` | 46.21% | 99.96% | 144.6 | 4507.0 | 2500ms | 1/2610 |
| ❌ | `nasa_apod` | 81.3% | 60.11% | 2616.7 | 11152.5 | 2000ms | 1041/2610 |
| ⚠️ | `dog_ceo_random` | 97.09% | 97.74% | 477.3 | 10244.1 | 2500ms | 59/2610 |
| ✅ | `open_meteo_weather` | 99.04% | 98.28% | 669.2 | 14877.1 | 2000ms | 45/2610 |
| ✅ | `useless_fact` | 99.12% | 99.5% | 668.9 | 10229.6 | 2500ms | 13/2610 |
| ✅ | `rest_countries` | 99.43% | 99.16% | 267.9 | 10221.5 | 2500ms | 22/2610 |
| ✅ | `catfact_random` | 99.81% | 99.5% | 262.4 | 10080.2 | 3000ms | 13/2610 |
| ✅ | `coingecko_bitcoin` | 99.85% | 99.92% | 96.7 | 4328.4 | 1500ms | 2/2610 |
| ✅ | `agify_name` | 99.92% | 99.54% | 402.5 | 16112.2 | 2000ms | 12/2610 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.89% | 182.1 | 3882.8 | 2000ms | 3/2610 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `numbers_trivia` | 03:00 | 4566.7 | 45.28% |
| `numbers_trivia` | 02:00 | 3519.9 | 33.33% |
| `numbers_trivia` | 10:00 | 3511.2 | 33.33% |
| `numbers_trivia` | 14:00 | 3255.8 | 31.36% |
| `nasa_apod` | 03:00 | 3254.9 | 47.17% |
| `numbers_trivia` | 09:00 | 3165.1 | 30.36% |
| `nasa_apod` | 11:00 | 3115.1 | 43.38% |
| `nasa_apod` | 17:00 | 3111.5 | 38.69% |
| `nasa_apod` | 12:00 | 3083.5 | 48.51% |
| `nasa_apod` | 09:00 | 3076.2 | 43.24% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
