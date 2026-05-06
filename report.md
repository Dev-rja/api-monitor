# API Reliability Monitor — SLA Report

> Last updated: **2026-05-06 17:11 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **5/12** &nbsp;|&nbsp; Avg uptime: **79.6%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 60.39% | 4154.6 | 10206.7 | 1000ms | 261/659 |
| ❌ | `public_apis_list` | 0.0% | 99.54% | 128.8 | 4595.4 | 1500ms | 3/659 |
| ❌ | `nasa_apod` | 71.93% | 51.44% | 3416.3 | 10549.1 | 2000ms | 320/659 |
| ❌ | `ipapi_check` | 86.95% | 100.0% | 156.7 | 363.0 | 2500ms | 0/659 |
| ⚠️ | `rest_countries` | 98.63% | 98.33% | 337.0 | 10221.5 | 2500ms | 11/659 |
| ⚠️ | `open_meteo_weather` | 98.79% | 96.81% | 720.9 | 14877.1 | 2000ms | 21/659 |
| ⚠️ | `dog_ceo_random` | 99.54% | 93.63% | 696.0 | 10244.1 | 2500ms | 42/659 |
| ✅ | `catfact_random` | 99.54% | 99.39% | 260.5 | 10080.2 | 3000ms | 4/659 |
| ✅ | `coingecko_bitcoin` | 99.54% | 100.0% | 98.5 | 252.0 | 1500ms | 0/659 |
| ✅ | `useless_fact` | 99.7% | 99.39% | 594.0 | 10229.6 | 2500ms | 4/659 |
| ✅ | `agify_name` | 100.0% | 99.85% | 368.8 | 3237.1 | 2000ms | 1/659 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.7% | 236.7 | 3882.8 | 2000ms | 2/659 |

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
