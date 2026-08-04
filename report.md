# API Reliability Monitor — SLA Report

> Last updated: **2026-08-04 10:02 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **78.2%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 77.47% | 2397.0 | 10420.1 | 1000ms | 386/1713 |
| ❌ | `public_apis_list` | 0.0% | 99.71% | 129.7 | 5052.3 | 1500ms | 5/1713 |
| ❌ | `ipapi_check` | 67.48% | 99.94% | 149.4 | 4507.0 | 2500ms | 1/1713 |
| ❌ | `nasa_apod` | 78.46% | 55.46% | 2918.6 | 11152.5 | 2000ms | 763/1713 |
| ⚠️ | `dog_ceo_random` | 95.56% | 96.67% | 539.5 | 10244.1 | 2500ms | 57/1713 |
| ⚠️ | `open_meteo_weather` | 98.89% | 97.61% | 698.5 | 14877.1 | 2000ms | 41/1713 |
| ✅ | `rest_countries` | 99.12% | 98.77% | 293.9 | 10221.5 | 2500ms | 21/1713 |
| ✅ | `useless_fact` | 99.71% | 99.71% | 644.6 | 10229.6 | 2500ms | 5/1713 |
| ✅ | `catfact_random` | 99.82% | 99.47% | 257.8 | 10080.2 | 3000ms | 9/1713 |
| ✅ | `coingecko_bitcoin` | 99.82% | 99.94% | 96.7 | 4328.4 | 1500ms | 1/1713 |
| ✅ | `agify_name` | 99.88% | 99.77% | 389.6 | 16112.2 | 2000ms | 4/1713 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.88% | 198.8 | 3882.8 | 2000ms | 2/1713 |

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
| `numbers_trivia` | 10:00 | 3390.0 | 31.75% |
| `nasa_apod` | 12:00 | 3346.7 | 50.68% |
| `nasa_apod` | 01:00 | 3245.5 | 47.17% |
| `nasa_apod` | 11:00 | 3213.9 | 47.31% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
