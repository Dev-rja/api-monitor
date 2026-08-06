# API Reliability Monitor — SLA Report

> Last updated: **2026-08-06 03:43 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **78.2%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 76.95% | 2448.5 | 10420.1 | 1000ms | 400/1735 |
| ❌ | `public_apis_list` | 0.0% | 99.71% | 130.4 | 5052.3 | 1500ms | 5/1735 |
| ❌ | `ipapi_check` | 67.09% | 99.94% | 149.4 | 4507.0 | 2500ms | 1/1735 |
| ❌ | `nasa_apod` | 78.67% | 55.73% | 2898.0 | 11152.5 | 2000ms | 768/1735 |
| ⚠️ | `dog_ceo_random` | 95.62% | 96.71% | 537.5 | 10244.1 | 2500ms | 57/1735 |
| ⚠️ | `open_meteo_weather` | 98.9% | 97.64% | 697.6 | 14877.1 | 2000ms | 41/1735 |
| ✅ | `rest_countries` | 99.14% | 98.79% | 293.1 | 10221.5 | 2500ms | 21/1735 |
| ✅ | `useless_fact` | 99.71% | 99.65% | 647.5 | 10229.6 | 2500ms | 6/1735 |
| ✅ | `catfact_random` | 99.83% | 99.48% | 257.9 | 10080.2 | 3000ms | 9/1735 |
| ✅ | `coingecko_bitcoin` | 99.83% | 99.94% | 96.9 | 4328.4 | 1500ms | 1/1735 |
| ✅ | `agify_name` | 99.88% | 99.71% | 392.4 | 16112.2 | 2000ms | 5/1735 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.88% | 198.4 | 3882.8 | 2000ms | 2/1735 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `nasa_apod` | 02:00 | 5333.5 | 66.67% |
| `numbers_trivia` | 03:00 | 4237.5 | 42.42% |
| `nasa_apod` | 05:00 | 4220.5 | 60.0% |
| `nasa_apod` | 09:00 | 3718.2 | 48.57% |
| `nasa_apod` | 03:00 | 3665.6 | 60.61% |
| `nasa_apod` | 17:00 | 3590.5 | 48.86% |
| `numbers_trivia` | 10:00 | 3337.8 | 31.25% |
| `nasa_apod` | 12:00 | 3268.6 | 49.33% |
| `nasa_apod` | 01:00 | 3218.1 | 46.3% |
| `nasa_apod` | 11:00 | 3213.9 | 47.31% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
