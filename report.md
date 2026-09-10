# API Reliability Monitor — SLA Report

> Last updated: **2026-09-10 11:13 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **7/12** &nbsp;|&nbsp; Avg uptime: **77.0%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 70.82% | 3051.1 | 10420.1 | 1000ms | 728/2495 |
| ❌ | `public_apis_list` | 0.0% | 99.4% | 142.4 | 5075.4 | 1500ms | 15/2495 |
| ❌ | `ipapi_check` | 48.22% | 99.96% | 145.0 | 4507.0 | 2500ms | 1/2495 |
| ❌ | `nasa_apod` | 80.84% | 59.24% | 2677.5 | 11152.5 | 2000ms | 1017/2495 |
| ⚠️ | `dog_ceo_random` | 96.95% | 97.64% | 481.2 | 10244.1 | 2500ms | 59/2495 |
| ✅ | `open_meteo_weather` | 99.04% | 98.24% | 672.8 | 14877.1 | 2000ms | 44/2495 |
| ✅ | `rest_countries` | 99.4% | 99.12% | 268.3 | 10221.5 | 2500ms | 22/2495 |
| ✅ | `useless_fact` | 99.48% | 99.6% | 663.4 | 10229.6 | 2500ms | 10/2495 |
| ✅ | `catfact_random` | 99.8% | 99.48% | 262.2 | 10080.2 | 3000ms | 13/2495 |
| ✅ | `coingecko_bitcoin` | 99.84% | 99.92% | 96.5 | 4328.4 | 1500ms | 2/2495 |
| ✅ | `agify_name` | 99.92% | 99.52% | 403.1 | 16112.2 | 2000ms | 12/2495 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.88% | 184.1 | 3882.8 | 2000ms | 3/2495 |

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
