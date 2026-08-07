# API Reliability Monitor — SLA Report

> Last updated: **2026-08-07 10:12 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **78.2%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 76.42% | 2501.1 | 10420.1 | 1000ms | 412/1747 |
| ❌ | `public_apis_list` | 0.0% | 99.66% | 132.0 | 5052.3 | 1500ms | 6/1747 |
| ❌ | `ipapi_check` | 66.63% | 99.94% | 149.2 | 4507.0 | 2500ms | 1/1747 |
| ❌ | `nasa_apod` | 78.53% | 55.52% | 2912.1 | 11152.5 | 2000ms | 777/1747 |
| ⚠️ | `dog_ceo_random` | 95.65% | 96.74% | 536.3 | 10244.1 | 2500ms | 57/1747 |
| ⚠️ | `open_meteo_weather` | 98.91% | 97.65% | 696.8 | 14877.1 | 2000ms | 41/1747 |
| ✅ | `rest_countries` | 99.14% | 98.8% | 292.5 | 10221.5 | 2500ms | 21/1747 |
| ✅ | `useless_fact` | 99.71% | 99.66% | 647.3 | 10229.6 | 2500ms | 6/1747 |
| ✅ | `catfact_random` | 99.83% | 99.48% | 257.1 | 10080.2 | 3000ms | 9/1747 |
| ✅ | `coingecko_bitcoin` | 99.83% | 99.94% | 96.8 | 4328.4 | 1500ms | 1/1747 |
| ✅ | `agify_name` | 99.89% | 99.71% | 392.0 | 16112.2 | 2000ms | 5/1747 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.89% | 198.2 | 3882.8 | 2000ms | 2/1747 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `nasa_apod` | 02:00 | 5333.5 | 66.67% |
| `numbers_trivia` | 03:00 | 4408.5 | 44.12% |
| `nasa_apod` | 05:00 | 4367.6 | 60.98% |
| `nasa_apod` | 03:00 | 3855.6 | 61.76% |
| `nasa_apod` | 09:00 | 3648.7 | 48.61% |
| `nasa_apod` | 17:00 | 3590.5 | 48.86% |
| `numbers_trivia` | 10:00 | 3440.9 | 32.31% |
| `nasa_apod` | 12:00 | 3268.6 | 49.33% |
| `nasa_apod` | 11:00 | 3260.8 | 47.87% |
| `nasa_apod` | 01:00 | 3218.1 | 46.3% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
