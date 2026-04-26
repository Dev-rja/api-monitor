# API Reliability Monitor — SLA Report

> Last updated: **2026-04-26 08:37 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **5/12** &nbsp;|&nbsp; Avg uptime: **79.1%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 55.0% | 4703.7 | 10206.7 | 1000ms | 225/500 |
| ❌ | `public_apis_list` | 0.0% | 99.6% | 127.2 | 4088.9 | 1500ms | 2/500 |
| ❌ | `nasa_apod` | 63.8% | 39.4% | 4225.4 | 10549.1 | 2000ms | 303/500 |
| ❌ | `ipapi_check` | 90.0% | 100.0% | 157.8 | 353.0 | 2500ms | 0/500 |
| ⚠️ | `open_meteo_weather` | 98.4% | 97.2% | 722.7 | 14877.1 | 2000ms | 14/500 |
| ⚠️ | `rest_countries` | 98.6% | 98.2% | 348.5 | 10221.5 | 2500ms | 9/500 |
| ⚠️ | `dog_ceo_random` | 99.4% | 91.6% | 794.5 | 10244.1 | 2500ms | 42/500 |
| ✅ | `catfact_random` | 99.4% | 99.4% | 260.5 | 10080.2 | 3000ms | 3/500 |
| ✅ | `useless_fact` | 99.6% | 99.2% | 580.5 | 10229.6 | 2500ms | 4/500 |
| ✅ | `coingecko_bitcoin` | 99.8% | 100.0% | 100.6 | 252.0 | 1500ms | 0/500 |
| ✅ | `agify_name` | 100.0% | 99.8% | 371.7 | 3237.1 | 2000ms | 1/500 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.6% | 241.8 | 3882.8 | 2000ms | 2/500 |

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
| `numbers_trivia` | 18:00 | 5218.5 | 50.0% |
| `numbers_trivia` | 05:00 | 5217.3 | 50.0% |
| `numbers_trivia` | 03:00 | 5200.2 | 50.0% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
