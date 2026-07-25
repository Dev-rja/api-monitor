# API Reliability Monitor — SLA Report

> Last updated: **2026-07-25 13:01 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **78.4%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 81.13% | 2061.1 | 10420.1 | 1000ms | 298/1579 |
| ❌ | `public_apis_list` | 0.0% | 99.75% | 123.6 | 4595.4 | 1500ms | 4/1579 |
| ❌ | `ipapi_check` | 71.06% | 99.94% | 151.4 | 4507.0 | 2500ms | 1/1579 |
| ❌ | `nasa_apod` | 77.26% | 53.64% | 3046.7 | 11152.5 | 2000ms | 732/1579 |
| ⚠️ | `dog_ceo_random` | 95.19% | 96.39% | 556.0 | 10244.1 | 2500ms | 57/1579 |
| ⚠️ | `open_meteo_weather` | 98.8% | 97.4% | 708.7 | 14877.1 | 2000ms | 41/1579 |
| ✅ | `rest_countries` | 99.05% | 98.73% | 299.9 | 10221.5 | 2500ms | 20/1579 |
| ✅ | `useless_fact` | 99.68% | 99.75% | 638.6 | 10229.6 | 2500ms | 4/1579 |
| ✅ | `catfact_random` | 99.81% | 99.43% | 256.9 | 10080.2 | 3000ms | 9/1579 |
| ✅ | `coingecko_bitcoin` | 99.81% | 99.94% | 96.5 | 4328.4 | 1500ms | 1/1579 |
| ✅ | `agify_name` | 99.87% | 99.75% | 387.3 | 16112.2 | 2000ms | 4/1579 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.87% | 202.4 | 3882.8 | 2000ms | 2/1579 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `nasa_apod` | 02:00 | 5333.5 | 66.67% |
| `nasa_apod` | 05:00 | 4220.5 | 60.0% |
| `nasa_apod` | 03:00 | 4032.1 | 69.23% |
| `nasa_apod` | 17:00 | 3753.3 | 51.25% |
| `nasa_apod` | 09:00 | 3719.9 | 49.25% |
| `numbers_trivia` | 03:00 | 3679.6 | 34.62% |
| `nasa_apod` | 12:00 | 3420.1 | 52.94% |
| `nasa_apod` | 11:00 | 3373.7 | 50.0% |
| `nasa_apod` | 01:00 | 3367.6 | 48.0% |
| `nasa_apod` | 18:00 | 3252.3 | 46.51% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
