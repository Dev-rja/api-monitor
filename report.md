# API Reliability Monitor — SLA Report

> Last updated: **2026-09-13 00:26 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **7/12** &nbsp;|&nbsp; Avg uptime: **76.9%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 71.05% | 3028.1 | 10420.1 | 1000ms | 728/2515 |
| ❌ | `public_apis_list` | 0.0% | 99.4% | 142.5 | 5075.4 | 1500ms | 15/2515 |
| ❌ | `ipapi_check` | 47.87% | 99.96% | 144.9 | 4507.0 | 2500ms | 1/2515 |
| ❌ | `nasa_apod` | 80.83% | 59.4% | 2666.3 | 11152.5 | 2000ms | 1021/2515 |
| ⚠️ | `dog_ceo_random` | 96.98% | 97.65% | 480.4 | 10244.1 | 2500ms | 59/2515 |
| ✅ | `open_meteo_weather` | 99.05% | 98.25% | 671.2 | 14877.1 | 2000ms | 44/2515 |
| ✅ | `rest_countries` | 99.4% | 99.13% | 268.0 | 10221.5 | 2500ms | 22/2515 |
| ✅ | `useless_fact` | 99.44% | 99.56% | 665.3 | 10229.6 | 2500ms | 11/2515 |
| ✅ | `catfact_random` | 99.8% | 99.48% | 261.9 | 10080.2 | 3000ms | 13/2515 |
| ✅ | `coingecko_bitcoin` | 99.84% | 99.92% | 96.6 | 4328.4 | 1500ms | 2/2515 |
| ✅ | `agify_name` | 99.92% | 99.52% | 402.9 | 16112.2 | 2000ms | 12/2515 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.88% | 183.7 | 3882.8 | 2000ms | 3/2515 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `numbers_trivia` | 03:00 | 4566.7 | 45.28% |
| `numbers_trivia` | 10:00 | 3684.4 | 35.05% |
| `numbers_trivia` | 02:00 | 3519.9 | 33.33% |
| `numbers_trivia` | 14:00 | 3421.8 | 33.04% |
| `numbers_trivia` | 00:00 | 3339.2 | 31.88% |
| `nasa_apod` | 03:00 | 3254.9 | 47.17% |
| `numbers_trivia` | 09:00 | 3246.5 | 31.19% |
| `nasa_apod` | 17:00 | 3235.8 | 40.46% |
| `numbers_trivia` | 17:00 | 3204.6 | 31.82% |
| `nasa_apod` | 12:00 | 3197.2 | 50.0% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
