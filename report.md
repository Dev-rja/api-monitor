# API Reliability Monitor — SLA Report

> Last updated: **2026-07-17 12:51 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **5/12** &nbsp;|&nbsp; Avg uptime: **78.5%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 81.74% | 2026.2 | 10206.7 | 1000ms | 267/1462 |
| ❌ | `public_apis_list` | 0.0% | 99.73% | 122.3 | 4595.4 | 1500ms | 4/1462 |
| ❌ | `ipapi_check` | 73.8% | 99.93% | 153.2 | 4507.0 | 2500ms | 1/1462 |
| ❌ | `nasa_apod` | 75.92% | 51.85% | 3187.7 | 11152.5 | 2000ms | 704/1462 |
| ❌ | `dog_ceo_random` | 94.94% | 96.51% | 548.0 | 10244.1 | 2500ms | 51/1462 |
| ⚠️ | `open_meteo_weather` | 98.7% | 97.2% | 718.2 | 14877.1 | 2000ms | 41/1462 |
| ⚠️ | `rest_countries` | 98.97% | 98.7% | 306.5 | 10221.5 | 2500ms | 19/1462 |
| ✅ | `useless_fact` | 99.66% | 99.73% | 634.7 | 10229.6 | 2500ms | 4/1462 |
| ✅ | `catfact_random` | 99.79% | 99.38% | 255.0 | 10080.2 | 3000ms | 9/1462 |
| ✅ | `coingecko_bitcoin` | 99.79% | 99.93% | 97.1 | 4328.4 | 1500ms | 1/1462 |
| ✅ | `agify_name` | 99.93% | 99.73% | 385.4 | 16112.2 | 2000ms | 4/1462 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.86% | 206.6 | 3882.8 | 2000ms | 2/1462 |

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
| `nasa_apod` | 11:00 | 3548.9 | 51.22% |
| `numbers_trivia` | 03:00 | 3543.3 | 33.33% |
| `nasa_apod` | 12:00 | 3541.4 | 53.13% |
| `nasa_apod` | 18:00 | 3522.6 | 50.0% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
