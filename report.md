# API Reliability Monitor — SLA Report

> Last updated: **2026-07-17 08:25 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **5/12** &nbsp;|&nbsp; Avg uptime: **78.5%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 81.7% | 2030.0 | 10206.7 | 1000ms | 267/1459 |
| ❌ | `public_apis_list` | 0.0% | 99.73% | 122.2 | 4595.4 | 1500ms | 4/1459 |
| ❌ | `ipapi_check` | 73.75% | 99.93% | 153.2 | 4507.0 | 2500ms | 1/1459 |
| ❌ | `nasa_apod` | 75.87% | 51.82% | 3191.8 | 11152.5 | 2000ms | 703/1459 |
| ⚠️ | `dog_ceo_random` | 95.0% | 96.57% | 545.2 | 10244.1 | 2500ms | 50/1459 |
| ⚠️ | `open_meteo_weather` | 98.7% | 97.19% | 718.5 | 14877.1 | 2000ms | 41/1459 |
| ⚠️ | `rest_countries` | 98.97% | 98.7% | 306.6 | 10221.5 | 2500ms | 19/1459 |
| ✅ | `useless_fact` | 99.66% | 99.73% | 634.7 | 10229.6 | 2500ms | 4/1459 |
| ✅ | `catfact_random` | 99.79% | 99.38% | 255.1 | 10080.2 | 3000ms | 9/1459 |
| ✅ | `coingecko_bitcoin` | 99.79% | 99.93% | 97.0 | 4328.4 | 1500ms | 1/1459 |
| ✅ | `agify_name` | 99.93% | 99.73% | 385.5 | 16112.2 | 2000ms | 4/1459 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.86% | 206.7 | 3882.8 | 2000ms | 2/1459 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `nasa_apod` | 02:00 | 5333.5 | 66.67% |
| `nasa_apod` | 03:00 | 4339.2 | 75.0% |
| `nasa_apod` | 05:00 | 4220.5 | 60.0% |
| `nasa_apod` | 09:00 | 4004.9 | 52.46% |
| `nasa_apod` | 17:00 | 3954.9 | 53.33% |
| `nasa_apod` | 01:00 | 3686.6 | 53.33% |
| `nasa_apod` | 11:00 | 3587.7 | 51.85% |
| `nasa_apod` | 12:00 | 3557.1 | 52.38% |
| `numbers_trivia` | 03:00 | 3543.3 | 33.33% |
| `nasa_apod` | 18:00 | 3522.6 | 50.0% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
