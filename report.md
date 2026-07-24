# API Reliability Monitor — SLA Report

> Last updated: **2026-07-24 10:50 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **78.4%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 81.96% | 1982.6 | 10353.0 | 1000ms | 282/1563 |
| ❌ | `public_apis_list` | 0.0% | 99.74% | 123.1 | 4595.4 | 1500ms | 4/1563 |
| ❌ | `ipapi_check` | 71.21% | 99.94% | 151.6 | 4507.0 | 2500ms | 1/1563 |
| ❌ | `nasa_apod` | 77.16% | 53.49% | 3056.6 | 11152.5 | 2000ms | 727/1563 |
| ⚠️ | `dog_ceo_random` | 95.14% | 96.35% | 558.3 | 10244.1 | 2500ms | 57/1563 |
| ⚠️ | `open_meteo_weather` | 98.78% | 97.38% | 709.9 | 14877.1 | 2000ms | 41/1563 |
| ✅ | `rest_countries` | 99.04% | 98.72% | 300.8 | 10221.5 | 2500ms | 20/1563 |
| ✅ | `useless_fact` | 99.68% | 99.74% | 638.2 | 10229.6 | 2500ms | 4/1563 |
| ✅ | `catfact_random` | 99.81% | 99.42% | 256.6 | 10080.2 | 3000ms | 9/1563 |
| ✅ | `coingecko_bitcoin` | 99.81% | 99.94% | 96.6 | 4328.4 | 1500ms | 1/1563 |
| ✅ | `agify_name` | 99.87% | 99.74% | 386.5 | 16112.2 | 2000ms | 4/1563 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.87% | 202.5 | 3882.8 | 2000ms | 2/1563 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `nasa_apod` | 02:00 | 5333.5 | 66.67% |
| `nasa_apod` | 05:00 | 4220.5 | 60.0% |
| `nasa_apod` | 03:00 | 4032.1 | 69.23% |
| `nasa_apod` | 17:00 | 3796.8 | 51.9% |
| `nasa_apod` | 09:00 | 3768.6 | 50.0% |
| `numbers_trivia` | 03:00 | 3679.6 | 34.62% |
| `nasa_apod` | 12:00 | 3432.5 | 52.24% |
| `nasa_apod` | 01:00 | 3423.8 | 48.98% |
| `nasa_apod` | 11:00 | 3406.9 | 50.57% |
| `nasa_apod` | 18:00 | 3286.5 | 47.06% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
