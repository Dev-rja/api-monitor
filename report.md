# API Reliability Monitor — SLA Report

> Last updated: **2026-08-08 18:27 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **78.0%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 74.75% | 2666.8 | 10420.1 | 1000ms | 451/1786 |
| ❌ | `public_apis_list` | 0.0% | 99.66% | 131.0 | 5052.3 | 1500ms | 6/1786 |
| ❌ | `ipapi_check` | 65.34% | 99.94% | 149.2 | 4507.0 | 2500ms | 1/1786 |
| ❌ | `nasa_apod` | 77.94% | 54.93% | 2971.9 | 11152.5 | 2000ms | 805/1786 |
| ⚠️ | `dog_ceo_random` | 95.74% | 96.81% | 532.5 | 10244.1 | 2500ms | 57/1786 |
| ⚠️ | `open_meteo_weather` | 98.94% | 97.7% | 693.6 | 14877.1 | 2000ms | 41/1786 |
| ✅ | `rest_countries` | 99.16% | 98.82% | 291.8 | 10221.5 | 2500ms | 21/1786 |
| ✅ | `useless_fact` | 99.72% | 99.66% | 647.1 | 10229.6 | 2500ms | 6/1786 |
| ✅ | `coingecko_bitcoin` | 99.78% | 99.94% | 97.3 | 4328.4 | 1500ms | 1/1786 |
| ✅ | `catfact_random` | 99.83% | 99.44% | 258.4 | 10080.2 | 3000ms | 10/1786 |
| ✅ | `agify_name` | 99.89% | 99.72% | 391.0 | 16112.2 | 2000ms | 5/1786 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.89% | 197.8 | 3882.8 | 2000ms | 2/1786 |

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
