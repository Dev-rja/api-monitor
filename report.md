# API Reliability Monitor — SLA Report

> Last updated: **2026-04-11 22:50 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **80.4%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 100.0% | 308.0 | 588.9 | 1000ms | 0/228 |
| ❌ | `public_apis_list` | 0.0% | 99.56% | 127.7 | 3806.8 | 1500ms | 1/228 |
| ❌ | `nasa_apod` | 76.32% | 57.89% | 2499.0 | 10538.0 | 2000ms | 96/228 |
| ❌ | `ipapi_check` | 94.3% | 100.0% | 156.9 | 252.2 | 2500ms | 0/228 |
| ⚠️ | `open_meteo_weather` | 96.49% | 95.61% | 885.7 | 14877.1 | 2000ms | 10/228 |
| ⚠️ | `dog_ceo_random` | 99.12% | 82.02% | 1251.6 | 5586.8 | 2500ms | 41/228 |
| ✅ | `useless_fact` | 99.12% | 99.56% | 586.9 | 10229.6 | 2500ms | 1/228 |
| ✅ | `catfact_random` | 99.12% | 99.56% | 271.7 | 10070.5 | 3000ms | 1/228 |
| ✅ | `agify_name` | 100.0% | 99.56% | 396.4 | 3237.1 | 2000ms | 1/228 |
| ✅ | `rest_countries` | 100.0% | 98.68% | 293.7 | 7269.1 | 2500ms | 3/228 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.56% | 239.6 | 2314.9 | 2000ms | 1/228 |
| ✅ | `coingecko_bitcoin` | 100.0% | 100.0% | 100.6 | 252.0 | 1500ms | 0/228 |

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
| `dog_ceo_random` | 13:00 | 2918.8 | 66.67% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
