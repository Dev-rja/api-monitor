# API Reliability Monitor — SLA Report

> Last updated: **2026-04-17 10:36 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **79.5%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 84.1% | 1858.4 | 10206.7 | 1000ms | 52/327 |
| ❌ | `public_apis_list` | 0.0% | 99.69% | 126.8 | 3806.8 | 1500ms | 1/327 |
| ❌ | `nasa_apod` | 65.44% | 43.73% | 3876.7 | 10538.0 | 2000ms | 184/327 |
| ❌ | `ipapi_check` | 93.27% | 100.0% | 160.0 | 353.0 | 2500ms | 0/327 |
| ⚠️ | `open_meteo_weather` | 97.55% | 96.33% | 794.3 | 14877.1 | 2000ms | 12/327 |
| ⚠️ | `dog_ceo_random` | 99.39% | 87.46% | 984.2 | 5586.8 | 2500ms | 41/327 |
| ✅ | `useless_fact` | 99.39% | 99.39% | 579.0 | 10229.6 | 2500ms | 2/327 |
| ✅ | `catfact_random` | 99.39% | 99.69% | 254.8 | 10070.5 | 3000ms | 1/327 |
| ✅ | `agify_name` | 100.0% | 99.69% | 381.6 | 3237.1 | 2000ms | 1/327 |
| ✅ | `rest_countries` | 100.0% | 98.78% | 274.4 | 7269.1 | 2500ms | 4/327 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.69% | 239.4 | 2314.9 | 2000ms | 1/327 |
| ✅ | `coingecko_bitcoin` | 100.0% | 100.0% | 101.5 | 252.0 | 1500ms | 0/327 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `nasa_apod` | 03:00 | 5840.5 | 88.89% |
| `nasa_apod` | 20:00 | 4815.7 | 68.18% |
| `nasa_apod` | 18:00 | 4765.6 | 76.92% |
| `nasa_apod` | 17:00 | 4677.2 | 61.11% |
| `nasa_apod` | 11:00 | 4414.7 | 60.0% |
| `nasa_apod` | 14:00 | 4220.6 | 55.56% |
| `numbers_trivia` | 00:00 | 4205.1 | 40.0% |
| `nasa_apod` | 10:00 | 4174.0 | 53.33% |
| `nasa_apod` | 21:00 | 4054.0 | 42.11% |
| `nasa_apod` | 05:00 | 3989.9 | 66.67% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
