# API Reliability Monitor — SLA Report

> Last updated: **2026-05-22 21:53 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **79.6%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 69.21% | 3265.3 | 10206.7 | 1000ms | 266/864 |
| ❌ | `public_apis_list` | 0.0% | 99.54% | 129.9 | 4595.4 | 1500ms | 4/864 |
| ❌ | `nasa_apod` | 77.89% | 58.33% | 2874.4 | 10549.1 | 2000ms | 360/864 |
| ❌ | `ipapi_check` | 80.9% | 100.0% | 154.1 | 431.8 | 2500ms | 0/864 |
| ⚠️ | `rest_countries` | 98.73% | 98.26% | 347.3 | 10221.5 | 2500ms | 15/864 |
| ⚠️ | `open_meteo_weather` | 98.96% | 97.22% | 694.8 | 14877.1 | 2000ms | 24/864 |
| ✅ | `dog_ceo_random` | 99.42% | 95.14% | 619.9 | 10244.1 | 2500ms | 42/864 |
| ✅ | `catfact_random` | 99.65% | 99.19% | 269.1 | 10080.2 | 3000ms | 7/864 |
| ✅ | `coingecko_bitcoin` | 99.65% | 100.0% | 97.7 | 253.3 | 1500ms | 0/864 |
| ✅ | `useless_fact` | 99.77% | 99.54% | 613.5 | 10229.6 | 2500ms | 4/864 |
| ✅ | `agify_name` | 99.88% | 99.65% | 389.3 | 16112.2 | 2000ms | 3/864 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.77% | 230.3 | 3882.8 | 2000ms | 2/864 |

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
