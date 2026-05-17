# API Reliability Monitor — SLA Report

> Last updated: **2026-05-17 14:16 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **5/12** &nbsp;|&nbsp; Avg uptime: **79.7%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 67.12% | 3463.0 | 10206.7 | 1000ms | 266/809 |
| ❌ | `public_apis_list` | 0.0% | 99.51% | 130.3 | 4595.4 | 1500ms | 4/809 |
| ❌ | `nasa_apod` | 76.39% | 56.86% | 3007.8 | 10549.1 | 2000ms | 349/809 |
| ❌ | `ipapi_check` | 83.56% | 100.0% | 154.7 | 363.0 | 2500ms | 0/809 |
| ⚠️ | `rest_countries` | 98.76% | 98.27% | 345.0 | 10221.5 | 2500ms | 14/809 |
| ⚠️ | `open_meteo_weather` | 98.89% | 97.03% | 703.3 | 14877.1 | 2000ms | 24/809 |
| ⚠️ | `dog_ceo_random` | 99.51% | 94.81% | 637.2 | 10244.1 | 2500ms | 42/809 |
| ✅ | `catfact_random` | 99.63% | 99.13% | 270.6 | 10080.2 | 3000ms | 7/809 |
| ✅ | `coingecko_bitcoin` | 99.63% | 100.0% | 97.9 | 252.0 | 1500ms | 0/809 |
| ✅ | `useless_fact` | 99.75% | 99.51% | 608.7 | 10229.6 | 2500ms | 4/809 |
| ✅ | `agify_name` | 99.88% | 99.63% | 393.8 | 16112.2 | 2000ms | 3/809 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.75% | 232.3 | 3882.8 | 2000ms | 2/809 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `nasa_apod` | 03:00 | 4729.0 | 77.78% |
| `numbers_trivia` | 03:00 | 4635.3 | 44.44% |
| `numbers_trivia` | 12:00 | 4162.0 | 39.39% |
| `numbers_trivia` | 05:00 | 4119.9 | 39.13% |
| `nasa_apod` | 17:00 | 4065.2 | 52.17% |
| `numbers_trivia` | 07:00 | 4051.7 | 38.46% |
| `numbers_trivia` | 10:00 | 3848.7 | 36.36% |
| `nasa_apod` | 11:00 | 3790.7 | 44.9% |
| `numbers_trivia` | 14:00 | 3756.9 | 37.21% |
| `numbers_trivia` | 00:00 | 3726.6 | 35.29% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
