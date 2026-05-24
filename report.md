# API Reliability Monitor — SLA Report

> Last updated: **2026-05-24 18:42 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **79.5%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 70.15% | 3172.5 | 10206.7 | 1000ms | 266/891 |
| ❌ | `public_apis_list` | 0.0% | 99.55% | 128.3 | 4595.4 | 1500ms | 4/891 |
| ❌ | `nasa_apod` | 78.23% | 58.7% | 2846.2 | 10549.1 | 2000ms | 368/891 |
| ❌ | `ipapi_check` | 79.69% | 100.0% | 153.9 | 431.8 | 2500ms | 0/891 |
| ⚠️ | `rest_countries` | 98.77% | 98.32% | 342.7 | 10221.5 | 2500ms | 15/891 |
| ⚠️ | `open_meteo_weather` | 98.99% | 97.19% | 695.5 | 14877.1 | 2000ms | 25/891 |
| ✅ | `dog_ceo_random` | 99.44% | 95.29% | 610.4 | 10244.1 | 2500ms | 42/891 |
| ✅ | `catfact_random` | 99.66% | 99.21% | 266.5 | 10080.2 | 3000ms | 7/891 |
| ✅ | `coingecko_bitcoin` | 99.66% | 100.0% | 97.9 | 253.3 | 1500ms | 0/891 |
| ✅ | `useless_fact` | 99.78% | 99.55% | 616.6 | 10229.6 | 2500ms | 4/891 |
| ✅ | `agify_name` | 99.89% | 99.66% | 386.6 | 16112.2 | 2000ms | 3/891 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.78% | 229.0 | 3882.8 | 2000ms | 2/891 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `nasa_apod` | 03:00 | 4729.0 | 77.78% |
| `numbers_trivia` | 03:00 | 4635.3 | 44.44% |
| `numbers_trivia` | 05:00 | 3808.4 | 36.0% |
| `numbers_trivia` | 07:00 | 3781.2 | 35.71% |
| `nasa_apod` | 11:00 | 3745.5 | 47.06% |
| `nasa_apod` | 17:00 | 3711.2 | 47.06% |
| `numbers_trivia` | 14:00 | 3674.8 | 36.36% |
| `numbers_trivia` | 12:00 | 3651.1 | 34.21% |
| `nasa_apod` | 05:00 | 3555.0 | 60.0% |
| `numbers_trivia` | 10:00 | 3544.0 | 33.33% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
