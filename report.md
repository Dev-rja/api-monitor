# API Reliability Monitor — SLA Report

> Last updated: **2026-05-05 18:59 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **5/12** &nbsp;|&nbsp; Avg uptime: **79.5%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 59.66% | 4227.7 | 10206.7 | 1000ms | 261/647 |
| ❌ | `public_apis_list` | 0.0% | 99.69% | 122.5 | 4088.9 | 1500ms | 2/647 |
| ❌ | `nasa_apod` | 71.41% | 50.7% | 3467.8 | 10549.1 | 2000ms | 319/647 |
| ❌ | `ipapi_check` | 86.86% | 100.0% | 156.5 | 363.0 | 2500ms | 0/647 |
| ⚠️ | `rest_countries` | 98.61% | 98.3% | 339.5 | 10221.5 | 2500ms | 11/647 |
| ⚠️ | `open_meteo_weather` | 98.76% | 96.75% | 724.0 | 14877.1 | 2000ms | 21/647 |
| ⚠️ | `dog_ceo_random` | 99.54% | 93.51% | 701.1 | 10244.1 | 2500ms | 42/647 |
| ✅ | `catfact_random` | 99.54% | 99.38% | 258.6 | 10080.2 | 3000ms | 4/647 |
| ✅ | `coingecko_bitcoin` | 99.54% | 100.0% | 98.7 | 252.0 | 1500ms | 0/647 |
| ✅ | `useless_fact` | 99.69% | 99.38% | 593.3 | 10229.6 | 2500ms | 4/647 |
| ✅ | `agify_name` | 100.0% | 99.85% | 369.0 | 3237.1 | 2000ms | 1/647 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.69% | 237.4 | 3882.8 | 2000ms | 2/647 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `numbers_trivia` | 00:00 | 5605.3 | 54.55% |
| `numbers_trivia` | 03:00 | 5199.6 | 50.0% |
| `numbers_trivia` | 12:00 | 5183.8 | 50.0% |
| `nasa_apod` | 03:00 | 5080.8 | 81.25% |
| `numbers_trivia` | 07:00 | 4955.2 | 47.62% |
| `nasa_apod` | 17:00 | 4716.3 | 57.89% |
| `numbers_trivia` | 05:00 | 4708.1 | 45.0% |
| `numbers_trivia` | 01:00 | 4686.2 | 45.45% |
| `numbers_trivia` | 10:00 | 4616.5 | 44.44% |
| `numbers_trivia` | 18:00 | 4526.1 | 43.33% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
