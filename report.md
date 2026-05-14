# API Reliability Monitor — SLA Report

> Last updated: **2026-05-14 15:29 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **5/12** &nbsp;|&nbsp; Avg uptime: **79.7%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 65.54% | 3618.1 | 10206.7 | 1000ms | 264/766 |
| ❌ | `public_apis_list` | 0.0% | 99.48% | 131.1 | 4595.4 | 1500ms | 4/766 |
| ❌ | `nasa_apod` | 75.2% | 56.01% | 3105.4 | 10549.1 | 2000ms | 337/766 |
| ❌ | `ipapi_check` | 84.99% | 100.0% | 155.1 | 363.0 | 2500ms | 0/766 |
| ⚠️ | `rest_countries` | 98.69% | 98.17% | 350.0 | 10221.5 | 2500ms | 14/766 |
| ⚠️ | `open_meteo_weather` | 98.83% | 97.0% | 708.4 | 14877.1 | 2000ms | 23/766 |
| ⚠️ | `dog_ceo_random` | 99.48% | 94.52% | 652.9 | 10244.1 | 2500ms | 42/766 |
| ✅ | `catfact_random` | 99.61% | 99.09% | 271.6 | 10080.2 | 3000ms | 7/766 |
| ✅ | `coingecko_bitcoin` | 99.61% | 100.0% | 98.1 | 252.0 | 1500ms | 0/766 |
| ✅ | `useless_fact` | 99.74% | 99.48% | 605.8 | 10229.6 | 2500ms | 4/766 |
| ✅ | `agify_name` | 99.87% | 99.74% | 391.9 | 16112.2 | 2000ms | 2/766 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.74% | 234.1 | 3882.8 | 2000ms | 2/766 |

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
