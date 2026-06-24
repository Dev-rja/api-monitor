# API Reliability Monitor — SLA Report

> Last updated: **2026-06-24 22:53 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **78.9%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 77.41% | 2452.5 | 10206.7 | 1000ms | 267/1182 |
| ❌ | `public_apis_list` | 0.0% | 99.66% | 124.9 | 4595.4 | 1500ms | 4/1182 |
| ❌ | `nasa_apod` | 74.45% | 50.85% | 3321.2 | 11152.5 | 2000ms | 581/1182 |
| ❌ | `ipapi_check` | 76.57% | 99.92% | 155.5 | 4507.0 | 2500ms | 1/1182 |
| ⚠️ | `rest_countries` | 98.73% | 98.39% | 335.1 | 10221.5 | 2500ms | 19/1182 |
| ⚠️ | `open_meteo_weather` | 98.98% | 96.95% | 711.6 | 14877.1 | 2000ms | 36/1182 |
| ✅ | `useless_fact` | 99.58% | 99.66% | 631.8 | 10229.6 | 2500ms | 4/1182 |
| ✅ | `dog_ceo_random` | 99.58% | 96.45% | 548.0 | 10244.1 | 2500ms | 42/1182 |
| ✅ | `catfact_random` | 99.75% | 99.24% | 261.1 | 10080.2 | 3000ms | 9/1182 |
| ✅ | `coingecko_bitcoin` | 99.75% | 100.0% | 95.8 | 253.3 | 1500ms | 0/1182 |
| ✅ | `agify_name` | 99.92% | 99.66% | 386.9 | 16112.2 | 2000ms | 4/1182 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.83% | 217.4 | 3882.8 | 2000ms | 2/1182 |

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
