# API Reliability Monitor — SLA Report

> Last updated: **2026-05-17 11:48 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **5/12** &nbsp;|&nbsp; Avg uptime: **79.7%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 67.16% | 3468.3 | 10206.7 | 1000ms | 265/807 |
| ❌ | `public_apis_list` | 0.0% | 99.5% | 130.3 | 4595.4 | 1500ms | 4/807 |
| ❌ | `nasa_apod` | 76.33% | 56.75% | 3014.0 | 10549.1 | 2000ms | 349/807 |
| ❌ | `ipapi_check` | 83.52% | 100.0% | 154.7 | 363.0 | 2500ms | 0/807 |
| ⚠️ | `rest_countries` | 98.76% | 98.27% | 345.0 | 10221.5 | 2500ms | 14/807 |
| ⚠️ | `open_meteo_weather` | 98.88% | 97.03% | 703.8 | 14877.1 | 2000ms | 24/807 |
| ⚠️ | `dog_ceo_random` | 99.5% | 94.8% | 637.8 | 10244.1 | 2500ms | 42/807 |
| ✅ | `catfact_random` | 99.63% | 99.13% | 270.7 | 10080.2 | 3000ms | 7/807 |
| ✅ | `coingecko_bitcoin` | 99.63% | 100.0% | 97.9 | 252.0 | 1500ms | 0/807 |
| ✅ | `useless_fact` | 99.75% | 99.5% | 608.4 | 10229.6 | 2500ms | 4/807 |
| ✅ | `agify_name` | 99.88% | 99.63% | 393.8 | 16112.2 | 2000ms | 3/807 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.75% | 232.5 | 3882.8 | 2000ms | 2/807 |

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
| `nasa_apod` | 11:00 | 3790.7 | 44.9% |
| `numbers_trivia` | 14:00 | 3788.5 | 35.71% |
| `numbers_trivia` | 00:00 | 3726.6 | 35.29% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
