# API Reliability Monitor — SLA Report

> Last updated: **2026-08-07 13:18 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **78.2%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 76.29% | 2514.1 | 10420.1 | 1000ms | 415/1750 |
| ❌ | `public_apis_list` | 0.0% | 99.66% | 131.9 | 5052.3 | 1500ms | 6/1750 |
| ❌ | `ipapi_check` | 66.57% | 99.94% | 149.2 | 4507.0 | 2500ms | 1/1750 |
| ❌ | `nasa_apod` | 78.4% | 55.43% | 2924.7 | 11152.5 | 2000ms | 780/1750 |
| ⚠️ | `dog_ceo_random` | 95.66% | 96.74% | 536.1 | 10244.1 | 2500ms | 57/1750 |
| ⚠️ | `open_meteo_weather` | 98.91% | 97.66% | 696.6 | 14877.1 | 2000ms | 41/1750 |
| ✅ | `rest_countries` | 99.14% | 98.8% | 292.4 | 10221.5 | 2500ms | 21/1750 |
| ✅ | `useless_fact` | 99.71% | 99.66% | 647.3 | 10229.6 | 2500ms | 6/1750 |
| ✅ | `catfact_random` | 99.83% | 99.49% | 256.9 | 10080.2 | 3000ms | 9/1750 |
| ✅ | `coingecko_bitcoin` | 99.83% | 99.94% | 96.7 | 4328.4 | 1500ms | 1/1750 |
| ✅ | `agify_name` | 99.89% | 99.71% | 392.0 | 16112.2 | 2000ms | 5/1750 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.89% | 198.1 | 3882.8 | 2000ms | 2/1750 |

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
| `nasa_apod` | 12:00 | 3268.6 | 49.33% |
| `nasa_apod` | 01:00 | 3218.1 | 46.3% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
