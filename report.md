# API Reliability Monitor — SLA Report

> Last updated: **2026-06-25 00:12 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **78.9%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 77.43% | 2450.5 | 10206.7 | 1000ms | 267/1183 |
| ❌ | `public_apis_list` | 0.0% | 99.66% | 125.0 | 4595.4 | 1500ms | 4/1183 |
| ❌ | `nasa_apod` | 74.39% | 50.8% | 3327.2 | 11152.5 | 2000ms | 582/1183 |
| ❌ | `ipapi_check` | 76.58% | 99.92% | 155.5 | 4507.0 | 2500ms | 1/1183 |
| ⚠️ | `rest_countries` | 98.73% | 98.39% | 335.0 | 10221.5 | 2500ms | 19/1183 |
| ⚠️ | `open_meteo_weather` | 98.99% | 96.96% | 711.4 | 14877.1 | 2000ms | 36/1183 |
| ✅ | `useless_fact` | 99.58% | 99.66% | 631.7 | 10229.6 | 2500ms | 4/1183 |
| ✅ | `dog_ceo_random` | 99.58% | 96.45% | 547.7 | 10244.1 | 2500ms | 42/1183 |
| ✅ | `catfact_random` | 99.75% | 99.24% | 260.9 | 10080.2 | 3000ms | 9/1183 |
| ✅ | `coingecko_bitcoin` | 99.75% | 100.0% | 95.8 | 253.3 | 1500ms | 0/1183 |
| ✅ | `agify_name` | 99.92% | 99.66% | 386.8 | 16112.2 | 2000ms | 4/1183 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.83% | 217.3 | 3882.8 | 2000ms | 2/1183 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `nasa_apod` | 02:00 | 5333.5 | 66.67% |
| `nasa_apod` | 03:00 | 4897.3 | 80.0% |
| `nasa_apod` | 05:00 | 4721.6 | 69.7% |
| `nasa_apod` | 17:00 | 4293.2 | 56.25% |
| `numbers_trivia` | 03:00 | 4200.6 | 40.0% |
| `nasa_apod` | 09:00 | 4114.4 | 54.0% |
| `nasa_apod` | 01:00 | 4107.5 | 60.0% |
| `nasa_apod` | 11:00 | 3739.0 | 52.31% |
| `nasa_apod` | 18:00 | 3715.0 | 53.33% |
| `nasa_apod` | 20:00 | 3537.6 | 48.68% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
