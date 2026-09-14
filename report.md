# API Reliability Monitor — SLA Report

> Last updated: **2026-09-14 01:43 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **7/12** &nbsp;|&nbsp; Avg uptime: **76.9%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 71.15% | 3019.0 | 10420.1 | 1000ms | 728/2523 |
| ❌ | `public_apis_list` | 0.0% | 99.41% | 142.7 | 5075.4 | 1500ms | 15/2523 |
| ❌ | `ipapi_check` | 47.72% | 99.96% | 144.9 | 4507.0 | 2500ms | 1/2523 |
| ❌ | `nasa_apod` | 80.9% | 59.53% | 2659.3 | 11152.5 | 2000ms | 1021/2523 |
| ⚠️ | `dog_ceo_random` | 96.99% | 97.66% | 480.1 | 10244.1 | 2500ms | 59/2523 |
| ✅ | `open_meteo_weather` | 99.05% | 98.26% | 670.4 | 14877.1 | 2000ms | 44/2523 |
| ✅ | `useless_fact` | 99.13% | 99.52% | 668.5 | 10229.6 | 2500ms | 12/2523 |
| ✅ | `rest_countries` | 99.41% | 99.13% | 267.7 | 10221.5 | 2500ms | 22/2523 |
| ✅ | `catfact_random` | 99.8% | 99.48% | 262.1 | 10080.2 | 3000ms | 13/2523 |
| ✅ | `coingecko_bitcoin` | 99.84% | 99.92% | 96.6 | 4328.4 | 1500ms | 2/2523 |
| ✅ | `agify_name` | 99.92% | 99.52% | 402.8 | 16112.2 | 2000ms | 12/2523 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.88% | 183.4 | 3882.8 | 2000ms | 3/2523 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `numbers_trivia` | 03:00 | 4566.7 | 45.28% |
| `numbers_trivia` | 10:00 | 3648.7 | 34.69% |
| `numbers_trivia` | 02:00 | 3519.9 | 33.33% |
| `numbers_trivia` | 14:00 | 3392.8 | 32.74% |
| `numbers_trivia` | 00:00 | 3339.2 | 31.88% |
| `nasa_apod` | 03:00 | 3254.9 | 47.17% |
| `numbers_trivia` | 09:00 | 3246.5 | 31.19% |
| `nasa_apod` | 17:00 | 3213.2 | 40.15% |
| `nasa_apod` | 12:00 | 3197.2 | 50.0% |
| `numbers_trivia` | 17:00 | 3182.1 | 31.58% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
