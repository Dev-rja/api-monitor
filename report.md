# API Reliability Monitor — SLA Report

> Last updated: **2026-05-03 18:31 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **5/12** &nbsp;|&nbsp; Avg uptime: **79.4%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 57.9% | 4401.4 | 10206.7 | 1000ms | 261/620 |
| ❌ | `public_apis_list` | 0.0% | 99.68% | 122.9 | 4088.9 | 1500ms | 2/620 |
| ❌ | `nasa_apod` | 70.16% | 48.71% | 3596.2 | 10549.1 | 2000ms | 318/620 |
| ❌ | `ipapi_check` | 87.1% | 100.0% | 155.9 | 353.0 | 2500ms | 0/620 |
| ⚠️ | `rest_countries` | 98.55% | 98.23% | 344.2 | 10221.5 | 2500ms | 11/620 |
| ⚠️ | `open_meteo_weather` | 98.71% | 97.1% | 715.1 | 14877.1 | 2000ms | 18/620 |
| ⚠️ | `dog_ceo_random` | 99.52% | 93.23% | 714.7 | 10244.1 | 2500ms | 42/620 |
| ✅ | `catfact_random` | 99.52% | 99.35% | 255.1 | 10080.2 | 3000ms | 4/620 |
| ✅ | `coingecko_bitcoin` | 99.52% | 100.0% | 98.0 | 252.0 | 1500ms | 0/620 |
| ✅ | `useless_fact` | 99.68% | 99.35% | 587.4 | 10229.6 | 2500ms | 4/620 |
| ✅ | `agify_name` | 100.0% | 99.84% | 369.4 | 3237.1 | 2000ms | 1/620 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.68% | 236.8 | 3882.8 | 2000ms | 2/620 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `numbers_trivia` | 00:00 | 5605.3 | 54.55% |
| `numbers_trivia` | 03:00 | 5199.6 | 50.0% |
| `numbers_trivia` | 12:00 | 5183.8 | 50.0% |
| `numbers_trivia` | 01:00 | 5126.1 | 50.0% |
| `nasa_apod` | 03:00 | 5080.8 | 81.25% |
| `numbers_trivia` | 07:00 | 4955.2 | 47.62% |
| `nasa_apod` | 17:00 | 4950.9 | 61.11% |
| `numbers_trivia` | 18:00 | 4840.2 | 46.43% |
| `numbers_trivia` | 10:00 | 4784.8 | 46.15% |
| `numbers_trivia` | 05:00 | 4708.1 | 45.0% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
