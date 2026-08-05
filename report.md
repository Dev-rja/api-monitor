# API Reliability Monitor — SLA Report

> Last updated: **2026-08-05 12:08 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **78.2%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 77.35% | 2408.8 | 10420.1 | 1000ms | 391/1726 |
| ❌ | `public_apis_list` | 0.0% | 99.71% | 130.1 | 5052.3 | 1500ms | 5/1726 |
| ❌ | `ipapi_check` | 67.21% | 99.94% | 149.5 | 4507.0 | 2500ms | 1/1726 |
| ❌ | `nasa_apod` | 78.62% | 55.68% | 2902.9 | 11152.5 | 2000ms | 765/1726 |
| ⚠️ | `dog_ceo_random` | 95.6% | 96.7% | 538.4 | 10244.1 | 2500ms | 57/1726 |
| ⚠️ | `open_meteo_weather` | 98.9% | 97.62% | 697.9 | 14877.1 | 2000ms | 41/1726 |
| ✅ | `rest_countries` | 99.13% | 98.78% | 293.4 | 10221.5 | 2500ms | 21/1726 |
| ✅ | `useless_fact` | 99.71% | 99.71% | 644.8 | 10229.6 | 2500ms | 5/1726 |
| ✅ | `catfact_random` | 99.83% | 99.48% | 257.9 | 10080.2 | 3000ms | 9/1726 |
| ✅ | `coingecko_bitcoin` | 99.83% | 99.94% | 96.8 | 4328.4 | 1500ms | 1/1726 |
| ✅ | `agify_name` | 99.88% | 99.71% | 391.8 | 16112.2 | 2000ms | 5/1726 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.88% | 198.5 | 3882.8 | 2000ms | 2/1726 |

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
| `numbers_trivia` | 10:00 | 3337.8 | 31.25% |
| `nasa_apod` | 12:00 | 3268.6 | 49.33% |
| `nasa_apod` | 01:00 | 3218.1 | 46.3% |
| `nasa_apod` | 11:00 | 3213.9 | 47.31% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
