# API Reliability Monitor — SLA Report

> Last updated: **2026-04-16 23:27 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **79.6%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 85.67% | 1704.5 | 10206.7 | 1000ms | 46/321 |
| ❌ | `public_apis_list` | 0.0% | 99.69% | 126.5 | 3806.8 | 1500ms | 1/321 |
| ❌ | `nasa_apod` | 66.04% | 44.24% | 3812.2 | 10538.0 | 2000ms | 179/321 |
| ❌ | `ipapi_check` | 93.15% | 100.0% | 159.7 | 353.0 | 2500ms | 0/321 |
| ⚠️ | `open_meteo_weather` | 97.51% | 96.26% | 799.5 | 14877.1 | 2000ms | 12/321 |
| ⚠️ | `dog_ceo_random` | 99.38% | 87.23% | 996.8 | 5586.8 | 2500ms | 41/321 |
| ✅ | `useless_fact` | 99.38% | 99.69% | 567.8 | 10229.6 | 2500ms | 1/321 |
| ✅ | `catfact_random` | 99.38% | 99.69% | 254.9 | 10070.5 | 3000ms | 1/321 |
| ✅ | `agify_name` | 100.0% | 99.69% | 381.8 | 3237.1 | 2000ms | 1/321 |
| ✅ | `rest_countries` | 100.0% | 98.75% | 276.2 | 7269.1 | 2500ms | 4/321 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.69% | 239.6 | 2314.9 | 2000ms | 1/321 |
| ✅ | `coingecko_bitcoin` | 100.0% | 100.0% | 101.1 | 252.0 | 1500ms | 0/321 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `nasa_apod` | 03:00 | 5273.5 | 87.5% |
| `nasa_apod` | 20:00 | 4815.7 | 68.18% |
| `nasa_apod` | 18:00 | 4765.6 | 76.92% |
| `nasa_apod` | 17:00 | 4677.2 | 61.11% |
| `nasa_apod` | 10:00 | 4445.3 | 57.14% |
| `nasa_apod` | 11:00 | 4414.7 | 60.0% |
| `nasa_apod` | 14:00 | 4220.6 | 55.56% |
| `nasa_apod` | 21:00 | 4054.0 | 42.11% |
| `nasa_apod` | 23:00 | 3923.8 | 48.0% |
| `nasa_apod` | 13:00 | 3734.4 | 57.14% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
