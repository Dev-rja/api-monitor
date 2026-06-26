# API Reliability Monitor — SLA Report

> Last updated: **2026-06-26 16:51 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **79.0%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 77.71% | 2422.2 | 10206.7 | 1000ms | 267/1198 |
| ❌ | `public_apis_list` | 0.0% | 99.67% | 125.5 | 4595.4 | 1500ms | 4/1198 |
| ❌ | `nasa_apod` | 74.37% | 50.42% | 3338.5 | 11152.5 | 2000ms | 594/1198 |
| ❌ | `ipapi_check` | 76.79% | 99.92% | 155.6 | 4507.0 | 2500ms | 1/1198 |
| ⚠️ | `rest_countries` | 98.75% | 98.41% | 332.9 | 10221.5 | 2500ms | 19/1198 |
| ⚠️ | `open_meteo_weather` | 98.91% | 96.91% | 717.5 | 14877.1 | 2000ms | 37/1198 |
| ✅ | `useless_fact` | 99.58% | 99.67% | 631.7 | 10229.6 | 2500ms | 4/1198 |
| ✅ | `dog_ceo_random` | 99.58% | 96.49% | 544.8 | 10244.1 | 2500ms | 42/1198 |
| ✅ | `catfact_random` | 99.75% | 99.25% | 260.4 | 10080.2 | 3000ms | 9/1198 |
| ✅ | `coingecko_bitcoin` | 99.75% | 100.0% | 95.8 | 253.3 | 1500ms | 0/1198 |
| ✅ | `agify_name` | 99.92% | 99.67% | 386.9 | 16112.2 | 2000ms | 4/1198 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.83% | 217.6 | 3882.8 | 2000ms | 2/1198 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `nasa_apod` | 02:00 | 5333.5 | 66.67% |
| `nasa_apod` | 03:00 | 4897.3 | 80.0% |
| `nasa_apod` | 05:00 | 4594.8 | 67.65% |
| `nasa_apod` | 17:00 | 4247.7 | 55.38% |
| `nasa_apod` | 09:00 | 4237.3 | 54.9% |
| `numbers_trivia` | 03:00 | 4200.6 | 40.0% |
| `nasa_apod` | 01:00 | 4057.3 | 61.29% |
| `nasa_apod` | 11:00 | 3721.6 | 53.03% |
| `nasa_apod` | 18:00 | 3715.0 | 53.33% |
| `nasa_apod` | 20:00 | 3626.2 | 49.35% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
