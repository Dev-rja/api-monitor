# API Reliability Monitor — SLA Report

> Last updated: **2026-05-20 19:09 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **79.6%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 68.45% | 3340.7 | 10206.7 | 1000ms | 266/843 |
| ❌ | `public_apis_list` | 0.0% | 99.53% | 130.4 | 4595.4 | 1500ms | 4/843 |
| ❌ | `nasa_apod` | 77.34% | 58.01% | 2919.5 | 10549.1 | 2000ms | 354/843 |
| ❌ | `ipapi_check` | 81.97% | 100.0% | 154.5 | 431.8 | 2500ms | 0/843 |
| ⚠️ | `rest_countries` | 98.81% | 98.34% | 339.0 | 10221.5 | 2500ms | 14/843 |
| ⚠️ | `open_meteo_weather` | 98.93% | 97.15% | 696.5 | 14877.1 | 2000ms | 24/843 |
| ✅ | `dog_ceo_random` | 99.41% | 95.02% | 626.1 | 10244.1 | 2500ms | 42/843 |
| ✅ | `catfact_random` | 99.64% | 99.17% | 268.1 | 10080.2 | 3000ms | 7/843 |
| ✅ | `coingecko_bitcoin` | 99.64% | 100.0% | 97.7 | 253.3 | 1500ms | 0/843 |
| ✅ | `useless_fact` | 99.76% | 99.53% | 610.3 | 10229.6 | 2500ms | 4/843 |
| ✅ | `agify_name` | 99.88% | 99.64% | 390.7 | 16112.2 | 2000ms | 3/843 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.76% | 230.6 | 3882.8 | 2000ms | 2/843 |

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
