# API Reliability Monitor — SLA Report

> Last updated: **2026-07-28 09:06 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **78.4%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 79.93% | 2170.8 | 10420.1 | 1000ms | 325/1619 |
| ❌ | `public_apis_list` | 0.0% | 99.75% | 124.7 | 4595.4 | 1500ms | 4/1619 |
| ❌ | `ipapi_check` | 70.17% | 99.94% | 150.3 | 4507.0 | 2500ms | 1/1619 |
| ❌ | `nasa_apod` | 77.7% | 54.23% | 3002.6 | 11152.5 | 2000ms | 741/1619 |
| ⚠️ | `dog_ceo_random` | 95.31% | 96.48% | 550.8 | 10244.1 | 2500ms | 57/1619 |
| ⚠️ | `open_meteo_weather` | 98.83% | 97.47% | 705.7 | 14877.1 | 2000ms | 41/1619 |
| ✅ | `rest_countries` | 99.07% | 98.76% | 296.9 | 10221.5 | 2500ms | 20/1619 |
| ✅ | `useless_fact` | 99.69% | 99.75% | 639.2 | 10229.6 | 2500ms | 4/1619 |
| ✅ | `catfact_random` | 99.81% | 99.44% | 257.1 | 10080.2 | 3000ms | 9/1619 |
| ✅ | `coingecko_bitcoin` | 99.81% | 99.94% | 95.9 | 4328.4 | 1500ms | 1/1619 |
| ✅ | `agify_name` | 99.88% | 99.75% | 388.4 | 16112.2 | 2000ms | 4/1619 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.88% | 200.8 | 3882.8 | 2000ms | 2/1619 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `nasa_apod` | 02:00 | 5333.5 | 66.67% |
| `nasa_apod` | 05:00 | 4220.5 | 60.0% |
| `nasa_apod` | 03:00 | 4134.2 | 67.86% |
| `numbers_trivia` | 03:00 | 3800.2 | 35.71% |
| `nasa_apod` | 09:00 | 3766.1 | 49.28% |
| `nasa_apod` | 17:00 | 3633.5 | 49.4% |
| `nasa_apod` | 12:00 | 3420.1 | 52.94% |
| `nasa_apod` | 01:00 | 3367.6 | 48.0% |
| `nasa_apod` | 11:00 | 3341.5 | 49.44% |
| `nasa_apod` | 18:00 | 3208.5 | 46.59% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
