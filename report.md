# API Reliability Monitor — SLA Report

> Last updated: **2026-05-05 04:29 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **5/12** &nbsp;|&nbsp; Avg uptime: **79.5%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 59.22% | 4271.5 | 10206.7 | 1000ms | 261/640 |
| ❌ | `public_apis_list` | 0.0% | 99.69% | 122.3 | 4088.9 | 1500ms | 2/640 |
| ❌ | `nasa_apod` | 71.09% | 50.16% | 3500.4 | 10549.1 | 2000ms | 319/640 |
| ❌ | `ipapi_check` | 87.03% | 100.0% | 156.2 | 353.0 | 2500ms | 0/640 |
| ⚠️ | `rest_countries` | 98.59% | 98.28% | 340.9 | 10221.5 | 2500ms | 11/640 |
| ⚠️ | `open_meteo_weather` | 98.75% | 96.72% | 726.2 | 14877.1 | 2000ms | 21/640 |
| ⚠️ | `dog_ceo_random` | 99.53% | 93.44% | 703.8 | 10244.1 | 2500ms | 42/640 |
| ✅ | `catfact_random` | 99.53% | 99.38% | 259.1 | 10080.2 | 3000ms | 4/640 |
| ✅ | `coingecko_bitcoin` | 99.53% | 100.0% | 98.7 | 252.0 | 1500ms | 0/640 |
| ✅ | `useless_fact` | 99.69% | 99.38% | 591.0 | 10229.6 | 2500ms | 4/640 |
| ✅ | `agify_name` | 100.0% | 99.84% | 369.3 | 3237.1 | 2000ms | 1/640 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.69% | 237.1 | 3882.8 | 2000ms | 2/640 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `numbers_trivia` | 00:00 | 5605.3 | 54.55% |
| `numbers_trivia` | 03:00 | 5199.6 | 50.0% |
| `numbers_trivia` | 12:00 | 5183.8 | 50.0% |
| `nasa_apod` | 03:00 | 5080.8 | 81.25% |
| `numbers_trivia` | 07:00 | 4955.2 | 47.62% |
| `nasa_apod` | 17:00 | 4828.5 | 59.46% |
| `numbers_trivia` | 10:00 | 4784.8 | 46.15% |
| `numbers_trivia` | 05:00 | 4708.1 | 45.0% |
| `numbers_trivia` | 01:00 | 4686.2 | 45.45% |
| `numbers_trivia` | 18:00 | 4677.8 | 44.83% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
