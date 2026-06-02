# API Reliability Monitor — SLA Report

> Last updated: **2026-06-02 18:56 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **79.2%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 72.83% | 2907.3 | 10206.7 | 1000ms | 266/979 |
| ❌ | `public_apis_list` | 0.0% | 99.59% | 125.9 | 4595.4 | 1500ms | 4/979 |
| ❌ | `ipapi_check` | 76.0% | 99.9% | 157.0 | 4507.0 | 2500ms | 1/979 |
| ❌ | `nasa_apod` | 78.35% | 57.71% | 2859.3 | 10549.1 | 2000ms | 414/979 |
| ⚠️ | `rest_countries` | 98.47% | 98.16% | 360.8 | 10221.5 | 2500ms | 18/979 |
| ⚠️ | `open_meteo_weather` | 98.98% | 96.94% | 705.0 | 14877.1 | 2000ms | 30/979 |
| ✅ | `dog_ceo_random` | 99.49% | 95.71% | 585.9 | 10244.1 | 2500ms | 42/979 |
| ✅ | `catfact_random` | 99.69% | 99.18% | 267.2 | 10080.2 | 3000ms | 8/979 |
| ✅ | `coingecko_bitcoin` | 99.69% | 100.0% | 97.0 | 253.3 | 1500ms | 0/979 |
| ✅ | `useless_fact` | 99.8% | 99.59% | 620.2 | 10229.6 | 2500ms | 4/979 |
| ✅ | `agify_name` | 99.9% | 99.69% | 382.3 | 16112.2 | 2000ms | 3/979 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.8% | 224.0 | 3882.8 | 2000ms | 2/979 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `nasa_apod` | 03:00 | 4611.9 | 78.95% |
| `numbers_trivia` | 03:00 | 4408.7 | 42.11% |
| `nasa_apod` | 17:00 | 3845.3 | 50.0% |
| `nasa_apod` | 11:00 | 3843.9 | 48.21% |
| `nasa_apod` | 02:00 | 3796.6 | 57.14% |
| `numbers_trivia` | 05:00 | 3674.1 | 34.62% |
| `numbers_trivia` | 07:00 | 3552.2 | 33.33% |
| `nasa_apod` | 09:00 | 3526.1 | 47.73% |
| `nasa_apod` | 05:00 | 3511.6 | 61.54% |
| `numbers_trivia` | 10:00 | 3454.8 | 32.43% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
