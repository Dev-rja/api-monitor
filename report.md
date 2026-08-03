# API Reliability Monitor — SLA Report

> Last updated: **2026-08-03 22:15 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **78.2%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 77.69% | 2374.5 | 10420.1 | 1000ms | 381/1708 |
| ❌ | `public_apis_list` | 0.0% | 99.71% | 129.5 | 5052.3 | 1500ms | 5/1708 |
| ❌ | `ipapi_check` | 67.62% | 99.94% | 149.5 | 4507.0 | 2500ms | 1/1708 |
| ❌ | `nasa_apod` | 78.4% | 55.44% | 2923.9 | 11152.5 | 2000ms | 761/1708 |
| ⚠️ | `dog_ceo_random` | 95.55% | 96.66% | 539.9 | 10244.1 | 2500ms | 57/1708 |
| ⚠️ | `open_meteo_weather` | 98.89% | 97.6% | 698.6 | 14877.1 | 2000ms | 41/1708 |
| ✅ | `rest_countries` | 99.12% | 98.77% | 294.1 | 10221.5 | 2500ms | 21/1708 |
| ✅ | `useless_fact` | 99.71% | 99.71% | 644.4 | 10229.6 | 2500ms | 5/1708 |
| ✅ | `catfact_random` | 99.82% | 99.47% | 257.8 | 10080.2 | 3000ms | 9/1708 |
| ✅ | `coingecko_bitcoin` | 99.82% | 99.94% | 96.7 | 4328.4 | 1500ms | 1/1708 |
| ✅ | `agify_name` | 99.88% | 99.77% | 389.5 | 16112.2 | 2000ms | 4/1708 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.88% | 198.8 | 3882.8 | 2000ms | 2/1708 |

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
