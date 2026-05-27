# API Reliability Monitor — SLA Report

> Last updated: **2026-05-27 14:40 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **79.5%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 71.02% | 3085.1 | 10206.7 | 1000ms | 266/918 |
| ❌ | `public_apis_list` | 0.0% | 99.56% | 127.0 | 4595.4 | 1500ms | 4/918 |
| ❌ | `nasa_apod` | 78.65% | 59.15% | 2809.2 | 10549.1 | 2000ms | 375/918 |
| ❌ | `ipapi_check` | 78.65% | 100.0% | 153.4 | 431.8 | 2500ms | 0/918 |
| ⚠️ | `rest_countries` | 98.8% | 98.37% | 338.2 | 10221.5 | 2500ms | 15/918 |
| ⚠️ | `open_meteo_weather` | 98.91% | 96.95% | 702.9 | 14877.1 | 2000ms | 28/918 |
| ✅ | `dog_ceo_random` | 99.46% | 95.42% | 602.1 | 10244.1 | 2500ms | 42/918 |
| ✅ | `catfact_random` | 99.67% | 99.24% | 263.7 | 10080.2 | 3000ms | 7/918 |
| ✅ | `coingecko_bitcoin` | 99.67% | 100.0% | 97.7 | 253.3 | 1500ms | 0/918 |
| ✅ | `useless_fact` | 99.78% | 99.56% | 616.6 | 10229.6 | 2500ms | 4/918 |
| ✅ | `agify_name` | 99.89% | 99.67% | 384.1 | 16112.2 | 2000ms | 3/918 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.78% | 226.9 | 3882.8 | 2000ms | 2/918 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `nasa_apod` | 03:00 | 4611.9 | 78.95% |
| `numbers_trivia` | 03:00 | 4408.7 | 42.11% |
| `numbers_trivia` | 05:00 | 3808.4 | 36.0% |
| `nasa_apod` | 11:00 | 3686.9 | 46.15% |
| `numbers_trivia` | 07:00 | 3664.8 | 34.48% |
| `nasa_apod` | 17:00 | 3662.8 | 49.06% |
| `numbers_trivia` | 12:00 | 3562.7 | 33.33% |
| `nasa_apod` | 05:00 | 3555.0 | 60.0% |
| `numbers_trivia` | 10:00 | 3544.0 | 33.33% |
| `numbers_trivia` | 14:00 | 3524.3 | 34.78% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
