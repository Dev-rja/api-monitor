# API Reliability Monitor — SLA Report

> Last updated: **2026-04-28 16:20 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **5/12** &nbsp;|&nbsp; Avg uptime: **79.1%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 51.58% | 5035.9 | 10206.7 | 1000ms | 260/537 |
| ❌ | `public_apis_list` | 0.0% | 99.63% | 125.2 | 4088.9 | 1500ms | 2/537 |
| ❌ | `nasa_apod` | 65.92% | 41.9% | 4029.9 | 10549.1 | 2000ms | 312/537 |
| ❌ | `ipapi_check` | 87.71% | 100.0% | 156.4 | 353.0 | 2500ms | 0/537 |
| ⚠️ | `open_meteo_weather` | 98.51% | 97.02% | 728.2 | 14877.1 | 2000ms | 16/537 |
| ⚠️ | `rest_countries` | 98.7% | 98.32% | 339.3 | 10221.5 | 2500ms | 9/537 |
| ⚠️ | `dog_ceo_random` | 99.44% | 92.18% | 764.8 | 10244.1 | 2500ms | 42/537 |
| ✅ | `catfact_random` | 99.44% | 99.44% | 255.3 | 10080.2 | 3000ms | 3/537 |
| ✅ | `useless_fact` | 99.63% | 99.26% | 582.3 | 10229.6 | 2500ms | 4/537 |
| ✅ | `coingecko_bitcoin` | 99.63% | 100.0% | 98.9 | 252.0 | 1500ms | 0/537 |
| ✅ | `agify_name` | 100.0% | 99.81% | 369.8 | 3237.1 | 2000ms | 1/537 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.63% | 239.5 | 3882.8 | 2000ms | 2/537 |

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
| `nasa_apod` | 17:00 | 5368.7 | 67.74% |
| `numbers_trivia` | 16:00 | 5367.2 | 52.0% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
