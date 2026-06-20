# API Reliability Monitor — SLA Report

> Last updated: **2026-06-20 18:17 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **78.9%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 76.69% | 2524.7 | 10206.7 | 1000ms | 266/1141 |
| ❌ | `public_apis_list` | 0.0% | 99.65% | 125.3 | 4595.4 | 1500ms | 4/1141 |
| ❌ | `nasa_apod` | 74.93% | 51.97% | 3241.7 | 11152.5 | 2000ms | 548/1141 |
| ❌ | `ipapi_check` | 76.25% | 99.91% | 155.6 | 4507.0 | 2500ms | 1/1141 |
| ⚠️ | `rest_countries` | 98.69% | 98.33% | 340.5 | 10221.5 | 2500ms | 19/1141 |
| ⚠️ | `open_meteo_weather` | 98.95% | 96.84% | 715.2 | 14877.1 | 2000ms | 36/1141 |
| ✅ | `useless_fact` | 99.56% | 99.65% | 629.0 | 10229.6 | 2500ms | 4/1141 |
| ✅ | `dog_ceo_random` | 99.56% | 96.32% | 554.3 | 10244.1 | 2500ms | 42/1141 |
| ✅ | `catfact_random` | 99.74% | 99.21% | 262.7 | 10080.2 | 3000ms | 9/1141 |
| ✅ | `coingecko_bitcoin` | 99.74% | 100.0% | 95.9 | 253.3 | 1500ms | 0/1141 |
| ✅ | `agify_name` | 99.91% | 99.74% | 377.0 | 16112.2 | 2000ms | 3/1141 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.82% | 218.6 | 3882.8 | 2000ms | 2/1141 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `nasa_apod` | 02:00 | 5333.5 | 66.67% |
| `nasa_apod` | 03:00 | 4611.9 | 78.95% |
| `nasa_apod` | 05:00 | 4415.7 | 66.67% |
| `numbers_trivia` | 03:00 | 4408.7 | 42.11% |
| `nasa_apod` | 17:00 | 4195.0 | 55.56% |
| `nasa_apod` | 09:00 | 4114.4 | 54.0% |
| `nasa_apod` | 01:00 | 3945.6 | 57.14% |
| `nasa_apod` | 11:00 | 3835.6 | 50.82% |
| `nasa_apod` | 18:00 | 3543.5 | 52.63% |
| `nasa_apod` | 14:00 | 3413.5 | 46.3% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
