# API Reliability Monitor — SLA Report

> Last updated: **2026-05-31 21:42 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **79.2%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 72.46% | 2943.1 | 10206.7 | 1000ms | 266/966 |
| ❌ | `public_apis_list` | 0.0% | 99.59% | 126.2 | 4595.4 | 1500ms | 4/966 |
| ❌ | `ipapi_check` | 76.29% | 100.0% | 152.5 | 431.8 | 2500ms | 0/966 |
| ❌ | `nasa_apod` | 78.67% | 58.18% | 2822.0 | 10549.1 | 2000ms | 404/966 |
| ⚠️ | `rest_countries` | 98.45% | 98.14% | 362.7 | 10221.5 | 2500ms | 18/966 |
| ⚠️ | `open_meteo_weather` | 98.96% | 96.89% | 707.0 | 14877.1 | 2000ms | 30/966 |
| ✅ | `dog_ceo_random` | 99.48% | 95.65% | 588.7 | 10244.1 | 2500ms | 42/966 |
| ✅ | `catfact_random` | 99.69% | 99.17% | 267.0 | 10080.2 | 3000ms | 8/966 |
| ✅ | `coingecko_bitcoin` | 99.69% | 100.0% | 97.1 | 253.3 | 1500ms | 0/966 |
| ✅ | `useless_fact` | 99.79% | 99.59% | 619.8 | 10229.6 | 2500ms | 4/966 |
| ✅ | `agify_name` | 99.9% | 99.69% | 382.3 | 16112.2 | 2000ms | 3/966 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.79% | 224.4 | 3882.8 | 2000ms | 2/966 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `nasa_apod` | 03:00 | 4611.9 | 78.95% |
| `numbers_trivia` | 03:00 | 4408.7 | 42.11% |
| `nasa_apod` | 17:00 | 3845.3 | 50.0% |
| `nasa_apod` | 11:00 | 3729.1 | 47.27% |
| `numbers_trivia` | 05:00 | 3674.1 | 34.62% |
| `numbers_trivia` | 07:00 | 3664.8 | 34.48% |
| `nasa_apod` | 09:00 | 3526.1 | 47.73% |
| `nasa_apod` | 05:00 | 3511.6 | 61.54% |
| `numbers_trivia` | 10:00 | 3454.8 | 32.43% |
| `numbers_trivia` | 12:00 | 3322.4 | 30.95% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
