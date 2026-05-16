# API Reliability Monitor — SLA Report

> Last updated: **2026-05-16 11:35 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **5/12** &nbsp;|&nbsp; Avg uptime: **79.7%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 66.58% | 3521.0 | 10206.7 | 1000ms | 264/790 |
| ❌ | `public_apis_list` | 0.0% | 99.49% | 130.9 | 4595.4 | 1500ms | 4/790 |
| ❌ | `nasa_apod` | 75.95% | 56.71% | 3039.6 | 10549.1 | 2000ms | 342/790 |
| ❌ | `ipapi_check` | 84.3% | 100.0% | 154.9 | 363.0 | 2500ms | 0/790 |
| ⚠️ | `rest_countries` | 98.73% | 98.23% | 345.2 | 10221.5 | 2500ms | 14/790 |
| ⚠️ | `open_meteo_weather` | 98.86% | 97.09% | 703.1 | 14877.1 | 2000ms | 23/790 |
| ⚠️ | `dog_ceo_random` | 99.49% | 94.68% | 643.7 | 10244.1 | 2500ms | 42/790 |
| ✅ | `catfact_random` | 99.62% | 99.11% | 268.8 | 10080.2 | 3000ms | 7/790 |
| ✅ | `coingecko_bitcoin` | 99.62% | 100.0% | 98.1 | 252.0 | 1500ms | 0/790 |
| ✅ | `useless_fact` | 99.75% | 99.49% | 606.6 | 10229.6 | 2500ms | 4/790 |
| ✅ | `agify_name` | 99.87% | 99.75% | 390.7 | 16112.2 | 2000ms | 2/790 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.75% | 233.7 | 3882.8 | 2000ms | 2/790 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `nasa_apod` | 03:00 | 4729.0 | 77.78% |
| `numbers_trivia` | 03:00 | 4635.3 | 44.44% |
| `numbers_trivia` | 12:00 | 4400.0 | 41.94% |
| `numbers_trivia` | 07:00 | 4196.6 | 40.0% |
| `nasa_apod` | 17:00 | 4145.1 | 53.33% |
| `numbers_trivia` | 05:00 | 4119.9 | 39.13% |
| `numbers_trivia` | 10:00 | 3957.5 | 37.5% |
| `numbers_trivia` | 00:00 | 3937.7 | 37.5% |
| `numbers_trivia` | 14:00 | 3873.8 | 36.59% |
| `numbers_trivia` | 18:00 | 3818.7 | 36.11% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
