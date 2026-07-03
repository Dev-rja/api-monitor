# API Reliability Monitor — SLA Report

> Last updated: **2026-07-03 19:54 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **5/12** &nbsp;|&nbsp; Avg uptime: **78.8%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 79.12% | 2283.1 | 10206.7 | 1000ms | 267/1279 |
| ❌ | `public_apis_list` | 0.0% | 99.69% | 125.1 | 4595.4 | 1500ms | 4/1279 |
| ❌ | `nasa_apod` | 73.49% | 48.94% | 3432.5 | 11152.5 | 2000ms | 653/1279 |
| ❌ | `ipapi_check` | 77.09% | 99.92% | 155.0 | 4507.0 | 2500ms | 1/1279 |
| ⚠️ | `dog_ceo_random` | 98.51% | 96.72% | 534.1 | 10244.1 | 2500ms | 42/1279 |
| ⚠️ | `rest_countries` | 98.83% | 98.51% | 322.8 | 10221.5 | 2500ms | 19/1279 |
| ⚠️ | `open_meteo_weather` | 98.91% | 97.03% | 716.6 | 14877.1 | 2000ms | 38/1279 |
| ✅ | `useless_fact` | 99.61% | 99.69% | 631.7 | 10229.6 | 2500ms | 4/1279 |
| ✅ | `catfact_random` | 99.77% | 99.3% | 257.2 | 10080.2 | 3000ms | 9/1279 |
| ✅ | `coingecko_bitcoin` | 99.77% | 99.92% | 98.1 | 4328.4 | 1500ms | 1/1279 |
| ✅ | `agify_name` | 99.92% | 99.69% | 386.5 | 16112.2 | 2000ms | 4/1279 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.84% | 215.5 | 3882.8 | 2000ms | 2/1279 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `nasa_apod` | 02:00 | 5333.5 | 66.67% |
| `nasa_apod` | 03:00 | 4897.3 | 80.0% |
| `nasa_apod` | 05:00 | 4477.1 | 65.71% |
| `nasa_apod` | 09:00 | 4433.0 | 57.41% |
| `nasa_apod` | 01:00 | 4430.3 | 63.89% |
| `numbers_trivia` | 03:00 | 4200.6 | 40.0% |
| `nasa_apod` | 17:00 | 4144.0 | 55.88% |
| `nasa_apod` | 18:00 | 3790.2 | 54.55% |
| `nasa_apod` | 11:00 | 3780.1 | 55.07% |
| `nasa_apod` | 12:00 | 3673.1 | 54.39% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
