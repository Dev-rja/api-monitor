# API Reliability Monitor — SLA Report

> Last updated: **2026-04-28 19:52 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **5/12** &nbsp;|&nbsp; Avg uptime: **79.1%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 51.76% | 5017.7 | 10206.7 | 1000ms | 260/539 |
| ❌ | `public_apis_list` | 0.0% | 99.63% | 124.9 | 4088.9 | 1500ms | 2/539 |
| ❌ | `nasa_apod` | 66.05% | 42.12% | 4016.2 | 10549.1 | 2000ms | 312/539 |
| ❌ | `ipapi_check` | 87.57% | 100.0% | 156.4 | 353.0 | 2500ms | 0/539 |
| ⚠️ | `open_meteo_weather` | 98.52% | 97.03% | 727.9 | 14877.1 | 2000ms | 16/539 |
| ⚠️ | `rest_countries` | 98.7% | 98.33% | 339.2 | 10221.5 | 2500ms | 9/539 |
| ⚠️ | `dog_ceo_random` | 99.44% | 92.21% | 764.5 | 10244.1 | 2500ms | 42/539 |
| ✅ | `catfact_random` | 99.44% | 99.44% | 255.6 | 10080.2 | 3000ms | 3/539 |
| ✅ | `useless_fact` | 99.63% | 99.26% | 582.4 | 10229.6 | 2500ms | 4/539 |
| ✅ | `coingecko_bitcoin` | 99.63% | 100.0% | 99.2 | 252.0 | 1500ms | 0/539 |
| ✅ | `agify_name` | 100.0% | 99.81% | 370.1 | 3237.1 | 2000ms | 1/539 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.63% | 239.9 | 3882.8 | 2000ms | 2/539 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `numbers_trivia` | 00:00 | 6811.3 | 66.67% |
| `numbers_trivia` | 01:00 | 6379.1 | 62.5% |
| `numbers_trivia` | 12:00 | 5840.1 | 56.52% |
| `numbers_trivia` | 07:00 | 5753.1 | 55.56% |
| `numbers_trivia` | 18:00 | 5621.4 | 54.17% |
| `numbers_trivia` | 03:00 | 5523.2 | 53.33% |
| `nasa_apod` | 03:00 | 5403.4 | 86.67% |
| `numbers_trivia` | 10:00 | 5392.0 | 52.17% |
| `numbers_trivia` | 16:00 | 5367.2 | 52.0% |
| `numbers_trivia` | 22:00 | 5332.4 | 51.43% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
