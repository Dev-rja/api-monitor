# API Reliability Monitor — SLA Report

> Last updated: **2026-07-17 18:30 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **5/12** &nbsp;|&nbsp; Avg uptime: **78.5%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 81.79% | 2021.2 | 10206.7 | 1000ms | 267/1466 |
| ❌ | `public_apis_list` | 0.0% | 99.73% | 122.2 | 4595.4 | 1500ms | 4/1466 |
| ❌ | `ipapi_check` | 73.67% | 99.93% | 153.1 | 4507.0 | 2500ms | 1/1466 |
| ❌ | `nasa_apod` | 75.92% | 51.91% | 3186.9 | 11152.5 | 2000ms | 705/1466 |
| ❌ | `dog_ceo_random` | 94.95% | 96.45% | 550.8 | 10244.1 | 2500ms | 52/1466 |
| ⚠️ | `open_meteo_weather` | 98.7% | 97.2% | 717.6 | 14877.1 | 2000ms | 41/1466 |
| ⚠️ | `rest_countries` | 98.98% | 98.7% | 306.3 | 10221.5 | 2500ms | 19/1466 |
| ✅ | `useless_fact` | 99.66% | 99.73% | 634.6 | 10229.6 | 2500ms | 4/1466 |
| ✅ | `catfact_random` | 99.8% | 99.39% | 254.9 | 10080.2 | 3000ms | 9/1466 |
| ✅ | `coingecko_bitcoin` | 99.8% | 99.93% | 97.1 | 4328.4 | 1500ms | 1/1466 |
| ✅ | `agify_name` | 99.93% | 99.73% | 385.2 | 16112.2 | 2000ms | 4/1466 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.86% | 206.5 | 3882.8 | 2000ms | 2/1466 |

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
