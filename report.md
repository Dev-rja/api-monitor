# API Reliability Monitor — SLA Report

> Last updated: **2026-05-14 02:42 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **5/12** &nbsp;|&nbsp; Avg uptime: **79.7%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 65.31% | 3638.6 | 10206.7 | 1000ms | 264/761 |
| ❌ | `public_apis_list` | 0.0% | 99.47% | 131.0 | 4595.4 | 1500ms | 4/761 |
| ❌ | `nasa_apod` | 75.03% | 55.85% | 3120.0 | 10549.1 | 2000ms | 336/761 |
| ❌ | `ipapi_check` | 85.15% | 100.0% | 155.1 | 363.0 | 2500ms | 0/761 |
| ⚠️ | `rest_countries` | 98.69% | 98.16% | 350.9 | 10221.5 | 2500ms | 14/761 |
| ⚠️ | `open_meteo_weather` | 98.82% | 96.98% | 709.1 | 14877.1 | 2000ms | 23/761 |
| ⚠️ | `dog_ceo_random` | 99.47% | 94.48% | 653.8 | 10244.1 | 2500ms | 42/761 |
| ✅ | `catfact_random` | 99.61% | 99.08% | 272.2 | 10080.2 | 3000ms | 7/761 |
| ✅ | `coingecko_bitcoin` | 99.61% | 100.0% | 98.1 | 252.0 | 1500ms | 0/761 |
| ✅ | `useless_fact` | 99.74% | 99.47% | 605.4 | 10229.6 | 2500ms | 4/761 |
| ✅ | `agify_name` | 99.87% | 99.74% | 392.3 | 16112.2 | 2000ms | 2/761 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.74% | 234.2 | 3882.8 | 2000ms | 2/761 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `nasa_apod` | 03:00 | 4729.0 | 77.78% |
| `numbers_trivia` | 03:00 | 4635.3 | 44.44% |
| `numbers_trivia` | 07:00 | 4535.2 | 43.48% |
| `numbers_trivia` | 12:00 | 4533.3 | 43.33% |
| `nasa_apod` | 17:00 | 4259.2 | 53.49% |
| `numbers_trivia` | 10:00 | 4190.5 | 40.0% |
| `numbers_trivia` | 00:00 | 4168.3 | 40.0% |
| `numbers_trivia` | 05:00 | 4119.9 | 39.13% |
| `nasa_apod` | 11:00 | 3963.6 | 45.65% |
| `numbers_trivia` | 14:00 | 3953.7 | 37.5% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
