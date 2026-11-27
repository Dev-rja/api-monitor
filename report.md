# API Reliability Monitor — SLA Report

> Last updated: **2026-11-27 21:39 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **76.1%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 74.74% | 2659.1 | 10420.1 | 1000ms | 729/2886 |
| ❌ | `public_apis_list` | 0.0% | 99.38% | 145.1 | 5075.4 | 1500ms | 18/2886 |
| ❌ | `ipapi_check` | 42.31% | 99.97% | 144.8 | 4507.0 | 2500ms | 1/2886 |
| ❌ | `nasa_apod` | 76.54% | 59.15% | 2717.6 | 11152.5 | 2000ms | 1179/2886 |
| ⚠️ | `dog_ceo_random` | 97.33% | 97.89% | 479.2 | 10509.6 | 2500ms | 61/2886 |
| ⚠️ | `open_meteo_weather` | 98.79% | 98.16% | 674.2 | 14877.1 | 2000ms | 53/2886 |
| ✅ | `useless_fact` | 99.03% | 99.55% | 669.9 | 10229.6 | 2500ms | 13/2886 |
| ✅ | `rest_countries` | 99.48% | 99.2% | 269.6 | 10221.5 | 2500ms | 23/2886 |
| ✅ | `coingecko_bitcoin` | 99.72% | 99.93% | 96.8 | 4328.4 | 1500ms | 2/2886 |
| ✅ | `catfact_random` | 99.83% | 99.51% | 267.1 | 10080.2 | 3000ms | 14/2886 |
| ✅ | `agify_name` | 99.93% | 99.41% | 407.2 | 16112.2 | 2000ms | 17/2886 |
| ✅ | `jsonplaceholder_posts` | 99.97% | 99.86% | 180.9 | 10927.2 | 2000ms | 4/2886 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `numbers_trivia` | 03:00 | 4120.0 | 40.68% |
| `nasa_apod` | 11:00 | 3199.1 | 43.66% |
| `nasa_apod` | 09:00 | 3117.8 | 44.17% |
| `nasa_apod` | 00:00 | 3108.8 | 40.63% |
| `numbers_trivia` | 10:00 | 3102.6 | 29.31% |
| `nasa_apod` | 18:00 | 3089.8 | 44.83% |
| `nasa_apod` | 03:00 | 3055.2 | 45.76% |
| `nasa_apod` | 17:00 | 3048.7 | 38.36% |
| `nasa_apod` | 02:00 | 3027.2 | 38.89% |
| `nasa_apod` | 05:00 | 3012.8 | 44.09% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
