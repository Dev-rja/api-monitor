# API Reliability Monitor — SLA Report

> Last updated: **2026-05-13 11:01 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **5/12** &nbsp;|&nbsp; Avg uptime: **79.6%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 64.94% | 3672.8 | 10206.7 | 1000ms | 264/753 |
| ❌ | `public_apis_list` | 0.0% | 99.47% | 131.2 | 4595.4 | 1500ms | 4/753 |
| ❌ | `nasa_apod` | 74.77% | 55.51% | 3145.5 | 10549.1 | 2000ms | 335/753 |
| ❌ | `ipapi_check` | 85.13% | 100.0% | 155.1 | 363.0 | 2500ms | 0/753 |
| ⚠️ | `rest_countries` | 98.67% | 98.14% | 352.8 | 10221.5 | 2500ms | 14/753 |
| ⚠️ | `open_meteo_weather` | 98.8% | 96.95% | 711.4 | 14877.1 | 2000ms | 23/753 |
| ⚠️ | `dog_ceo_random` | 99.47% | 94.42% | 657.4 | 10244.1 | 2500ms | 42/753 |
| ✅ | `catfact_random` | 99.6% | 99.07% | 273.6 | 10080.2 | 3000ms | 7/753 |
| ✅ | `coingecko_bitcoin` | 99.6% | 100.0% | 98.3 | 252.0 | 1500ms | 0/753 |
| ✅ | `useless_fact` | 99.73% | 99.47% | 604.5 | 10229.6 | 2500ms | 4/753 |
| ✅ | `agify_name` | 99.87% | 99.73% | 392.7 | 16112.2 | 2000ms | 2/753 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.73% | 234.7 | 3882.8 | 2000ms | 2/753 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `nasa_apod` | 03:00 | 4729.0 | 77.78% |
| `numbers_trivia` | 03:00 | 4635.3 | 44.44% |
| `numbers_trivia` | 07:00 | 4535.2 | 43.48% |
| `numbers_trivia` | 12:00 | 4533.3 | 43.33% |
| `nasa_apod` | 17:00 | 4259.2 | 53.49% |
| `numbers_trivia` | 10:00 | 4190.5 | 40.0% |
| `numbers_trivia` | 00:00 | 4168.3 | 40.0% |
| `numbers_trivia` | 05:00 | 4119.9 | 39.13% |
| `numbers_trivia` | 16:00 | 3994.4 | 38.24% |
| `nasa_apod` | 11:00 | 3963.6 | 45.65% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
