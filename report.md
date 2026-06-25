# API Reliability Monitor — SLA Report

> Last updated: **2026-06-25 20:16 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **78.9%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 77.56% | 2437.3 | 10206.7 | 1000ms | 267/1190 |
| ❌ | `public_apis_list` | 0.0% | 99.66% | 125.1 | 4595.4 | 1500ms | 4/1190 |
| ❌ | `nasa_apod` | 74.29% | 50.67% | 3336.2 | 11152.5 | 2000ms | 587/1190 |
| ❌ | `ipapi_check` | 76.72% | 99.92% | 155.6 | 4507.0 | 2500ms | 1/1190 |
| ⚠️ | `rest_countries` | 98.74% | 98.4% | 334.0 | 10221.5 | 2500ms | 19/1190 |
| ⚠️ | `open_meteo_weather` | 98.99% | 96.97% | 710.6 | 14877.1 | 2000ms | 36/1190 |
| ✅ | `useless_fact` | 99.58% | 99.66% | 632.1 | 10229.6 | 2500ms | 4/1190 |
| ✅ | `dog_ceo_random` | 99.58% | 96.47% | 546.3 | 10244.1 | 2500ms | 42/1190 |
| ✅ | `catfact_random` | 99.75% | 99.24% | 260.7 | 10080.2 | 3000ms | 9/1190 |
| ✅ | `coingecko_bitcoin` | 99.75% | 100.0% | 95.7 | 253.3 | 1500ms | 0/1190 |
| ✅ | `agify_name` | 99.92% | 99.66% | 386.8 | 16112.2 | 2000ms | 4/1190 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.83% | 217.8 | 3882.8 | 2000ms | 2/1190 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `nasa_apod` | 02:00 | 5333.5 | 66.67% |
| `nasa_apod` | 03:00 | 4897.3 | 80.0% |
| `nasa_apod` | 05:00 | 4721.6 | 69.7% |
| `nasa_apod` | 17:00 | 4247.7 | 55.38% |
| `numbers_trivia` | 03:00 | 4200.6 | 40.0% |
| `nasa_apod` | 09:00 | 4114.4 | 54.0% |
| `nasa_apod` | 01:00 | 4107.5 | 60.0% |
| `nasa_apod` | 11:00 | 3739.0 | 52.31% |
| `nasa_apod` | 18:00 | 3715.0 | 53.33% |
| `nasa_apod` | 20:00 | 3626.2 | 49.35% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
