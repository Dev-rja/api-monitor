# API Reliability Monitor — SLA Report

> Last updated: **2026-07-28 17:07 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **78.4%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 79.91% | 2167.2 | 10420.1 | 1000ms | 326/1623 |
| ❌ | `public_apis_list` | 0.0% | 99.75% | 124.9 | 4595.4 | 1500ms | 4/1623 |
| ❌ | `ipapi_check` | 70.06% | 99.94% | 150.3 | 4507.0 | 2500ms | 1/1623 |
| ❌ | `nasa_apod` | 77.76% | 54.28% | 2997.6 | 11152.5 | 2000ms | 742/1623 |
| ⚠️ | `dog_ceo_random` | 95.32% | 96.49% | 550.6 | 10244.1 | 2500ms | 57/1623 |
| ⚠️ | `open_meteo_weather` | 98.83% | 97.47% | 705.2 | 14877.1 | 2000ms | 41/1623 |
| ✅ | `rest_countries` | 99.08% | 98.77% | 297.1 | 10221.5 | 2500ms | 20/1623 |
| ✅ | `useless_fact` | 99.69% | 99.75% | 639.1 | 10229.6 | 2500ms | 4/1623 |
| ✅ | `catfact_random` | 99.82% | 99.45% | 257.1 | 10080.2 | 3000ms | 9/1623 |
| ✅ | `coingecko_bitcoin` | 99.82% | 99.94% | 95.9 | 4328.4 | 1500ms | 1/1623 |
| ✅ | `agify_name` | 99.88% | 99.75% | 388.6 | 16112.2 | 2000ms | 4/1623 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.88% | 200.7 | 3882.8 | 2000ms | 2/1623 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `nasa_apod` | 02:00 | 5333.5 | 66.67% |
| `nasa_apod` | 05:00 | 4220.5 | 60.0% |
| `nasa_apod` | 03:00 | 4134.2 | 67.86% |
| `numbers_trivia` | 03:00 | 3800.2 | 35.71% |
| `nasa_apod` | 09:00 | 3766.1 | 49.28% |
| `nasa_apod` | 17:00 | 3596.1 | 48.81% |
| `nasa_apod` | 12:00 | 3420.1 | 52.94% |
| `nasa_apod` | 01:00 | 3367.6 | 48.0% |
| `nasa_apod` | 11:00 | 3309.8 | 48.89% |
| `nasa_apod` | 18:00 | 3208.5 | 46.59% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
