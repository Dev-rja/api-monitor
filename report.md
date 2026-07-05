# API Reliability Monitor — SLA Report

> Last updated: **2026-07-05 23:18 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **5/12** &nbsp;|&nbsp; Avg uptime: **78.6%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 79.63% | 2232.4 | 10206.7 | 1000ms | 267/1311 |
| ❌ | `public_apis_list` | 0.0% | 99.69% | 123.3 | 4595.4 | 1500ms | 4/1311 |
| ❌ | `nasa_apod` | 73.99% | 49.58% | 3384.8 | 11152.5 | 2000ms | 661/1311 |
| ❌ | `ipapi_check` | 76.51% | 99.92% | 154.8 | 4507.0 | 2500ms | 1/1311 |
| ⚠️ | `dog_ceo_random` | 96.11% | 96.8% | 531.2 | 10244.1 | 2500ms | 42/1311 |
| ⚠️ | `open_meteo_weather` | 98.63% | 96.87% | 735.7 | 14877.1 | 2000ms | 41/1311 |
| ⚠️ | `rest_countries` | 98.86% | 98.55% | 319.4 | 10221.5 | 2500ms | 19/1311 |
| ✅ | `useless_fact` | 99.62% | 99.69% | 632.6 | 10229.6 | 2500ms | 4/1311 |
| ✅ | `catfact_random` | 99.77% | 99.31% | 255.7 | 10080.2 | 3000ms | 9/1311 |
| ✅ | `coingecko_bitcoin` | 99.77% | 99.92% | 97.9 | 4328.4 | 1500ms | 1/1311 |
| ✅ | `agify_name` | 99.92% | 99.69% | 384.2 | 16112.2 | 2000ms | 4/1311 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.85% | 213.4 | 3882.8 | 2000ms | 2/1311 |

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
| `nasa_apod` | 17:00 | 4069.4 | 55.71% |
| `nasa_apod` | 18:00 | 3840.1 | 54.41% |
| `nasa_apod` | 11:00 | 3686.0 | 53.52% |
| `nasa_apod` | 20:00 | 3626.6 | 50.6% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
