# API Reliability Monitor — SLA Report

> Last updated: **2026-05-16 12:43 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **5/12** &nbsp;|&nbsp; Avg uptime: **79.7%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 66.62% | 3517.5 | 10206.7 | 1000ms | 264/791 |
| ❌ | `public_apis_list` | 0.0% | 99.49% | 130.8 | 4595.4 | 1500ms | 4/791 |
| ❌ | `nasa_apod` | 75.98% | 56.76% | 3036.2 | 10549.1 | 2000ms | 342/791 |
| ❌ | `ipapi_check` | 84.32% | 100.0% | 154.9 | 363.0 | 2500ms | 0/791 |
| ⚠️ | `rest_countries` | 98.74% | 98.23% | 345.0 | 10221.5 | 2500ms | 14/791 |
| ⚠️ | `open_meteo_weather` | 98.86% | 97.09% | 703.0 | 14877.1 | 2000ms | 23/791 |
| ⚠️ | `dog_ceo_random` | 99.49% | 94.69% | 643.5 | 10244.1 | 2500ms | 42/791 |
| ✅ | `catfact_random` | 99.62% | 99.12% | 269.5 | 10080.2 | 3000ms | 7/791 |
| ✅ | `coingecko_bitcoin` | 99.62% | 100.0% | 98.1 | 252.0 | 1500ms | 0/791 |
| ✅ | `useless_fact` | 99.75% | 99.49% | 606.7 | 10229.6 | 2500ms | 4/791 |
| ✅ | `agify_name` | 99.87% | 99.75% | 390.7 | 16112.2 | 2000ms | 2/791 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.75% | 233.6 | 3882.8 | 2000ms | 2/791 |

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
| `numbers_trivia` | 14:00 | 3873.8 | 36.59% |
| `numbers_trivia` | 18:00 | 3818.7 | 36.11% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
