# API Reliability Monitor — SLA Report

> Last updated: **2026-07-06 23:18 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **5/12** &nbsp;|&nbsp; Avg uptime: **78.5%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 79.77% | 2218.6 | 10206.7 | 1000ms | 267/1320 |
| ❌ | `public_apis_list` | 0.0% | 99.7% | 122.9 | 4595.4 | 1500ms | 4/1320 |
| ❌ | `nasa_apod` | 74.17% | 49.85% | 3366.5 | 11152.5 | 2000ms | 662/1320 |
| ❌ | `ipapi_check` | 76.44% | 99.92% | 155.0 | 4507.0 | 2500ms | 1/1320 |
| ⚠️ | `dog_ceo_random` | 95.45% | 96.82% | 530.8 | 10244.1 | 2500ms | 42/1320 |
| ⚠️ | `open_meteo_weather` | 98.56% | 96.89% | 734.4 | 14877.1 | 2000ms | 41/1320 |
| ⚠️ | `rest_countries` | 98.86% | 98.56% | 319.0 | 10221.5 | 2500ms | 19/1320 |
| ✅ | `useless_fact` | 99.62% | 99.7% | 632.7 | 10229.6 | 2500ms | 4/1320 |
| ✅ | `catfact_random` | 99.77% | 99.32% | 256.4 | 10080.2 | 3000ms | 9/1320 |
| ✅ | `coingecko_bitcoin` | 99.77% | 99.92% | 98.0 | 4328.4 | 1500ms | 1/1320 |
| ✅ | `agify_name` | 99.92% | 99.7% | 383.8 | 16112.2 | 2000ms | 4/1320 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.85% | 213.1 | 3882.8 | 2000ms | 2/1320 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `nasa_apod` | 02:00 | 5333.5 | 66.67% |
| `nasa_apod` | 03:00 | 4897.3 | 80.0% |
| `nasa_apod` | 05:00 | 4367.1 | 63.89% |
| `nasa_apod` | 01:00 | 4222.8 | 60.53% |
| `nasa_apod` | 09:00 | 4216.7 | 54.39% |
| `numbers_trivia` | 03:00 | 4200.6 | 40.0% |
| `nasa_apod` | 17:00 | 4069.4 | 55.71% |
| `nasa_apod` | 18:00 | 3790.7 | 53.62% |
| `nasa_apod` | 11:00 | 3686.0 | 53.52% |
| `nasa_apod` | 20:00 | 3588.9 | 50.0% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
