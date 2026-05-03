# API Reliability Monitor — SLA Report

> Last updated: **2026-05-03 13:50 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **5/12** &nbsp;|&nbsp; Avg uptime: **79.4%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 57.56% | 4435.0 | 10206.7 | 1000ms | 261/615 |
| ❌ | `public_apis_list` | 0.0% | 99.67% | 123.3 | 4088.9 | 1500ms | 2/615 |
| ❌ | `nasa_apod` | 69.92% | 48.29% | 3622.6 | 10549.1 | 2000ms | 318/615 |
| ❌ | `ipapi_check` | 87.15% | 100.0% | 156.2 | 353.0 | 2500ms | 0/615 |
| ⚠️ | `rest_countries` | 98.54% | 98.21% | 345.3 | 10221.5 | 2500ms | 11/615 |
| ⚠️ | `open_meteo_weather` | 98.7% | 97.07% | 715.5 | 14877.1 | 2000ms | 18/615 |
| ⚠️ | `dog_ceo_random` | 99.51% | 93.17% | 717.5 | 10244.1 | 2500ms | 42/615 |
| ✅ | `catfact_random` | 99.51% | 99.51% | 250.5 | 10080.2 | 3000ms | 3/615 |
| ✅ | `coingecko_bitcoin` | 99.51% | 100.0% | 98.4 | 252.0 | 1500ms | 0/615 |
| ✅ | `useless_fact` | 99.67% | 99.35% | 587.3 | 10229.6 | 2500ms | 4/615 |
| ✅ | `agify_name` | 100.0% | 99.84% | 368.9 | 3237.1 | 2000ms | 1/615 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.67% | 237.4 | 3882.8 | 2000ms | 2/615 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `numbers_trivia` | 00:00 | 5605.3 | 54.55% |
| `numbers_trivia` | 03:00 | 5199.6 | 50.0% |
| `numbers_trivia` | 12:00 | 5183.8 | 50.0% |
| `numbers_trivia` | 01:00 | 5126.1 | 50.0% |
| `nasa_apod` | 17:00 | 5085.4 | 62.86% |
| `nasa_apod` | 03:00 | 5080.8 | 81.25% |
| `numbers_trivia` | 18:00 | 5006.2 | 48.15% |
| `numbers_trivia` | 07:00 | 4955.2 | 47.62% |
| `numbers_trivia` | 10:00 | 4784.8 | 46.15% |
| `numbers_trivia` | 14:00 | 4734.2 | 45.45% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
