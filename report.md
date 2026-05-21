# API Reliability Monitor — SLA Report

> Last updated: **2026-05-21 11:41 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **79.6%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 68.67% | 3319.2 | 10206.7 | 1000ms | 266/849 |
| ❌ | `public_apis_list` | 0.0% | 99.53% | 130.3 | 4595.4 | 1500ms | 4/849 |
| ❌ | `nasa_apod` | 77.5% | 58.07% | 2906.7 | 10549.1 | 2000ms | 356/849 |
| ❌ | `ipapi_check` | 81.74% | 100.0% | 154.2 | 431.8 | 2500ms | 0/849 |
| ⚠️ | `rest_countries` | 98.82% | 98.35% | 338.1 | 10221.5 | 2500ms | 14/849 |
| ⚠️ | `open_meteo_weather` | 98.94% | 97.17% | 696.3 | 14877.1 | 2000ms | 24/849 |
| ✅ | `dog_ceo_random` | 99.41% | 95.05% | 624.4 | 10244.1 | 2500ms | 42/849 |
| ✅ | `catfact_random` | 99.65% | 99.18% | 267.4 | 10080.2 | 3000ms | 7/849 |
| ✅ | `coingecko_bitcoin` | 99.65% | 100.0% | 97.4 | 253.3 | 1500ms | 0/849 |
| ✅ | `useless_fact` | 99.76% | 99.53% | 610.7 | 10229.6 | 2500ms | 4/849 |
| ✅ | `agify_name` | 99.88% | 99.65% | 390.8 | 16112.2 | 2000ms | 3/849 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.76% | 230.5 | 3882.8 | 2000ms | 2/849 |

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
| `numbers_trivia` | 14:00 | 3756.9 | 37.21% |
| `numbers_trivia` | 10:00 | 3747.3 | 35.29% |
| `nasa_apod` | 05:00 | 3586.6 | 58.33% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
