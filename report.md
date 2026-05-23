# API Reliability Monitor — SLA Report

> Last updated: **2026-05-23 11:43 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **79.5%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 69.46% | 3240.7 | 10206.7 | 1000ms | 266/871 |
| ❌ | `public_apis_list` | 0.0% | 99.54% | 129.4 | 4595.4 | 1500ms | 4/871 |
| ❌ | `nasa_apod` | 78.07% | 58.32% | 2862.6 | 10549.1 | 2000ms | 363/871 |
| ❌ | `ipapi_check` | 80.37% | 100.0% | 153.9 | 431.8 | 2500ms | 0/871 |
| ⚠️ | `rest_countries` | 98.74% | 98.28% | 346.2 | 10221.5 | 2500ms | 15/871 |
| ⚠️ | `open_meteo_weather` | 98.97% | 97.13% | 699.3 | 14877.1 | 2000ms | 25/871 |
| ✅ | `dog_ceo_random` | 99.43% | 95.18% | 617.4 | 10244.1 | 2500ms | 42/871 |
| ✅ | `catfact_random` | 99.66% | 99.2% | 268.4 | 10080.2 | 3000ms | 7/871 |
| ✅ | `coingecko_bitcoin` | 99.66% | 100.0% | 97.7 | 253.3 | 1500ms | 0/871 |
| ✅ | `useless_fact` | 99.77% | 99.54% | 614.0 | 10229.6 | 2500ms | 4/871 |
| ✅ | `agify_name` | 99.89% | 99.66% | 388.7 | 16112.2 | 2000ms | 3/871 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.77% | 230.1 | 3882.8 | 2000ms | 2/871 |

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
| `nasa_apod` | 11:00 | 3745.5 | 47.06% |
| `numbers_trivia` | 14:00 | 3674.8 | 36.36% |
| `numbers_trivia` | 10:00 | 3642.8 | 34.29% |
| `nasa_apod` | 05:00 | 3555.0 | 60.0% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
