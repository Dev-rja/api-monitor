# API Reliability Monitor — SLA Report

> Last updated: **2026-07-27 20:47 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **78.4%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 79.91% | 2175.7 | 10420.1 | 1000ms | 324/1613 |
| ❌ | `public_apis_list` | 0.0% | 99.75% | 124.4 | 4595.4 | 1500ms | 4/1613 |
| ❌ | `ipapi_check` | 70.18% | 99.94% | 150.5 | 4507.0 | 2500ms | 1/1613 |
| ❌ | `nasa_apod` | 77.74% | 54.31% | 2997.3 | 11152.5 | 2000ms | 737/1613 |
| ⚠️ | `dog_ceo_random` | 95.29% | 96.47% | 551.9 | 10244.1 | 2500ms | 57/1613 |
| ⚠️ | `open_meteo_weather` | 98.82% | 97.46% | 706.3 | 14877.1 | 2000ms | 41/1613 |
| ✅ | `rest_countries` | 99.07% | 98.76% | 297.4 | 10221.5 | 2500ms | 20/1613 |
| ✅ | `useless_fact` | 99.69% | 99.75% | 639.3 | 10229.6 | 2500ms | 4/1613 |
| ✅ | `catfact_random` | 99.81% | 99.44% | 257.2 | 10080.2 | 3000ms | 9/1613 |
| ✅ | `coingecko_bitcoin` | 99.81% | 99.94% | 96.0 | 4328.4 | 1500ms | 1/1613 |
| ✅ | `agify_name` | 99.88% | 99.75% | 388.5 | 16112.2 | 2000ms | 4/1613 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.88% | 200.9 | 3882.8 | 2000ms | 2/1613 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `nasa_apod` | 02:00 | 5333.5 | 66.67% |
| `nasa_apod` | 05:00 | 4220.5 | 60.0% |
| `numbers_trivia` | 03:00 | 3922.7 | 37.04% |
| `nasa_apod` | 03:00 | 3903.4 | 66.67% |
| `nasa_apod` | 09:00 | 3672.5 | 48.53% |
| `nasa_apod` | 17:00 | 3633.5 | 49.4% |
| `nasa_apod` | 12:00 | 3420.1 | 52.94% |
| `nasa_apod` | 01:00 | 3367.6 | 48.0% |
| `nasa_apod` | 11:00 | 3341.5 | 49.44% |
| `nasa_apod` | 18:00 | 3208.5 | 46.59% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
