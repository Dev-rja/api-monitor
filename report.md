# API Reliability Monitor — SLA Report

> Last updated: **2026-05-26 21:21 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **79.5%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 70.83% | 3103.7 | 10206.7 | 1000ms | 266/912 |
| ❌ | `public_apis_list` | 0.0% | 99.56% | 127.1 | 4595.4 | 1500ms | 4/912 |
| ❌ | `nasa_apod` | 78.62% | 59.1% | 2811.8 | 10549.1 | 2000ms | 373/912 |
| ❌ | `ipapi_check` | 79.17% | 100.0% | 153.7 | 431.8 | 2500ms | 0/912 |
| ⚠️ | `rest_countries` | 98.79% | 98.36% | 338.9 | 10221.5 | 2500ms | 15/912 |
| ⚠️ | `open_meteo_weather` | 98.9% | 96.93% | 703.8 | 14877.1 | 2000ms | 28/912 |
| ✅ | `dog_ceo_random` | 99.45% | 95.39% | 603.8 | 10244.1 | 2500ms | 42/912 |
| ✅ | `catfact_random` | 99.67% | 99.23% | 264.6 | 10080.2 | 3000ms | 7/912 |
| ✅ | `coingecko_bitcoin` | 99.67% | 100.0% | 97.8 | 253.3 | 1500ms | 0/912 |
| ✅ | `useless_fact` | 99.78% | 99.56% | 616.3 | 10229.6 | 2500ms | 4/912 |
| ✅ | `agify_name` | 99.89% | 99.67% | 384.3 | 16112.2 | 2000ms | 3/912 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.78% | 227.5 | 3882.8 | 2000ms | 2/912 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `nasa_apod` | 03:00 | 4729.0 | 77.78% |
| `numbers_trivia` | 03:00 | 4635.3 | 44.44% |
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
