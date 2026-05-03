# API Reliability Monitor — SLA Report

> Last updated: **2026-05-03 14:40 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **5/12** &nbsp;|&nbsp; Avg uptime: **79.4%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 57.63% | 4428.2 | 10206.7 | 1000ms | 261/616 |
| ❌ | `public_apis_list` | 0.0% | 99.68% | 123.2 | 4088.9 | 1500ms | 2/616 |
| ❌ | `nasa_apod` | 69.97% | 48.38% | 3617.4 | 10549.1 | 2000ms | 318/616 |
| ❌ | `ipapi_check` | 87.01% | 100.0% | 156.2 | 353.0 | 2500ms | 0/616 |
| ⚠️ | `rest_countries` | 98.54% | 98.21% | 345.1 | 10221.5 | 2500ms | 11/616 |
| ⚠️ | `open_meteo_weather` | 98.7% | 97.08% | 715.7 | 14877.1 | 2000ms | 18/616 |
| ⚠️ | `dog_ceo_random` | 99.51% | 93.18% | 717.0 | 10244.1 | 2500ms | 42/616 |
| ✅ | `catfact_random` | 99.51% | 99.35% | 255.5 | 10080.2 | 3000ms | 4/616 |
| ✅ | `coingecko_bitcoin` | 99.51% | 100.0% | 98.3 | 252.0 | 1500ms | 0/616 |
| ✅ | `useless_fact` | 99.68% | 99.35% | 587.0 | 10229.6 | 2500ms | 4/616 |
| ✅ | `agify_name` | 100.0% | 99.84% | 368.9 | 3237.1 | 2000ms | 1/616 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.68% | 237.4 | 3882.8 | 2000ms | 2/616 |

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
| `numbers_trivia` | 05:00 | 4708.1 | 45.0% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
