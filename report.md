# API Reliability Monitor — SLA Report

> Last updated: **2026-04-29 04:02 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **5/12** &nbsp;|&nbsp; Avg uptime: **79.1%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 52.21% | 4973.3 | 10206.7 | 1000ms | 260/544 |
| ❌ | `public_apis_list` | 0.0% | 99.63% | 124.5 | 4088.9 | 1500ms | 2/544 |
| ❌ | `nasa_apod` | 66.36% | 42.46% | 3987.5 | 10549.1 | 2000ms | 313/544 |
| ❌ | `ipapi_check` | 87.32% | 100.0% | 156.3 | 353.0 | 2500ms | 0/544 |
| ⚠️ | `open_meteo_weather` | 98.53% | 97.06% | 726.8 | 14877.1 | 2000ms | 16/544 |
| ⚠️ | `rest_countries` | 98.71% | 98.35% | 338.7 | 10221.5 | 2500ms | 9/544 |
| ⚠️ | `dog_ceo_random` | 99.45% | 92.28% | 760.8 | 10244.1 | 2500ms | 42/544 |
| ✅ | `catfact_random` | 99.45% | 99.45% | 255.4 | 10080.2 | 3000ms | 3/544 |
| ✅ | `useless_fact` | 99.63% | 99.26% | 582.2 | 10229.6 | 2500ms | 4/544 |
| ✅ | `coingecko_bitcoin` | 99.63% | 100.0% | 99.3 | 252.0 | 1500ms | 0/544 |
| ✅ | `agify_name` | 100.0% | 99.82% | 370.5 | 3237.1 | 2000ms | 1/544 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.63% | 239.9 | 3882.8 | 2000ms | 2/544 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `numbers_trivia` | 01:00 | 6379.1 | 62.5% |
| `numbers_trivia` | 00:00 | 6148.6 | 60.0% |
| `numbers_trivia` | 12:00 | 5840.1 | 56.52% |
| `numbers_trivia` | 07:00 | 5753.1 | 55.56% |
| `numbers_trivia` | 18:00 | 5621.4 | 54.17% |
| `numbers_trivia` | 03:00 | 5523.2 | 53.33% |
| `nasa_apod` | 03:00 | 5403.4 | 86.67% |
| `numbers_trivia` | 10:00 | 5392.0 | 52.17% |
| `numbers_trivia` | 16:00 | 5367.2 | 52.0% |
| `numbers_trivia` | 05:00 | 5217.3 | 50.0% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
