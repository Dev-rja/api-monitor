# API Reliability Monitor — SLA Report

> Last updated: **2026-05-15 22:40 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **5/12** &nbsp;|&nbsp; Avg uptime: **79.7%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 66.28% | 3548.2 | 10206.7 | 1000ms | 264/783 |
| ❌ | `public_apis_list` | 0.0% | 99.49% | 131.2 | 4595.4 | 1500ms | 4/783 |
| ❌ | `nasa_apod` | 75.73% | 56.58% | 3057.1 | 10549.1 | 2000ms | 340/783 |
| ❌ | `ipapi_check` | 84.67% | 100.0% | 155.0 | 363.0 | 2500ms | 0/783 |
| ⚠️ | `rest_countries` | 98.72% | 98.21% | 346.5 | 10221.5 | 2500ms | 14/783 |
| ⚠️ | `open_meteo_weather` | 98.85% | 97.06% | 704.7 | 14877.1 | 2000ms | 23/783 |
| ⚠️ | `dog_ceo_random` | 99.49% | 94.64% | 646.5 | 10244.1 | 2500ms | 42/783 |
| ✅ | `catfact_random` | 99.62% | 99.11% | 269.7 | 10080.2 | 3000ms | 7/783 |
| ✅ | `coingecko_bitcoin` | 99.62% | 100.0% | 98.0 | 252.0 | 1500ms | 0/783 |
| ✅ | `useless_fact` | 99.74% | 99.49% | 606.6 | 10229.6 | 2500ms | 4/783 |
| ✅ | `agify_name` | 99.87% | 99.74% | 391.1 | 16112.2 | 2000ms | 2/783 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.74% | 233.9 | 3882.8 | 2000ms | 2/783 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `nasa_apod` | 03:00 | 4729.0 | 77.78% |
| `numbers_trivia` | 03:00 | 4635.3 | 44.44% |
| `numbers_trivia` | 12:00 | 4400.0 | 41.94% |
| `numbers_trivia` | 07:00 | 4356.2 | 41.67% |
| `nasa_apod` | 17:00 | 4145.1 | 53.33% |
| `numbers_trivia` | 05:00 | 4119.9 | 39.13% |
| `numbers_trivia` | 10:00 | 4070.5 | 38.71% |
| `numbers_trivia` | 00:00 | 3937.7 | 37.5% |
| `nasa_apod` | 11:00 | 3887.5 | 44.68% |
| `numbers_trivia` | 14:00 | 3873.8 | 36.59% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
