# API Reliability Monitor — SLA Report

> Last updated: **2026-06-21 13:23 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **78.9%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 76.85% | 2509.0 | 10206.7 | 1000ms | 266/1149 |
| ❌ | `public_apis_list` | 0.0% | 99.65% | 125.1 | 4595.4 | 1500ms | 4/1149 |
| ❌ | `nasa_apod` | 74.76% | 51.78% | 3261.4 | 11152.5 | 2000ms | 554/1149 |
| ❌ | `ipapi_check` | 76.24% | 99.91% | 155.8 | 4507.0 | 2500ms | 1/1149 |
| ⚠️ | `rest_countries` | 98.69% | 98.35% | 339.4 | 10221.5 | 2500ms | 19/1149 |
| ⚠️ | `open_meteo_weather` | 98.96% | 96.87% | 715.0 | 14877.1 | 2000ms | 36/1149 |
| ✅ | `useless_fact` | 99.56% | 99.65% | 629.8 | 10229.6 | 2500ms | 4/1149 |
| ✅ | `dog_ceo_random` | 99.56% | 96.34% | 553.0 | 10244.1 | 2500ms | 42/1149 |
| ✅ | `catfact_random` | 99.74% | 99.22% | 262.6 | 10080.2 | 3000ms | 9/1149 |
| ✅ | `coingecko_bitcoin` | 99.74% | 100.0% | 96.1 | 253.3 | 1500ms | 0/1149 |
| ✅ | `agify_name` | 99.91% | 99.74% | 377.3 | 16112.2 | 2000ms | 3/1149 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.83% | 218.3 | 3882.8 | 2000ms | 2/1149 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `nasa_apod` | 02:00 | 5333.5 | 66.67% |
| `nasa_apod` | 03:00 | 4897.3 | 80.0% |
| `nasa_apod` | 05:00 | 4415.7 | 66.67% |
| `numbers_trivia` | 03:00 | 4200.6 | 40.0% |
| `nasa_apod` | 17:00 | 4195.0 | 55.56% |
| `nasa_apod` | 09:00 | 4114.4 | 54.0% |
| `nasa_apod` | 01:00 | 3945.6 | 57.14% |
| `nasa_apod` | 11:00 | 3815.6 | 51.61% |
| `nasa_apod` | 18:00 | 3543.5 | 52.63% |
| `nasa_apod` | 14:00 | 3413.5 | 46.3% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
