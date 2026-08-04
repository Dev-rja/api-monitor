# API Reliability Monitor — SLA Report

> Last updated: **2026-08-04 20:02 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **78.2%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 77.3% | 2413.6 | 10420.1 | 1000ms | 390/1718 |
| ❌ | `public_apis_list` | 0.0% | 99.71% | 129.8 | 5052.3 | 1500ms | 5/1718 |
| ❌ | `ipapi_check` | 67.4% | 99.94% | 149.3 | 4507.0 | 2500ms | 1/1718 |
| ❌ | `nasa_apod` | 78.52% | 55.53% | 2912.4 | 11152.5 | 2000ms | 764/1718 |
| ⚠️ | `dog_ceo_random` | 95.58% | 96.68% | 539.2 | 10244.1 | 2500ms | 57/1718 |
| ⚠️ | `open_meteo_weather` | 98.89% | 97.61% | 698.2 | 14877.1 | 2000ms | 41/1718 |
| ✅ | `rest_countries` | 99.13% | 98.78% | 293.5 | 10221.5 | 2500ms | 21/1718 |
| ✅ | `useless_fact` | 99.71% | 99.71% | 644.5 | 10229.6 | 2500ms | 5/1718 |
| ✅ | `catfact_random` | 99.83% | 99.48% | 257.7 | 10080.2 | 3000ms | 9/1718 |
| ✅ | `coingecko_bitcoin` | 99.83% | 99.94% | 96.6 | 4328.4 | 1500ms | 1/1718 |
| ✅ | `agify_name` | 99.88% | 99.77% | 390.2 | 16112.2 | 2000ms | 4/1718 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.88% | 198.6 | 3882.8 | 2000ms | 2/1718 |

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
| `nasa_apod` | 12:00 | 3304.8 | 50.0% |
| `nasa_apod` | 01:00 | 3245.5 | 47.17% |
| `nasa_apod` | 11:00 | 3213.9 | 47.31% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
