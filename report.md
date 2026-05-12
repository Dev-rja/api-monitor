# API Reliability Monitor — SLA Report

> Last updated: **2026-05-12 22:47 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **5/12** &nbsp;|&nbsp; Avg uptime: **79.6%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 64.71% | 3695.6 | 10206.7 | 1000ms | 264/748 |
| ❌ | `public_apis_list` | 0.0% | 99.47% | 131.5 | 4595.4 | 1500ms | 4/748 |
| ❌ | `nasa_apod` | 74.6% | 55.21% | 3163.5 | 10549.1 | 2000ms | 335/748 |
| ❌ | `ipapi_check` | 85.16% | 100.0% | 155.5 | 363.0 | 2500ms | 0/748 |
| ⚠️ | `rest_countries` | 98.66% | 98.13% | 353.8 | 10221.5 | 2500ms | 14/748 |
| ⚠️ | `open_meteo_weather` | 98.8% | 96.93% | 712.2 | 14877.1 | 2000ms | 23/748 |
| ⚠️ | `dog_ceo_random` | 99.47% | 94.39% | 658.9 | 10244.1 | 2500ms | 42/748 |
| ✅ | `catfact_random` | 99.6% | 99.06% | 274.4 | 10080.2 | 3000ms | 7/748 |
| ✅ | `coingecko_bitcoin` | 99.6% | 100.0% | 98.3 | 252.0 | 1500ms | 0/748 |
| ✅ | `useless_fact` | 99.73% | 99.47% | 603.9 | 10229.6 | 2500ms | 4/748 |
| ✅ | `agify_name` | 99.87% | 99.73% | 392.2 | 16112.2 | 2000ms | 2/748 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.73% | 234.9 | 3882.8 | 2000ms | 2/748 |

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
| `nasa_apod` | 11:00 | 4043.5 | 46.67% |
| `numbers_trivia` | 01:00 | 4037.8 | 38.46% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
