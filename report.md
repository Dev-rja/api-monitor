# API Reliability Monitor — SLA Report

> Last updated: **2026-05-09 18:07 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **5/12** &nbsp;|&nbsp; Avg uptime: **79.6%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 62.93% | 3904.8 | 10206.7 | 1000ms | 261/704 |
| ❌ | `public_apis_list` | 0.0% | 99.57% | 127.0 | 4595.4 | 1500ms | 3/704 |
| ❌ | `nasa_apod` | 73.44% | 53.84% | 3266.4 | 10549.1 | 2000ms | 325/704 |
| ❌ | `ipapi_check` | 85.65% | 100.0% | 155.9 | 363.0 | 2500ms | 0/704 |
| ⚠️ | `rest_countries` | 98.58% | 98.01% | 362.9 | 10221.5 | 2500ms | 14/704 |
| ⚠️ | `open_meteo_weather` | 98.86% | 97.02% | 711.8 | 14877.1 | 2000ms | 21/704 |
| ⚠️ | `dog_ceo_random` | 99.57% | 94.03% | 678.4 | 10244.1 | 2500ms | 42/704 |
| ✅ | `catfact_random` | 99.57% | 99.15% | 270.5 | 10080.2 | 3000ms | 6/704 |
| ✅ | `coingecko_bitcoin` | 99.57% | 100.0% | 98.7 | 252.0 | 1500ms | 0/704 |
| ✅ | `useless_fact` | 99.72% | 99.43% | 601.1 | 10229.6 | 2500ms | 4/704 |
| ✅ | `agify_name` | 99.86% | 99.72% | 392.0 | 16112.2 | 2000ms | 2/704 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.72% | 235.9 | 3882.8 | 2000ms | 2/704 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `nasa_apod` | 03:00 | 4729.0 | 77.78% |
| `numbers_trivia` | 12:00 | 4674.2 | 44.83% |
| `numbers_trivia` | 03:00 | 4635.3 | 44.44% |
| `numbers_trivia` | 07:00 | 4535.2 | 43.48% |
| `numbers_trivia` | 05:00 | 4499.3 | 42.86% |
| `numbers_trivia` | 00:00 | 4460.1 | 42.86% |
| `nasa_apod` | 17:00 | 4398.4 | 53.66% |
| `numbers_trivia` | 01:00 | 4309.0 | 41.67% |
| `numbers_trivia` | 16:00 | 4228.5 | 40.63% |
| `numbers_trivia` | 10:00 | 4190.5 | 40.0% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
