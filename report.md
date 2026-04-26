# API Reliability Monitor — SLA Report

> Last updated: **2026-04-26 16:05 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **5/12** &nbsp;|&nbsp; Avg uptime: **79.0%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 54.13% | 4788.0 | 10206.7 | 1000ms | 233/508 |
| ❌ | `public_apis_list` | 0.0% | 99.61% | 126.5 | 4088.9 | 1500ms | 2/508 |
| ❌ | `nasa_apod` | 63.98% | 39.57% | 4212.2 | 10549.1 | 2000ms | 307/508 |
| ❌ | `ipapi_check` | 88.98% | 100.0% | 157.3 | 353.0 | 2500ms | 0/508 |
| ⚠️ | `open_meteo_weather` | 98.43% | 97.24% | 720.3 | 14877.1 | 2000ms | 14/508 |
| ⚠️ | `rest_countries` | 98.62% | 98.23% | 346.8 | 10221.5 | 2500ms | 9/508 |
| ⚠️ | `dog_ceo_random` | 99.41% | 91.73% | 787.6 | 10244.1 | 2500ms | 42/508 |
| ✅ | `catfact_random` | 99.41% | 99.41% | 260.9 | 10080.2 | 3000ms | 3/508 |
| ✅ | `useless_fact` | 99.61% | 99.21% | 580.1 | 10229.6 | 2500ms | 4/508 |
| ✅ | `coingecko_bitcoin` | 99.8% | 100.0% | 100.1 | 252.0 | 1500ms | 0/508 |
| ✅ | `agify_name` | 100.0% | 99.8% | 371.6 | 3237.1 | 2000ms | 1/508 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.61% | 241.3 | 3882.8 | 2000ms | 2/508 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `numbers_trivia` | 00:00 | 6402.8 | 62.5% |
| `numbers_trivia` | 01:00 | 5854.0 | 57.14% |
| `numbers_trivia` | 12:00 | 5645.9 | 54.55% |
| `nasa_apod` | 17:00 | 5623.1 | 68.97% |
| `nasa_apod` | 03:00 | 5600.9 | 85.71% |
| `nasa_apod` | 18:00 | 5530.3 | 81.82% |
| `numbers_trivia` | 07:00 | 5499.9 | 52.94% |
| `numbers_trivia` | 16:00 | 5394.5 | 52.17% |
| `numbers_trivia` | 10:00 | 5392.0 | 52.17% |
| `nasa_apod` | 11:00 | 5354.0 | 63.33% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
