# API Reliability Monitor — SLA Report

> Last updated: **2026-06-30 01:52 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **79.0%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 78.47% | 2347.5 | 10206.7 | 1000ms | 267/1240 |
| ❌ | `public_apis_list` | 0.0% | 99.68% | 125.7 | 4595.4 | 1500ms | 4/1240 |
| ❌ | `nasa_apod` | 73.79% | 49.35% | 3404.5 | 11152.5 | 2000ms | 628/1240 |
| ❌ | `ipapi_check` | 77.34% | 99.92% | 155.5 | 4507.0 | 2500ms | 1/1240 |
| ⚠️ | `rest_countries` | 98.79% | 98.47% | 327.5 | 10221.5 | 2500ms | 19/1240 |
| ⚠️ | `open_meteo_weather` | 98.95% | 97.02% | 712.7 | 14877.1 | 2000ms | 37/1240 |
| ✅ | `useless_fact` | 99.6% | 99.68% | 631.3 | 10229.6 | 2500ms | 4/1240 |
| ✅ | `dog_ceo_random` | 99.6% | 96.61% | 538.4 | 10244.1 | 2500ms | 42/1240 |
| ✅ | `catfact_random` | 99.76% | 99.27% | 258.6 | 10080.2 | 3000ms | 9/1240 |
| ✅ | `coingecko_bitcoin` | 99.76% | 100.0% | 95.3 | 253.3 | 1500ms | 0/1240 |
| ✅ | `agify_name` | 99.92% | 99.68% | 386.8 | 16112.2 | 2000ms | 4/1240 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.84% | 217.2 | 3882.8 | 2000ms | 2/1240 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `nasa_apod` | 02:00 | 5333.5 | 66.67% |
| `nasa_apod` | 03:00 | 4897.3 | 80.0% |
| `nasa_apod` | 05:00 | 4594.8 | 67.65% |
| `nasa_apod` | 09:00 | 4467.2 | 56.6% |
| `nasa_apod` | 01:00 | 4372.6 | 64.71% |
| `numbers_trivia` | 03:00 | 4200.6 | 40.0% |
| `nasa_apod` | 17:00 | 4168.0 | 55.22% |
| `nasa_apod` | 18:00 | 3910.9 | 55.56% |
| `nasa_apod` | 11:00 | 3683.6 | 54.41% |
| `nasa_apod` | 20:00 | 3681.4 | 50.62% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
