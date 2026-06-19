# API Reliability Monitor — SLA Report

> Last updated: **2026-06-19 23:40 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **79.0%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 76.52% | 2541.4 | 10206.7 | 1000ms | 266/1133 |
| ❌ | `public_apis_list` | 0.0% | 99.65% | 125.5 | 4595.4 | 1500ms | 4/1133 |
| ❌ | `nasa_apod` | 74.93% | 52.25% | 3240.3 | 11152.5 | 2000ms | 541/1133 |
| ❌ | `ipapi_check` | 76.26% | 99.91% | 155.7 | 4507.0 | 2500ms | 1/1133 |
| ⚠️ | `rest_countries` | 98.68% | 98.32% | 341.8 | 10221.5 | 2500ms | 19/1133 |
| ⚠️ | `open_meteo_weather` | 98.94% | 96.82% | 716.6 | 14877.1 | 2000ms | 36/1133 |
| ✅ | `dog_ceo_random` | 99.56% | 96.29% | 556.1 | 10244.1 | 2500ms | 42/1133 |
| ✅ | `useless_fact` | 99.74% | 99.65% | 629.1 | 10229.6 | 2500ms | 4/1133 |
| ✅ | `catfact_random` | 99.74% | 99.21% | 263.4 | 10080.2 | 3000ms | 9/1133 |
| ✅ | `coingecko_bitcoin` | 99.74% | 100.0% | 96.1 | 253.3 | 1500ms | 0/1133 |
| ✅ | `agify_name` | 99.91% | 99.74% | 377.8 | 16112.2 | 2000ms | 3/1133 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.82% | 218.9 | 3882.8 | 2000ms | 2/1133 |

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
