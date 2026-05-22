# API Reliability Monitor — SLA Report

> Last updated: **2026-05-22 01:49 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **79.6%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 68.93% | 3294.1 | 10206.7 | 1000ms | 266/856 |
| ❌ | `public_apis_list` | 0.0% | 99.53% | 129.8 | 4595.4 | 1500ms | 4/856 |
| ❌ | `nasa_apod` | 77.69% | 58.06% | 2894.0 | 10549.1 | 2000ms | 359/856 |
| ❌ | `ipapi_check` | 81.31% | 100.0% | 154.3 | 431.8 | 2500ms | 0/856 |
| ⚠️ | `rest_countries` | 98.83% | 98.36% | 337.3 | 10221.5 | 2500ms | 14/856 |
| ⚠️ | `open_meteo_weather` | 98.95% | 97.2% | 695.2 | 14877.1 | 2000ms | 24/856 |
| ✅ | `dog_ceo_random` | 99.42% | 95.09% | 622.4 | 10244.1 | 2500ms | 42/856 |
| ✅ | `catfact_random` | 99.65% | 99.18% | 268.2 | 10080.2 | 3000ms | 7/856 |
| ✅ | `coingecko_bitcoin` | 99.65% | 100.0% | 97.5 | 253.3 | 1500ms | 0/856 |
| ✅ | `useless_fact` | 99.77% | 99.53% | 613.4 | 10229.6 | 2500ms | 4/856 |
| ✅ | `agify_name` | 99.88% | 99.65% | 390.4 | 16112.2 | 2000ms | 3/856 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.77% | 230.9 | 3882.8 | 2000ms | 2/856 |

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
