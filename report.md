# API Reliability Monitor — SLA Report

> Last updated: **2026-07-26 18:45 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **78.4%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 80.06% | 2160.4 | 10420.1 | 1000ms | 319/1600 |
| ❌ | `public_apis_list` | 0.0% | 99.75% | 124.1 | 4595.4 | 1500ms | 4/1600 |
| ❌ | `ipapi_check` | 70.63% | 99.94% | 150.9 | 4507.0 | 2500ms | 1/1600 |
| ❌ | `nasa_apod` | 77.56% | 54.06% | 3016.2 | 11152.5 | 2000ms | 735/1600 |
| ⚠️ | `dog_ceo_random` | 95.25% | 96.44% | 553.3 | 10244.1 | 2500ms | 57/1600 |
| ⚠️ | `open_meteo_weather` | 98.81% | 97.44% | 707.1 | 14877.1 | 2000ms | 41/1600 |
| ✅ | `rest_countries` | 99.06% | 98.75% | 298.3 | 10221.5 | 2500ms | 20/1600 |
| ✅ | `useless_fact` | 99.69% | 99.75% | 639.2 | 10229.6 | 2500ms | 4/1600 |
| ✅ | `catfact_random` | 99.81% | 99.44% | 256.8 | 10080.2 | 3000ms | 9/1600 |
| ✅ | `coingecko_bitcoin` | 99.81% | 99.94% | 96.2 | 4328.4 | 1500ms | 1/1600 |
| ✅ | `agify_name` | 99.88% | 99.75% | 387.9 | 16112.2 | 2000ms | 4/1600 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.88% | 201.5 | 3882.8 | 2000ms | 2/1600 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `nasa_apod` | 02:00 | 5333.5 | 66.67% |
| `nasa_apod` | 05:00 | 4220.5 | 60.0% |
| `numbers_trivia` | 03:00 | 3922.7 | 37.04% |
| `nasa_apod` | 03:00 | 3903.4 | 66.67% |
| `nasa_apod` | 09:00 | 3672.5 | 48.53% |
| `nasa_apod` | 17:00 | 3672.2 | 50.0% |
| `nasa_apod` | 12:00 | 3420.1 | 52.94% |
| `nasa_apod` | 01:00 | 3367.6 | 48.0% |
| `nasa_apod` | 11:00 | 3341.5 | 49.44% |
| `nasa_apod` | 18:00 | 3208.5 | 46.59% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
