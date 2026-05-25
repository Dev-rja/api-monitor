# API Reliability Monitor — SLA Report

> Last updated: **2026-05-25 00:11 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **7/12** &nbsp;|&nbsp; Avg uptime: **79.5%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 70.31% | 3155.8 | 10206.7 | 1000ms | 266/896 |
| ❌ | `public_apis_list` | 0.0% | 99.55% | 127.8 | 4595.4 | 1500ms | 4/896 |
| ❌ | `nasa_apod` | 78.35% | 58.93% | 2833.2 | 10549.1 | 2000ms | 368/896 |
| ❌ | `ipapi_check` | 79.69% | 100.0% | 153.9 | 431.8 | 2500ms | 0/896 |
| ⚠️ | `rest_countries` | 98.77% | 98.33% | 341.6 | 10221.5 | 2500ms | 15/896 |
| ✅ | `open_meteo_weather` | 99.0% | 97.21% | 694.2 | 14877.1 | 2000ms | 25/896 |
| ✅ | `dog_ceo_random` | 99.44% | 95.31% | 608.9 | 10244.1 | 2500ms | 42/896 |
| ✅ | `catfact_random` | 99.67% | 99.22% | 265.7 | 10080.2 | 3000ms | 7/896 |
| ✅ | `coingecko_bitcoin` | 99.67% | 100.0% | 97.9 | 253.3 | 1500ms | 0/896 |
| ✅ | `useless_fact` | 99.78% | 99.55% | 616.4 | 10229.6 | 2500ms | 4/896 |
| ✅ | `agify_name` | 99.89% | 99.67% | 385.7 | 16112.2 | 2000ms | 3/896 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.78% | 228.6 | 3882.8 | 2000ms | 2/896 |

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
