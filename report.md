# API Reliability Monitor — SLA Report

> Last updated: **2026-05-27 03:31 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **79.5%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 70.93% | 3094.3 | 10206.7 | 1000ms | 266/915 |
| ❌ | `public_apis_list` | 0.0% | 99.56% | 127.0 | 4595.4 | 1500ms | 4/915 |
| ❌ | `nasa_apod` | 78.58% | 59.02% | 2817.1 | 10549.1 | 2000ms | 375/915 |
| ❌ | `ipapi_check` | 78.91% | 100.0% | 153.6 | 431.8 | 2500ms | 0/915 |
| ⚠️ | `rest_countries` | 98.8% | 98.36% | 338.6 | 10221.5 | 2500ms | 15/915 |
| ⚠️ | `open_meteo_weather` | 98.91% | 96.94% | 703.2 | 14877.1 | 2000ms | 28/915 |
| ✅ | `dog_ceo_random` | 99.45% | 95.41% | 602.9 | 10244.1 | 2500ms | 42/915 |
| ✅ | `catfact_random` | 99.67% | 99.23% | 264.1 | 10080.2 | 3000ms | 7/915 |
| ✅ | `coingecko_bitcoin` | 99.67% | 100.0% | 97.8 | 253.3 | 1500ms | 0/915 |
| ✅ | `useless_fact` | 99.78% | 99.56% | 616.6 | 10229.6 | 2500ms | 4/915 |
| ✅ | `agify_name` | 99.89% | 99.67% | 383.9 | 16112.2 | 2000ms | 3/915 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.78% | 227.2 | 3882.8 | 2000ms | 2/915 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `nasa_apod` | 03:00 | 4611.9 | 78.95% |
| `numbers_trivia` | 03:00 | 4408.7 | 42.11% |
| `numbers_trivia` | 05:00 | 3808.4 | 36.0% |
| `numbers_trivia` | 07:00 | 3781.2 | 35.71% |
| `nasa_apod` | 11:00 | 3745.5 | 47.06% |
| `nasa_apod` | 17:00 | 3662.8 | 49.06% |
| `numbers_trivia` | 14:00 | 3594.7 | 35.56% |
| `numbers_trivia` | 12:00 | 3562.7 | 33.33% |
| `nasa_apod` | 05:00 | 3555.0 | 60.0% |
| `numbers_trivia` | 10:00 | 3544.0 | 33.33% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
