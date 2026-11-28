# API Reliability Monitor — SLA Report

> Last updated: **2026-11-28 12:15 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **76.1%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 74.76% | 2657.4 | 10420.1 | 1000ms | 729/2888 |
| ❌ | `public_apis_list` | 0.0% | 99.38% | 145.1 | 5075.4 | 1500ms | 18/2888 |
| ❌ | `ipapi_check` | 42.35% | 99.97% | 144.8 | 4507.0 | 2500ms | 1/2888 |
| ❌ | `nasa_apod` | 76.52% | 59.14% | 2717.1 | 11152.5 | 2000ms | 1180/2888 |
| ⚠️ | `dog_ceo_random` | 97.33% | 97.89% | 479.2 | 10509.6 | 2500ms | 61/2888 |
| ⚠️ | `open_meteo_weather` | 98.75% | 98.13% | 677.3 | 14877.1 | 2000ms | 54/2888 |
| ✅ | `useless_fact` | 99.03% | 99.55% | 669.9 | 10229.6 | 2500ms | 13/2888 |
| ✅ | `rest_countries` | 99.48% | 99.2% | 269.6 | 10221.5 | 2500ms | 23/2888 |
| ✅ | `coingecko_bitcoin` | 99.72% | 99.93% | 96.8 | 4328.4 | 1500ms | 2/2888 |
| ✅ | `catfact_random` | 99.83% | 99.52% | 267.1 | 10080.2 | 3000ms | 14/2888 |
| ✅ | `agify_name` | 99.93% | 99.41% | 407.2 | 16112.2 | 2000ms | 17/2888 |
| ✅ | `jsonplaceholder_posts` | 99.97% | 99.86% | 180.8 | 10927.2 | 2000ms | 4/2888 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `numbers_trivia` | 03:00 | 4053.3 | 40.0% |
| `nasa_apod` | 11:00 | 3199.1 | 43.66% |
| `nasa_apod` | 09:00 | 3117.8 | 44.17% |
| `nasa_apod` | 00:00 | 3108.8 | 40.63% |
| `numbers_trivia` | 10:00 | 3102.6 | 29.31% |
| `nasa_apod` | 18:00 | 3089.8 | 44.83% |
| `nasa_apod` | 03:00 | 3063.8 | 46.67% |
| `nasa_apod` | 17:00 | 3048.7 | 38.36% |
| `nasa_apod` | 02:00 | 3027.2 | 38.89% |
| `nasa_apod` | 05:00 | 3012.8 | 44.09% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
