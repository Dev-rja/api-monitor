# API Reliability Monitor — SLA Report

> Last updated: **2026-07-24 22:38 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **78.4%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 81.54% | 2024.9 | 10420.1 | 1000ms | 290/1571 |
| ❌ | `public_apis_list` | 0.0% | 99.75% | 123.5 | 4595.4 | 1500ms | 4/1571 |
| ❌ | `ipapi_check` | 71.1% | 99.94% | 151.5 | 4507.0 | 2500ms | 1/1571 |
| ❌ | `nasa_apod` | 77.21% | 53.53% | 3052.4 | 11152.5 | 2000ms | 730/1571 |
| ⚠️ | `dog_ceo_random` | 95.16% | 96.37% | 557.2 | 10244.1 | 2500ms | 57/1571 |
| ⚠️ | `open_meteo_weather` | 98.79% | 97.39% | 709.5 | 14877.1 | 2000ms | 41/1571 |
| ✅ | `rest_countries` | 99.05% | 98.73% | 300.5 | 10221.5 | 2500ms | 20/1571 |
| ✅ | `useless_fact` | 99.68% | 99.75% | 638.2 | 10229.6 | 2500ms | 4/1571 |
| ✅ | `catfact_random` | 99.81% | 99.43% | 257.2 | 10080.2 | 3000ms | 9/1571 |
| ✅ | `coingecko_bitcoin` | 99.81% | 99.94% | 96.6 | 4328.4 | 1500ms | 1/1571 |
| ✅ | `agify_name` | 99.87% | 99.75% | 387.2 | 16112.2 | 2000ms | 4/1571 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.87% | 202.4 | 3882.8 | 2000ms | 2/1571 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `nasa_apod` | 02:00 | 5333.5 | 66.67% |
| `nasa_apod` | 05:00 | 4220.5 | 60.0% |
| `nasa_apod` | 03:00 | 4032.1 | 69.23% |
| `nasa_apod` | 09:00 | 3768.6 | 50.0% |
| `nasa_apod` | 17:00 | 3753.3 | 51.25% |
| `numbers_trivia` | 03:00 | 3679.6 | 34.62% |
| `nasa_apod` | 01:00 | 3423.8 | 48.98% |
| `nasa_apod` | 12:00 | 3420.1 | 52.94% |
| `nasa_apod` | 11:00 | 3406.9 | 50.57% |
| `nasa_apod` | 18:00 | 3252.3 | 46.51% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
