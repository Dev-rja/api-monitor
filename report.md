# API Reliability Monitor — SLA Report

> Last updated: **2026-05-08 20:04 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **5/12** &nbsp;|&nbsp; Avg uptime: **79.6%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 62.06% | 3989.8 | 10206.7 | 1000ms | 261/688 |
| ❌ | `public_apis_list` | 0.0% | 99.56% | 127.7 | 4595.4 | 1500ms | 3/688 |
| ❌ | `nasa_apod` | 73.11% | 53.34% | 3297.3 | 10549.1 | 2000ms | 321/688 |
| ❌ | `ipapi_check` | 86.05% | 100.0% | 156.6 | 363.0 | 2500ms | 0/688 |
| ⚠️ | `rest_countries` | 98.55% | 97.97% | 366.1 | 10221.5 | 2500ms | 14/688 |
| ⚠️ | `open_meteo_weather` | 98.84% | 96.95% | 715.2 | 14877.1 | 2000ms | 21/688 |
| ⚠️ | `dog_ceo_random` | 99.56% | 93.9% | 684.4 | 10244.1 | 2500ms | 42/688 |
| ✅ | `catfact_random` | 99.56% | 99.13% | 271.4 | 10080.2 | 3000ms | 6/688 |
| ✅ | `coingecko_bitcoin` | 99.56% | 100.0% | 98.9 | 252.0 | 1500ms | 0/688 |
| ✅ | `useless_fact` | 99.71% | 99.42% | 598.3 | 10229.6 | 2500ms | 4/688 |
| ✅ | `agify_name` | 99.85% | 99.71% | 392.1 | 16112.2 | 2000ms | 2/688 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.71% | 235.7 | 3882.8 | 2000ms | 2/688 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `numbers_trivia` | 03:00 | 4902.0 | 47.06% |
| `numbers_trivia` | 12:00 | 4824.9 | 46.43% |
| `nasa_apod` | 03:00 | 4821.6 | 76.47% |
| `numbers_trivia` | 00:00 | 4778.2 | 46.15% |
| `numbers_trivia` | 07:00 | 4535.2 | 43.48% |
| `numbers_trivia` | 05:00 | 4499.3 | 42.86% |
| `nasa_apod` | 17:00 | 4497.7 | 55.0% |
| `numbers_trivia` | 16:00 | 4357.4 | 41.94% |
| `numbers_trivia` | 10:00 | 4318.4 | 41.38% |
| `numbers_trivia` | 01:00 | 4309.0 | 41.67% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
