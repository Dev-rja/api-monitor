# API Reliability Monitor — SLA Report

> Last updated: **2026-05-02 22:39 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **5/12** &nbsp;|&nbsp; Avg uptime: **79.4%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 56.86% | 4504.9 | 10206.7 | 1000ms | 261/605 |
| ❌ | `public_apis_list` | 0.0% | 99.67% | 123.4 | 4088.9 | 1500ms | 2/605 |
| ❌ | `nasa_apod` | 69.59% | 47.6% | 3657.6 | 10549.1 | 2000ms | 317/605 |
| ❌ | `ipapi_check` | 87.77% | 100.0% | 155.9 | 353.0 | 2500ms | 0/605 |
| ⚠️ | `rest_countries` | 98.51% | 98.35% | 342.1 | 10221.5 | 2500ms | 10/605 |
| ⚠️ | `open_meteo_weather` | 98.68% | 97.19% | 713.9 | 14877.1 | 2000ms | 17/605 |
| ⚠️ | `dog_ceo_random` | 99.5% | 93.06% | 722.8 | 10244.1 | 2500ms | 42/605 |
| ✅ | `catfact_random` | 99.5% | 99.5% | 249.8 | 10080.2 | 3000ms | 3/605 |
| ✅ | `coingecko_bitcoin` | 99.5% | 100.0% | 98.6 | 252.0 | 1500ms | 0/605 |
| ✅ | `useless_fact` | 99.67% | 99.34% | 587.8 | 10229.6 | 2500ms | 4/605 |
| ✅ | `agify_name` | 100.0% | 99.83% | 369.8 | 3237.1 | 2000ms | 1/605 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.67% | 238.2 | 3882.8 | 2000ms | 2/605 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `numbers_trivia` | 00:00 | 6148.6 | 60.0% |
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
