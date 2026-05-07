# API Reliability Monitor — SLA Report

> Last updated: **2026-05-07 10:09 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **5/12** &nbsp;|&nbsp; Avg uptime: **79.6%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 60.93% | 4101.6 | 10206.7 | 1000ms | 261/668 |
| ❌ | `public_apis_list` | 0.0% | 99.55% | 128.7 | 4595.4 | 1500ms | 3/668 |
| ❌ | `nasa_apod` | 72.31% | 52.1% | 3376.7 | 10549.1 | 2000ms | 320/668 |
| ❌ | `ipapi_check` | 87.13% | 100.0% | 157.0 | 363.0 | 2500ms | 0/668 |
| ⚠️ | `rest_countries` | 98.65% | 98.35% | 338.2 | 10221.5 | 2500ms | 11/668 |
| ⚠️ | `open_meteo_weather` | 98.8% | 96.86% | 719.3 | 14877.1 | 2000ms | 21/668 |
| ⚠️ | `dog_ceo_random` | 99.55% | 93.71% | 693.0 | 10244.1 | 2500ms | 42/668 |
| ✅ | `catfact_random` | 99.55% | 99.4% | 259.4 | 10080.2 | 3000ms | 4/668 |
| ✅ | `coingecko_bitcoin` | 99.55% | 100.0% | 98.9 | 252.0 | 1500ms | 0/668 |
| ✅ | `useless_fact` | 99.7% | 99.4% | 595.9 | 10229.6 | 2500ms | 4/668 |
| ✅ | `agify_name` | 100.0% | 99.85% | 368.0 | 3237.1 | 2000ms | 1/668 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.7% | 235.9 | 3882.8 | 2000ms | 2/668 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `numbers_trivia` | 03:00 | 5199.6 | 50.0% |
| `numbers_trivia` | 12:00 | 5183.8 | 50.0% |
| `numbers_trivia` | 00:00 | 5152.0 | 50.0% |
| `nasa_apod` | 03:00 | 5080.8 | 81.25% |
| `numbers_trivia` | 07:00 | 4734.0 | 45.45% |
| `numbers_trivia` | 05:00 | 4708.1 | 45.0% |
| `nasa_apod` | 17:00 | 4607.0 | 56.41% |
| `numbers_trivia` | 18:00 | 4526.1 | 43.33% |
| `numbers_trivia` | 16:00 | 4497.5 | 43.33% |
| `numbers_trivia` | 14:00 | 4479.4 | 42.86% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
