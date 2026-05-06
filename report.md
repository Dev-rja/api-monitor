# API Reliability Monitor — SLA Report

> Last updated: **2026-05-06 21:47 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **5/12** &nbsp;|&nbsp; Avg uptime: **79.6%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 60.57% | 4136.6 | 10206.7 | 1000ms | 261/662 |
| ❌ | `public_apis_list` | 0.0% | 99.55% | 128.9 | 4595.4 | 1500ms | 3/662 |
| ❌ | `nasa_apod` | 72.05% | 51.66% | 3403.1 | 10549.1 | 2000ms | 320/662 |
| ❌ | `ipapi_check` | 87.01% | 100.0% | 156.8 | 363.0 | 2500ms | 0/662 |
| ⚠️ | `rest_countries` | 98.64% | 98.34% | 336.5 | 10221.5 | 2500ms | 11/662 |
| ⚠️ | `open_meteo_weather` | 98.79% | 96.83% | 721.2 | 14877.1 | 2000ms | 21/662 |
| ⚠️ | `dog_ceo_random` | 99.55% | 93.66% | 695.2 | 10244.1 | 2500ms | 42/662 |
| ✅ | `catfact_random` | 99.55% | 99.4% | 260.1 | 10080.2 | 3000ms | 4/662 |
| ✅ | `coingecko_bitcoin` | 99.55% | 100.0% | 98.8 | 252.0 | 1500ms | 0/662 |
| ✅ | `useless_fact` | 99.7% | 99.4% | 593.6 | 10229.6 | 2500ms | 4/662 |
| ✅ | `agify_name` | 100.0% | 99.85% | 368.2 | 3237.1 | 2000ms | 1/662 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.7% | 236.4 | 3882.8 | 2000ms | 2/662 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `numbers_trivia` | 03:00 | 5199.6 | 50.0% |
| `numbers_trivia` | 12:00 | 5183.8 | 50.0% |
| `numbers_trivia` | 00:00 | 5152.0 | 50.0% |
| `nasa_apod` | 03:00 | 5080.8 | 81.25% |
| `numbers_trivia` | 07:00 | 4955.2 | 47.62% |
| `numbers_trivia` | 05:00 | 4708.1 | 45.0% |
| `numbers_trivia` | 01:00 | 4686.2 | 45.45% |
| `numbers_trivia` | 10:00 | 4616.5 | 44.44% |
| `nasa_apod` | 17:00 | 4607.0 | 56.41% |
| `numbers_trivia` | 18:00 | 4526.1 | 43.33% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
