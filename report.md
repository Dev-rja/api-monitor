# API Reliability Monitor — SLA Report

> Last updated: **2026-05-23 22:02 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **79.5%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 69.74% | 3213.1 | 10206.7 | 1000ms | 266/879 |
| ❌ | `public_apis_list` | 0.0% | 99.54% | 128.9 | 4595.4 | 1500ms | 4/879 |
| ❌ | `nasa_apod` | 78.04% | 58.48% | 2863.0 | 10549.1 | 2000ms | 365/879 |
| ❌ | `ipapi_check` | 80.2% | 100.0% | 153.9 | 431.8 | 2500ms | 0/879 |
| ⚠️ | `rest_countries` | 98.75% | 98.29% | 344.8 | 10221.5 | 2500ms | 15/879 |
| ⚠️ | `open_meteo_weather` | 98.98% | 97.16% | 697.9 | 14877.1 | 2000ms | 25/879 |
| ✅ | `dog_ceo_random` | 99.43% | 95.22% | 614.7 | 10244.1 | 2500ms | 42/879 |
| ✅ | `catfact_random` | 99.66% | 99.2% | 267.5 | 10080.2 | 3000ms | 7/879 |
| ✅ | `coingecko_bitcoin` | 99.66% | 100.0% | 97.8 | 253.3 | 1500ms | 0/879 |
| ✅ | `useless_fact` | 99.77% | 99.54% | 614.6 | 10229.6 | 2500ms | 4/879 |
| ✅ | `agify_name` | 99.89% | 99.66% | 387.6 | 16112.2 | 2000ms | 3/879 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.77% | 229.7 | 3882.8 | 2000ms | 2/879 |

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
