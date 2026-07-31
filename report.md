# API Reliability Monitor — SLA Report

> Last updated: **2026-07-31 18:12 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **78.3%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 79.3% | 2227.5 | 10420.1 | 1000ms | 344/1662 |
| ❌ | `public_apis_list` | 0.0% | 99.7% | 129.0 | 5052.3 | 1500ms | 5/1662 |
| ❌ | `ipapi_check` | 69.19% | 99.94% | 150.2 | 4507.0 | 2500ms | 1/1662 |
| ❌ | `nasa_apod` | 78.1% | 54.93% | 2954.8 | 11152.5 | 2000ms | 749/1662 |
| ⚠️ | `dog_ceo_random` | 95.43% | 96.57% | 545.8 | 10244.1 | 2500ms | 57/1662 |
| ⚠️ | `open_meteo_weather` | 98.86% | 97.53% | 702.0 | 14877.1 | 2000ms | 41/1662 |
| ✅ | `rest_countries` | 99.1% | 98.74% | 297.1 | 10221.5 | 2500ms | 21/1662 |
| ✅ | `useless_fact` | 99.7% | 99.7% | 643.9 | 10229.6 | 2500ms | 5/1662 |
| ✅ | `catfact_random` | 99.82% | 99.46% | 258.4 | 10080.2 | 3000ms | 9/1662 |
| ✅ | `coingecko_bitcoin` | 99.82% | 99.94% | 97.0 | 4328.4 | 1500ms | 1/1662 |
| ✅ | `agify_name` | 99.88% | 99.76% | 388.9 | 16112.2 | 2000ms | 4/1662 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.88% | 200.2 | 3882.8 | 2000ms | 2/1662 |

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
| `nasa_apod` | 18:00 | 3106.4 | 45.65% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
