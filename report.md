# API Reliability Monitor — SLA Report

> Last updated: **2026-07-25 22:05 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **78.4%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 80.72% | 2098.9 | 10420.1 | 1000ms | 306/1587 |
| ❌ | `public_apis_list` | 0.0% | 99.75% | 123.9 | 4595.4 | 1500ms | 4/1587 |
| ❌ | `ipapi_check` | 70.76% | 99.94% | 151.2 | 4507.0 | 2500ms | 1/1587 |
| ❌ | `nasa_apod` | 77.38% | 53.69% | 3037.5 | 11152.5 | 2000ms | 735/1587 |
| ⚠️ | `dog_ceo_random` | 95.21% | 96.41% | 554.9 | 10244.1 | 2500ms | 57/1587 |
| ⚠️ | `open_meteo_weather` | 98.8% | 97.42% | 708.0 | 14877.1 | 2000ms | 41/1587 |
| ✅ | `rest_countries` | 99.05% | 98.74% | 299.4 | 10221.5 | 2500ms | 20/1587 |
| ✅ | `useless_fact` | 99.68% | 99.75% | 638.9 | 10229.6 | 2500ms | 4/1587 |
| ✅ | `catfact_random` | 99.81% | 99.43% | 256.8 | 10080.2 | 3000ms | 9/1587 |
| ✅ | `coingecko_bitcoin` | 99.81% | 99.94% | 96.4 | 4328.4 | 1500ms | 1/1587 |
| ✅ | `agify_name` | 99.87% | 99.75% | 387.5 | 16112.2 | 2000ms | 4/1587 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.87% | 202.0 | 3882.8 | 2000ms | 2/1587 |

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
