# API Reliability Monitor — SLA Report

> Last updated: **2026-09-13 21:48 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **7/12** &nbsp;|&nbsp; Avg uptime: **76.9%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 71.12% | 3021.3 | 10420.1 | 1000ms | 728/2521 |
| ❌ | `public_apis_list` | 0.0% | 99.4% | 142.7 | 5075.4 | 1500ms | 15/2521 |
| ❌ | `ipapi_check` | 47.76% | 99.96% | 144.9 | 4507.0 | 2500ms | 1/2521 |
| ❌ | `nasa_apod` | 80.88% | 59.5% | 2661.0 | 11152.5 | 2000ms | 1021/2521 |
| ⚠️ | `dog_ceo_random` | 96.99% | 97.66% | 480.1 | 10244.1 | 2500ms | 59/2521 |
| ✅ | `open_meteo_weather` | 99.05% | 98.25% | 670.7 | 14877.1 | 2000ms | 44/2521 |
| ✅ | `useless_fact` | 99.21% | 99.56% | 665.9 | 10229.6 | 2500ms | 11/2521 |
| ✅ | `rest_countries` | 99.4% | 99.13% | 267.7 | 10221.5 | 2500ms | 22/2521 |
| ✅ | `catfact_random` | 99.8% | 99.48% | 262.2 | 10080.2 | 3000ms | 13/2521 |
| ✅ | `coingecko_bitcoin` | 99.84% | 99.92% | 96.6 | 4328.4 | 1500ms | 2/2521 |
| ✅ | `agify_name` | 99.92% | 99.52% | 402.9 | 16112.2 | 2000ms | 12/2521 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.88% | 183.5 | 3882.8 | 2000ms | 3/2521 |

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
