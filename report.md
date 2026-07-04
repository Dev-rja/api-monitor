# API Reliability Monitor — SLA Report

> Last updated: **2026-07-04 09:53 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **5/12** &nbsp;|&nbsp; Avg uptime: **78.7%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 79.24% | 2271.8 | 10206.7 | 1000ms | 267/1286 |
| ❌ | `public_apis_list` | 0.0% | 99.69% | 124.7 | 4595.4 | 1500ms | 4/1286 |
| ❌ | `nasa_apod` | 73.56% | 49.07% | 3425.8 | 11152.5 | 2000ms | 655/1286 |
| ❌ | `ipapi_check` | 76.83% | 99.92% | 154.9 | 4507.0 | 2500ms | 1/1286 |
| ⚠️ | `dog_ceo_random` | 97.98% | 96.73% | 533.7 | 10244.1 | 2500ms | 42/1286 |
| ⚠️ | `open_meteo_weather` | 98.68% | 96.81% | 738.5 | 14877.1 | 2000ms | 41/1286 |
| ⚠️ | `rest_countries` | 98.83% | 98.52% | 322.0 | 10221.5 | 2500ms | 19/1286 |
| ✅ | `useless_fact` | 99.61% | 99.69% | 632.0 | 10229.6 | 2500ms | 4/1286 |
| ✅ | `catfact_random` | 99.77% | 99.3% | 256.9 | 10080.2 | 3000ms | 9/1286 |
| ✅ | `coingecko_bitcoin` | 99.77% | 99.92% | 98.1 | 4328.4 | 1500ms | 1/1286 |
| ✅ | `agify_name` | 99.92% | 99.69% | 385.9 | 16112.2 | 2000ms | 4/1286 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.84% | 214.9 | 3882.8 | 2000ms | 2/1286 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `nasa_apod` | 02:00 | 5333.5 | 66.67% |
| `nasa_apod` | 03:00 | 4897.3 | 80.0% |
| `nasa_apod` | 05:00 | 4477.1 | 65.71% |
| `nasa_apod` | 09:00 | 4356.6 | 56.36% |
| `nasa_apod` | 01:00 | 4324.4 | 62.16% |
| `numbers_trivia` | 03:00 | 4200.6 | 40.0% |
| `nasa_apod` | 17:00 | 4144.0 | 55.88% |
| `nasa_apod` | 18:00 | 3790.2 | 54.55% |
| `nasa_apod` | 11:00 | 3780.1 | 55.07% |
| `nasa_apod` | 12:00 | 3673.1 | 54.39% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
