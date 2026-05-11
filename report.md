# API Reliability Monitor — SLA Report

> Last updated: **2026-05-11 08:46 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **5/12** &nbsp;|&nbsp; Avg uptime: **79.6%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 63.84% | 3781.6 | 10206.7 | 1000ms | 264/730 |
| ❌ | `public_apis_list` | 0.0% | 99.59% | 126.2 | 4595.4 | 1500ms | 3/730 |
| ❌ | `nasa_apod` | 73.97% | 54.66% | 3215.8 | 10549.1 | 2000ms | 331/730 |
| ❌ | `ipapi_check` | 85.89% | 100.0% | 155.7 | 363.0 | 2500ms | 0/730 |
| ⚠️ | `rest_countries` | 98.63% | 98.08% | 357.3 | 10221.5 | 2500ms | 14/730 |
| ⚠️ | `open_meteo_weather` | 98.77% | 96.99% | 709.7 | 14877.1 | 2000ms | 22/730 |
| ⚠️ | `dog_ceo_random` | 99.59% | 94.25% | 667.6 | 10244.1 | 2500ms | 42/730 |
| ✅ | `catfact_random` | 99.59% | 99.04% | 275.3 | 10080.2 | 3000ms | 7/730 |
| ✅ | `coingecko_bitcoin` | 99.59% | 100.0% | 98.6 | 252.0 | 1500ms | 0/730 |
| ✅ | `useless_fact` | 99.73% | 99.45% | 602.6 | 10229.6 | 2500ms | 4/730 |
| ✅ | `agify_name` | 99.86% | 99.73% | 391.6 | 16112.2 | 2000ms | 2/730 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.73% | 234.9 | 3882.8 | 2000ms | 2/730 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `nasa_apod` | 03:00 | 4729.0 | 77.78% |
| `numbers_trivia` | 03:00 | 4635.3 | 44.44% |
| `numbers_trivia` | 07:00 | 4535.2 | 43.48% |
| `numbers_trivia` | 12:00 | 4533.3 | 43.33% |
| `numbers_trivia` | 00:00 | 4460.1 | 42.86% |
| `nasa_apod` | 17:00 | 4350.3 | 54.76% |
| `numbers_trivia` | 05:00 | 4297.7 | 40.91% |
| `numbers_trivia` | 10:00 | 4190.5 | 40.0% |
| `numbers_trivia` | 16:00 | 4111.4 | 39.39% |
| `nasa_apod` | 11:00 | 4102.8 | 46.51% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
