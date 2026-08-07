# API Reliability Monitor — SLA Report

> Last updated: **2026-08-07 15:28 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **78.2%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 76.2% | 2522.8 | 10420.1 | 1000ms | 417/1752 |
| ❌ | `public_apis_list` | 0.0% | 99.66% | 131.8 | 5052.3 | 1500ms | 6/1752 |
| ❌ | `ipapi_check` | 66.5% | 99.94% | 149.1 | 4507.0 | 2500ms | 1/1752 |
| ❌ | `nasa_apod` | 78.37% | 55.42% | 2927.5 | 11152.5 | 2000ms | 781/1752 |
| ⚠️ | `dog_ceo_random` | 95.66% | 96.75% | 535.8 | 10244.1 | 2500ms | 57/1752 |
| ⚠️ | `open_meteo_weather` | 98.92% | 97.66% | 696.3 | 14877.1 | 2000ms | 41/1752 |
| ✅ | `rest_countries` | 99.14% | 98.8% | 292.4 | 10221.5 | 2500ms | 21/1752 |
| ✅ | `useless_fact` | 99.71% | 99.66% | 647.2 | 10229.6 | 2500ms | 6/1752 |
| ✅ | `catfact_random` | 99.83% | 99.49% | 256.9 | 10080.2 | 3000ms | 9/1752 |
| ✅ | `coingecko_bitcoin` | 99.83% | 99.94% | 96.7 | 4328.4 | 1500ms | 1/1752 |
| ✅ | `agify_name` | 99.89% | 99.71% | 391.8 | 16112.2 | 2000ms | 5/1752 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.89% | 198.0 | 3882.8 | 2000ms | 2/1752 |

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
| `nasa_apod` | 11:00 | 3405.2 | 48.96% |
| `numbers_trivia` | 14:00 | 3280.1 | 31.65% |
| `nasa_apod` | 12:00 | 3268.6 | 49.33% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
