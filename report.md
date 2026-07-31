# API Reliability Monitor — SLA Report

> Last updated: **2026-07-31 16:47 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **78.3%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 79.29% | 2228.8 | 10420.1 | 1000ms | 344/1661 |
| ❌ | `public_apis_list` | 0.0% | 99.7% | 128.9 | 5052.3 | 1500ms | 5/1661 |
| ❌ | `ipapi_check` | 69.18% | 99.94% | 150.3 | 4507.0 | 2500ms | 1/1661 |
| ❌ | `nasa_apod` | 78.09% | 54.97% | 2955.3 | 11152.5 | 2000ms | 748/1661 |
| ⚠️ | `dog_ceo_random` | 95.42% | 96.57% | 546.0 | 10244.1 | 2500ms | 57/1661 |
| ⚠️ | `open_meteo_weather` | 98.86% | 97.53% | 702.0 | 14877.1 | 2000ms | 41/1661 |
| ✅ | `rest_countries` | 99.1% | 98.74% | 297.1 | 10221.5 | 2500ms | 21/1661 |
| ✅ | `useless_fact` | 99.7% | 99.7% | 643.9 | 10229.6 | 2500ms | 5/1661 |
| ✅ | `catfact_random` | 99.82% | 99.46% | 258.3 | 10080.2 | 3000ms | 9/1661 |
| ✅ | `coingecko_bitcoin` | 99.82% | 99.94% | 96.9 | 4328.4 | 1500ms | 1/1661 |
| ✅ | `agify_name` | 99.88% | 99.76% | 388.9 | 16112.2 | 2000ms | 4/1661 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.88% | 200.3 | 3882.8 | 2000ms | 2/1661 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `nasa_apod` | 02:00 | 5333.5 | 66.67% |
| `nasa_apod` | 05:00 | 4220.5 | 60.0% |
| `numbers_trivia` | 03:00 | 4015.9 | 37.93% |
| `nasa_apod` | 03:00 | 4011.2 | 65.52% |
| `nasa_apod` | 09:00 | 3718.2 | 48.57% |
| `nasa_apod` | 17:00 | 3560.0 | 48.24% |
| `nasa_apod` | 12:00 | 3293.3 | 50.7% |
| `nasa_apod` | 11:00 | 3276.0 | 48.35% |
| `nasa_apod` | 01:00 | 3257.3 | 46.15% |
| `nasa_apod` | 18:00 | 3115.7 | 45.05% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
