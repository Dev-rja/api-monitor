# API Reliability Monitor — SLA Report

> Last updated: **2026-08-22 05:13 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **77.2%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 67.37% | 3393.4 | 10420.1 | 1000ms | 728/2231 |
| ❌ | `public_apis_list` | 0.0% | 99.55% | 136.6 | 5075.4 | 1500ms | 10/2231 |
| ❌ | `ipapi_check` | 53.29% | 99.96% | 145.0 | 4507.0 | 2500ms | 1/2231 |
| ❌ | `nasa_apod` | 79.43% | 56.66% | 2832.3 | 11152.5 | 2000ms | 967/2231 |
| ⚠️ | `dog_ceo_random` | 96.59% | 97.4% | 491.2 | 10244.1 | 2500ms | 58/2231 |
| ⚠️ | `open_meteo_weather` | 98.97% | 98.07% | 681.8 | 14877.1 | 2000ms | 43/2231 |
| ✅ | `rest_countries` | 99.33% | 99.06% | 272.0 | 10221.5 | 2500ms | 21/2231 |
| ✅ | `useless_fact` | 99.78% | 99.69% | 652.4 | 10229.6 | 2500ms | 7/2231 |
| ✅ | `catfact_random` | 99.78% | 99.42% | 262.8 | 10080.2 | 3000ms | 13/2231 |
| ✅ | `coingecko_bitcoin` | 99.82% | 99.91% | 96.5 | 4328.4 | 1500ms | 2/2231 |
| ✅ | `agify_name` | 99.91% | 99.69% | 396.3 | 16112.2 | 2000ms | 7/2231 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.91% | 187.1 | 3882.8 | 2000ms | 2/2231 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `numbers_trivia` | 03:00 | 5024.8 | 50.0% |
| `numbers_trivia` | 02:00 | 4199.6 | 40.0% |
| `numbers_trivia` | 10:00 | 4179.5 | 40.0% |
| `numbers_trivia` | 14:00 | 3852.3 | 37.37% |
| `numbers_trivia` | 09:00 | 3742.1 | 36.17% |
| `numbers_trivia` | 00:00 | 3701.8 | 35.48% |
| `numbers_trivia` | 17:00 | 3655.0 | 36.52% |
| `nasa_apod` | 05:00 | 3611.5 | 51.61% |
| `numbers_trivia` | 05:00 | 3606.9 | 35.48% |
| `nasa_apod` | 09:00 | 3548.8 | 49.46% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
