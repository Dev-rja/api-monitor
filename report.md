# API Reliability Monitor — SLA Report

> Last updated: **2026-07-06 16:42 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **5/12** &nbsp;|&nbsp; Avg uptime: **78.6%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 79.71% | 2224.6 | 10206.7 | 1000ms | 267/1316 |
| ❌ | `public_apis_list` | 0.0% | 99.7% | 123.0 | 4595.4 | 1500ms | 4/1316 |
| ❌ | `nasa_apod` | 74.09% | 49.7% | 3375.3 | 11152.5 | 2000ms | 662/1316 |
| ❌ | `ipapi_check` | 76.52% | 99.92% | 154.8 | 4507.0 | 2500ms | 1/1316 |
| ⚠️ | `dog_ceo_random` | 95.74% | 96.81% | 530.9 | 10244.1 | 2500ms | 42/1316 |
| ⚠️ | `open_meteo_weather` | 98.63% | 96.88% | 734.9 | 14877.1 | 2000ms | 41/1316 |
| ⚠️ | `rest_countries` | 98.86% | 98.56% | 319.2 | 10221.5 | 2500ms | 19/1316 |
| ✅ | `useless_fact` | 99.62% | 99.7% | 632.5 | 10229.6 | 2500ms | 4/1316 |
| ✅ | `catfact_random` | 99.77% | 99.32% | 255.5 | 10080.2 | 3000ms | 9/1316 |
| ✅ | `coingecko_bitcoin` | 99.77% | 99.92% | 98.0 | 4328.4 | 1500ms | 1/1316 |
| ✅ | `agify_name` | 99.92% | 99.7% | 383.8 | 16112.2 | 2000ms | 4/1316 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.85% | 213.2 | 3882.8 | 2000ms | 2/1316 |

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
| `nasa_apod` | 18:00 | 3840.1 | 54.41% |
| `nasa_apod` | 11:00 | 3686.0 | 53.52% |
| `nasa_apod` | 20:00 | 3626.6 | 50.6% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
