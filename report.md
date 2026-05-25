# API Reliability Monitor — SLA Report

> Last updated: **2026-05-25 15:40 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **7/12** &nbsp;|&nbsp; Avg uptime: **79.5%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 70.44% | 3142.9 | 10206.7 | 1000ms | 266/900 |
| ❌ | `public_apis_list` | 0.0% | 99.56% | 127.5 | 4595.4 | 1500ms | 4/900 |
| ❌ | `nasa_apod` | 78.33% | 59.0% | 2833.4 | 10549.1 | 2000ms | 369/900 |
| ❌ | `ipapi_check` | 79.56% | 100.0% | 153.8 | 431.8 | 2500ms | 0/900 |
| ⚠️ | `rest_countries` | 98.78% | 98.33% | 341.1 | 10221.5 | 2500ms | 15/900 |
| ✅ | `open_meteo_weather` | 99.0% | 97.11% | 698.7 | 14877.1 | 2000ms | 26/900 |
| ✅ | `dog_ceo_random` | 99.44% | 95.33% | 607.5 | 10244.1 | 2500ms | 42/900 |
| ✅ | `catfact_random` | 99.67% | 99.22% | 265.7 | 10080.2 | 3000ms | 7/900 |
| ✅ | `coingecko_bitcoin` | 99.67% | 100.0% | 97.9 | 253.3 | 1500ms | 0/900 |
| ✅ | `useless_fact` | 99.78% | 99.56% | 616.9 | 10229.6 | 2500ms | 4/900 |
| ✅ | `agify_name` | 99.89% | 99.67% | 385.7 | 16112.2 | 2000ms | 3/900 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.78% | 228.3 | 3882.8 | 2000ms | 2/900 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `nasa_apod` | 03:00 | 4729.0 | 77.78% |
| `numbers_trivia` | 03:00 | 4635.3 | 44.44% |
| `numbers_trivia` | 05:00 | 3808.4 | 36.0% |
| `numbers_trivia` | 07:00 | 3781.2 | 35.71% |
| `nasa_apod` | 11:00 | 3745.5 | 47.06% |
| `nasa_apod` | 17:00 | 3711.2 | 47.06% |
| `numbers_trivia` | 14:00 | 3674.8 | 36.36% |
| `numbers_trivia` | 12:00 | 3562.7 | 33.33% |
| `nasa_apod` | 05:00 | 3555.0 | 60.0% |
| `numbers_trivia` | 10:00 | 3544.0 | 33.33% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
