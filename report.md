# API Reliability Monitor — SLA Report

> Last updated: **2026-07-30 21:16 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **78.3%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 79.18% | 2240.3 | 10420.1 | 1000ms | 344/1652 |
| ❌ | `public_apis_list` | 0.0% | 99.76% | 125.6 | 4595.4 | 1500ms | 4/1652 |
| ❌ | `ipapi_check` | 69.37% | 99.94% | 150.2 | 4507.0 | 2500ms | 1/1652 |
| ❌ | `nasa_apod` | 78.09% | 54.84% | 2961.8 | 11152.5 | 2000ms | 746/1652 |
| ⚠️ | `dog_ceo_random` | 95.4% | 96.55% | 547.2 | 10244.1 | 2500ms | 57/1652 |
| ⚠️ | `open_meteo_weather` | 98.85% | 97.52% | 702.7 | 14877.1 | 2000ms | 41/1652 |
| ✅ | `rest_countries` | 99.09% | 98.79% | 295.8 | 10221.5 | 2500ms | 20/1652 |
| ✅ | `useless_fact` | 99.7% | 99.7% | 643.2 | 10229.6 | 2500ms | 5/1652 |
| ✅ | `catfact_random` | 99.82% | 99.46% | 258.0 | 10080.2 | 3000ms | 9/1652 |
| ✅ | `coingecko_bitcoin` | 99.82% | 99.94% | 96.1 | 4328.4 | 1500ms | 1/1652 |
| ✅ | `agify_name` | 99.88% | 99.76% | 389.0 | 16112.2 | 2000ms | 4/1652 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.88% | 200.0 | 3882.8 | 2000ms | 2/1652 |

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
| `nasa_apod` | 01:00 | 3309.8 | 47.06% |
| `nasa_apod` | 11:00 | 3276.0 | 48.35% |
| `nasa_apod` | 18:00 | 3115.7 | 45.05% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
