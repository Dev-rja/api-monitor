# API Reliability Monitor — SLA Report

> Last updated: **2026-05-17 10:46 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **5/12** &nbsp;|&nbsp; Avg uptime: **79.7%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 67.25% | 3460.0 | 10206.7 | 1000ms | 264/806 |
| ❌ | `public_apis_list` | 0.0% | 99.5% | 130.4 | 4595.4 | 1500ms | 4/806 |
| ❌ | `nasa_apod` | 76.3% | 56.82% | 3014.5 | 10549.1 | 2000ms | 348/806 |
| ❌ | `ipapi_check` | 83.5% | 100.0% | 154.6 | 363.0 | 2500ms | 0/806 |
| ⚠️ | `rest_countries` | 98.76% | 98.26% | 345.3 | 10221.5 | 2500ms | 14/806 |
| ⚠️ | `open_meteo_weather` | 98.88% | 97.02% | 704.1 | 14877.1 | 2000ms | 24/806 |
| ⚠️ | `dog_ceo_random` | 99.5% | 94.79% | 638.1 | 10244.1 | 2500ms | 42/806 |
| ✅ | `catfact_random` | 99.63% | 99.13% | 270.6 | 10080.2 | 3000ms | 7/806 |
| ✅ | `coingecko_bitcoin` | 99.63% | 100.0% | 97.9 | 252.0 | 1500ms | 0/806 |
| ✅ | `useless_fact` | 99.75% | 99.5% | 608.6 | 10229.6 | 2500ms | 4/806 |
| ✅ | `agify_name` | 99.88% | 99.63% | 394.0 | 16112.2 | 2000ms | 3/806 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.75% | 232.6 | 3882.8 | 2000ms | 2/806 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `nasa_apod` | 03:00 | 4729.0 | 77.78% |
| `numbers_trivia` | 03:00 | 4635.3 | 44.44% |
| `numbers_trivia` | 12:00 | 4284.2 | 40.63% |
| `numbers_trivia` | 05:00 | 4119.9 | 39.13% |
| `nasa_apod` | 17:00 | 4065.2 | 52.17% |
| `numbers_trivia` | 07:00 | 4051.7 | 38.46% |
| `numbers_trivia` | 10:00 | 3848.7 | 36.36% |
| `nasa_apod` | 11:00 | 3814.3 | 43.75% |
| `numbers_trivia` | 14:00 | 3788.5 | 35.71% |
| `numbers_trivia` | 00:00 | 3726.6 | 35.29% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
