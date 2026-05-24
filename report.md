# API Reliability Monitor — SLA Report

> Last updated: **2026-05-24 04:39 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **79.5%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 69.84% | 3202.9 | 10206.7 | 1000ms | 266/882 |
| ❌ | `public_apis_list` | 0.0% | 99.55% | 128.7 | 4595.4 | 1500ms | 4/882 |
| ❌ | `nasa_apod` | 78.12% | 58.5% | 2857.0 | 10549.1 | 2000ms | 366/882 |
| ❌ | `ipapi_check` | 80.05% | 100.0% | 153.9 | 431.8 | 2500ms | 0/882 |
| ⚠️ | `rest_countries` | 98.75% | 98.3% | 344.4 | 10221.5 | 2500ms | 15/882 |
| ⚠️ | `open_meteo_weather` | 98.98% | 97.17% | 697.5 | 14877.1 | 2000ms | 25/882 |
| ✅ | `dog_ceo_random` | 99.43% | 95.24% | 613.6 | 10244.1 | 2500ms | 42/882 |
| ✅ | `catfact_random` | 99.66% | 99.21% | 267.2 | 10080.2 | 3000ms | 7/882 |
| ✅ | `coingecko_bitcoin` | 99.66% | 100.0% | 97.9 | 253.3 | 1500ms | 0/882 |
| ✅ | `useless_fact` | 99.77% | 99.55% | 615.0 | 10229.6 | 2500ms | 4/882 |
| ✅ | `agify_name` | 99.89% | 99.66% | 387.3 | 16112.2 | 2000ms | 3/882 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.77% | 229.6 | 3882.8 | 2000ms | 2/882 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `nasa_apod` | 03:00 | 4729.0 | 77.78% |
| `numbers_trivia` | 03:00 | 4635.3 | 44.44% |
| `numbers_trivia` | 07:00 | 3915.1 | 37.04% |
| `numbers_trivia` | 05:00 | 3808.4 | 36.0% |
| `nasa_apod` | 17:00 | 3778.9 | 48.0% |
| `nasa_apod` | 11:00 | 3745.5 | 47.06% |
| `numbers_trivia` | 12:00 | 3742.4 | 35.14% |
| `numbers_trivia` | 14:00 | 3674.8 | 36.36% |
| `numbers_trivia` | 10:00 | 3642.8 | 34.29% |
| `nasa_apod` | 05:00 | 3555.0 | 60.0% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
