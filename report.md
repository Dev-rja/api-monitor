# API Reliability Monitor — SLA Report

> Last updated: **2026-05-22 22:56 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **79.6%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 69.25% | 3261.6 | 10206.7 | 1000ms | 266/865 |
| ❌ | `public_apis_list` | 0.0% | 99.54% | 130.0 | 4595.4 | 1500ms | 4/865 |
| ❌ | `nasa_apod` | 77.92% | 58.27% | 2874.4 | 10549.1 | 2000ms | 361/865 |
| ❌ | `ipapi_check` | 80.81% | 100.0% | 154.1 | 431.8 | 2500ms | 0/865 |
| ⚠️ | `rest_countries` | 98.73% | 98.27% | 347.1 | 10221.5 | 2500ms | 15/865 |
| ⚠️ | `open_meteo_weather` | 98.96% | 97.23% | 694.5 | 14877.1 | 2000ms | 24/865 |
| ✅ | `dog_ceo_random` | 99.42% | 95.14% | 619.6 | 10244.1 | 2500ms | 42/865 |
| ✅ | `catfact_random` | 99.65% | 99.19% | 268.9 | 10080.2 | 3000ms | 7/865 |
| ✅ | `coingecko_bitcoin` | 99.65% | 100.0% | 97.6 | 253.3 | 1500ms | 0/865 |
| ✅ | `useless_fact` | 99.77% | 99.54% | 613.4 | 10229.6 | 2500ms | 4/865 |
| ✅ | `agify_name` | 99.88% | 99.65% | 389.0 | 16112.2 | 2000ms | 3/865 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.77% | 230.4 | 3882.8 | 2000ms | 2/865 |

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
| `numbers_trivia` | 10:00 | 3747.3 | 35.29% |
| `numbers_trivia` | 14:00 | 3674.8 | 36.36% |
| `nasa_apod` | 05:00 | 3555.0 | 60.0% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
