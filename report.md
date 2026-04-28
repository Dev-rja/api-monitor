# API Reliability Monitor — SLA Report

> Last updated: **2026-04-28 07:29 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **5/12** &nbsp;|&nbsp; Avg uptime: **79.1%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 51.5% | 5045.1 | 10206.7 | 1000ms | 259/534 |
| ❌ | `public_apis_list` | 0.0% | 99.63% | 125.3 | 4088.9 | 1500ms | 2/534 |
| ❌ | `nasa_apod` | 65.73% | 41.57% | 4049.8 | 10549.1 | 2000ms | 312/534 |
| ❌ | `ipapi_check` | 88.01% | 100.0% | 156.3 | 353.0 | 2500ms | 0/534 |
| ⚠️ | `open_meteo_weather` | 98.5% | 97.19% | 723.6 | 14877.1 | 2000ms | 15/534 |
| ⚠️ | `rest_countries` | 98.69% | 98.31% | 340.5 | 10221.5 | 2500ms | 9/534 |
| ⚠️ | `dog_ceo_random` | 99.44% | 92.13% | 767.2 | 10244.1 | 2500ms | 42/534 |
| ✅ | `catfact_random` | 99.44% | 99.44% | 255.4 | 10080.2 | 3000ms | 3/534 |
| ✅ | `useless_fact` | 99.63% | 99.25% | 580.4 | 10229.6 | 2500ms | 4/534 |
| ✅ | `coingecko_bitcoin` | 99.63% | 100.0% | 98.8 | 252.0 | 1500ms | 0/534 |
| ✅ | `agify_name` | 100.0% | 99.81% | 370.4 | 3237.1 | 2000ms | 1/534 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.63% | 239.4 | 3882.8 | 2000ms | 2/534 |

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
