# API Reliability Monitor — SLA Report

> Last updated: **2026-05-27 11:25 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **79.5%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 70.99% | 3088.1 | 10206.7 | 1000ms | 266/917 |
| ❌ | `public_apis_list` | 0.0% | 99.56% | 127.1 | 4595.4 | 1500ms | 4/917 |
| ❌ | `nasa_apod` | 78.63% | 59.11% | 2812.0 | 10549.1 | 2000ms | 375/917 |
| ❌ | `ipapi_check` | 78.74% | 100.0% | 153.5 | 431.8 | 2500ms | 0/917 |
| ⚠️ | `rest_countries` | 98.8% | 98.36% | 338.2 | 10221.5 | 2500ms | 15/917 |
| ⚠️ | `open_meteo_weather` | 98.91% | 96.95% | 702.9 | 14877.1 | 2000ms | 28/917 |
| ✅ | `dog_ceo_random` | 99.45% | 95.42% | 602.3 | 10244.1 | 2500ms | 42/917 |
| ✅ | `catfact_random` | 99.67% | 99.24% | 263.8 | 10080.2 | 3000ms | 7/917 |
| ✅ | `coingecko_bitcoin` | 99.67% | 100.0% | 97.8 | 253.3 | 1500ms | 0/917 |
| ✅ | `useless_fact` | 99.78% | 99.56% | 616.6 | 10229.6 | 2500ms | 4/917 |
| ✅ | `agify_name` | 99.89% | 99.67% | 384.0 | 16112.2 | 2000ms | 3/917 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.78% | 227.0 | 3882.8 | 2000ms | 2/917 |

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
| `numbers_trivia` | 14:00 | 3594.7 | 35.56% |
| `numbers_trivia` | 12:00 | 3562.7 | 33.33% |
| `nasa_apod` | 05:00 | 3555.0 | 60.0% |
| `numbers_trivia` | 10:00 | 3544.0 | 33.33% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
