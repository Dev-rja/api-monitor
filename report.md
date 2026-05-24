# API Reliability Monitor — SLA Report

> Last updated: **2026-05-24 09:32 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **79.5%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 69.91% | 3196.2 | 10206.7 | 1000ms | 266/884 |
| ❌ | `public_apis_list` | 0.0% | 99.55% | 128.8 | 4595.4 | 1500ms | 4/884 |
| ❌ | `nasa_apod` | 78.05% | 58.37% | 2865.2 | 10549.1 | 2000ms | 368/884 |
| ❌ | `ipapi_check` | 79.98% | 100.0% | 153.9 | 431.8 | 2500ms | 0/884 |
| ⚠️ | `rest_countries` | 98.76% | 98.3% | 344.1 | 10221.5 | 2500ms | 15/884 |
| ⚠️ | `open_meteo_weather` | 98.98% | 97.17% | 697.2 | 14877.1 | 2000ms | 25/884 |
| ✅ | `dog_ceo_random` | 99.43% | 95.25% | 613.0 | 10244.1 | 2500ms | 42/884 |
| ✅ | `catfact_random` | 99.66% | 99.21% | 267.3 | 10080.2 | 3000ms | 7/884 |
| ✅ | `coingecko_bitcoin` | 99.66% | 100.0% | 97.9 | 253.3 | 1500ms | 0/884 |
| ✅ | `useless_fact` | 99.77% | 99.55% | 615.4 | 10229.6 | 2500ms | 4/884 |
| ✅ | `agify_name` | 99.89% | 99.66% | 387.4 | 16112.2 | 2000ms | 3/884 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.77% | 229.5 | 3882.8 | 2000ms | 2/884 |

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
| `numbers_trivia` | 10:00 | 3642.8 | 34.29% |
| `nasa_apod` | 05:00 | 3555.0 | 60.0% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
