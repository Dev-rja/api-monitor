# API Reliability Monitor — SLA Report

> Last updated: **2026-05-16 16:14 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **5/12** &nbsp;|&nbsp; Avg uptime: **79.7%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 66.75% | 3505.6 | 10206.7 | 1000ms | 264/794 |
| ❌ | `public_apis_list` | 0.0% | 99.5% | 130.8 | 4595.4 | 1500ms | 4/794 |
| ❌ | `nasa_apod` | 76.07% | 56.68% | 3031.5 | 10549.1 | 2000ms | 344/794 |
| ❌ | `ipapi_check` | 84.26% | 100.0% | 154.8 | 363.0 | 2500ms | 0/794 |
| ⚠️ | `rest_countries` | 98.74% | 98.24% | 344.5 | 10221.5 | 2500ms | 14/794 |
| ⚠️ | `open_meteo_weather` | 98.87% | 97.1% | 702.2 | 14877.1 | 2000ms | 23/794 |
| ⚠️ | `dog_ceo_random` | 99.5% | 94.71% | 642.1 | 10244.1 | 2500ms | 42/794 |
| ✅ | `catfact_random` | 99.62% | 99.12% | 268.8 | 10080.2 | 3000ms | 7/794 |
| ✅ | `coingecko_bitcoin` | 99.62% | 100.0% | 97.9 | 252.0 | 1500ms | 0/794 |
| ✅ | `useless_fact` | 99.75% | 99.5% | 606.9 | 10229.6 | 2500ms | 4/794 |
| ✅ | `agify_name` | 99.87% | 99.75% | 390.6 | 16112.2 | 2000ms | 2/794 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.75% | 233.1 | 3882.8 | 2000ms | 2/794 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `nasa_apod` | 03:00 | 4729.0 | 77.78% |
| `numbers_trivia` | 03:00 | 4635.3 | 44.44% |
| `numbers_trivia` | 12:00 | 4284.2 | 40.63% |
| `numbers_trivia` | 07:00 | 4196.6 | 40.0% |
| `nasa_apod` | 17:00 | 4145.1 | 53.33% |
| `numbers_trivia` | 05:00 | 4119.9 | 39.13% |
| `numbers_trivia` | 10:00 | 3957.5 | 37.5% |
| `numbers_trivia` | 00:00 | 3937.7 | 37.5% |
| `numbers_trivia` | 18:00 | 3818.7 | 36.11% |
| `nasa_apod` | 11:00 | 3814.3 | 43.75% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
