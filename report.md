# API Reliability Monitor — SLA Report

> Last updated: **2026-06-19 20:02 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **79.0%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 76.46% | 2547.6 | 10206.7 | 1000ms | 266/1130 |
| ❌ | `public_apis_list` | 0.0% | 99.65% | 125.4 | 4595.4 | 1500ms | 4/1130 |
| ❌ | `nasa_apod` | 74.87% | 52.39% | 3239.3 | 11152.5 | 2000ms | 538/1130 |
| ❌ | `ipapi_check` | 76.28% | 99.91% | 155.7 | 4507.0 | 2500ms | 1/1130 |
| ⚠️ | `rest_countries` | 98.67% | 98.32% | 342.3 | 10221.5 | 2500ms | 19/1130 |
| ⚠️ | `open_meteo_weather` | 98.94% | 96.81% | 717.0 | 14877.1 | 2000ms | 36/1130 |
| ✅ | `dog_ceo_random` | 99.56% | 96.28% | 556.8 | 10244.1 | 2500ms | 42/1130 |
| ✅ | `useless_fact` | 99.73% | 99.65% | 628.9 | 10229.6 | 2500ms | 4/1130 |
| ✅ | `catfact_random` | 99.73% | 99.2% | 263.6 | 10080.2 | 3000ms | 9/1130 |
| ✅ | `coingecko_bitcoin` | 99.73% | 100.0% | 96.1 | 253.3 | 1500ms | 0/1130 |
| ✅ | `agify_name` | 99.91% | 99.73% | 378.0 | 16112.2 | 2000ms | 3/1130 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.82% | 219.0 | 3882.8 | 2000ms | 2/1130 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `nasa_apod` | 02:00 | 5333.5 | 66.67% |
| `nasa_apod` | 03:00 | 4611.9 | 78.95% |
| `nasa_apod` | 05:00 | 4415.7 | 66.67% |
| `numbers_trivia` | 03:00 | 4408.7 | 42.11% |
| `nasa_apod` | 17:00 | 4195.0 | 55.56% |
| `nasa_apod` | 09:00 | 4142.5 | 53.06% |
| `nasa_apod` | 01:00 | 3988.3 | 55.56% |
| `nasa_apod` | 11:00 | 3861.7 | 50.0% |
| `nasa_apod` | 18:00 | 3597.8 | 53.57% |
| `nasa_apod` | 14:00 | 3413.5 | 46.3% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
