# API Reliability Monitor — SLA Report

> Last updated: **2026-04-29 20:40 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **5/12** &nbsp;|&nbsp; Avg uptime: **79.1%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 52.8% | 4911.9 | 10206.7 | 1000ms | 261/553 |
| ❌ | `public_apis_list` | 0.0% | 99.64% | 124.5 | 4088.9 | 1500ms | 2/553 |
| ❌ | `nasa_apod` | 66.73% | 43.22% | 3948.3 | 10549.1 | 2000ms | 314/553 |
| ❌ | `ipapi_check` | 87.34% | 100.0% | 156.3 | 353.0 | 2500ms | 0/553 |
| ⚠️ | `rest_countries` | 98.37% | 98.19% | 353.6 | 10221.5 | 2500ms | 10/553 |
| ⚠️ | `open_meteo_weather` | 98.55% | 97.11% | 725.9 | 14877.1 | 2000ms | 16/553 |
| ⚠️ | `dog_ceo_random` | 99.46% | 92.41% | 753.8 | 10244.1 | 2500ms | 42/553 |
| ✅ | `catfact_random` | 99.46% | 99.46% | 253.8 | 10080.2 | 3000ms | 3/553 |
| ✅ | `useless_fact` | 99.64% | 99.28% | 582.3 | 10229.6 | 2500ms | 4/553 |
| ✅ | `coingecko_bitcoin` | 99.64% | 100.0% | 99.0 | 252.0 | 1500ms | 0/553 |
| ✅ | `agify_name` | 100.0% | 99.82% | 369.6 | 3237.1 | 2000ms | 1/553 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.64% | 239.3 | 3882.8 | 2000ms | 2/553 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `numbers_trivia` | 01:00 | 6379.1 | 62.5% |
| `numbers_trivia` | 00:00 | 6148.6 | 60.0% |
| `numbers_trivia` | 07:00 | 5753.1 | 55.56% |
| `numbers_trivia` | 18:00 | 5621.4 | 54.17% |
| `numbers_trivia` | 12:00 | 5601.9 | 54.17% |
| `numbers_trivia` | 03:00 | 5523.2 | 53.33% |
| `nasa_apod` | 03:00 | 5403.4 | 86.67% |
| `numbers_trivia` | 10:00 | 5392.0 | 52.17% |
| `nasa_apod` | 17:00 | 5367.0 | 66.67% |
| `numbers_trivia` | 05:00 | 5217.3 | 50.0% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
