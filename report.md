# API Reliability Monitor — SLA Report

> Last updated: **2026-04-16 14:30 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **79.6%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 87.86% | 1490.0 | 10206.7 | 1000ms | 38/313 |
| ❌ | `public_apis_list` | 0.0% | 99.68% | 127.1 | 3806.8 | 1500ms | 1/313 |
| ❌ | `nasa_apod` | 66.45% | 45.05% | 3753.5 | 10538.0 | 2000ms | 172/313 |
| ❌ | `ipapi_check` | 93.29% | 100.0% | 159.5 | 353.0 | 2500ms | 0/313 |
| ⚠️ | `open_meteo_weather` | 97.44% | 96.17% | 804.8 | 14877.1 | 2000ms | 12/313 |
| ⚠️ | `dog_ceo_random` | 99.36% | 86.9% | 1011.6 | 5586.8 | 2500ms | 41/313 |
| ✅ | `useless_fact` | 99.36% | 99.68% | 569.2 | 10229.6 | 2500ms | 1/313 |
| ✅ | `catfact_random` | 99.36% | 99.68% | 254.6 | 10070.5 | 3000ms | 1/313 |
| ✅ | `agify_name` | 100.0% | 99.68% | 381.6 | 3237.1 | 2000ms | 1/313 |
| ✅ | `rest_countries` | 100.0% | 98.72% | 276.9 | 7269.1 | 2500ms | 4/313 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.68% | 239.9 | 2314.9 | 2000ms | 1/313 |
| ✅ | `coingecko_bitcoin` | 100.0% | 100.0% | 100.7 | 252.0 | 1500ms | 0/313 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `nasa_apod` | 03:00 | 5273.5 | 87.5% |
| `nasa_apod` | 18:00 | 4952.5 | 75.0% |
| `nasa_apod` | 20:00 | 4550.4 | 66.67% |
| `nasa_apod` | 10:00 | 4445.3 | 57.14% |
| `nasa_apod` | 11:00 | 4414.7 | 60.0% |
| `nasa_apod` | 17:00 | 4370.4 | 58.82% |
| `nasa_apod` | 14:00 | 4220.6 | 55.56% |
| `nasa_apod` | 13:00 | 3734.4 | 57.14% |
| `nasa_apod` | 21:00 | 3704.5 | 38.89% |
| `nasa_apod` | 15:00 | 3689.4 | 62.5% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
