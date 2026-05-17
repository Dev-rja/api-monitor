# API Reliability Monitor — SLA Report

> Last updated: **2026-05-17 18:43 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **5/12** &nbsp;|&nbsp; Avg uptime: **79.7%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 67.28% | 3448.2 | 10206.7 | 1000ms | 266/813 |
| ❌ | `public_apis_list` | 0.0% | 99.51% | 130.5 | 4595.4 | 1500ms | 4/813 |
| ❌ | `nasa_apod` | 76.51% | 57.07% | 2995.7 | 10549.1 | 2000ms | 349/813 |
| ❌ | `ipapi_check` | 83.27% | 100.0% | 154.8 | 363.0 | 2500ms | 0/813 |
| ⚠️ | `rest_countries` | 98.77% | 98.28% | 344.0 | 10221.5 | 2500ms | 14/813 |
| ⚠️ | `open_meteo_weather` | 98.89% | 97.05% | 702.3 | 14877.1 | 2000ms | 24/813 |
| ⚠️ | `dog_ceo_random` | 99.51% | 94.83% | 635.7 | 10244.1 | 2500ms | 42/813 |
| ✅ | `catfact_random` | 99.63% | 99.14% | 270.5 | 10080.2 | 3000ms | 7/813 |
| ✅ | `coingecko_bitcoin` | 99.63% | 100.0% | 97.8 | 252.0 | 1500ms | 0/813 |
| ✅ | `useless_fact` | 99.75% | 99.51% | 608.8 | 10229.6 | 2500ms | 4/813 |
| ✅ | `agify_name` | 99.88% | 99.63% | 393.3 | 16112.2 | 2000ms | 3/813 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.75% | 232.0 | 3882.8 | 2000ms | 2/813 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `nasa_apod` | 03:00 | 4729.0 | 77.78% |
| `numbers_trivia` | 03:00 | 4635.3 | 44.44% |
| `numbers_trivia` | 12:00 | 4162.0 | 39.39% |
| `numbers_trivia` | 05:00 | 4119.9 | 39.13% |
| `numbers_trivia` | 07:00 | 4051.7 | 38.46% |
| `nasa_apod` | 17:00 | 3990.5 | 51.06% |
| `numbers_trivia` | 10:00 | 3848.7 | 36.36% |
| `nasa_apod` | 11:00 | 3790.7 | 44.9% |
| `numbers_trivia` | 14:00 | 3756.9 | 37.21% |
| `numbers_trivia` | 00:00 | 3726.6 | 35.29% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
