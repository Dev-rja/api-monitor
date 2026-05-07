# API Reliability Monitor — SLA Report

> Last updated: **2026-05-07 16:29 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **5/12** &nbsp;|&nbsp; Avg uptime: **79.6%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 61.1% | 4084.3 | 10206.7 | 1000ms | 261/671 |
| ❌ | `public_apis_list` | 0.0% | 99.55% | 128.6 | 4595.4 | 1500ms | 3/671 |
| ❌ | `nasa_apod` | 72.43% | 52.31% | 3363.3 | 10549.1 | 2000ms | 320/671 |
| ❌ | `ipapi_check` | 87.18% | 100.0% | 156.9 | 363.0 | 2500ms | 0/671 |
| ⚠️ | `rest_countries` | 98.66% | 98.36% | 337.6 | 10221.5 | 2500ms | 11/671 |
| ⚠️ | `open_meteo_weather` | 98.81% | 96.87% | 718.7 | 14877.1 | 2000ms | 21/671 |
| ⚠️ | `dog_ceo_random` | 99.55% | 93.74% | 691.8 | 10244.1 | 2500ms | 42/671 |
| ✅ | `catfact_random` | 99.55% | 99.4% | 259.1 | 10080.2 | 3000ms | 4/671 |
| ✅ | `coingecko_bitcoin` | 99.55% | 100.0% | 98.8 | 252.0 | 1500ms | 0/671 |
| ✅ | `useless_fact` | 99.7% | 99.4% | 596.3 | 10229.6 | 2500ms | 4/671 |
| ✅ | `agify_name` | 100.0% | 99.85% | 368.0 | 3237.1 | 2000ms | 1/671 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.7% | 235.7 | 3882.8 | 2000ms | 2/671 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `numbers_trivia` | 03:00 | 5199.6 | 50.0% |
| `numbers_trivia` | 00:00 | 5152.0 | 50.0% |
| `nasa_apod` | 03:00 | 5080.8 | 81.25% |
| `numbers_trivia` | 12:00 | 5000.0 | 48.15% |
| `numbers_trivia` | 07:00 | 4734.0 | 45.45% |
| `numbers_trivia` | 05:00 | 4708.1 | 45.0% |
| `nasa_apod` | 17:00 | 4607.0 | 56.41% |
| `numbers_trivia` | 18:00 | 4526.1 | 43.33% |
| `numbers_trivia` | 10:00 | 4461.5 | 42.86% |
| `numbers_trivia` | 14:00 | 4365.7 | 41.67% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
