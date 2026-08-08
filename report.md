# API Reliability Monitor — SLA Report

> Last updated: **2026-08-08 08:09 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **78.1%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 75.42% | 2599.6 | 10420.1 | 1000ms | 435/1770 |
| ❌ | `public_apis_list` | 0.0% | 99.66% | 131.2 | 5052.3 | 1500ms | 6/1770 |
| ❌ | `ipapi_check` | 65.82% | 99.94% | 149.2 | 4507.0 | 2500ms | 1/1770 |
| ❌ | `nasa_apod` | 78.08% | 55.08% | 2956.7 | 11152.5 | 2000ms | 795/1770 |
| ⚠️ | `dog_ceo_random` | 95.71% | 96.78% | 533.9 | 10244.1 | 2500ms | 57/1770 |
| ⚠️ | `open_meteo_weather` | 98.93% | 97.68% | 695.0 | 14877.1 | 2000ms | 41/1770 |
| ✅ | `rest_countries` | 99.15% | 98.81% | 292.2 | 10221.5 | 2500ms | 21/1770 |
| ✅ | `useless_fact` | 99.72% | 99.66% | 647.3 | 10229.6 | 2500ms | 6/1770 |
| ✅ | `catfact_random` | 99.83% | 99.49% | 256.9 | 10080.2 | 3000ms | 9/1770 |
| ✅ | `coingecko_bitcoin` | 99.83% | 99.94% | 97.0 | 4328.4 | 1500ms | 1/1770 |
| ✅ | `agify_name` | 99.89% | 99.72% | 391.4 | 16112.2 | 2000ms | 5/1770 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.89% | 197.8 | 3882.8 | 2000ms | 2/1770 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `nasa_apod` | 02:00 | 5124.8 | 70.0% |
| `numbers_trivia` | 03:00 | 4569.7 | 45.71% |
| `nasa_apod` | 05:00 | 4505.5 | 61.9% |
| `nasa_apod` | 03:00 | 3753.8 | 60.0% |
| `nasa_apod` | 09:00 | 3648.7 | 48.61% |
| `nasa_apod` | 17:00 | 3579.6 | 49.44% |
| `numbers_trivia` | 10:00 | 3440.9 | 32.31% |
| `nasa_apod` | 11:00 | 3405.2 | 48.96% |
| `numbers_trivia` | 14:00 | 3280.1 | 31.65% |
| `nasa_apod` | 12:00 | 3268.6 | 49.33% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
