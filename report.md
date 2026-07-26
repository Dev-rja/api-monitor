# API Reliability Monitor — SLA Report

> Last updated: **2026-07-26 14:46 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **78.4%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 80.26% | 2142.2 | 10420.1 | 1000ms | 315/1596 |
| ❌ | `public_apis_list` | 0.0% | 99.75% | 124.0 | 4595.4 | 1500ms | 4/1596 |
| ❌ | `ipapi_check` | 70.68% | 99.94% | 151.0 | 4507.0 | 2500ms | 1/1596 |
| ❌ | `nasa_apod` | 77.51% | 53.95% | 3022.6 | 11152.5 | 2000ms | 735/1596 |
| ⚠️ | `dog_ceo_random` | 95.24% | 96.43% | 553.7 | 10244.1 | 2500ms | 57/1596 |
| ⚠️ | `open_meteo_weather` | 98.81% | 97.43% | 707.4 | 14877.1 | 2000ms | 41/1596 |
| ✅ | `rest_countries` | 99.06% | 98.75% | 298.6 | 10221.5 | 2500ms | 20/1596 |
| ✅ | `useless_fact` | 99.69% | 99.75% | 639.1 | 10229.6 | 2500ms | 4/1596 |
| ✅ | `catfact_random` | 99.81% | 99.44% | 256.6 | 10080.2 | 3000ms | 9/1596 |
| ✅ | `coingecko_bitcoin` | 99.81% | 99.94% | 96.2 | 4328.4 | 1500ms | 1/1596 |
| ✅ | `agify_name` | 99.87% | 99.75% | 387.8 | 16112.2 | 2000ms | 4/1596 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.87% | 201.7 | 3882.8 | 2000ms | 2/1596 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `nasa_apod` | 02:00 | 5333.5 | 66.67% |
| `nasa_apod` | 05:00 | 4220.5 | 60.0% |
| `numbers_trivia` | 03:00 | 3922.7 | 37.04% |
| `nasa_apod` | 03:00 | 3903.4 | 66.67% |
| `nasa_apod` | 17:00 | 3710.1 | 50.62% |
| `nasa_apod` | 09:00 | 3672.5 | 48.53% |
| `nasa_apod` | 12:00 | 3420.1 | 52.94% |
| `nasa_apod` | 01:00 | 3367.6 | 48.0% |
| `nasa_apod` | 11:00 | 3341.5 | 49.44% |
| `nasa_apod` | 18:00 | 3242.2 | 47.13% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
