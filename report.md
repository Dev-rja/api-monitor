# API Reliability Monitor — SLA Report

> Last updated: **2026-05-16 10:35 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **5/12** &nbsp;|&nbsp; Avg uptime: **79.7%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 66.54% | 3524.6 | 10206.7 | 1000ms | 264/789 |
| ❌ | `public_apis_list` | 0.0% | 99.49% | 131.0 | 4595.4 | 1500ms | 4/789 |
| ❌ | `nasa_apod` | 75.92% | 56.65% | 3043.0 | 10549.1 | 2000ms | 342/789 |
| ❌ | `ipapi_check` | 84.41% | 100.0% | 155.0 | 363.0 | 2500ms | 0/789 |
| ⚠️ | `rest_countries` | 98.73% | 98.23% | 345.1 | 10221.5 | 2500ms | 14/789 |
| ⚠️ | `open_meteo_weather` | 98.86% | 97.08% | 703.2 | 14877.1 | 2000ms | 23/789 |
| ⚠️ | `dog_ceo_random` | 99.49% | 94.68% | 644.1 | 10244.1 | 2500ms | 42/789 |
| ✅ | `catfact_random` | 99.62% | 99.11% | 268.9 | 10080.2 | 3000ms | 7/789 |
| ✅ | `coingecko_bitcoin` | 99.62% | 100.0% | 98.0 | 252.0 | 1500ms | 0/789 |
| ✅ | `useless_fact` | 99.75% | 99.49% | 606.2 | 10229.6 | 2500ms | 4/789 |
| ✅ | `agify_name` | 99.87% | 99.75% | 390.5 | 16112.2 | 2000ms | 2/789 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.75% | 233.8 | 3882.8 | 2000ms | 2/789 |

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
| `nasa_apod` | 11:00 | 3887.5 | 44.68% |
| `numbers_trivia` | 14:00 | 3873.8 | 36.59% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
