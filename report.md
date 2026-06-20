# API Reliability Monitor — SLA Report

> Last updated: **2026-06-20 13:16 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **78.9%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 76.63% | 2530.9 | 10206.7 | 1000ms | 266/1138 |
| ❌ | `public_apis_list` | 0.0% | 99.65% | 125.4 | 4595.4 | 1500ms | 4/1138 |
| ❌ | `nasa_apod` | 74.96% | 52.02% | 3238.2 | 11152.5 | 2000ms | 546/1138 |
| ❌ | `ipapi_check` | 76.27% | 99.91% | 155.7 | 4507.0 | 2500ms | 1/1138 |
| ⚠️ | `rest_countries` | 98.68% | 98.33% | 340.9 | 10221.5 | 2500ms | 19/1138 |
| ⚠️ | `open_meteo_weather` | 98.95% | 96.84% | 715.9 | 14877.1 | 2000ms | 36/1138 |
| ✅ | `useless_fact` | 99.56% | 99.65% | 629.3 | 10229.6 | 2500ms | 4/1138 |
| ✅ | `dog_ceo_random` | 99.56% | 96.31% | 554.9 | 10244.1 | 2500ms | 42/1138 |
| ✅ | `catfact_random` | 99.74% | 99.21% | 262.8 | 10080.2 | 3000ms | 9/1138 |
| ✅ | `coingecko_bitcoin` | 99.74% | 100.0% | 95.9 | 253.3 | 1500ms | 0/1138 |
| ✅ | `agify_name` | 99.91% | 99.74% | 377.2 | 16112.2 | 2000ms | 3/1138 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.82% | 218.7 | 3882.8 | 2000ms | 2/1138 |

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
| `nasa_apod` | 18:00 | 3597.8 | 53.57% |
| `nasa_apod` | 14:00 | 3413.5 | 46.3% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
