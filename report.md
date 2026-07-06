# API Reliability Monitor — SLA Report

> Last updated: **2026-07-06 05:37 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **5/12** &nbsp;|&nbsp; Avg uptime: **78.6%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 79.66% | 2229.3 | 10206.7 | 1000ms | 267/1313 |
| ❌ | `public_apis_list` | 0.0% | 99.7% | 123.2 | 4595.4 | 1500ms | 4/1313 |
| ❌ | `nasa_apod` | 74.03% | 49.66% | 3380.4 | 11152.5 | 2000ms | 661/1313 |
| ❌ | `ipapi_check` | 76.47% | 99.92% | 154.8 | 4507.0 | 2500ms | 1/1313 |
| ⚠️ | `dog_ceo_random` | 95.96% | 96.8% | 531.0 | 10244.1 | 2500ms | 42/1313 |
| ⚠️ | `open_meteo_weather` | 98.63% | 96.88% | 735.5 | 14877.1 | 2000ms | 41/1313 |
| ⚠️ | `rest_countries` | 98.86% | 98.55% | 319.3 | 10221.5 | 2500ms | 19/1313 |
| ✅ | `useless_fact` | 99.62% | 99.7% | 632.5 | 10229.6 | 2500ms | 4/1313 |
| ✅ | `catfact_random` | 99.77% | 99.31% | 255.6 | 10080.2 | 3000ms | 9/1313 |
| ✅ | `coingecko_bitcoin` | 99.77% | 99.92% | 97.9 | 4328.4 | 1500ms | 1/1313 |
| ✅ | `agify_name` | 99.92% | 99.7% | 384.1 | 16112.2 | 2000ms | 4/1313 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.85% | 213.3 | 3882.8 | 2000ms | 2/1313 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `nasa_apod` | 02:00 | 5333.5 | 66.67% |
| `nasa_apod` | 03:00 | 4897.3 | 80.0% |
| `nasa_apod` | 05:00 | 4367.1 | 63.89% |
| `nasa_apod` | 09:00 | 4282.5 | 55.36% |
| `nasa_apod` | 01:00 | 4222.8 | 60.53% |
| `numbers_trivia` | 03:00 | 4200.6 | 40.0% |
| `nasa_apod` | 17:00 | 4069.4 | 55.71% |
| `nasa_apod` | 18:00 | 3840.1 | 54.41% |
| `nasa_apod` | 11:00 | 3686.0 | 53.52% |
| `nasa_apod` | 20:00 | 3626.6 | 50.6% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
