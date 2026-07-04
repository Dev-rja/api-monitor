# API Reliability Monitor — SLA Report

> Last updated: **2026-07-04 17:45 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **5/12** &nbsp;|&nbsp; Avg uptime: **78.7%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 79.33% | 2262.1 | 10206.7 | 1000ms | 267/1292 |
| ❌ | `public_apis_list` | 0.0% | 99.69% | 124.3 | 4595.4 | 1500ms | 4/1292 |
| ❌ | `nasa_apod` | 73.68% | 49.23% | 3413.7 | 11152.5 | 2000ms | 656/1292 |
| ❌ | `ipapi_check` | 76.86% | 99.92% | 155.0 | 4507.0 | 2500ms | 1/1292 |
| ⚠️ | `dog_ceo_random` | 97.52% | 96.75% | 532.9 | 10244.1 | 2500ms | 42/1292 |
| ⚠️ | `open_meteo_weather` | 98.61% | 96.83% | 737.7 | 14877.1 | 2000ms | 41/1292 |
| ⚠️ | `rest_countries` | 98.84% | 98.53% | 321.5 | 10221.5 | 2500ms | 19/1292 |
| ✅ | `useless_fact` | 99.61% | 99.69% | 632.0 | 10229.6 | 2500ms | 4/1292 |
| ✅ | `catfact_random` | 99.77% | 99.3% | 256.8 | 10080.2 | 3000ms | 9/1292 |
| ✅ | `coingecko_bitcoin` | 99.77% | 99.92% | 98.1 | 4328.4 | 1500ms | 1/1292 |
| ✅ | `agify_name` | 99.92% | 99.69% | 385.6 | 16112.2 | 2000ms | 4/1292 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.85% | 214.6 | 3882.8 | 2000ms | 2/1292 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `nasa_apod` | 02:00 | 5333.5 | 66.67% |
| `nasa_apod` | 03:00 | 4897.3 | 80.0% |
| `nasa_apod` | 05:00 | 4477.1 | 65.71% |
| `nasa_apod` | 09:00 | 4356.6 | 56.36% |
| `nasa_apod` | 01:00 | 4324.4 | 62.16% |
| `numbers_trivia` | 03:00 | 4200.6 | 40.0% |
| `nasa_apod` | 17:00 | 4089.9 | 55.07% |
| `nasa_apod` | 18:00 | 3790.2 | 54.55% |
| `nasa_apod` | 11:00 | 3732.2 | 54.29% |
| `nasa_apod` | 20:00 | 3626.6 | 50.6% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
