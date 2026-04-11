# API Reliability Monitor — SLA Report

> Last updated: **2026-04-11 23:22 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **80.4%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 100.0% | 308.3 | 588.9 | 1000ms | 0/229 |
| ❌ | `public_apis_list` | 0.0% | 99.56% | 127.4 | 3806.8 | 1500ms | 1/229 |
| ❌ | `nasa_apod` | 75.98% | 57.64% | 2532.7 | 10538.0 | 2000ms | 97/229 |
| ❌ | `ipapi_check` | 94.32% | 100.0% | 157.0 | 252.2 | 2500ms | 0/229 |
| ⚠️ | `open_meteo_weather` | 96.51% | 95.63% | 884.6 | 14877.1 | 2000ms | 10/229 |
| ⚠️ | `dog_ceo_random` | 99.13% | 82.1% | 1247.5 | 5586.8 | 2500ms | 41/229 |
| ✅ | `useless_fact` | 99.13% | 99.56% | 587.2 | 10229.6 | 2500ms | 1/229 |
| ✅ | `catfact_random` | 99.13% | 99.56% | 272.5 | 10070.5 | 3000ms | 1/229 |
| ✅ | `agify_name` | 100.0% | 99.56% | 397.1 | 3237.1 | 2000ms | 1/229 |
| ✅ | `rest_countries` | 100.0% | 98.69% | 293.7 | 7269.1 | 2500ms | 3/229 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.56% | 239.3 | 2314.9 | 2000ms | 1/229 |
| ✅ | `coingecko_bitcoin` | 100.0% | 100.0% | 100.8 | 252.0 | 1500ms | 0/229 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `catfact_random` | 00:00 | 5139.3 | 50.0% |
| `nasa_apod` | 13:00 | 4268.1 | 66.67% |
| `nasa_apod` | 18:00 | 4037.8 | 66.67% |
| `nasa_apod` | 20:00 | 3714.0 | 56.25% |
| `nasa_apod` | 17:00 | 3163.1 | 41.67% |
| `nasa_apod` | 19:00 | 3079.8 | 42.86% |
| `nasa_apod` | 11:00 | 3069.2 | 53.33% |
| `useless_fact` | 03:00 | 2972.0 | 25.0% |
| `nasa_apod` | 22:00 | 2961.3 | 46.67% |
| `nasa_apod` | 23:00 | 2942.6 | 35.29% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
