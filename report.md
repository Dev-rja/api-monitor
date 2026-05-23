# API Reliability Monitor — SLA Report

> Last updated: **2026-05-23 10:27 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **79.6%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 69.43% | 3244.2 | 10206.7 | 1000ms | 266/870 |
| ❌ | `public_apis_list` | 0.0% | 99.54% | 129.5 | 4595.4 | 1500ms | 4/870 |
| ❌ | `nasa_apod` | 78.05% | 58.39% | 2862.8 | 10549.1 | 2000ms | 362/870 |
| ❌ | `ipapi_check` | 80.46% | 100.0% | 153.9 | 431.8 | 2500ms | 0/870 |
| ⚠️ | `rest_countries` | 98.74% | 98.28% | 346.4 | 10221.5 | 2500ms | 15/870 |
| ⚠️ | `open_meteo_weather` | 98.97% | 97.13% | 699.5 | 14877.1 | 2000ms | 25/870 |
| ✅ | `dog_ceo_random` | 99.43% | 95.17% | 617.9 | 10244.1 | 2500ms | 42/870 |
| ✅ | `catfact_random` | 99.66% | 99.2% | 268.5 | 10080.2 | 3000ms | 7/870 |
| ✅ | `coingecko_bitcoin` | 99.66% | 100.0% | 97.7 | 253.3 | 1500ms | 0/870 |
| ✅ | `useless_fact` | 99.77% | 99.54% | 613.7 | 10229.6 | 2500ms | 4/870 |
| ✅ | `agify_name` | 99.89% | 99.66% | 388.8 | 16112.2 | 2000ms | 3/870 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.77% | 230.1 | 3882.8 | 2000ms | 2/870 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `nasa_apod` | 03:00 | 4729.0 | 77.78% |
| `numbers_trivia` | 03:00 | 4635.3 | 44.44% |
| `numbers_trivia` | 07:00 | 3915.1 | 37.04% |
| `nasa_apod` | 17:00 | 3847.1 | 48.98% |
| `numbers_trivia` | 12:00 | 3843.8 | 36.11% |
| `numbers_trivia` | 05:00 | 3808.4 | 36.0% |
| `nasa_apod` | 11:00 | 3767.9 | 46.0% |
| `numbers_trivia` | 14:00 | 3674.8 | 36.36% |
| `numbers_trivia` | 10:00 | 3642.8 | 34.29% |
| `nasa_apod` | 05:00 | 3555.0 | 60.0% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
