# API Reliability Monitor — SLA Report

> Last updated: **2026-05-16 17:18 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **5/12** &nbsp;|&nbsp; Avg uptime: **79.7%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 66.79% | 3501.8 | 10206.7 | 1000ms | 264/795 |
| ❌ | `public_apis_list` | 0.0% | 99.5% | 130.9 | 4595.4 | 1500ms | 4/795 |
| ❌ | `nasa_apod` | 76.1% | 56.73% | 3028.3 | 10549.1 | 2000ms | 344/795 |
| ❌ | `ipapi_check` | 84.15% | 100.0% | 154.8 | 363.0 | 2500ms | 0/795 |
| ⚠️ | `rest_countries` | 98.74% | 98.24% | 344.6 | 10221.5 | 2500ms | 14/795 |
| ⚠️ | `open_meteo_weather` | 98.87% | 97.11% | 701.8 | 14877.1 | 2000ms | 23/795 |
| ⚠️ | `dog_ceo_random` | 99.5% | 94.72% | 641.9 | 10244.1 | 2500ms | 42/795 |
| ✅ | `catfact_random` | 99.62% | 99.12% | 268.8 | 10080.2 | 3000ms | 7/795 |
| ✅ | `coingecko_bitcoin` | 99.62% | 100.0% | 98.0 | 252.0 | 1500ms | 0/795 |
| ✅ | `useless_fact` | 99.75% | 99.5% | 606.8 | 10229.6 | 2500ms | 4/795 |
| ✅ | `agify_name` | 99.87% | 99.75% | 390.5 | 16112.2 | 2000ms | 2/795 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.75% | 233.2 | 3882.8 | 2000ms | 2/795 |

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
| `numbers_trivia` | 00:00 | 3937.7 | 37.5% |
| `numbers_trivia` | 18:00 | 3818.7 | 36.11% |
| `nasa_apod` | 11:00 | 3814.3 | 43.75% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
