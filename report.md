# API Reliability Monitor — SLA Report

> Last updated: **2026-04-17 00:07 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **79.6%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 85.4% | 1730.4 | 10206.7 | 1000ms | 47/322 |
| ❌ | `public_apis_list` | 0.0% | 99.69% | 126.3 | 3806.8 | 1500ms | 1/322 |
| ❌ | `nasa_apod` | 65.84% | 44.1% | 3832.6 | 10538.0 | 2000ms | 180/322 |
| ❌ | `ipapi_check` | 93.17% | 100.0% | 160.0 | 353.0 | 2500ms | 0/322 |
| ⚠️ | `open_meteo_weather` | 97.52% | 96.27% | 799.0 | 14877.1 | 2000ms | 12/322 |
| ⚠️ | `dog_ceo_random` | 99.38% | 87.27% | 994.8 | 5586.8 | 2500ms | 41/322 |
| ✅ | `useless_fact` | 99.38% | 99.69% | 568.1 | 10229.6 | 2500ms | 1/322 |
| ✅ | `catfact_random` | 99.38% | 99.69% | 254.7 | 10070.5 | 3000ms | 1/322 |
| ✅ | `agify_name` | 100.0% | 99.69% | 382.4 | 3237.1 | 2000ms | 1/322 |
| ✅ | `rest_countries` | 100.0% | 98.76% | 276.1 | 7269.1 | 2500ms | 4/322 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.69% | 239.8 | 2314.9 | 2000ms | 1/322 |
| ✅ | `coingecko_bitcoin` | 100.0% | 100.0% | 101.3 | 252.0 | 1500ms | 0/322 |

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
| `numbers_trivia` | 00:00 | 4205.1 | 40.0% |
| `nasa_apod` | 21:00 | 4054.0 | 42.11% |
| `nasa_apod` | 00:00 | 3961.1 | 60.0% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
