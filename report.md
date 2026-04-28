# API Reliability Monitor — SLA Report

> Last updated: **2026-04-28 11:54 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **5/12** &nbsp;|&nbsp; Avg uptime: **79.1%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 51.49% | 5045.2 | 10206.7 | 1000ms | 260/536 |
| ❌ | `public_apis_list` | 0.0% | 99.63% | 125.0 | 4088.9 | 1500ms | 2/536 |
| ❌ | `nasa_apod` | 65.86% | 41.79% | 4036.4 | 10549.1 | 2000ms | 312/536 |
| ❌ | `ipapi_check` | 87.69% | 100.0% | 156.3 | 353.0 | 2500ms | 0/536 |
| ⚠️ | `open_meteo_weather` | 98.51% | 97.2% | 722.8 | 14877.1 | 2000ms | 15/536 |
| ⚠️ | `rest_countries` | 98.69% | 98.32% | 339.8 | 10221.5 | 2500ms | 9/536 |
| ⚠️ | `dog_ceo_random` | 99.44% | 92.16% | 765.5 | 10244.1 | 2500ms | 42/536 |
| ✅ | `catfact_random` | 99.44% | 99.44% | 255.3 | 10080.2 | 3000ms | 3/536 |
| ✅ | `useless_fact` | 99.63% | 99.25% | 579.9 | 10229.6 | 2500ms | 4/536 |
| ✅ | `coingecko_bitcoin` | 99.63% | 100.0% | 98.9 | 252.0 | 1500ms | 0/536 |
| ✅ | `agify_name` | 100.0% | 99.81% | 370.0 | 3237.1 | 2000ms | 1/536 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.63% | 239.3 | 3882.8 | 2000ms | 2/536 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `numbers_trivia` | 00:00 | 6811.3 | 66.67% |
| `numbers_trivia` | 01:00 | 6379.1 | 62.5% |
| `numbers_trivia` | 12:00 | 5840.1 | 56.52% |
| `numbers_trivia` | 07:00 | 5753.1 | 55.56% |
| `numbers_trivia` | 18:00 | 5621.4 | 54.17% |
| `numbers_trivia` | 16:00 | 5588.5 | 54.17% |
| `numbers_trivia` | 03:00 | 5523.2 | 53.33% |
| `nasa_apod` | 03:00 | 5403.4 | 86.67% |
| `numbers_trivia` | 10:00 | 5392.0 | 52.17% |
| `nasa_apod` | 17:00 | 5368.7 | 67.74% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
