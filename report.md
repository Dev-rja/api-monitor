# API Reliability Monitor — SLA Report

> Last updated: **2026-07-05 12:56 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **5/12** &nbsp;|&nbsp; Avg uptime: **78.7%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 79.51% | 2244.8 | 10206.7 | 1000ms | 267/1303 |
| ❌ | `public_apis_list` | 0.0% | 99.69% | 123.7 | 4595.4 | 1500ms | 4/1303 |
| ❌ | `nasa_apod` | 73.91% | 49.58% | 3390.3 | 11152.5 | 2000ms | 657/1303 |
| ❌ | `ipapi_check` | 76.67% | 99.92% | 154.9 | 4507.0 | 2500ms | 1/1303 |
| ⚠️ | `dog_ceo_random` | 96.7% | 96.78% | 531.7 | 10244.1 | 2500ms | 42/1303 |
| ⚠️ | `open_meteo_weather` | 98.62% | 96.85% | 736.5 | 14877.1 | 2000ms | 41/1303 |
| ⚠️ | `rest_countries` | 98.85% | 98.54% | 320.3 | 10221.5 | 2500ms | 19/1303 |
| ✅ | `useless_fact` | 99.62% | 99.69% | 632.2 | 10229.6 | 2500ms | 4/1303 |
| ✅ | `catfact_random` | 99.77% | 99.31% | 256.2 | 10080.2 | 3000ms | 9/1303 |
| ✅ | `coingecko_bitcoin` | 99.77% | 99.92% | 97.9 | 4328.4 | 1500ms | 1/1303 |
| ✅ | `agify_name` | 99.92% | 99.69% | 384.7 | 16112.2 | 2000ms | 4/1303 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.85% | 213.9 | 3882.8 | 2000ms | 2/1303 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `nasa_apod` | 02:00 | 5333.5 | 66.67% |
| `nasa_apod` | 03:00 | 4897.3 | 80.0% |
| `nasa_apod` | 05:00 | 4477.1 | 65.71% |
| `nasa_apod` | 01:00 | 4324.4 | 62.16% |
| `nasa_apod` | 09:00 | 4282.5 | 55.36% |
| `numbers_trivia` | 03:00 | 4200.6 | 40.0% |
| `nasa_apod` | 17:00 | 4089.9 | 55.07% |
| `nasa_apod` | 18:00 | 3742.2 | 53.73% |
| `nasa_apod` | 11:00 | 3686.0 | 53.52% |
| `nasa_apod` | 20:00 | 3626.6 | 50.6% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
