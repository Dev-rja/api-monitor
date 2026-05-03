# API Reliability Monitor — SLA Report

> Last updated: **2026-05-03 08:27 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **5/12** &nbsp;|&nbsp; Avg uptime: **79.4%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 57.21% | 4469.8 | 10206.7 | 1000ms | 261/610 |
| ❌ | `public_apis_list` | 0.0% | 99.67% | 123.3 | 4088.9 | 1500ms | 2/610 |
| ❌ | `nasa_apod` | 69.67% | 47.87% | 3647.9 | 10549.1 | 2000ms | 318/610 |
| ❌ | `ipapi_check` | 87.7% | 100.0% | 156.1 | 353.0 | 2500ms | 0/610 |
| ⚠️ | `rest_countries` | 98.52% | 98.36% | 340.8 | 10221.5 | 2500ms | 10/610 |
| ⚠️ | `open_meteo_weather` | 98.69% | 97.05% | 717.4 | 14877.1 | 2000ms | 18/610 |
| ⚠️ | `dog_ceo_random` | 99.51% | 93.11% | 720.1 | 10244.1 | 2500ms | 42/610 |
| ✅ | `catfact_random` | 99.51% | 99.51% | 251.5 | 10080.2 | 3000ms | 3/610 |
| ✅ | `coingecko_bitcoin` | 99.51% | 100.0% | 98.5 | 252.0 | 1500ms | 0/610 |
| ✅ | `useless_fact` | 99.67% | 99.34% | 587.6 | 10229.6 | 2500ms | 4/610 |
| ✅ | `agify_name` | 100.0% | 99.84% | 369.4 | 3237.1 | 2000ms | 1/610 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.67% | 238.0 | 3882.8 | 2000ms | 2/610 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `numbers_trivia` | 00:00 | 5605.3 | 54.55% |
| `numbers_trivia` | 12:00 | 5382.0 | 52.0% |
| `numbers_trivia` | 03:00 | 5199.6 | 50.0% |
| `numbers_trivia` | 01:00 | 5126.1 | 50.0% |
| `nasa_apod` | 17:00 | 5085.4 | 62.86% |
| `nasa_apod` | 03:00 | 5080.8 | 81.25% |
| `numbers_trivia` | 18:00 | 5006.2 | 48.15% |
| `numbers_trivia` | 10:00 | 4972.0 | 48.0% |
| `numbers_trivia` | 07:00 | 4955.2 | 47.62% |
| `numbers_trivia` | 14:00 | 4734.2 | 45.45% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
