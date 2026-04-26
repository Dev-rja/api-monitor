# API Reliability Monitor — SLA Report

> Last updated: **2026-04-26 10:28 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **5/12** &nbsp;|&nbsp; Avg uptime: **79.1%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 54.78% | 4725.1 | 10206.7 | 1000ms | 227/502 |
| ❌ | `public_apis_list` | 0.0% | 99.6% | 126.8 | 4088.9 | 1500ms | 2/502 |
| ❌ | `nasa_apod` | 63.94% | 39.24% | 4218.3 | 10549.1 | 2000ms | 305/502 |
| ❌ | `ipapi_check` | 90.04% | 100.0% | 157.5 | 353.0 | 2500ms | 0/502 |
| ⚠️ | `open_meteo_weather` | 98.41% | 97.21% | 722.4 | 14877.1 | 2000ms | 14/502 |
| ⚠️ | `rest_countries` | 98.61% | 98.21% | 348.2 | 10221.5 | 2500ms | 9/502 |
| ⚠️ | `dog_ceo_random` | 99.4% | 91.63% | 793.3 | 10244.1 | 2500ms | 42/502 |
| ✅ | `catfact_random` | 99.4% | 99.4% | 260.2 | 10080.2 | 3000ms | 3/502 |
| ✅ | `useless_fact` | 99.6% | 99.2% | 580.3 | 10229.6 | 2500ms | 4/502 |
| ✅ | `coingecko_bitcoin` | 99.8% | 100.0% | 100.4 | 252.0 | 1500ms | 0/502 |
| ✅ | `agify_name` | 100.0% | 99.8% | 372.2 | 3237.1 | 2000ms | 1/502 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.6% | 241.4 | 3882.8 | 2000ms | 2/502 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `numbers_trivia` | 00:00 | 6402.8 | 62.5% |
| `numbers_trivia` | 01:00 | 5854.0 | 57.14% |
| `nasa_apod` | 17:00 | 5623.1 | 68.97% |
| `nasa_apod` | 03:00 | 5600.9 | 85.71% |
| `nasa_apod` | 18:00 | 5530.3 | 81.82% |
| `numbers_trivia` | 07:00 | 5499.9 | 52.94% |
| `numbers_trivia` | 12:00 | 5436.1 | 52.38% |
| `numbers_trivia` | 10:00 | 5392.0 | 52.17% |
| `numbers_trivia` | 18:00 | 5218.5 | 50.0% |
| `numbers_trivia` | 05:00 | 5217.3 | 50.0% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
