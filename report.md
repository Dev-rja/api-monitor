# API Reliability Monitor — SLA Report

> Last updated: **2026-07-02 16:55 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **78.9%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 78.89% | 2306.1 | 10206.7 | 1000ms | 267/1265 |
| ❌ | `public_apis_list` | 0.0% | 99.68% | 125.9 | 4595.4 | 1500ms | 4/1265 |
| ❌ | `nasa_apod` | 73.28% | 48.7% | 3452.4 | 11152.5 | 2000ms | 649/1265 |
| ❌ | `ipapi_check` | 77.23% | 99.92% | 155.1 | 4507.0 | 2500ms | 1/1265 |
| ⚠️ | `rest_countries` | 98.81% | 98.5% | 324.3 | 10221.5 | 2500ms | 19/1265 |
| ⚠️ | `open_meteo_weather` | 98.97% | 97.08% | 710.3 | 14877.1 | 2000ms | 37/1265 |
| ✅ | `useless_fact` | 99.6% | 99.68% | 631.5 | 10229.6 | 2500ms | 4/1265 |
| ✅ | `dog_ceo_random` | 99.6% | 96.68% | 535.1 | 10244.1 | 2500ms | 42/1265 |
| ✅ | `catfact_random` | 99.76% | 99.29% | 257.9 | 10080.2 | 3000ms | 9/1265 |
| ✅ | `coingecko_bitcoin` | 99.76% | 100.0% | 95.0 | 253.3 | 1500ms | 0/1265 |
| ✅ | `agify_name` | 99.92% | 99.68% | 387.3 | 16112.2 | 2000ms | 4/1265 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.84% | 216.2 | 3882.8 | 2000ms | 2/1265 |

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
| `nasa_apod` | 18:00 | 3859.0 | 54.69% |
| `nasa_apod` | 11:00 | 3683.6 | 54.41% |
| `nasa_apod` | 12:00 | 3673.1 | 54.39% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
