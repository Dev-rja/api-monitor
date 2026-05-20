# API Reliability Monitor — SLA Report

> Last updated: **2026-05-20 10:56 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **79.6%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 68.33% | 3350.4 | 10206.7 | 1000ms | 266/840 |
| ❌ | `public_apis_list` | 0.0% | 99.52% | 130.6 | 4595.4 | 1500ms | 4/840 |
| ❌ | `nasa_apod` | 77.26% | 57.98% | 2926.2 | 10549.1 | 2000ms | 353/840 |
| ❌ | `ipapi_check` | 81.9% | 100.0% | 154.4 | 431.8 | 2500ms | 0/840 |
| ⚠️ | `rest_countries` | 98.81% | 98.33% | 339.5 | 10221.5 | 2500ms | 14/840 |
| ⚠️ | `open_meteo_weather` | 98.93% | 97.14% | 697.0 | 14877.1 | 2000ms | 24/840 |
| ✅ | `dog_ceo_random` | 99.4% | 95.0% | 626.8 | 10244.1 | 2500ms | 42/840 |
| ✅ | `catfact_random` | 99.64% | 99.17% | 268.3 | 10080.2 | 3000ms | 7/840 |
| ✅ | `coingecko_bitcoin` | 99.64% | 100.0% | 97.7 | 253.3 | 1500ms | 0/840 |
| ✅ | `useless_fact` | 99.76% | 99.52% | 609.7 | 10229.6 | 2500ms | 4/840 |
| ✅ | `agify_name` | 99.88% | 99.64% | 390.7 | 16112.2 | 2000ms | 3/840 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.76% | 230.7 | 3882.8 | 2000ms | 2/840 |

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
| `nasa_apod` | 11:00 | 3790.7 | 44.9% |
| `numbers_trivia` | 14:00 | 3756.9 | 37.21% |
| `numbers_trivia` | 10:00 | 3747.3 | 35.29% |
| `nasa_apod` | 05:00 | 3586.6 | 58.33% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
