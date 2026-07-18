# API Reliability Monitor — SLA Report

> Last updated: **2026-07-18 00:59 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **5/12** &nbsp;|&nbsp; Avg uptime: **78.4%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 81.86% | 2013.7 | 10206.7 | 1000ms | 267/1472 |
| ❌ | `public_apis_list` | 0.0% | 99.73% | 122.3 | 4595.4 | 1500ms | 4/1472 |
| ❌ | `ipapi_check` | 73.51% | 99.93% | 153.1 | 4507.0 | 2500ms | 1/1472 |
| ❌ | `nasa_apod` | 76.02% | 51.9% | 3180.2 | 11152.5 | 2000ms | 708/1472 |
| ❌ | `dog_ceo_random` | 94.97% | 96.4% | 552.9 | 10244.1 | 2500ms | 53/1472 |
| ⚠️ | `open_meteo_weather` | 98.71% | 97.21% | 716.8 | 14877.1 | 2000ms | 41/1472 |
| ⚠️ | `rest_countries` | 98.98% | 98.71% | 305.8 | 10221.5 | 2500ms | 19/1472 |
| ✅ | `useless_fact` | 99.66% | 99.73% | 634.7 | 10229.6 | 2500ms | 4/1472 |
| ✅ | `catfact_random` | 99.8% | 99.39% | 255.1 | 10080.2 | 3000ms | 9/1472 |
| ✅ | `coingecko_bitcoin` | 99.8% | 99.93% | 97.0 | 4328.4 | 1500ms | 1/1472 |
| ✅ | `agify_name` | 99.93% | 99.73% | 384.9 | 16112.2 | 2000ms | 4/1472 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.86% | 206.3 | 3882.8 | 2000ms | 2/1472 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `nasa_apod` | 02:00 | 5333.5 | 66.67% |
| `nasa_apod` | 03:00 | 4339.2 | 75.0% |
| `nasa_apod` | 05:00 | 4220.5 | 60.0% |
| `nasa_apod` | 09:00 | 4004.9 | 52.46% |
| `nasa_apod` | 17:00 | 3908.4 | 52.63% |
| `nasa_apod` | 01:00 | 3686.6 | 53.33% |
| `nasa_apod` | 11:00 | 3548.9 | 51.22% |
| `numbers_trivia` | 03:00 | 3543.3 | 33.33% |
| `nasa_apod` | 12:00 | 3541.4 | 53.13% |
| `nasa_apod` | 18:00 | 3483.6 | 49.37% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
