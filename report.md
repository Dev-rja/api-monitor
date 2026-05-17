# API Reliability Monitor — SLA Report

> Last updated: **2026-05-17 04:32 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **5/12** &nbsp;|&nbsp; Avg uptime: **79.7%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 67.12% | 3471.0 | 10206.7 | 1000ms | 264/803 |
| ❌ | `public_apis_list` | 0.0% | 99.5% | 130.7 | 4595.4 | 1500ms | 4/803 |
| ❌ | `nasa_apod` | 76.34% | 56.91% | 3008.9 | 10549.1 | 2000ms | 346/803 |
| ❌ | `ipapi_check` | 83.69% | 100.0% | 154.7 | 363.0 | 2500ms | 0/803 |
| ⚠️ | `rest_countries` | 98.75% | 98.26% | 345.7 | 10221.5 | 2500ms | 14/803 |
| ⚠️ | `open_meteo_weather` | 98.88% | 97.01% | 704.5 | 14877.1 | 2000ms | 24/803 |
| ⚠️ | `dog_ceo_random` | 99.5% | 94.77% | 638.8 | 10244.1 | 2500ms | 42/803 |
| ✅ | `catfact_random` | 99.63% | 99.13% | 270.5 | 10080.2 | 3000ms | 7/803 |
| ✅ | `coingecko_bitcoin` | 99.63% | 100.0% | 97.8 | 252.0 | 1500ms | 0/803 |
| ✅ | `useless_fact` | 99.75% | 99.5% | 607.5 | 10229.6 | 2500ms | 4/803 |
| ✅ | `agify_name` | 99.88% | 99.63% | 393.9 | 16112.2 | 2000ms | 3/803 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.75% | 232.7 | 3882.8 | 2000ms | 2/803 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `nasa_apod` | 03:00 | 4729.0 | 77.78% |
| `numbers_trivia` | 03:00 | 4635.3 | 44.44% |
| `numbers_trivia` | 12:00 | 4284.2 | 40.63% |
| `numbers_trivia` | 07:00 | 4196.6 | 40.0% |
| `numbers_trivia` | 05:00 | 4119.9 | 39.13% |
| `nasa_apod` | 17:00 | 4065.2 | 52.17% |
| `numbers_trivia` | 10:00 | 3957.5 | 37.5% |
| `nasa_apod` | 11:00 | 3814.3 | 43.75% |
| `numbers_trivia` | 14:00 | 3788.5 | 35.71% |
| `numbers_trivia` | 00:00 | 3726.6 | 35.29% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
