# API Reliability Monitor — SLA Report

> Last updated: **2026-06-20 22:43 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **78.9%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 76.75% | 2518.8 | 10206.7 | 1000ms | 266/1144 |
| ❌ | `public_apis_list` | 0.0% | 99.65% | 125.1 | 4595.4 | 1500ms | 4/1144 |
| ❌ | `nasa_apod` | 74.83% | 51.92% | 3251.6 | 11152.5 | 2000ms | 550/1144 |
| ❌ | `ipapi_check` | 76.22% | 99.91% | 155.6 | 4507.0 | 2500ms | 1/1144 |
| ⚠️ | `rest_countries` | 98.69% | 98.34% | 340.0 | 10221.5 | 2500ms | 19/1144 |
| ⚠️ | `open_meteo_weather` | 98.95% | 96.85% | 715.1 | 14877.1 | 2000ms | 36/1144 |
| ✅ | `useless_fact` | 99.56% | 99.65% | 629.2 | 10229.6 | 2500ms | 4/1144 |
| ✅ | `dog_ceo_random` | 99.56% | 96.33% | 553.8 | 10244.1 | 2500ms | 42/1144 |
| ✅ | `catfact_random` | 99.74% | 99.21% | 262.6 | 10080.2 | 3000ms | 9/1144 |
| ✅ | `coingecko_bitcoin` | 99.74% | 100.0% | 96.0 | 253.3 | 1500ms | 0/1144 |
| ✅ | `agify_name` | 99.91% | 99.74% | 377.0 | 16112.2 | 2000ms | 3/1144 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.83% | 218.4 | 3882.8 | 2000ms | 2/1144 |

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
