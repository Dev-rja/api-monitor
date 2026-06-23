# API Reliability Monitor — SLA Report

> Last updated: **2026-06-23 05:42 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **78.9%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 77.15% | 2479.2 | 10206.7 | 1000ms | 266/1164 |
| ❌ | `public_apis_list` | 0.0% | 99.66% | 124.9 | 4595.4 | 1500ms | 4/1164 |
| ❌ | `nasa_apod` | 74.4% | 51.37% | 3295.8 | 11152.5 | 2000ms | 566/1164 |
| ❌ | `ipapi_check` | 76.37% | 99.91% | 155.7 | 4507.0 | 2500ms | 1/1164 |
| ⚠️ | `rest_countries` | 98.71% | 98.37% | 337.7 | 10221.5 | 2500ms | 19/1164 |
| ⚠️ | `open_meteo_weather` | 98.97% | 96.91% | 713.0 | 14877.1 | 2000ms | 36/1164 |
| ✅ | `useless_fact` | 99.57% | 99.66% | 631.0 | 10229.6 | 2500ms | 4/1164 |
| ✅ | `dog_ceo_random` | 99.57% | 96.39% | 550.0 | 10244.1 | 2500ms | 42/1164 |
| ✅ | `catfact_random` | 99.74% | 99.23% | 262.0 | 10080.2 | 3000ms | 9/1164 |
| ✅ | `coingecko_bitcoin` | 99.74% | 100.0% | 95.9 | 253.3 | 1500ms | 0/1164 |
| ✅ | `agify_name` | 99.91% | 99.74% | 376.4 | 16112.2 | 2000ms | 3/1164 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.83% | 217.7 | 3882.8 | 2000ms | 2/1164 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `nasa_apod` | 02:00 | 5333.5 | 66.67% |
| `nasa_apod` | 03:00 | 4897.3 | 80.0% |
| `nasa_apod` | 05:00 | 4788.8 | 68.75% |
| `nasa_apod` | 17:00 | 4293.2 | 56.25% |
| `numbers_trivia` | 03:00 | 4200.6 | 40.0% |
| `nasa_apod` | 01:00 | 4165.7 | 58.62% |
| `nasa_apod` | 09:00 | 4114.4 | 54.0% |
| `nasa_apod` | 11:00 | 3796.3 | 52.38% |
| `nasa_apod` | 18:00 | 3660.2 | 53.45% |
| `nasa_apod` | 14:00 | 3413.5 | 46.3% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
