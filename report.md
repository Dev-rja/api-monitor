# API Reliability Monitor — SLA Report

> Last updated: **2026-05-11 20:55 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **5/12** &nbsp;|&nbsp; Avg uptime: **79.6%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 64.08% | 3757.0 | 10206.7 | 1000ms | 264/735 |
| ❌ | `public_apis_list` | 0.0% | 99.46% | 132.0 | 4595.4 | 1500ms | 4/735 |
| ❌ | `nasa_apod` | 74.15% | 54.83% | 3200.3 | 10549.1 | 2000ms | 332/735 |
| ❌ | `ipapi_check` | 85.58% | 100.0% | 155.6 | 363.0 | 2500ms | 0/735 |
| ⚠️ | `rest_countries` | 98.64% | 98.1% | 356.0 | 10221.5 | 2500ms | 14/735 |
| ⚠️ | `open_meteo_weather` | 98.78% | 97.01% | 708.4 | 14877.1 | 2000ms | 22/735 |
| ⚠️ | `dog_ceo_random` | 99.59% | 94.29% | 665.0 | 10244.1 | 2500ms | 42/735 |
| ✅ | `catfact_random` | 99.59% | 99.05% | 274.7 | 10080.2 | 3000ms | 7/735 |
| ✅ | `coingecko_bitcoin` | 99.59% | 100.0% | 98.5 | 252.0 | 1500ms | 0/735 |
| ✅ | `useless_fact` | 99.73% | 99.46% | 602.9 | 10229.6 | 2500ms | 4/735 |
| ✅ | `agify_name` | 99.86% | 99.73% | 391.2 | 16112.2 | 2000ms | 2/735 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.73% | 235.5 | 3882.8 | 2000ms | 2/735 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `nasa_apod` | 03:00 | 4729.0 | 77.78% |
| `numbers_trivia` | 03:00 | 4635.3 | 44.44% |
| `numbers_trivia` | 07:00 | 4535.2 | 43.48% |
| `numbers_trivia` | 12:00 | 4533.3 | 43.33% |
| `numbers_trivia` | 00:00 | 4460.1 | 42.86% |
| `numbers_trivia` | 05:00 | 4297.7 | 40.91% |
| `nasa_apod` | 17:00 | 4259.2 | 53.49% |
| `numbers_trivia` | 10:00 | 4190.5 | 40.0% |
| `numbers_trivia` | 16:00 | 4111.4 | 39.39% |
| `numbers_trivia` | 01:00 | 4037.8 | 38.46% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
