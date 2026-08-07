# API Reliability Monitor — SLA Report

> Last updated: **2026-08-07 00:33 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **78.2%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 76.68% | 2475.0 | 10420.1 | 1000ms | 406/1741 |
| ❌ | `public_apis_list` | 0.0% | 99.71% | 130.2 | 5052.3 | 1500ms | 5/1741 |
| ❌ | `ipapi_check` | 66.86% | 99.94% | 149.3 | 4507.0 | 2500ms | 1/1741 |
| ❌ | `nasa_apod` | 78.69% | 55.6% | 2902.7 | 11152.5 | 2000ms | 773/1741 |
| ⚠️ | `dog_ceo_random` | 95.63% | 96.73% | 536.7 | 10244.1 | 2500ms | 57/1741 |
| ⚠️ | `open_meteo_weather` | 98.91% | 97.65% | 697.0 | 14877.1 | 2000ms | 41/1741 |
| ✅ | `rest_countries` | 99.14% | 98.79% | 292.7 | 10221.5 | 2500ms | 21/1741 |
| ✅ | `useless_fact` | 99.71% | 99.66% | 647.2 | 10229.6 | 2500ms | 6/1741 |
| ✅ | `catfact_random` | 99.83% | 99.48% | 257.5 | 10080.2 | 3000ms | 9/1741 |
| ✅ | `coingecko_bitcoin` | 99.83% | 99.94% | 96.9 | 4328.4 | 1500ms | 1/1741 |
| ✅ | `agify_name` | 99.89% | 99.71% | 392.1 | 16112.2 | 2000ms | 5/1741 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.89% | 198.2 | 3882.8 | 2000ms | 2/1741 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `nasa_apod` | 02:00 | 5333.5 | 66.67% |
| `numbers_trivia` | 03:00 | 4237.5 | 42.42% |
| `nasa_apod` | 05:00 | 4220.5 | 60.0% |
| `nasa_apod` | 09:00 | 3695.6 | 49.3% |
| `nasa_apod` | 03:00 | 3665.6 | 60.61% |
| `nasa_apod` | 17:00 | 3590.5 | 48.86% |
| `numbers_trivia` | 10:00 | 3337.8 | 31.25% |
| `nasa_apod` | 12:00 | 3268.6 | 49.33% |
| `nasa_apod` | 11:00 | 3260.8 | 47.87% |
| `nasa_apod` | 01:00 | 3218.1 | 46.3% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
