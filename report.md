# API Reliability Monitor — SLA Report

> Last updated: **2026-04-29 21:44 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **5/12** &nbsp;|&nbsp; Avg uptime: **79.1%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 52.89% | 4903.4 | 10206.7 | 1000ms | 261/554 |
| ❌ | `public_apis_list` | 0.0% | 99.64% | 124.5 | 4088.9 | 1500ms | 2/554 |
| ❌ | `nasa_apod` | 66.79% | 43.32% | 3941.7 | 10549.1 | 2000ms | 314/554 |
| ❌ | `ipapi_check` | 87.36% | 100.0% | 156.4 | 353.0 | 2500ms | 0/554 |
| ⚠️ | `rest_countries` | 98.38% | 98.19% | 353.4 | 10221.5 | 2500ms | 10/554 |
| ⚠️ | `open_meteo_weather` | 98.56% | 97.11% | 725.7 | 14877.1 | 2000ms | 16/554 |
| ⚠️ | `dog_ceo_random` | 99.46% | 92.42% | 753.1 | 10244.1 | 2500ms | 42/554 |
| ✅ | `catfact_random` | 99.46% | 99.46% | 253.7 | 10080.2 | 3000ms | 3/554 |
| ✅ | `useless_fact` | 99.64% | 99.28% | 583.0 | 10229.6 | 2500ms | 4/554 |
| ✅ | `coingecko_bitcoin` | 99.64% | 100.0% | 99.1 | 252.0 | 1500ms | 0/554 |
| ✅ | `agify_name` | 100.0% | 99.82% | 370.0 | 3237.1 | 2000ms | 1/554 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.64% | 240.4 | 3882.8 | 2000ms | 2/554 |

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
