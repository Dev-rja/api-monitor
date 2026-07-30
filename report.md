# API Reliability Monitor — SLA Report

> Last updated: **2026-07-30 09:04 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **78.3%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 79.09% | 2249.4 | 10420.1 | 1000ms | 344/1645 |
| ❌ | `public_apis_list` | 0.0% | 99.76% | 125.4 | 4595.4 | 1500ms | 4/1645 |
| ❌ | `ipapi_check` | 69.6% | 99.94% | 150.4 | 4507.0 | 2500ms | 1/1645 |
| ❌ | `nasa_apod` | 77.99% | 54.71% | 2971.8 | 11152.5 | 2000ms | 745/1645 |
| ⚠️ | `dog_ceo_random` | 95.38% | 96.53% | 547.9 | 10244.1 | 2500ms | 57/1645 |
| ⚠️ | `open_meteo_weather` | 98.84% | 97.51% | 703.1 | 14877.1 | 2000ms | 41/1645 |
| ✅ | `rest_countries` | 99.09% | 98.78% | 296.3 | 10221.5 | 2500ms | 20/1645 |
| ✅ | `useless_fact` | 99.7% | 99.7% | 643.1 | 10229.6 | 2500ms | 5/1645 |
| ✅ | `catfact_random` | 99.82% | 99.45% | 257.2 | 10080.2 | 3000ms | 9/1645 |
| ✅ | `coingecko_bitcoin` | 99.82% | 99.94% | 96.2 | 4328.4 | 1500ms | 1/1645 |
| ✅ | `agify_name` | 99.88% | 99.76% | 388.6 | 16112.2 | 2000ms | 4/1645 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.88% | 200.3 | 3882.8 | 2000ms | 2/1645 |

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
| `nasa_apod` | 12:00 | 3377.7 | 52.17% |
| `nasa_apod` | 01:00 | 3309.8 | 47.06% |
| `nasa_apod` | 11:00 | 3309.8 | 48.89% |
| `nasa_apod` | 18:00 | 3147.7 | 45.56% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
