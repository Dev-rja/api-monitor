# API Reliability Monitor — SLA Report

> Last updated: **2026-07-16 20:05 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **5/12** &nbsp;|&nbsp; Avg uptime: **78.5%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 81.61% | 2038.7 | 10206.7 | 1000ms | 267/1452 |
| ❌ | `public_apis_list` | 0.0% | 99.72% | 122.2 | 4595.4 | 1500ms | 4/1452 |
| ❌ | `ipapi_check` | 73.97% | 99.93% | 153.3 | 4507.0 | 2500ms | 1/1452 |
| ❌ | `nasa_apod` | 75.9% | 51.72% | 3202.1 | 11152.5 | 2000ms | 701/1452 |
| ❌ | `dog_ceo_random` | 94.97% | 96.63% | 541.8 | 10244.1 | 2500ms | 49/1452 |
| ⚠️ | `open_meteo_weather` | 98.69% | 97.18% | 719.2 | 14877.1 | 2000ms | 41/1452 |
| ⚠️ | `rest_countries` | 98.97% | 98.69% | 307.0 | 10221.5 | 2500ms | 19/1452 |
| ✅ | `useless_fact` | 99.66% | 99.72% | 634.6 | 10229.6 | 2500ms | 4/1452 |
| ✅ | `catfact_random` | 99.79% | 99.38% | 255.1 | 10080.2 | 3000ms | 9/1452 |
| ✅ | `coingecko_bitcoin` | 99.79% | 99.93% | 97.1 | 4328.4 | 1500ms | 1/1452 |
| ✅ | `agify_name` | 99.93% | 99.72% | 385.4 | 16112.2 | 2000ms | 4/1452 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.86% | 207.1 | 3882.8 | 2000ms | 2/1452 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `nasa_apod` | 02:00 | 5333.5 | 66.67% |
| `nasa_apod` | 03:00 | 4510.1 | 78.26% |
| `nasa_apod` | 05:00 | 4220.5 | 60.0% |
| `nasa_apod` | 09:00 | 4004.9 | 52.46% |
| `nasa_apod` | 17:00 | 3954.9 | 53.33% |
| `nasa_apod` | 01:00 | 3686.6 | 53.33% |
| `numbers_trivia` | 03:00 | 3681.5 | 34.78% |
| `nasa_apod` | 11:00 | 3587.7 | 51.85% |
| `nasa_apod` | 12:00 | 3557.1 | 52.38% |
| `nasa_apod` | 18:00 | 3522.6 | 50.0% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
