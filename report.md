# API Reliability Monitor — SLA Report

> Last updated: **2026-04-27 23:35 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **5/12** &nbsp;|&nbsp; Avg uptime: **79.1%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 51.79% | 5016.7 | 10206.7 | 1000ms | 256/531 |
| ❌ | `public_apis_list` | 0.0% | 99.62% | 125.7 | 4088.9 | 1500ms | 2/531 |
| ❌ | `nasa_apod` | 65.54% | 41.43% | 4067.1 | 10549.1 | 2000ms | 311/531 |
| ❌ | `ipapi_check` | 88.14% | 100.0% | 156.5 | 353.0 | 2500ms | 0/531 |
| ⚠️ | `open_meteo_weather` | 98.49% | 97.18% | 724.0 | 14877.1 | 2000ms | 15/531 |
| ⚠️ | `rest_countries` | 98.68% | 98.31% | 340.5 | 10221.5 | 2500ms | 9/531 |
| ⚠️ | `dog_ceo_random` | 99.44% | 92.09% | 769.3 | 10244.1 | 2500ms | 42/531 |
| ✅ | `catfact_random` | 99.44% | 99.44% | 255.4 | 10080.2 | 3000ms | 3/531 |
| ✅ | `useless_fact` | 99.62% | 99.25% | 580.1 | 10229.6 | 2500ms | 4/531 |
| ✅ | `coingecko_bitcoin` | 99.62% | 100.0% | 98.8 | 252.0 | 1500ms | 0/531 |
| ✅ | `agify_name` | 100.0% | 99.81% | 369.4 | 3237.1 | 2000ms | 1/531 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.62% | 239.9 | 3882.8 | 2000ms | 2/531 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `numbers_trivia` | 00:00 | 6811.3 | 66.67% |
| `numbers_trivia` | 01:00 | 5854.0 | 57.14% |
| `numbers_trivia` | 12:00 | 5840.1 | 56.52% |
| `numbers_trivia` | 18:00 | 5621.4 | 54.17% |
| `numbers_trivia` | 16:00 | 5588.5 | 54.17% |
| `numbers_trivia` | 03:00 | 5523.2 | 53.33% |
| `numbers_trivia` | 07:00 | 5499.9 | 52.94% |
| `nasa_apod` | 03:00 | 5403.4 | 86.67% |
| `numbers_trivia` | 10:00 | 5392.0 | 52.17% |
| `nasa_apod` | 17:00 | 5368.7 | 67.74% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
