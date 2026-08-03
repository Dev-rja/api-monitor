# API Reliability Monitor — SLA Report

> Last updated: **2026-08-03 16:10 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **78.2%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 77.88% | 2356.3 | 10420.1 | 1000ms | 377/1704 |
| ❌ | `public_apis_list` | 0.0% | 99.71% | 129.3 | 5052.3 | 1500ms | 5/1704 |
| ❌ | `ipapi_check` | 67.78% | 99.94% | 149.6 | 4507.0 | 2500ms | 1/1704 |
| ❌ | `nasa_apod` | 78.35% | 55.34% | 2929.8 | 11152.5 | 2000ms | 761/1704 |
| ⚠️ | `dog_ceo_random` | 95.54% | 96.65% | 540.5 | 10244.1 | 2500ms | 57/1704 |
| ⚠️ | `open_meteo_weather` | 98.88% | 97.59% | 698.9 | 14877.1 | 2000ms | 41/1704 |
| ✅ | `rest_countries` | 99.12% | 98.77% | 294.3 | 10221.5 | 2500ms | 21/1704 |
| ✅ | `useless_fact` | 99.71% | 99.71% | 644.2 | 10229.6 | 2500ms | 5/1704 |
| ✅ | `catfact_random` | 99.82% | 99.47% | 257.8 | 10080.2 | 3000ms | 9/1704 |
| ✅ | `coingecko_bitcoin` | 99.82% | 99.94% | 96.6 | 4328.4 | 1500ms | 1/1704 |
| ✅ | `agify_name` | 99.88% | 99.77% | 389.6 | 16112.2 | 2000ms | 4/1704 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.88% | 198.9 | 3882.8 | 2000ms | 2/1704 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `nasa_apod` | 02:00 | 5333.5 | 66.67% |
| `nasa_apod` | 05:00 | 4220.5 | 60.0% |
| `numbers_trivia` | 03:00 | 4056.0 | 40.63% |
| `nasa_apod` | 03:00 | 3757.1 | 62.5% |
| `nasa_apod` | 09:00 | 3718.2 | 48.57% |
| `nasa_apod` | 17:00 | 3515.1 | 48.28% |
| `nasa_apod` | 12:00 | 3346.7 | 50.68% |
| `numbers_trivia` | 10:00 | 3280.5 | 30.65% |
| `nasa_apod` | 01:00 | 3257.3 | 46.15% |
| `nasa_apod` | 11:00 | 3213.9 | 47.31% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
