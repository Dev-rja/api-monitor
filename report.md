# API Reliability Monitor — SLA Report

> Last updated: **2026-04-11 22:03 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **80.4%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 100.0% | 307.7 | 588.9 | 1000ms | 0/227 |
| ❌ | `public_apis_list` | 0.0% | 99.56% | 127.3 | 3806.8 | 1500ms | 1/227 |
| ❌ | `nasa_apod` | 76.21% | 58.15% | 2498.6 | 10538.0 | 2000ms | 95/227 |
| ❌ | `ipapi_check` | 94.27% | 100.0% | 156.5 | 252.2 | 2500ms | 0/227 |
| ⚠️ | `open_meteo_weather` | 96.48% | 95.59% | 887.0 | 14877.1 | 2000ms | 10/227 |
| ⚠️ | `dog_ceo_random` | 99.12% | 81.94% | 1255.3 | 5586.8 | 2500ms | 41/227 |
| ✅ | `useless_fact` | 99.12% | 99.56% | 587.4 | 10229.6 | 2500ms | 1/227 |
| ✅ | `catfact_random` | 99.12% | 99.56% | 271.1 | 10070.5 | 3000ms | 1/227 |
| ✅ | `agify_name` | 100.0% | 99.56% | 395.6 | 3237.1 | 2000ms | 1/227 |
| ✅ | `rest_countries` | 100.0% | 98.68% | 293.5 | 7269.1 | 2500ms | 3/227 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.56% | 239.4 | 2314.9 | 2000ms | 1/227 |
| ✅ | `coingecko_bitcoin` | 100.0% | 100.0% | 100.4 | 252.0 | 1500ms | 0/227 |

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
| `nasa_apod` | 22:00 | 2986.8 | 42.86% |
| `useless_fact` | 03:00 | 2972.0 | 25.0% |
| `dog_ceo_random` | 13:00 | 2918.8 | 66.67% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
