# API Reliability Monitor — SLA Report

> Last updated: **2026-07-03 16:56 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **5/12** &nbsp;|&nbsp; Avg uptime: **78.8%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 79.09% | 2286.3 | 10206.7 | 1000ms | 267/1277 |
| ❌ | `public_apis_list` | 0.0% | 99.69% | 125.2 | 4595.4 | 1500ms | 4/1277 |
| ❌ | `nasa_apod` | 73.45% | 48.94% | 3435.3 | 11152.5 | 2000ms | 652/1277 |
| ❌ | `ipapi_check` | 77.06% | 99.92% | 154.9 | 4507.0 | 2500ms | 1/1277 |
| ⚠️ | `dog_ceo_random` | 98.67% | 96.71% | 534.2 | 10244.1 | 2500ms | 42/1277 |
| ⚠️ | `rest_countries` | 98.83% | 98.51% | 323.0 | 10221.5 | 2500ms | 19/1277 |
| ⚠️ | `open_meteo_weather` | 98.9% | 97.02% | 716.5 | 14877.1 | 2000ms | 38/1277 |
| ✅ | `useless_fact` | 99.61% | 99.69% | 631.4 | 10229.6 | 2500ms | 4/1277 |
| ✅ | `catfact_random` | 99.77% | 99.3% | 257.1 | 10080.2 | 3000ms | 9/1277 |
| ✅ | `coingecko_bitcoin` | 99.77% | 100.0% | 94.8 | 253.3 | 1500ms | 0/1277 |
| ✅ | `agify_name` | 99.92% | 99.69% | 386.6 | 16112.2 | 2000ms | 4/1277 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.84% | 215.5 | 3882.8 | 2000ms | 2/1277 |

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
| `nasa_apod` | 18:00 | 3842.4 | 55.38% |
| `nasa_apod` | 11:00 | 3780.1 | 55.07% |
| `nasa_apod` | 12:00 | 3673.1 | 54.39% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
