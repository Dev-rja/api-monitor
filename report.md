# API Reliability Monitor — SLA Report

> Last updated: **2026-05-24 17:28 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **79.5%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 70.11% | 3176.0 | 10206.7 | 1000ms | 266/890 |
| ❌ | `public_apis_list` | 0.0% | 99.55% | 128.4 | 4595.4 | 1500ms | 4/890 |
| ❌ | `nasa_apod` | 78.2% | 58.65% | 2848.9 | 10549.1 | 2000ms | 368/890 |
| ❌ | `ipapi_check` | 79.66% | 100.0% | 153.8 | 431.8 | 2500ms | 0/890 |
| ⚠️ | `rest_countries` | 98.76% | 98.31% | 342.9 | 10221.5 | 2500ms | 15/890 |
| ⚠️ | `open_meteo_weather` | 98.99% | 97.19% | 695.8 | 14877.1 | 2000ms | 25/890 |
| ✅ | `dog_ceo_random` | 99.44% | 95.28% | 611.0 | 10244.1 | 2500ms | 42/890 |
| ✅ | `catfact_random` | 99.66% | 99.21% | 266.7 | 10080.2 | 3000ms | 7/890 |
| ✅ | `coingecko_bitcoin` | 99.66% | 100.0% | 98.0 | 253.3 | 1500ms | 0/890 |
| ✅ | `useless_fact` | 99.78% | 99.55% | 616.5 | 10229.6 | 2500ms | 4/890 |
| ✅ | `agify_name` | 99.89% | 99.66% | 386.9 | 16112.2 | 2000ms | 3/890 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.78% | 229.0 | 3882.8 | 2000ms | 2/890 |

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
