# API Reliability Monitor — SLA Report

> Last updated: **2026-05-24 10:58 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **79.5%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 69.94% | 3192.7 | 10206.7 | 1000ms | 266/885 |
| ❌ | `public_apis_list` | 0.0% | 99.55% | 128.7 | 4595.4 | 1500ms | 4/885 |
| ❌ | `nasa_apod` | 78.08% | 58.42% | 2862.5 | 10549.1 | 2000ms | 368/885 |
| ❌ | `ipapi_check` | 79.89% | 100.0% | 153.9 | 431.8 | 2500ms | 0/885 |
| ⚠️ | `rest_countries` | 98.76% | 98.31% | 343.9 | 10221.5 | 2500ms | 15/885 |
| ⚠️ | `open_meteo_weather` | 98.98% | 97.18% | 696.8 | 14877.1 | 2000ms | 25/885 |
| ✅ | `dog_ceo_random` | 99.44% | 95.25% | 612.6 | 10244.1 | 2500ms | 42/885 |
| ✅ | `catfact_random` | 99.66% | 99.21% | 267.1 | 10080.2 | 3000ms | 7/885 |
| ✅ | `coingecko_bitcoin` | 99.66% | 100.0% | 97.9 | 253.3 | 1500ms | 0/885 |
| ✅ | `useless_fact` | 99.77% | 99.55% | 615.4 | 10229.6 | 2500ms | 4/885 |
| ✅ | `agify_name` | 99.89% | 99.66% | 387.2 | 16112.2 | 2000ms | 3/885 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.77% | 229.4 | 3882.8 | 2000ms | 2/885 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `nasa_apod` | 03:00 | 4729.0 | 77.78% |
| `numbers_trivia` | 03:00 | 4635.3 | 44.44% |
| `numbers_trivia` | 05:00 | 3808.4 | 36.0% |
| `numbers_trivia` | 07:00 | 3781.2 | 35.71% |
| `nasa_apod` | 17:00 | 3778.9 | 48.0% |
| `nasa_apod` | 11:00 | 3745.5 | 47.06% |
| `numbers_trivia` | 12:00 | 3742.4 | 35.14% |
| `numbers_trivia` | 14:00 | 3674.8 | 36.36% |
| `nasa_apod` | 05:00 | 3555.0 | 60.0% |
| `numbers_trivia` | 10:00 | 3544.0 | 33.33% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
