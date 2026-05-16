# API Reliability Monitor — SLA Report

> Last updated: **2026-05-16 07:12 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **5/12** &nbsp;|&nbsp; Avg uptime: **79.7%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 66.45% | 3532.2 | 10206.7 | 1000ms | 264/787 |
| ❌ | `public_apis_list` | 0.0% | 99.49% | 131.2 | 4595.4 | 1500ms | 4/787 |
| ❌ | `nasa_apod` | 75.86% | 56.67% | 3046.8 | 10549.1 | 2000ms | 341/787 |
| ❌ | `ipapi_check` | 84.5% | 100.0% | 155.1 | 363.0 | 2500ms | 0/787 |
| ⚠️ | `rest_countries` | 98.73% | 98.22% | 345.6 | 10221.5 | 2500ms | 14/787 |
| ⚠️ | `open_meteo_weather` | 98.86% | 97.08% | 703.5 | 14877.1 | 2000ms | 23/787 |
| ⚠️ | `dog_ceo_random` | 99.49% | 94.66% | 645.0 | 10244.1 | 2500ms | 42/787 |
| ✅ | `catfact_random` | 99.62% | 99.11% | 269.3 | 10080.2 | 3000ms | 7/787 |
| ✅ | `coingecko_bitcoin` | 99.62% | 100.0% | 98.1 | 252.0 | 1500ms | 0/787 |
| ✅ | `useless_fact` | 99.75% | 99.49% | 606.3 | 10229.6 | 2500ms | 4/787 |
| ✅ | `agify_name` | 99.87% | 99.75% | 390.7 | 16112.2 | 2000ms | 2/787 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.75% | 233.9 | 3882.8 | 2000ms | 2/787 |

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
| `numbers_trivia` | 10:00 | 4070.5 | 38.71% |
| `numbers_trivia` | 00:00 | 3937.7 | 37.5% |
| `nasa_apod` | 11:00 | 3887.5 | 44.68% |
| `numbers_trivia` | 14:00 | 3873.8 | 36.59% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
