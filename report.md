# API Reliability Monitor — SLA Report

> Last updated: **2026-05-15 00:08 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **5/12** &nbsp;|&nbsp; Avg uptime: **79.7%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 65.8% | 3593.0 | 10206.7 | 1000ms | 264/772 |
| ❌ | `public_apis_list` | 0.0% | 99.48% | 131.2 | 4595.4 | 1500ms | 4/772 |
| ❌ | `nasa_apod` | 75.39% | 56.22% | 3088.8 | 10549.1 | 2000ms | 338/772 |
| ❌ | `ipapi_check` | 84.84% | 100.0% | 155.0 | 363.0 | 2500ms | 0/772 |
| ⚠️ | `rest_countries` | 98.7% | 98.19% | 348.5 | 10221.5 | 2500ms | 14/772 |
| ⚠️ | `open_meteo_weather` | 98.83% | 97.02% | 706.6 | 14877.1 | 2000ms | 23/772 |
| ⚠️ | `dog_ceo_random` | 99.48% | 94.56% | 649.7 | 10244.1 | 2500ms | 42/772 |
| ✅ | `catfact_random` | 99.61% | 99.09% | 271.2 | 10080.2 | 3000ms | 7/772 |
| ✅ | `coingecko_bitcoin` | 99.61% | 100.0% | 98.1 | 252.0 | 1500ms | 0/772 |
| ✅ | `useless_fact` | 99.74% | 99.48% | 605.6 | 10229.6 | 2500ms | 4/772 |
| ✅ | `agify_name` | 99.87% | 99.74% | 391.3 | 16112.2 | 2000ms | 2/772 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.74% | 233.6 | 3882.8 | 2000ms | 2/772 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `nasa_apod` | 03:00 | 4729.0 | 77.78% |
| `numbers_trivia` | 03:00 | 4635.3 | 44.44% |
| `numbers_trivia` | 07:00 | 4535.2 | 43.48% |
| `numbers_trivia` | 12:00 | 4533.3 | 43.33% |
| `numbers_trivia` | 10:00 | 4190.5 | 40.0% |
| `nasa_apod` | 17:00 | 4177.6 | 52.27% |
| `numbers_trivia` | 05:00 | 4119.9 | 39.13% |
| `numbers_trivia` | 14:00 | 3953.7 | 37.5% |
| `numbers_trivia` | 00:00 | 3937.7 | 37.5% |
| `numbers_trivia` | 16:00 | 3893.1 | 37.14% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
