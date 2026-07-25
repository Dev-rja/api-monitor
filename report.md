# API Reliability Monitor — SLA Report

> Last updated: **2026-07-25 19:59 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **78.4%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 80.82% | 2088.6 | 10420.1 | 1000ms | 304/1585 |
| ❌ | `public_apis_list` | 0.0% | 99.75% | 123.8 | 4595.4 | 1500ms | 4/1585 |
| ❌ | `ipapi_check` | 70.85% | 99.94% | 151.2 | 4507.0 | 2500ms | 1/1585 |
| ❌ | `nasa_apod` | 77.35% | 53.69% | 3039.2 | 11152.5 | 2000ms | 734/1585 |
| ⚠️ | `dog_ceo_random` | 95.21% | 96.4% | 555.1 | 10244.1 | 2500ms | 57/1585 |
| ⚠️ | `open_meteo_weather` | 98.8% | 97.41% | 708.2 | 14877.1 | 2000ms | 41/1585 |
| ✅ | `rest_countries` | 99.05% | 98.74% | 299.4 | 10221.5 | 2500ms | 20/1585 |
| ✅ | `useless_fact` | 99.68% | 99.75% | 638.9 | 10229.6 | 2500ms | 4/1585 |
| ✅ | `catfact_random` | 99.81% | 99.43% | 256.7 | 10080.2 | 3000ms | 9/1585 |
| ✅ | `coingecko_bitcoin` | 99.81% | 99.94% | 96.4 | 4328.4 | 1500ms | 1/1585 |
| ✅ | `agify_name` | 99.87% | 99.75% | 387.5 | 16112.2 | 2000ms | 4/1585 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.87% | 202.1 | 3882.8 | 2000ms | 2/1585 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `nasa_apod` | 02:00 | 5333.5 | 66.67% |
| `nasa_apod` | 05:00 | 4220.5 | 60.0% |
| `nasa_apod` | 03:00 | 4032.1 | 69.23% |
| `nasa_apod` | 09:00 | 3719.9 | 49.25% |
| `nasa_apod` | 17:00 | 3710.1 | 50.62% |
| `numbers_trivia` | 03:00 | 3679.6 | 34.62% |
| `nasa_apod` | 12:00 | 3420.1 | 52.94% |
| `nasa_apod` | 11:00 | 3373.7 | 50.0% |
| `nasa_apod` | 01:00 | 3367.6 | 48.0% |
| `nasa_apod` | 18:00 | 3242.2 | 47.13% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
