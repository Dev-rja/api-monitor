# API Reliability Monitor — SLA Report

> Last updated: **2026-05-21 14:27 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **79.6%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 68.71% | 3315.5 | 10206.7 | 1000ms | 266/850 |
| ❌ | `public_apis_list` | 0.0% | 99.53% | 130.2 | 4595.4 | 1500ms | 4/850 |
| ❌ | `nasa_apod` | 77.53% | 58.12% | 2904.0 | 10549.1 | 2000ms | 356/850 |
| ❌ | `ipapi_check` | 81.65% | 100.0% | 154.2 | 431.8 | 2500ms | 0/850 |
| ⚠️ | `rest_countries` | 98.82% | 98.35% | 337.8 | 10221.5 | 2500ms | 14/850 |
| ⚠️ | `open_meteo_weather` | 98.94% | 97.18% | 695.9 | 14877.1 | 2000ms | 24/850 |
| ✅ | `dog_ceo_random` | 99.41% | 95.06% | 623.9 | 10244.1 | 2500ms | 42/850 |
| ✅ | `catfact_random` | 99.65% | 99.18% | 267.6 | 10080.2 | 3000ms | 7/850 |
| ✅ | `coingecko_bitcoin` | 99.65% | 100.0% | 97.4 | 253.3 | 1500ms | 0/850 |
| ✅ | `useless_fact` | 99.76% | 99.53% | 610.6 | 10229.6 | 2500ms | 4/850 |
| ✅ | `agify_name` | 99.88% | 99.65% | 390.7 | 16112.2 | 2000ms | 3/850 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.76% | 230.4 | 3882.8 | 2000ms | 2/850 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `nasa_apod` | 03:00 | 4729.0 | 77.78% |
| `numbers_trivia` | 03:00 | 4635.3 | 44.44% |
| `nasa_apod` | 17:00 | 3990.5 | 51.06% |
| `numbers_trivia` | 05:00 | 3963.3 | 37.5% |
| `numbers_trivia` | 12:00 | 3951.0 | 37.14% |
| `numbers_trivia` | 07:00 | 3915.1 | 37.04% |
| `nasa_apod` | 11:00 | 3767.9 | 46.0% |
| `numbers_trivia` | 10:00 | 3747.3 | 35.29% |
| `numbers_trivia` | 14:00 | 3674.8 | 36.36% |
| `nasa_apod` | 05:00 | 3586.6 | 58.33% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
