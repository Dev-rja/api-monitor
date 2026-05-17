# API Reliability Monitor — SLA Report

> Last updated: **2026-05-17 15:32 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **5/12** &nbsp;|&nbsp; Avg uptime: **79.7%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 67.16% | 3459.6 | 10206.7 | 1000ms | 266/810 |
| ❌ | `public_apis_list` | 0.0% | 99.51% | 130.2 | 4595.4 | 1500ms | 4/810 |
| ❌ | `nasa_apod` | 76.42% | 56.91% | 3004.6 | 10549.1 | 2000ms | 349/810 |
| ❌ | `ipapi_check` | 83.46% | 100.0% | 154.7 | 363.0 | 2500ms | 0/810 |
| ⚠️ | `rest_countries` | 98.77% | 98.27% | 344.9 | 10221.5 | 2500ms | 14/810 |
| ⚠️ | `open_meteo_weather` | 98.89% | 97.04% | 703.2 | 14877.1 | 2000ms | 24/810 |
| ⚠️ | `dog_ceo_random` | 99.51% | 94.81% | 636.9 | 10244.1 | 2500ms | 42/810 |
| ✅ | `catfact_random` | 99.63% | 99.14% | 270.5 | 10080.2 | 3000ms | 7/810 |
| ✅ | `coingecko_bitcoin` | 99.63% | 100.0% | 97.9 | 252.0 | 1500ms | 0/810 |
| ✅ | `useless_fact` | 99.75% | 99.51% | 608.9 | 10229.6 | 2500ms | 4/810 |
| ✅ | `agify_name` | 99.88% | 99.63% | 393.9 | 16112.2 | 2000ms | 3/810 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.75% | 232.3 | 3882.8 | 2000ms | 2/810 |

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
