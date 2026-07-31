# API Reliability Monitor — SLA Report

> Last updated: **2026-07-31 04:43 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **78.3%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 79.23% | 2235.2 | 10420.1 | 1000ms | 344/1656 |
| ❌ | `public_apis_list` | 0.0% | 99.76% | 125.8 | 4595.4 | 1500ms | 4/1656 |
| ❌ | `ipapi_check` | 69.32% | 99.94% | 150.2 | 4507.0 | 2500ms | 1/1656 |
| ❌ | `nasa_apod` | 78.02% | 54.89% | 2961.7 | 11152.5 | 2000ms | 747/1656 |
| ⚠️ | `dog_ceo_random` | 95.41% | 96.56% | 546.7 | 10244.1 | 2500ms | 57/1656 |
| ⚠️ | `open_meteo_weather` | 98.85% | 97.52% | 702.2 | 14877.1 | 2000ms | 41/1656 |
| ✅ | `rest_countries` | 99.09% | 98.79% | 295.5 | 10221.5 | 2500ms | 20/1656 |
| ✅ | `useless_fact` | 99.7% | 99.7% | 643.6 | 10229.6 | 2500ms | 5/1656 |
| ✅ | `catfact_random` | 99.82% | 99.46% | 258.1 | 10080.2 | 3000ms | 9/1656 |
| ✅ | `coingecko_bitcoin` | 99.82% | 99.94% | 96.2 | 4328.4 | 1500ms | 1/1656 |
| ✅ | `agify_name` | 99.88% | 99.76% | 388.8 | 16112.2 | 2000ms | 4/1656 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.88% | 200.1 | 3882.8 | 2000ms | 2/1656 |

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
| `nasa_apod` | 12:00 | 3334.2 | 51.43% |
| `nasa_apod` | 11:00 | 3276.0 | 48.35% |
| `nasa_apod` | 01:00 | 3257.3 | 46.15% |
| `nasa_apod` | 18:00 | 3115.7 | 45.05% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
