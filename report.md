# API Reliability Monitor — SLA Report

> Last updated: **2026-05-30 23:43 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **79.3%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 72.12% | 2977.4 | 10206.7 | 1000ms | 266/954 |
| ❌ | `public_apis_list` | 0.0% | 99.58% | 126.3 | 4595.4 | 1500ms | 4/954 |
| ❌ | `ipapi_check` | 76.83% | 100.0% | 152.7 | 431.8 | 2500ms | 0/954 |
| ❌ | `nasa_apod` | 78.83% | 58.81% | 2795.0 | 10549.1 | 2000ms | 393/954 |
| ⚠️ | `rest_countries` | 98.43% | 98.11% | 364.9 | 10221.5 | 2500ms | 18/954 |
| ⚠️ | `open_meteo_weather` | 98.95% | 96.86% | 709.3 | 14877.1 | 2000ms | 30/954 |
| ✅ | `dog_ceo_random` | 99.48% | 95.6% | 591.7 | 10244.1 | 2500ms | 42/954 |
| ✅ | `catfact_random` | 99.69% | 99.16% | 267.5 | 10080.2 | 3000ms | 8/954 |
| ✅ | `coingecko_bitcoin` | 99.69% | 100.0% | 97.0 | 253.3 | 1500ms | 0/954 |
| ✅ | `useless_fact` | 99.79% | 99.58% | 618.1 | 10229.6 | 2500ms | 4/954 |
| ✅ | `agify_name` | 99.9% | 99.69% | 383.2 | 16112.2 | 2000ms | 3/954 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.79% | 225.0 | 3882.8 | 2000ms | 2/954 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `nasa_apod` | 03:00 | 4611.9 | 78.95% |
| `numbers_trivia` | 03:00 | 4408.7 | 42.11% |
| `nasa_apod` | 17:00 | 3728.7 | 49.09% |
| `numbers_trivia` | 05:00 | 3674.1 | 34.62% |
| `numbers_trivia` | 07:00 | 3664.8 | 34.48% |
| `nasa_apod` | 11:00 | 3605.9 | 46.3% |
| `nasa_apod` | 05:00 | 3511.6 | 61.54% |
| `numbers_trivia` | 10:00 | 3454.8 | 32.43% |
| `numbers_trivia` | 12:00 | 3394.7 | 31.71% |
| `numbers_trivia` | 14:00 | 3388.1 | 33.33% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
