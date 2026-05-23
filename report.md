# API Reliability Monitor — SLA Report

> Last updated: **2026-05-23 12:45 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **79.5%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 69.5% | 3237.1 | 10206.7 | 1000ms | 266/872 |
| ❌ | `public_apis_list` | 0.0% | 99.54% | 129.3 | 4595.4 | 1500ms | 4/872 |
| ❌ | `nasa_apod` | 77.98% | 58.26% | 2871.2 | 10549.1 | 2000ms | 364/872 |
| ❌ | `ipapi_check` | 80.28% | 100.0% | 153.8 | 431.8 | 2500ms | 0/872 |
| ⚠️ | `rest_countries` | 98.74% | 98.28% | 346.0 | 10221.5 | 2500ms | 15/872 |
| ⚠️ | `open_meteo_weather` | 98.97% | 97.13% | 699.0 | 14877.1 | 2000ms | 25/872 |
| ✅ | `dog_ceo_random` | 99.43% | 95.18% | 617.0 | 10244.1 | 2500ms | 42/872 |
| ✅ | `catfact_random` | 99.66% | 99.2% | 268.1 | 10080.2 | 3000ms | 7/872 |
| ✅ | `coingecko_bitcoin` | 99.66% | 100.0% | 97.8 | 253.3 | 1500ms | 0/872 |
| ✅ | `useless_fact` | 99.77% | 99.54% | 614.2 | 10229.6 | 2500ms | 4/872 |
| ✅ | `agify_name` | 99.89% | 99.66% | 388.4 | 16112.2 | 2000ms | 3/872 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.77% | 230.1 | 3882.8 | 2000ms | 2/872 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `nasa_apod` | 03:00 | 4729.0 | 77.78% |
| `numbers_trivia` | 03:00 | 4635.3 | 44.44% |
| `numbers_trivia` | 07:00 | 3915.1 | 37.04% |
| `nasa_apod` | 17:00 | 3847.1 | 48.98% |
| `numbers_trivia` | 05:00 | 3808.4 | 36.0% |
| `nasa_apod` | 11:00 | 3745.5 | 47.06% |
| `numbers_trivia` | 12:00 | 3742.4 | 35.14% |
| `numbers_trivia` | 14:00 | 3674.8 | 36.36% |
| `numbers_trivia` | 10:00 | 3642.8 | 34.29% |
| `nasa_apod` | 05:00 | 3555.0 | 60.0% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
