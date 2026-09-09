# API Reliability Monitor — SLA Report

> Last updated: **2026-09-09 11:50 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **7/12** &nbsp;|&nbsp; Avg uptime: **77.0%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 70.74% | 3059.1 | 10420.1 | 1000ms | 728/2488 |
| ❌ | `public_apis_list` | 0.0% | 99.4% | 142.4 | 5075.4 | 1500ms | 15/2488 |
| ❌ | `ipapi_check` | 48.31% | 99.96% | 144.8 | 4507.0 | 2500ms | 1/2488 |
| ❌ | `nasa_apod` | 80.79% | 59.12% | 2684.2 | 11152.5 | 2000ms | 1017/2488 |
| ⚠️ | `dog_ceo_random` | 96.95% | 97.63% | 481.3 | 10244.1 | 2500ms | 59/2488 |
| ✅ | `open_meteo_weather` | 99.04% | 98.23% | 673.0 | 14877.1 | 2000ms | 44/2488 |
| ✅ | `rest_countries` | 99.4% | 99.12% | 267.9 | 10221.5 | 2500ms | 22/2488 |
| ✅ | `useless_fact` | 99.48% | 99.64% | 662.3 | 10229.6 | 2500ms | 9/2488 |
| ✅ | `catfact_random` | 99.8% | 99.48% | 261.9 | 10080.2 | 3000ms | 13/2488 |
| ✅ | `coingecko_bitcoin` | 99.84% | 99.92% | 96.4 | 4328.4 | 1500ms | 2/2488 |
| ✅ | `agify_name` | 99.92% | 99.52% | 403.0 | 16112.2 | 2000ms | 12/2488 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.88% | 184.0 | 3882.8 | 2000ms | 3/2488 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `numbers_trivia` | 03:00 | 4566.7 | 45.28% |
| `numbers_trivia` | 10:00 | 3720.9 | 35.42% |
| `numbers_trivia` | 02:00 | 3519.9 | 33.33% |
| `numbers_trivia` | 14:00 | 3451.0 | 33.33% |
| `numbers_trivia` | 00:00 | 3434.9 | 32.84% |
| `numbers_trivia` | 09:00 | 3274.8 | 31.48% |
| `nasa_apod` | 17:00 | 3258.5 | 40.77% |
| `nasa_apod` | 03:00 | 3254.9 | 47.17% |
| `numbers_trivia` | 17:00 | 3227.8 | 32.06% |
| `nasa_apod` | 12:00 | 3226.3 | 50.53% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
