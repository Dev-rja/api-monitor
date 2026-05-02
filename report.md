# API Reliability Monitor — SLA Report

> Last updated: **2026-05-02 19:18 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **5/12** &nbsp;|&nbsp; Avg uptime: **79.4%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 56.57% | 4533.3 | 10206.7 | 1000ms | 261/601 |
| ❌ | `public_apis_list` | 0.0% | 99.67% | 123.3 | 4088.9 | 1500ms | 2/601 |
| ❌ | `nasa_apod` | 69.38% | 47.25% | 3679.3 | 10549.1 | 2000ms | 317/601 |
| ❌ | `ipapi_check` | 87.69% | 100.0% | 155.9 | 353.0 | 2500ms | 0/601 |
| ⚠️ | `rest_countries` | 98.5% | 98.34% | 343.2 | 10221.5 | 2500ms | 10/601 |
| ⚠️ | `open_meteo_weather` | 98.67% | 97.17% | 715.2 | 14877.1 | 2000ms | 17/601 |
| ⚠️ | `dog_ceo_random` | 99.5% | 93.01% | 725.1 | 10244.1 | 2500ms | 42/601 |
| ✅ | `catfact_random` | 99.5% | 99.5% | 250.2 | 10080.2 | 3000ms | 3/601 |
| ✅ | `coingecko_bitcoin` | 99.5% | 100.0% | 98.5 | 252.0 | 1500ms | 0/601 |
| ✅ | `useless_fact` | 99.67% | 99.33% | 586.8 | 10229.6 | 2500ms | 4/601 |
| ✅ | `agify_name` | 100.0% | 99.83% | 369.7 | 3237.1 | 2000ms | 1/601 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.67% | 238.5 | 3882.8 | 2000ms | 2/601 |

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
| `numbers_trivia` | 22:00 | 4801.0 | 46.15% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
