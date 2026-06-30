# API Reliability Monitor — SLA Report

> Last updated: **2026-06-30 17:13 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **79.0%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 78.55% | 2339.2 | 10206.7 | 1000ms | 267/1245 |
| ❌ | `public_apis_list` | 0.0% | 99.68% | 125.9 | 4595.4 | 1500ms | 4/1245 |
| ❌ | `nasa_apod` | 73.65% | 49.16% | 3419.5 | 11152.5 | 2000ms | 633/1245 |
| ❌ | `ipapi_check` | 77.35% | 99.92% | 155.4 | 4507.0 | 2500ms | 1/1245 |
| ⚠️ | `rest_countries` | 98.8% | 98.47% | 326.8 | 10221.5 | 2500ms | 19/1245 |
| ⚠️ | `open_meteo_weather` | 98.96% | 97.03% | 712.1 | 14877.1 | 2000ms | 37/1245 |
| ✅ | `useless_fact` | 99.6% | 99.68% | 631.3 | 10229.6 | 2500ms | 4/1245 |
| ✅ | `dog_ceo_random` | 99.6% | 96.63% | 537.5 | 10244.1 | 2500ms | 42/1245 |
| ✅ | `catfact_random` | 99.76% | 99.28% | 258.5 | 10080.2 | 3000ms | 9/1245 |
| ✅ | `coingecko_bitcoin` | 99.76% | 100.0% | 95.2 | 253.3 | 1500ms | 0/1245 |
| ✅ | `agify_name` | 99.92% | 99.68% | 387.2 | 16112.2 | 2000ms | 4/1245 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.84% | 217.1 | 3882.8 | 2000ms | 2/1245 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `nasa_apod` | 02:00 | 5333.5 | 66.67% |
| `nasa_apod` | 03:00 | 4897.3 | 80.0% |
| `nasa_apod` | 05:00 | 4594.8 | 67.65% |
| `nasa_apod` | 09:00 | 4433.0 | 57.41% |
| `nasa_apod` | 01:00 | 4372.6 | 64.71% |
| `numbers_trivia` | 03:00 | 4200.6 | 40.0% |
| `nasa_apod` | 17:00 | 4144.0 | 55.88% |
| `nasa_apod` | 18:00 | 3910.9 | 55.56% |
| `nasa_apod` | 12:00 | 3690.4 | 53.57% |
| `nasa_apod` | 11:00 | 3683.6 | 54.41% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
