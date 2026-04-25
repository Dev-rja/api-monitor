# API Reliability Monitor — SLA Report

> Last updated: **2026-04-25 23:51 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **5/12** &nbsp;|&nbsp; Avg uptime: **79.1%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 55.44% | 4660.4 | 10206.7 | 1000ms | 221/496 |
| ❌ | `public_apis_list` | 0.0% | 99.6% | 127.4 | 4088.9 | 1500ms | 2/496 |
| ❌ | `nasa_apod` | 63.51% | 39.11% | 4250.5 | 10549.1 | 2000ms | 302/496 |
| ❌ | `ipapi_check` | 90.32% | 100.0% | 157.8 | 353.0 | 2500ms | 0/496 |
| ⚠️ | `open_meteo_weather` | 98.39% | 97.18% | 723.7 | 14877.1 | 2000ms | 14/496 |
| ⚠️ | `rest_countries` | 98.59% | 98.19% | 349.6 | 10221.5 | 2500ms | 9/496 |
| ⚠️ | `dog_ceo_random` | 99.4% | 91.53% | 797.8 | 10244.1 | 2500ms | 42/496 |
| ✅ | `catfact_random` | 99.4% | 99.4% | 261.1 | 10080.2 | 3000ms | 3/496 |
| ✅ | `useless_fact` | 99.6% | 99.19% | 580.9 | 10229.6 | 2500ms | 4/496 |
| ✅ | `coingecko_bitcoin` | 99.8% | 100.0% | 100.5 | 252.0 | 1500ms | 0/496 |
| ✅ | `agify_name` | 100.0% | 99.8% | 371.5 | 3237.1 | 2000ms | 1/496 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.6% | 241.2 | 3882.8 | 2000ms | 2/496 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `numbers_trivia` | 00:00 | 6402.8 | 62.5% |
| `nasa_apod` | 01:00 | 5838.7 | 66.67% |
| `nasa_apod` | 17:00 | 5623.1 | 68.97% |
| `nasa_apod` | 03:00 | 5600.9 | 85.71% |
| `nasa_apod` | 18:00 | 5530.3 | 81.82% |
| `numbers_trivia` | 12:00 | 5436.1 | 52.38% |
| `numbers_trivia` | 18:00 | 5218.5 | 50.0% |
| `numbers_trivia` | 07:00 | 5211.4 | 50.0% |
| `numbers_trivia` | 03:00 | 5200.2 | 50.0% |
| `nasa_apod` | 00:00 | 5195.1 | 75.0% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
