# API Reliability Monitor — SLA Report

> Last updated: **2026-05-02 16:26 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **5/12** &nbsp;|&nbsp; Avg uptime: **79.3%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 56.35% | 4555.1 | 10206.7 | 1000ms | 261/598 |
| ❌ | `public_apis_list` | 0.0% | 99.67% | 123.2 | 4088.9 | 1500ms | 2/598 |
| ❌ | `nasa_apod` | 69.23% | 46.99% | 3695.3 | 10549.1 | 2000ms | 317/598 |
| ❌ | `ipapi_check` | 87.63% | 100.0% | 156.0 | 353.0 | 2500ms | 0/598 |
| ⚠️ | `rest_countries` | 98.49% | 98.33% | 343.7 | 10221.5 | 2500ms | 10/598 |
| ⚠️ | `open_meteo_weather` | 98.66% | 97.16% | 716.1 | 14877.1 | 2000ms | 17/598 |
| ⚠️ | `dog_ceo_random` | 99.5% | 92.98% | 726.7 | 10244.1 | 2500ms | 42/598 |
| ✅ | `catfact_random` | 99.5% | 99.5% | 250.7 | 10080.2 | 3000ms | 3/598 |
| ✅ | `coingecko_bitcoin` | 99.5% | 100.0% | 98.8 | 252.0 | 1500ms | 0/598 |
| ✅ | `useless_fact` | 99.67% | 99.33% | 586.4 | 10229.6 | 2500ms | 4/598 |
| ✅ | `agify_name` | 100.0% | 99.83% | 369.8 | 3237.1 | 2000ms | 1/598 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.67% | 238.7 | 3882.8 | 2000ms | 2/598 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `numbers_trivia` | 00:00 | 6148.6 | 60.0% |
| `numbers_trivia` | 12:00 | 5382.0 | 52.0% |
| `nasa_apod` | 17:00 | 5222.7 | 64.71% |
| `numbers_trivia` | 03:00 | 5199.6 | 50.0% |
| `numbers_trivia` | 18:00 | 5196.2 | 50.0% |
| `numbers_trivia` | 01:00 | 5126.1 | 50.0% |
| `nasa_apod` | 03:00 | 5080.8 | 81.25% |
| `numbers_trivia` | 10:00 | 4972.0 | 48.0% |
| `numbers_trivia` | 07:00 | 4955.2 | 47.62% |
| `numbers_trivia` | 22:00 | 4801.0 | 46.15% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
