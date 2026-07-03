# API Reliability Monitor — SLA Report

> Last updated: **2026-07-03 01:19 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **78.9%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 78.99% | 2296.1 | 10206.7 | 1000ms | 267/1271 |
| ❌ | `public_apis_list` | 0.0% | 99.69% | 125.6 | 4595.4 | 1500ms | 4/1271 |
| ❌ | `nasa_apod` | 73.41% | 48.78% | 3441.9 | 11152.5 | 2000ms | 651/1271 |
| ❌ | `ipapi_check` | 77.18% | 99.92% | 155.1 | 4507.0 | 2500ms | 1/1271 |
| ⚠️ | `rest_countries` | 98.82% | 98.51% | 323.7 | 10221.5 | 2500ms | 19/1271 |
| ⚠️ | `open_meteo_weather` | 98.98% | 97.09% | 709.8 | 14877.1 | 2000ms | 37/1271 |
| ✅ | `dog_ceo_random` | 99.13% | 96.7% | 534.9 | 10244.1 | 2500ms | 42/1271 |
| ✅ | `useless_fact` | 99.61% | 99.69% | 631.8 | 10229.6 | 2500ms | 4/1271 |
| ✅ | `catfact_random` | 99.76% | 99.29% | 257.5 | 10080.2 | 3000ms | 9/1271 |
| ✅ | `coingecko_bitcoin` | 99.76% | 100.0% | 95.0 | 253.3 | 1500ms | 0/1271 |
| ✅ | `agify_name` | 99.92% | 99.69% | 387.0 | 16112.2 | 2000ms | 4/1271 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.84% | 216.0 | 3882.8 | 2000ms | 2/1271 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `nasa_apod` | 02:00 | 5333.5 | 66.67% |
| `nasa_apod` | 03:00 | 4897.3 | 80.0% |
| `nasa_apod` | 05:00 | 4594.8 | 67.65% |
| `nasa_apod` | 09:00 | 4433.0 | 57.41% |
| `nasa_apod` | 01:00 | 4430.3 | 63.89% |
| `numbers_trivia` | 03:00 | 4200.6 | 40.0% |
| `nasa_apod` | 17:00 | 4144.0 | 55.88% |
| `nasa_apod` | 18:00 | 3842.4 | 55.38% |
| `nasa_apod` | 11:00 | 3683.6 | 54.41% |
| `nasa_apod` | 12:00 | 3673.1 | 54.39% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
