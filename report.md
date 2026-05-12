# API Reliability Monitor — SLA Report

> Last updated: **2026-05-12 11:32 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **5/12** &nbsp;|&nbsp; Avg uptime: **79.6%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 64.42% | 3723.6 | 10206.7 | 1000ms | 264/742 |
| ❌ | `public_apis_list` | 0.0% | 99.46% | 131.7 | 4595.4 | 1500ms | 4/742 |
| ❌ | `nasa_apod` | 74.39% | 54.99% | 3182.9 | 10549.1 | 2000ms | 334/742 |
| ❌ | `ipapi_check` | 85.31% | 100.0% | 155.5 | 363.0 | 2500ms | 0/742 |
| ⚠️ | `rest_countries` | 98.65% | 98.11% | 354.9 | 10221.5 | 2500ms | 14/742 |
| ⚠️ | `open_meteo_weather` | 98.79% | 97.04% | 706.8 | 14877.1 | 2000ms | 22/742 |
| ⚠️ | `dog_ceo_random` | 99.6% | 94.34% | 661.7 | 10244.1 | 2500ms | 42/742 |
| ✅ | `catfact_random` | 99.6% | 99.06% | 274.6 | 10080.2 | 3000ms | 7/742 |
| ✅ | `coingecko_bitcoin` | 99.6% | 100.0% | 98.4 | 252.0 | 1500ms | 0/742 |
| ✅ | `useless_fact` | 99.73% | 99.46% | 603.5 | 10229.6 | 2500ms | 4/742 |
| ✅ | `agify_name` | 99.87% | 99.73% | 391.1 | 16112.2 | 2000ms | 2/742 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.73% | 235.2 | 3882.8 | 2000ms | 2/742 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `nasa_apod` | 03:00 | 4729.0 | 77.78% |
| `numbers_trivia` | 03:00 | 4635.3 | 44.44% |
| `numbers_trivia` | 07:00 | 4535.2 | 43.48% |
| `numbers_trivia` | 12:00 | 4533.3 | 43.33% |
| `numbers_trivia` | 05:00 | 4297.7 | 40.91% |
| `nasa_apod` | 17:00 | 4259.2 | 53.49% |
| `numbers_trivia` | 10:00 | 4190.5 | 40.0% |
| `numbers_trivia` | 00:00 | 4168.3 | 40.0% |
| `numbers_trivia` | 16:00 | 4111.4 | 39.39% |
| `nasa_apod` | 11:00 | 4043.5 | 46.67% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
