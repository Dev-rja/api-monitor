# API Reliability Monitor — SLA Report

> Last updated: **2026-08-08 13:54 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **78.1%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 75.08% | 2633.4 | 10420.1 | 1000ms | 443/1778 |
| ❌ | `public_apis_list` | 0.0% | 99.66% | 130.9 | 5052.3 | 1500ms | 6/1778 |
| ❌ | `ipapi_check` | 65.64% | 99.94% | 149.1 | 4507.0 | 2500ms | 1/1778 |
| ❌ | `nasa_apod` | 77.95% | 54.95% | 2969.9 | 11152.5 | 2000ms | 801/1778 |
| ⚠️ | `dog_ceo_random` | 95.73% | 96.79% | 533.0 | 10244.1 | 2500ms | 57/1778 |
| ⚠️ | `open_meteo_weather` | 98.93% | 97.69% | 694.2 | 14877.1 | 2000ms | 41/1778 |
| ✅ | `rest_countries` | 99.16% | 98.82% | 291.8 | 10221.5 | 2500ms | 21/1778 |
| ✅ | `useless_fact` | 99.72% | 99.66% | 647.1 | 10229.6 | 2500ms | 6/1778 |
| ✅ | `coingecko_bitcoin` | 99.78% | 99.94% | 97.0 | 4328.4 | 1500ms | 1/1778 |
| ✅ | `catfact_random` | 99.83% | 99.49% | 256.5 | 10080.2 | 3000ms | 9/1778 |
| ✅ | `agify_name` | 99.89% | 99.72% | 390.9 | 16112.2 | 2000ms | 5/1778 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.89% | 197.6 | 3882.8 | 2000ms | 2/1778 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `nasa_apod` | 02:00 | 5124.8 | 70.0% |
| `numbers_trivia` | 03:00 | 4569.7 | 45.71% |
| `nasa_apod` | 05:00 | 4505.5 | 61.9% |
| `nasa_apod` | 03:00 | 3753.8 | 60.0% |
| `nasa_apod` | 09:00 | 3740.6 | 49.32% |
| `numbers_trivia` | 10:00 | 3638.5 | 34.33% |
| `nasa_apod` | 17:00 | 3579.6 | 49.44% |
| `nasa_apod` | 11:00 | 3547.5 | 50.0% |
| `numbers_trivia` | 14:00 | 3280.1 | 31.65% |
| `nasa_apod` | 12:00 | 3268.6 | 49.33% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
