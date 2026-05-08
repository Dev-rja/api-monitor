# API Reliability Monitor — SLA Report

> Last updated: **2026-05-08 00:10 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **5/12** &nbsp;|&nbsp; Avg uptime: **79.6%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 61.45% | 4050.6 | 10206.7 | 1000ms | 261/677 |
| ❌ | `public_apis_list` | 0.0% | 99.56% | 128.3 | 4595.4 | 1500ms | 3/677 |
| ❌ | `nasa_apod` | 72.67% | 52.73% | 3337.2 | 10549.1 | 2000ms | 320/677 |
| ❌ | `ipapi_check` | 86.71% | 100.0% | 156.7 | 363.0 | 2500ms | 0/677 |
| ⚠️ | `rest_countries` | 98.67% | 98.38% | 336.8 | 10221.5 | 2500ms | 11/677 |
| ⚠️ | `open_meteo_weather` | 98.82% | 96.9% | 717.6 | 14877.1 | 2000ms | 21/677 |
| ⚠️ | `dog_ceo_random` | 99.56% | 93.8% | 688.8 | 10244.1 | 2500ms | 42/677 |
| ✅ | `catfact_random` | 99.56% | 99.41% | 261.9 | 10080.2 | 3000ms | 4/677 |
| ✅ | `coingecko_bitcoin` | 99.56% | 100.0% | 99.0 | 252.0 | 1500ms | 0/677 |
| ✅ | `useless_fact` | 99.7% | 99.41% | 596.9 | 10229.6 | 2500ms | 4/677 |
| ✅ | `agify_name` | 100.0% | 99.85% | 368.5 | 3237.1 | 2000ms | 1/677 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.7% | 235.5 | 3882.8 | 2000ms | 2/677 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `numbers_trivia` | 03:00 | 5199.6 | 50.0% |
| `nasa_apod` | 03:00 | 5080.8 | 81.25% |
| `numbers_trivia` | 12:00 | 5000.0 | 48.15% |
| `numbers_trivia` | 00:00 | 4778.2 | 46.15% |
| `numbers_trivia` | 07:00 | 4734.0 | 45.45% |
| `numbers_trivia` | 05:00 | 4708.1 | 45.0% |
| `nasa_apod` | 17:00 | 4607.0 | 56.41% |
| `numbers_trivia` | 10:00 | 4461.5 | 42.86% |
| `numbers_trivia` | 18:00 | 4390.9 | 41.94% |
| `numbers_trivia` | 14:00 | 4365.7 | 41.67% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
