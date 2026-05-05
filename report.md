# API Reliability Monitor — SLA Report

> Last updated: **2026-05-05 17:47 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **5/12** &nbsp;|&nbsp; Avg uptime: **79.5%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 59.6% | 4234.1 | 10206.7 | 1000ms | 261/646 |
| ❌ | `public_apis_list` | 0.0% | 99.69% | 122.4 | 4088.9 | 1500ms | 2/646 |
| ❌ | `nasa_apod` | 71.36% | 50.62% | 3472.5 | 10549.1 | 2000ms | 319/646 |
| ❌ | `ipapi_check` | 87.0% | 100.0% | 156.6 | 363.0 | 2500ms | 0/646 |
| ⚠️ | `rest_countries` | 98.61% | 98.3% | 339.7 | 10221.5 | 2500ms | 11/646 |
| ⚠️ | `open_meteo_weather` | 98.76% | 96.75% | 724.4 | 14877.1 | 2000ms | 21/646 |
| ⚠️ | `dog_ceo_random` | 99.54% | 93.5% | 701.7 | 10244.1 | 2500ms | 42/646 |
| ✅ | `catfact_random` | 99.54% | 99.38% | 258.8 | 10080.2 | 3000ms | 4/646 |
| ✅ | `coingecko_bitcoin` | 99.54% | 100.0% | 98.7 | 252.0 | 1500ms | 0/646 |
| ✅ | `useless_fact` | 99.69% | 99.38% | 593.3 | 10229.6 | 2500ms | 4/646 |
| ✅ | `agify_name` | 100.0% | 99.85% | 369.2 | 3237.1 | 2000ms | 1/646 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.69% | 237.3 | 3882.8 | 2000ms | 2/646 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `numbers_trivia` | 00:00 | 5605.3 | 54.55% |
| `numbers_trivia` | 03:00 | 5199.6 | 50.0% |
| `numbers_trivia` | 12:00 | 5183.8 | 50.0% |
| `nasa_apod` | 03:00 | 5080.8 | 81.25% |
| `numbers_trivia` | 07:00 | 4955.2 | 47.62% |
| `nasa_apod` | 17:00 | 4716.3 | 57.89% |
| `numbers_trivia` | 05:00 | 4708.1 | 45.0% |
| `numbers_trivia` | 01:00 | 4686.2 | 45.45% |
| `numbers_trivia` | 18:00 | 4677.8 | 44.83% |
| `numbers_trivia` | 10:00 | 4616.5 | 44.44% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
