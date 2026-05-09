# API Reliability Monitor — SLA Report

> Last updated: **2026-05-09 00:12 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **5/12** &nbsp;|&nbsp; Avg uptime: **79.6%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 62.28% | 3968.3 | 10206.7 | 1000ms | 261/692 |
| ❌ | `public_apis_list` | 0.0% | 99.57% | 127.3 | 4595.4 | 1500ms | 3/692 |
| ❌ | `nasa_apod` | 73.27% | 53.61% | 3280.2 | 10549.1 | 2000ms | 321/692 |
| ❌ | `ipapi_check` | 86.13% | 100.0% | 156.4 | 363.0 | 2500ms | 0/692 |
| ⚠️ | `rest_countries` | 98.55% | 97.98% | 365.5 | 10221.5 | 2500ms | 14/692 |
| ⚠️ | `open_meteo_weather` | 98.84% | 96.97% | 714.7 | 14877.1 | 2000ms | 21/692 |
| ⚠️ | `dog_ceo_random` | 99.57% | 93.93% | 682.6 | 10244.1 | 2500ms | 42/692 |
| ✅ | `catfact_random` | 99.57% | 99.13% | 271.6 | 10080.2 | 3000ms | 6/692 |
| ✅ | `coingecko_bitcoin` | 99.57% | 100.0% | 98.9 | 252.0 | 1500ms | 0/692 |
| ✅ | `useless_fact` | 99.71% | 99.42% | 598.5 | 10229.6 | 2500ms | 4/692 |
| ✅ | `agify_name` | 99.86% | 99.71% | 392.4 | 16112.2 | 2000ms | 2/692 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.71% | 235.3 | 3882.8 | 2000ms | 2/692 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `numbers_trivia` | 03:00 | 4902.0 | 47.06% |
| `numbers_trivia` | 12:00 | 4824.9 | 46.43% |
| `nasa_apod` | 03:00 | 4821.6 | 76.47% |
| `numbers_trivia` | 07:00 | 4535.2 | 43.48% |
| `numbers_trivia` | 05:00 | 4499.3 | 42.86% |
| `nasa_apod` | 17:00 | 4497.7 | 55.0% |
| `numbers_trivia` | 00:00 | 4460.1 | 42.86% |
| `numbers_trivia` | 16:00 | 4357.4 | 41.94% |
| `numbers_trivia` | 10:00 | 4318.4 | 41.38% |
| `numbers_trivia` | 01:00 | 4309.0 | 41.67% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
