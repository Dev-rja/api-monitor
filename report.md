# API Reliability Monitor — SLA Report

> Last updated: **2026-07-07 01:12 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **5/12** &nbsp;|&nbsp; Avg uptime: **78.5%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 79.79% | 2217.2 | 10206.7 | 1000ms | 267/1321 |
| ❌ | `public_apis_list` | 0.0% | 99.7% | 122.8 | 4595.4 | 1500ms | 4/1321 |
| ❌ | `nasa_apod` | 74.19% | 49.89% | 3364.3 | 11152.5 | 2000ms | 662/1321 |
| ❌ | `ipapi_check` | 76.46% | 99.92% | 155.0 | 4507.0 | 2500ms | 1/1321 |
| ⚠️ | `dog_ceo_random` | 95.38% | 96.82% | 530.8 | 10244.1 | 2500ms | 42/1321 |
| ⚠️ | `open_meteo_weather` | 98.56% | 96.9% | 734.4 | 14877.1 | 2000ms | 41/1321 |
| ⚠️ | `rest_countries` | 98.86% | 98.56% | 318.8 | 10221.5 | 2500ms | 19/1321 |
| ✅ | `useless_fact` | 99.62% | 99.7% | 632.8 | 10229.6 | 2500ms | 4/1321 |
| ✅ | `catfact_random` | 99.77% | 99.32% | 256.3 | 10080.2 | 3000ms | 9/1321 |
| ✅ | `coingecko_bitcoin` | 99.77% | 99.92% | 98.0 | 4328.4 | 1500ms | 1/1321 |
| ✅ | `agify_name` | 99.92% | 99.7% | 384.0 | 16112.2 | 2000ms | 4/1321 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.85% | 213.0 | 3882.8 | 2000ms | 2/1321 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `nasa_apod` | 02:00 | 5333.5 | 66.67% |
| `nasa_apod` | 03:00 | 4897.3 | 80.0% |
| `nasa_apod` | 05:00 | 4367.1 | 63.89% |
| `nasa_apod` | 09:00 | 4216.7 | 54.39% |
| `numbers_trivia` | 03:00 | 4200.6 | 40.0% |
| `nasa_apod` | 01:00 | 4125.5 | 58.97% |
| `nasa_apod` | 17:00 | 4069.4 | 55.71% |
| `nasa_apod` | 18:00 | 3790.7 | 53.62% |
| `nasa_apod` | 11:00 | 3686.0 | 53.52% |
| `nasa_apod` | 20:00 | 3588.9 | 50.0% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
