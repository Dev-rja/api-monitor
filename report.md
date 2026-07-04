# API Reliability Monitor — SLA Report

> Last updated: **2026-07-04 22:11 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **5/12** &nbsp;|&nbsp; Avg uptime: **78.7%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 79.4% | 2255.5 | 10206.7 | 1000ms | 267/1296 |
| ❌ | `public_apis_list` | 0.0% | 99.69% | 124.1 | 4595.4 | 1500ms | 4/1296 |
| ❌ | `nasa_apod` | 73.77% | 49.38% | 3404.7 | 11152.5 | 2000ms | 656/1296 |
| ❌ | `ipapi_check` | 76.77% | 99.92% | 155.0 | 4507.0 | 2500ms | 1/1296 |
| ⚠️ | `dog_ceo_random` | 97.22% | 96.76% | 532.2 | 10244.1 | 2500ms | 42/1296 |
| ⚠️ | `open_meteo_weather` | 98.61% | 96.84% | 737.1 | 14877.1 | 2000ms | 41/1296 |
| ⚠️ | `rest_countries` | 98.84% | 98.53% | 321.1 | 10221.5 | 2500ms | 19/1296 |
| ✅ | `useless_fact` | 99.61% | 99.69% | 631.9 | 10229.6 | 2500ms | 4/1296 |
| ✅ | `catfact_random` | 99.77% | 99.31% | 256.3 | 10080.2 | 3000ms | 9/1296 |
| ✅ | `coingecko_bitcoin` | 99.77% | 99.92% | 98.0 | 4328.4 | 1500ms | 1/1296 |
| ✅ | `agify_name` | 99.92% | 99.69% | 385.0 | 16112.2 | 2000ms | 4/1296 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.85% | 214.4 | 3882.8 | 2000ms | 2/1296 |

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
| `nasa_apod` | 17:00 | 4089.9 | 55.07% |
| `nasa_apod` | 18:00 | 3742.2 | 53.73% |
| `nasa_apod` | 11:00 | 3732.2 | 54.29% |
| `nasa_apod` | 20:00 | 3626.6 | 50.6% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
