# API Reliability Monitor — SLA Report

> Last updated: **2026-05-20 21:13 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **79.6%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 68.48% | 3337.2 | 10206.7 | 1000ms | 266/844 |
| ❌ | `public_apis_list` | 0.0% | 99.53% | 130.3 | 4595.4 | 1500ms | 4/844 |
| ❌ | `nasa_apod` | 77.37% | 58.06% | 2916.3 | 10549.1 | 2000ms | 354/844 |
| ❌ | `ipapi_check` | 81.87% | 100.0% | 154.4 | 431.8 | 2500ms | 0/844 |
| ⚠️ | `rest_countries` | 98.82% | 98.34% | 338.9 | 10221.5 | 2500ms | 14/844 |
| ⚠️ | `open_meteo_weather` | 98.93% | 97.16% | 696.5 | 14877.1 | 2000ms | 24/844 |
| ✅ | `dog_ceo_random` | 99.41% | 95.02% | 625.8 | 10244.1 | 2500ms | 42/844 |
| ✅ | `catfact_random` | 99.64% | 99.17% | 268.1 | 10080.2 | 3000ms | 7/844 |
| ✅ | `coingecko_bitcoin` | 99.64% | 100.0% | 97.7 | 253.3 | 1500ms | 0/844 |
| ✅ | `useless_fact` | 99.76% | 99.53% | 610.3 | 10229.6 | 2500ms | 4/844 |
| ✅ | `agify_name` | 99.88% | 99.64% | 390.9 | 16112.2 | 2000ms | 3/844 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.76% | 230.6 | 3882.8 | 2000ms | 2/844 |

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
