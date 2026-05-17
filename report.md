# API Reliability Monitor — SLA Report

> Last updated: **2026-05-17 12:44 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **5/12** &nbsp;|&nbsp; Avg uptime: **79.7%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 67.2% | 3464.3 | 10206.7 | 1000ms | 265/808 |
| ❌ | `public_apis_list` | 0.0% | 99.5% | 130.4 | 4595.4 | 1500ms | 4/808 |
| ❌ | `nasa_apod` | 76.36% | 56.81% | 3011.1 | 10549.1 | 2000ms | 349/808 |
| ❌ | `ipapi_check` | 83.54% | 100.0% | 154.7 | 363.0 | 2500ms | 0/808 |
| ⚠️ | `rest_countries` | 98.76% | 98.27% | 345.1 | 10221.5 | 2500ms | 14/808 |
| ⚠️ | `open_meteo_weather` | 98.89% | 97.03% | 703.4 | 14877.1 | 2000ms | 24/808 |
| ⚠️ | `dog_ceo_random` | 99.5% | 94.8% | 637.5 | 10244.1 | 2500ms | 42/808 |
| ✅ | `catfact_random` | 99.63% | 99.13% | 270.8 | 10080.2 | 3000ms | 7/808 |
| ✅ | `coingecko_bitcoin` | 99.63% | 100.0% | 97.9 | 252.0 | 1500ms | 0/808 |
| ✅ | `useless_fact` | 99.75% | 99.5% | 608.4 | 10229.6 | 2500ms | 4/808 |
| ✅ | `agify_name` | 99.88% | 99.63% | 393.7 | 16112.2 | 2000ms | 3/808 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.75% | 232.4 | 3882.8 | 2000ms | 2/808 |

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
| `numbers_trivia` | 14:00 | 3788.5 | 35.71% |
| `numbers_trivia` | 00:00 | 3726.6 | 35.29% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
