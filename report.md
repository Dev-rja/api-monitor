# API Reliability Monitor — SLA Report

> Last updated: **2026-04-17 11:35 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **79.5%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 83.84% | 1883.5 | 10206.7 | 1000ms | 53/328 |
| ❌ | `public_apis_list` | 0.0% | 99.7% | 126.7 | 3806.8 | 1500ms | 1/328 |
| ❌ | `nasa_apod` | 65.24% | 43.6% | 3896.5 | 10538.0 | 2000ms | 185/328 |
| ❌ | `ipapi_check` | 93.29% | 100.0% | 160.2 | 353.0 | 2500ms | 0/328 |
| ⚠️ | `open_meteo_weather` | 97.56% | 96.34% | 793.6 | 14877.1 | 2000ms | 12/328 |
| ⚠️ | `dog_ceo_random` | 99.39% | 87.5% | 982.7 | 5586.8 | 2500ms | 41/328 |
| ✅ | `useless_fact` | 99.39% | 99.39% | 578.6 | 10229.6 | 2500ms | 2/328 |
| ✅ | `catfact_random` | 99.39% | 99.7% | 254.4 | 10070.5 | 3000ms | 1/328 |
| ✅ | `agify_name` | 100.0% | 99.7% | 381.4 | 3237.1 | 2000ms | 1/328 |
| ✅ | `rest_countries` | 100.0% | 98.78% | 274.2 | 7269.1 | 2500ms | 4/328 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.7% | 239.5 | 2314.9 | 2000ms | 1/328 |
| ✅ | `coingecko_bitcoin` | 100.0% | 100.0% | 101.9 | 252.0 | 1500ms | 0/328 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `nasa_apod` | 03:00 | 5840.5 | 88.89% |
| `nasa_apod` | 20:00 | 4815.7 | 68.18% |
| `nasa_apod` | 18:00 | 4765.6 | 76.92% |
| `nasa_apod` | 11:00 | 4698.9 | 61.9% |
| `nasa_apod` | 17:00 | 4677.2 | 61.11% |
| `nasa_apod` | 14:00 | 4220.6 | 55.56% |
| `numbers_trivia` | 00:00 | 4205.1 | 40.0% |
| `nasa_apod` | 10:00 | 4174.0 | 53.33% |
| `nasa_apod` | 21:00 | 4054.0 | 42.11% |
| `nasa_apod` | 05:00 | 3989.9 | 66.67% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
