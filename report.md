# API Reliability Monitor — SLA Report

> Last updated: **2026-08-07 19:17 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **78.1%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 76.03% | 2540.0 | 10420.1 | 1000ms | 421/1756 |
| ❌ | `public_apis_list` | 0.0% | 99.66% | 131.6 | 5052.3 | 1500ms | 6/1756 |
| ❌ | `ipapi_check` | 66.34% | 99.94% | 149.2 | 4507.0 | 2500ms | 1/1756 |
| ❌ | `nasa_apod` | 78.42% | 55.35% | 2932.5 | 11152.5 | 2000ms | 784/1756 |
| ⚠️ | `dog_ceo_random` | 95.67% | 96.75% | 535.4 | 10244.1 | 2500ms | 57/1756 |
| ⚠️ | `open_meteo_weather` | 98.92% | 97.67% | 695.9 | 14877.1 | 2000ms | 41/1756 |
| ✅ | `rest_countries` | 99.15% | 98.8% | 292.2 | 10221.5 | 2500ms | 21/1756 |
| ✅ | `useless_fact` | 99.72% | 99.66% | 647.3 | 10229.6 | 2500ms | 6/1756 |
| ✅ | `catfact_random` | 99.83% | 99.49% | 256.8 | 10080.2 | 3000ms | 9/1756 |
| ✅ | `coingecko_bitcoin` | 99.83% | 99.94% | 96.7 | 4328.4 | 1500ms | 1/1756 |
| ✅ | `agify_name` | 99.89% | 99.72% | 391.6 | 16112.2 | 2000ms | 5/1756 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.89% | 198.0 | 3882.8 | 2000ms | 2/1756 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `nasa_apod` | 02:00 | 5333.5 | 66.67% |
| `numbers_trivia` | 03:00 | 4408.5 | 44.12% |
| `nasa_apod` | 05:00 | 4367.6 | 60.98% |
| `nasa_apod` | 03:00 | 3855.6 | 61.76% |
| `nasa_apod` | 09:00 | 3648.7 | 48.61% |
| `nasa_apod` | 17:00 | 3579.6 | 49.44% |
| `numbers_trivia` | 10:00 | 3440.9 | 32.31% |
| `nasa_apod` | 11:00 | 3405.2 | 48.96% |
| `numbers_trivia` | 14:00 | 3280.1 | 31.65% |
| `nasa_apod` | 12:00 | 3268.6 | 49.33% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
