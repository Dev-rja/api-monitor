# API Reliability Monitor — SLA Report

> Last updated: **2026-05-21 23:42 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **79.6%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 68.89% | 3297.7 | 10206.7 | 1000ms | 266/855 |
| ❌ | `public_apis_list` | 0.0% | 99.53% | 129.9 | 4595.4 | 1500ms | 4/855 |
| ❌ | `nasa_apod` | 77.66% | 58.13% | 2894.4 | 10549.1 | 2000ms | 358/855 |
| ❌ | `ipapi_check` | 81.29% | 100.0% | 154.3 | 431.8 | 2500ms | 0/855 |
| ⚠️ | `rest_countries` | 98.83% | 98.36% | 337.5 | 10221.5 | 2500ms | 14/855 |
| ⚠️ | `open_meteo_weather` | 98.95% | 97.19% | 695.4 | 14877.1 | 2000ms | 24/855 |
| ✅ | `dog_ceo_random` | 99.42% | 95.09% | 622.9 | 10244.1 | 2500ms | 42/855 |
| ✅ | `catfact_random` | 99.65% | 99.18% | 268.1 | 10080.2 | 3000ms | 7/855 |
| ✅ | `coingecko_bitcoin` | 99.65% | 100.0% | 97.6 | 253.3 | 1500ms | 0/855 |
| ✅ | `useless_fact` | 99.77% | 99.53% | 611.8 | 10229.6 | 2500ms | 4/855 |
| ✅ | `agify_name` | 99.88% | 99.65% | 390.5 | 16112.2 | 2000ms | 3/855 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.77% | 231.0 | 3882.8 | 2000ms | 2/855 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `nasa_apod` | 03:00 | 4729.0 | 77.78% |
| `numbers_trivia` | 03:00 | 4635.3 | 44.44% |
| `numbers_trivia` | 05:00 | 3963.3 | 37.5% |
| `numbers_trivia` | 12:00 | 3951.0 | 37.14% |
| `numbers_trivia` | 07:00 | 3915.1 | 37.04% |
| `nasa_apod` | 17:00 | 3914.7 | 50.0% |
| `nasa_apod` | 11:00 | 3767.9 | 46.0% |
| `numbers_trivia` | 10:00 | 3747.3 | 35.29% |
| `numbers_trivia` | 14:00 | 3674.8 | 36.36% |
| `nasa_apod` | 05:00 | 3586.6 | 58.33% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
