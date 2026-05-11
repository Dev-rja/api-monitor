# API Reliability Monitor — SLA Report

> Last updated: **2026-05-11 17:10 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **5/12** &nbsp;|&nbsp; Avg uptime: **79.6%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 63.98% | 3766.9 | 10206.7 | 1000ms | 264/733 |
| ❌ | `public_apis_list` | 0.0% | 99.45% | 131.8 | 4595.4 | 1500ms | 4/733 |
| ❌ | `nasa_apod` | 74.08% | 54.84% | 3204.9 | 10549.1 | 2000ms | 331/733 |
| ❌ | `ipapi_check` | 85.68% | 100.0% | 155.7 | 363.0 | 2500ms | 0/733 |
| ⚠️ | `rest_countries` | 98.64% | 98.09% | 356.6 | 10221.5 | 2500ms | 14/733 |
| ⚠️ | `open_meteo_weather` | 98.77% | 97.0% | 709.0 | 14877.1 | 2000ms | 22/733 |
| ⚠️ | `dog_ceo_random` | 99.59% | 94.27% | 666.1 | 10244.1 | 2500ms | 42/733 |
| ✅ | `catfact_random` | 99.59% | 99.05% | 275.3 | 10080.2 | 3000ms | 7/733 |
| ✅ | `coingecko_bitcoin` | 99.59% | 100.0% | 98.6 | 252.0 | 1500ms | 0/733 |
| ✅ | `useless_fact` | 99.73% | 99.45% | 603.0 | 10229.6 | 2500ms | 4/733 |
| ✅ | `agify_name` | 99.86% | 99.73% | 391.6 | 16112.2 | 2000ms | 2/733 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.73% | 235.8 | 3882.8 | 2000ms | 2/733 |

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
