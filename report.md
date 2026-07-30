# API Reliability Monitor — SLA Report

> Last updated: **2026-07-30 06:11 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **78.3%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 79.08% | 2250.6 | 10420.1 | 1000ms | 344/1644 |
| ❌ | `public_apis_list` | 0.0% | 99.76% | 125.3 | 4595.4 | 1500ms | 4/1644 |
| ❌ | `ipapi_check` | 69.65% | 99.94% | 150.4 | 4507.0 | 2500ms | 1/1644 |
| ❌ | `nasa_apod` | 77.98% | 54.68% | 2973.3 | 11152.5 | 2000ms | 745/1644 |
| ⚠️ | `dog_ceo_random` | 95.38% | 96.53% | 548.0 | 10244.1 | 2500ms | 57/1644 |
| ⚠️ | `open_meteo_weather` | 98.84% | 97.51% | 703.2 | 14877.1 | 2000ms | 41/1644 |
| ✅ | `rest_countries` | 99.09% | 98.78% | 296.4 | 10221.5 | 2500ms | 20/1644 |
| ✅ | `useless_fact` | 99.7% | 99.7% | 643.1 | 10229.6 | 2500ms | 5/1644 |
| ✅ | `catfact_random` | 99.82% | 99.45% | 257.2 | 10080.2 | 3000ms | 9/1644 |
| ✅ | `coingecko_bitcoin` | 99.82% | 99.94% | 96.2 | 4328.4 | 1500ms | 1/1644 |
| ✅ | `agify_name` | 99.88% | 99.76% | 388.7 | 16112.2 | 2000ms | 4/1644 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.88% | 200.4 | 3882.8 | 2000ms | 2/1644 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `nasa_apod` | 02:00 | 5333.5 | 66.67% |
| `nasa_apod` | 05:00 | 4220.5 | 60.0% |
| `numbers_trivia` | 03:00 | 4015.9 | 37.93% |
| `nasa_apod` | 03:00 | 4011.2 | 65.52% |
| `nasa_apod` | 09:00 | 3766.1 | 49.28% |
| `nasa_apod` | 17:00 | 3560.0 | 48.24% |
| `nasa_apod` | 12:00 | 3377.7 | 52.17% |
| `nasa_apod` | 01:00 | 3309.8 | 47.06% |
| `nasa_apod` | 11:00 | 3309.8 | 48.89% |
| `nasa_apod` | 18:00 | 3147.7 | 45.56% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
