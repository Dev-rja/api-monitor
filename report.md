# API Reliability Monitor — SLA Report

> Last updated: **2026-05-22 15:21 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **79.6%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 69.07% | 3279.5 | 10206.7 | 1000ms | 266/860 |
| ❌ | `public_apis_list` | 0.0% | 99.53% | 129.9 | 4595.4 | 1500ms | 4/860 |
| ❌ | `nasa_apod` | 77.79% | 58.14% | 2885.4 | 10549.1 | 2000ms | 360/860 |
| ❌ | `ipapi_check` | 81.16% | 100.0% | 154.3 | 431.8 | 2500ms | 0/860 |
| ⚠️ | `rest_countries` | 98.84% | 98.37% | 336.5 | 10221.5 | 2500ms | 14/860 |
| ⚠️ | `open_meteo_weather` | 98.95% | 97.21% | 695.0 | 14877.1 | 2000ms | 24/860 |
| ✅ | `dog_ceo_random` | 99.42% | 95.12% | 620.8 | 10244.1 | 2500ms | 42/860 |
| ✅ | `catfact_random` | 99.65% | 99.19% | 268.1 | 10080.2 | 3000ms | 7/860 |
| ✅ | `coingecko_bitcoin` | 99.65% | 100.0% | 97.7 | 253.3 | 1500ms | 0/860 |
| ✅ | `useless_fact` | 99.77% | 99.53% | 613.6 | 10229.6 | 2500ms | 4/860 |
| ✅ | `agify_name` | 99.88% | 99.65% | 389.7 | 16112.2 | 2000ms | 3/860 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.77% | 230.6 | 3882.8 | 2000ms | 2/860 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `nasa_apod` | 03:00 | 4729.0 | 77.78% |
| `numbers_trivia` | 03:00 | 4635.3 | 44.44% |
| `numbers_trivia` | 07:00 | 3915.1 | 37.04% |
| `nasa_apod` | 17:00 | 3914.7 | 50.0% |
| `numbers_trivia` | 12:00 | 3843.8 | 36.11% |
| `numbers_trivia` | 05:00 | 3808.4 | 36.0% |
| `nasa_apod` | 11:00 | 3767.9 | 46.0% |
| `numbers_trivia` | 10:00 | 3747.3 | 35.29% |
| `numbers_trivia` | 14:00 | 3674.8 | 36.36% |
| `nasa_apod` | 05:00 | 3555.0 | 60.0% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
