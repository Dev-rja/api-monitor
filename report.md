# API Reliability Monitor — SLA Report

> Last updated: **2026-09-24 12:05 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **7/12** &nbsp;|&nbsp; Avg uptime: **76.8%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 71.86% | 2948.4 | 10420.1 | 1000ms | 728/2587 |
| ❌ | `public_apis_list` | 0.0% | 99.42% | 142.6 | 5075.4 | 1500ms | 15/2587 |
| ❌ | `ipapi_check` | 46.58% | 99.96% | 144.7 | 4507.0 | 2500ms | 1/2587 |
| ❌ | `nasa_apod` | 81.18% | 59.91% | 2633.0 | 11152.5 | 2000ms | 1037/2587 |
| ⚠️ | `dog_ceo_random` | 97.06% | 97.72% | 478.0 | 10244.1 | 2500ms | 59/2587 |
| ✅ | `open_meteo_weather` | 99.03% | 98.26% | 671.1 | 14877.1 | 2000ms | 45/2587 |
| ✅ | `useless_fact` | 99.11% | 99.54% | 668.5 | 10229.6 | 2500ms | 12/2587 |
| ✅ | `rest_countries` | 99.42% | 99.15% | 267.7 | 10221.5 | 2500ms | 22/2587 |
| ✅ | `catfact_random` | 99.81% | 99.5% | 262.8 | 10080.2 | 3000ms | 13/2587 |
| ✅ | `coingecko_bitcoin` | 99.85% | 99.92% | 96.8 | 4328.4 | 1500ms | 2/2587 |
| ✅ | `agify_name` | 99.92% | 99.54% | 402.9 | 16112.2 | 2000ms | 12/2587 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.88% | 182.4 | 3882.8 | 2000ms | 3/2587 |

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
| `nasa_apod` | 17:00 | 3152.7 | 39.26% |
| `numbers_trivia` | 00:00 | 3126.9 | 29.73% |
| `nasa_apod` | 11:00 | 3115.1 | 43.38% |
| `nasa_apod` | 12:00 | 3115.1 | 48.48% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
