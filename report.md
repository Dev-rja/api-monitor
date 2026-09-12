# API Reliability Monitor — SLA Report

> Last updated: **2026-09-12 09:22 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **7/12** &nbsp;|&nbsp; Avg uptime: **76.9%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 70.98% | 3035.0 | 10420.1 | 1000ms | 728/2509 |
| ❌ | `public_apis_list` | 0.0% | 99.4% | 142.4 | 5075.4 | 1500ms | 15/2509 |
| ❌ | `ipapi_check` | 47.99% | 99.96% | 144.9 | 4507.0 | 2500ms | 1/2509 |
| ❌ | `nasa_apod` | 80.79% | 59.35% | 2670.6 | 11152.5 | 2000ms | 1020/2509 |
| ⚠️ | `dog_ceo_random` | 96.97% | 97.65% | 480.6 | 10244.1 | 2500ms | 59/2509 |
| ✅ | `open_meteo_weather` | 99.04% | 98.25% | 671.4 | 14877.1 | 2000ms | 44/2509 |
| ✅ | `rest_countries` | 99.4% | 99.12% | 268.1 | 10221.5 | 2500ms | 22/2509 |
| ✅ | `useless_fact` | 99.48% | 99.6% | 663.8 | 10229.6 | 2500ms | 10/2509 |
| ✅ | `catfact_random` | 99.8% | 99.48% | 262.0 | 10080.2 | 3000ms | 13/2509 |
| ✅ | `coingecko_bitcoin` | 99.84% | 99.92% | 96.6 | 4328.4 | 1500ms | 2/2509 |
| ✅ | `agify_name` | 99.92% | 99.52% | 402.9 | 16112.2 | 2000ms | 12/2509 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.88% | 183.8 | 3882.8 | 2000ms | 3/2509 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `numbers_trivia` | 03:00 | 4566.7 | 45.28% |
| `numbers_trivia` | 10:00 | 3684.4 | 35.05% |
| `numbers_trivia` | 02:00 | 3519.9 | 33.33% |
| `numbers_trivia` | 14:00 | 3421.8 | 33.04% |
| `numbers_trivia` | 00:00 | 3385.7 | 32.35% |
| `nasa_apod` | 03:00 | 3254.9 | 47.17% |
| `numbers_trivia` | 09:00 | 3246.5 | 31.19% |
| `nasa_apod` | 17:00 | 3235.8 | 40.46% |
| `nasa_apod` | 12:00 | 3226.3 | 50.53% |
| `numbers_trivia` | 17:00 | 3204.6 | 31.82% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
