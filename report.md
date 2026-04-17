# API Reliability Monitor — SLA Report

> Last updated: **2026-04-17 15:17 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **79.5%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 83.08% | 1957.8 | 10206.7 | 1000ms | 56/331 |
| ❌ | `public_apis_list` | 0.0% | 99.7% | 126.4 | 3806.8 | 1500ms | 1/331 |
| ❌ | `nasa_apod` | 65.56% | 43.81% | 3873.4 | 10538.0 | 2000ms | 186/331 |
| ❌ | `ipapi_check` | 93.05% | 100.0% | 160.4 | 353.0 | 2500ms | 0/331 |
| ⚠️ | `open_meteo_weather` | 97.58% | 96.37% | 790.3 | 14877.1 | 2000ms | 12/331 |
| ⚠️ | `dog_ceo_random` | 99.09% | 87.31% | 1006.3 | 10244.1 | 2500ms | 42/331 |
| ✅ | `useless_fact` | 99.4% | 99.09% | 588.2 | 10229.6 | 2500ms | 3/331 |
| ✅ | `catfact_random` | 99.4% | 99.7% | 253.1 | 10070.5 | 3000ms | 1/331 |
| ✅ | `agify_name` | 100.0% | 99.7% | 380.0 | 3237.1 | 2000ms | 1/331 |
| ✅ | `rest_countries` | 100.0% | 98.79% | 272.5 | 7269.1 | 2500ms | 4/331 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.7% | 239.7 | 2314.9 | 2000ms | 1/331 |
| ✅ | `coingecko_bitcoin` | 100.0% | 100.0% | 101.7 | 252.0 | 1500ms | 0/331 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `nasa_apod` | 03:00 | 5840.5 | 88.89% |
| `nasa_apod` | 20:00 | 4815.7 | 68.18% |
| `nasa_apod` | 18:00 | 4765.6 | 76.92% |
| `nasa_apod` | 11:00 | 4698.9 | 61.9% |
| `nasa_apod` | 17:00 | 4677.2 | 61.11% |
| `numbers_trivia` | 00:00 | 4205.1 | 40.0% |
| `nasa_apod` | 10:00 | 4174.0 | 53.33% |
| `nasa_apod` | 21:00 | 4054.0 | 42.11% |
| `nasa_apod` | 14:00 | 4029.0 | 52.63% |
| `nasa_apod` | 05:00 | 3989.9 | 66.67% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
