# API Reliability Monitor — SLA Report

> Last updated: **2026-04-30 15:19 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **5/12** &nbsp;|&nbsp; Avg uptime: **79.2%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 53.64% | 4826.9 | 10206.7 | 1000ms | 261/563 |
| ❌ | `public_apis_list` | 0.0% | 99.64% | 123.4 | 4088.9 | 1500ms | 2/563 |
| ❌ | `nasa_apod` | 67.32% | 44.05% | 3888.3 | 10549.1 | 2000ms | 315/563 |
| ❌ | `ipapi_check` | 87.39% | 100.0% | 156.2 | 353.0 | 2500ms | 0/563 |
| ⚠️ | `rest_countries` | 98.4% | 98.22% | 352.0 | 10221.5 | 2500ms | 10/563 |
| ⚠️ | `open_meteo_weather` | 98.58% | 97.16% | 724.2 | 14877.1 | 2000ms | 16/563 |
| ⚠️ | `dog_ceo_random` | 99.47% | 92.54% | 748.0 | 10244.1 | 2500ms | 42/563 |
| ✅ | `catfact_random` | 99.47% | 99.47% | 253.0 | 10080.2 | 3000ms | 3/563 |
| ✅ | `useless_fact` | 99.64% | 99.29% | 584.6 | 10229.6 | 2500ms | 4/563 |
| ✅ | `coingecko_bitcoin` | 99.64% | 100.0% | 99.1 | 252.0 | 1500ms | 0/563 |
| ✅ | `agify_name` | 100.0% | 99.82% | 370.4 | 3237.1 | 2000ms | 1/563 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.64% | 239.6 | 3882.8 | 2000ms | 2/563 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `numbers_trivia` | 00:00 | 6148.6 | 60.0% |
| `numbers_trivia` | 01:00 | 5682.4 | 55.56% |
| `numbers_trivia` | 18:00 | 5621.4 | 54.17% |
| `numbers_trivia` | 03:00 | 5523.2 | 53.33% |
| `numbers_trivia` | 07:00 | 5456.4 | 52.63% |
| `nasa_apod` | 03:00 | 5403.4 | 86.67% |
| `numbers_trivia` | 10:00 | 5392.0 | 52.17% |
| `numbers_trivia` | 12:00 | 5382.0 | 52.0% |
| `nasa_apod` | 17:00 | 5367.0 | 66.67% |
| `numbers_trivia` | 05:00 | 5217.3 | 50.0% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
