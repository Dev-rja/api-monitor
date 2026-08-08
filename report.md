# API Reliability Monitor — SLA Report

> Last updated: **2026-08-08 22:52 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **78.0%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 74.41% | 2699.9 | 10420.1 | 1000ms | 459/1794 |
| ❌ | `public_apis_list` | 0.0% | 99.67% | 131.0 | 5052.3 | 1500ms | 6/1794 |
| ❌ | `ipapi_check` | 65.05% | 99.94% | 149.0 | 4507.0 | 2500ms | 1/1794 |
| ❌ | `nasa_apod` | 77.76% | 54.68% | 2991.5 | 11152.5 | 2000ms | 813/1794 |
| ⚠️ | `dog_ceo_random` | 95.76% | 96.82% | 531.6 | 10244.1 | 2500ms | 57/1794 |
| ⚠️ | `open_meteo_weather` | 98.94% | 97.71% | 693.2 | 14877.1 | 2000ms | 41/1794 |
| ✅ | `rest_countries` | 99.16% | 98.83% | 291.3 | 10221.5 | 2500ms | 21/1794 |
| ✅ | `useless_fact` | 99.72% | 99.61% | 649.4 | 10229.6 | 2500ms | 7/1794 |
| ✅ | `coingecko_bitcoin` | 99.78% | 99.94% | 97.2 | 4328.4 | 1500ms | 1/1794 |
| ✅ | `catfact_random` | 99.83% | 99.44% | 258.0 | 10080.2 | 3000ms | 10/1794 |
| ✅ | `agify_name` | 99.89% | 99.72% | 390.9 | 16112.2 | 2000ms | 5/1794 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.89% | 197.5 | 3882.8 | 2000ms | 2/1794 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `nasa_apod` | 02:00 | 5124.8 | 70.0% |
| `numbers_trivia` | 03:00 | 4569.7 | 45.71% |
| `nasa_apod` | 05:00 | 4505.5 | 61.9% |
| `nasa_apod` | 03:00 | 3753.8 | 60.0% |
| `nasa_apod` | 09:00 | 3740.6 | 49.32% |
| `nasa_apod` | 17:00 | 3728.4 | 50.55% |
| `numbers_trivia` | 10:00 | 3638.5 | 34.33% |
| `nasa_apod` | 11:00 | 3547.5 | 50.0% |
| `numbers_trivia` | 14:00 | 3365.7 | 32.5% |
| `nasa_apod` | 12:00 | 3268.6 | 49.33% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
