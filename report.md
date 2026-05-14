# API Reliability Monitor — SLA Report

> Last updated: **2026-05-14 11:06 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **5/12** &nbsp;|&nbsp; Avg uptime: **79.7%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 65.45% | 3626.3 | 10206.7 | 1000ms | 264/764 |
| ❌ | `public_apis_list` | 0.0% | 99.48% | 131.0 | 4595.4 | 1500ms | 4/764 |
| ❌ | `nasa_apod` | 75.13% | 55.89% | 3112.6 | 10549.1 | 2000ms | 337/764 |
| ❌ | `ipapi_check` | 84.95% | 100.0% | 155.1 | 363.0 | 2500ms | 0/764 |
| ⚠️ | `rest_countries` | 98.69% | 98.17% | 350.3 | 10221.5 | 2500ms | 14/764 |
| ⚠️ | `open_meteo_weather` | 98.82% | 96.99% | 708.7 | 14877.1 | 2000ms | 23/764 |
| ⚠️ | `dog_ceo_random` | 99.48% | 94.5% | 653.8 | 10244.1 | 2500ms | 42/764 |
| ✅ | `catfact_random` | 99.61% | 99.08% | 271.9 | 10080.2 | 3000ms | 7/764 |
| ✅ | `coingecko_bitcoin` | 99.61% | 100.0% | 98.1 | 252.0 | 1500ms | 0/764 |
| ✅ | `useless_fact` | 99.74% | 99.48% | 605.7 | 10229.6 | 2500ms | 4/764 |
| ✅ | `agify_name` | 99.87% | 99.74% | 392.1 | 16112.2 | 2000ms | 2/764 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.74% | 234.3 | 3882.8 | 2000ms | 2/764 |

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
| `numbers_trivia` | 14:00 | 3953.7 | 37.5% |
| `numbers_trivia` | 16:00 | 3893.1 | 37.14% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
