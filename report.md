# API Reliability Monitor — SLA Report

> Last updated: **2026-07-01 13:21 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **78.9%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 78.69% | 2325.8 | 10206.7 | 1000ms | 267/1253 |
| ❌ | `public_apis_list` | 0.0% | 99.68% | 126.0 | 4595.4 | 1500ms | 4/1253 |
| ❌ | `nasa_apod` | 73.42% | 49.0% | 3437.5 | 11152.5 | 2000ms | 639/1253 |
| ❌ | `ipapi_check` | 77.25% | 99.92% | 155.2 | 4507.0 | 2500ms | 1/1253 |
| ⚠️ | `rest_countries` | 98.8% | 98.48% | 325.6 | 10221.5 | 2500ms | 19/1253 |
| ⚠️ | `open_meteo_weather` | 98.96% | 97.05% | 711.3 | 14877.1 | 2000ms | 37/1253 |
| ✅ | `useless_fact` | 99.6% | 99.68% | 631.2 | 10229.6 | 2500ms | 4/1253 |
| ✅ | `dog_ceo_random` | 99.6% | 96.65% | 536.3 | 10244.1 | 2500ms | 42/1253 |
| ✅ | `catfact_random` | 99.76% | 99.28% | 257.7 | 10080.2 | 3000ms | 9/1253 |
| ✅ | `coingecko_bitcoin` | 99.76% | 100.0% | 95.1 | 253.3 | 1500ms | 0/1253 |
| ✅ | `agify_name` | 99.92% | 99.68% | 387.2 | 16112.2 | 2000ms | 4/1253 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.84% | 216.8 | 3882.8 | 2000ms | 2/1253 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `nasa_apod` | 02:00 | 5333.5 | 66.67% |
| `nasa_apod` | 03:00 | 4897.3 | 80.0% |
| `nasa_apod` | 05:00 | 4594.8 | 67.65% |
| `nasa_apod` | 01:00 | 4545.0 | 65.71% |
| `nasa_apod` | 09:00 | 4433.0 | 57.41% |
| `numbers_trivia` | 03:00 | 4200.6 | 40.0% |
| `nasa_apod` | 17:00 | 4144.0 | 55.88% |
| `nasa_apod` | 18:00 | 3910.9 | 55.56% |
| `nasa_apod` | 12:00 | 3690.4 | 53.57% |
| `nasa_apod` | 11:00 | 3683.6 | 54.41% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
