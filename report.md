# API Reliability Monitor — SLA Report

> Last updated: **2026-06-12 23:43 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **79.0%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 75.21% | 2671.3 | 10206.7 | 1000ms | 266/1073 |
| ❌ | `public_apis_list` | 0.0% | 99.63% | 125.9 | 4595.4 | 1500ms | 4/1073 |
| ❌ | `nasa_apod` | 75.96% | 54.43% | 3116.9 | 10565.8 | 2000ms | 489/1073 |
| ❌ | `ipapi_check` | 76.42% | 99.91% | 157.0 | 4507.0 | 2500ms | 1/1073 |
| ⚠️ | `rest_countries` | 98.6% | 98.32% | 345.9 | 10221.5 | 2500ms | 18/1073 |
| ⚠️ | `open_meteo_weather` | 98.88% | 96.64% | 722.7 | 14877.1 | 2000ms | 36/1073 |
| ✅ | `dog_ceo_random` | 99.53% | 96.09% | 568.0 | 10244.1 | 2500ms | 42/1073 |
| ✅ | `catfact_random` | 99.72% | 99.16% | 266.1 | 10080.2 | 3000ms | 9/1073 |
| ✅ | `coingecko_bitcoin` | 99.72% | 100.0% | 96.8 | 253.3 | 1500ms | 0/1073 |
| ✅ | `useless_fact` | 99.81% | 99.63% | 626.7 | 10229.6 | 2500ms | 4/1073 |
| ✅ | `agify_name` | 99.91% | 99.72% | 379.0 | 16112.2 | 2000ms | 3/1073 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.81% | 220.6 | 3882.8 | 2000ms | 2/1073 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `nasa_apod` | 03:00 | 4611.9 | 78.95% |
| `nasa_apod` | 02:00 | 4606.1 | 62.5% |
| `numbers_trivia` | 03:00 | 4408.7 | 42.11% |
| `nasa_apod` | 05:00 | 4214.9 | 65.52% |
| `nasa_apod` | 17:00 | 4014.1 | 53.33% |
| `nasa_apod` | 09:00 | 3884.0 | 51.06% |
| `nasa_apod` | 11:00 | 3751.1 | 49.15% |
| `nasa_apod` | 01:00 | 3562.3 | 47.83% |
| `nasa_apod` | 18:00 | 3493.4 | 50.94% |
| `nasa_apod` | 12:00 | 3419.7 | 48.98% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
