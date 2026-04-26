# API Reliability Monitor — SLA Report

> Last updated: **2026-04-26 17:00 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **5/12** &nbsp;|&nbsp; Avg uptime: **79.0%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 54.03% | 4798.5 | 10206.7 | 1000ms | 234/509 |
| ❌ | `public_apis_list` | 0.0% | 99.61% | 126.3 | 4088.9 | 1500ms | 2/509 |
| ❌ | `nasa_apod` | 64.05% | 39.49% | 4209.3 | 10549.1 | 2000ms | 308/509 |
| ❌ | `ipapi_check` | 88.8% | 100.0% | 157.2 | 353.0 | 2500ms | 0/509 |
| ⚠️ | `open_meteo_weather` | 98.43% | 97.05% | 731.5 | 14877.1 | 2000ms | 15/509 |
| ⚠️ | `rest_countries` | 98.62% | 98.23% | 346.2 | 10221.5 | 2500ms | 9/509 |
| ⚠️ | `dog_ceo_random` | 99.41% | 91.75% | 786.8 | 10244.1 | 2500ms | 42/509 |
| ✅ | `catfact_random` | 99.41% | 99.41% | 260.5 | 10080.2 | 3000ms | 3/509 |
| ✅ | `useless_fact` | 99.61% | 99.21% | 580.0 | 10229.6 | 2500ms | 4/509 |
| ✅ | `coingecko_bitcoin` | 99.8% | 100.0% | 100.1 | 252.0 | 1500ms | 0/509 |
| ✅ | `agify_name` | 100.0% | 99.8% | 371.2 | 3237.1 | 2000ms | 1/509 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.61% | 241.1 | 3882.8 | 2000ms | 2/509 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `numbers_trivia` | 00:00 | 6402.8 | 62.5% |
| `numbers_trivia` | 01:00 | 5854.0 | 57.14% |
| `numbers_trivia` | 12:00 | 5645.9 | 54.55% |
| `nasa_apod` | 03:00 | 5600.9 | 85.71% |
| `nasa_apod` | 18:00 | 5530.3 | 81.82% |
| `nasa_apod` | 17:00 | 5526.2 | 70.0% |
| `numbers_trivia` | 07:00 | 5499.9 | 52.94% |
| `numbers_trivia` | 16:00 | 5394.5 | 52.17% |
| `numbers_trivia` | 10:00 | 5392.0 | 52.17% |
| `nasa_apod` | 11:00 | 5354.0 | 63.33% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
