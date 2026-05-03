# API Reliability Monitor — SLA Report

> Last updated: **2026-05-03 11:31 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **5/12** &nbsp;|&nbsp; Avg uptime: **79.4%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 57.42% | 4448.9 | 10206.7 | 1000ms | 261/613 |
| ❌ | `public_apis_list` | 0.0% | 99.67% | 123.1 | 4088.9 | 1500ms | 2/613 |
| ❌ | `nasa_apod` | 69.82% | 48.12% | 3632.6 | 10549.1 | 2000ms | 318/613 |
| ❌ | `ipapi_check` | 87.28% | 100.0% | 156.3 | 353.0 | 2500ms | 0/613 |
| ⚠️ | `rest_countries` | 98.53% | 98.37% | 339.9 | 10221.5 | 2500ms | 10/613 |
| ⚠️ | `open_meteo_weather` | 98.69% | 97.06% | 716.3 | 14877.1 | 2000ms | 18/613 |
| ⚠️ | `dog_ceo_random` | 99.51% | 93.15% | 718.9 | 10244.1 | 2500ms | 42/613 |
| ✅ | `catfact_random` | 99.51% | 99.51% | 250.7 | 10080.2 | 3000ms | 3/613 |
| ✅ | `coingecko_bitcoin` | 99.51% | 100.0% | 98.3 | 252.0 | 1500ms | 0/613 |
| ✅ | `useless_fact` | 99.67% | 99.35% | 587.5 | 10229.6 | 2500ms | 4/613 |
| ✅ | `agify_name` | 100.0% | 99.84% | 369.2 | 3237.1 | 2000ms | 1/613 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.67% | 237.7 | 3882.8 | 2000ms | 2/613 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `numbers_trivia` | 00:00 | 5605.3 | 54.55% |
| `numbers_trivia` | 12:00 | 5382.0 | 52.0% |
| `numbers_trivia` | 03:00 | 5199.6 | 50.0% |
| `numbers_trivia` | 01:00 | 5126.1 | 50.0% |
| `nasa_apod` | 17:00 | 5085.4 | 62.86% |
| `nasa_apod` | 03:00 | 5080.8 | 81.25% |
| `numbers_trivia` | 18:00 | 5006.2 | 48.15% |
| `numbers_trivia` | 07:00 | 4955.2 | 47.62% |
| `numbers_trivia` | 10:00 | 4784.8 | 46.15% |
| `numbers_trivia` | 14:00 | 4734.2 | 45.45% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
