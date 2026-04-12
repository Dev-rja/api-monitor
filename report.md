# API Reliability Monitor — SLA Report

> Last updated: **2026-04-12 20:00 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **80.2%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 100.0% | 305.5 | 588.9 | 1000ms | 0/249 |
| ❌ | `public_apis_list` | 0.0% | 99.6% | 129.1 | 3806.8 | 1500ms | 1/249 |
| ❌ | `nasa_apod` | 73.49% | 54.62% | 2852.4 | 10538.0 | 2000ms | 113/249 |
| ❌ | `ipapi_check` | 94.78% | 100.0% | 158.3 | 353.0 | 2500ms | 0/249 |
| ⚠️ | `open_meteo_weather` | 96.79% | 95.98% | 859.0 | 14877.1 | 2000ms | 10/249 |
| ⚠️ | `dog_ceo_random` | 99.2% | 83.53% | 1176.9 | 5586.8 | 2500ms | 41/249 |
| ✅ | `useless_fact` | 99.2% | 99.6% | 580.5 | 10229.6 | 2500ms | 1/249 |
| ✅ | `catfact_random` | 99.2% | 99.6% | 268.2 | 10070.5 | 3000ms | 1/249 |
| ✅ | `agify_name` | 100.0% | 99.6% | 391.1 | 3237.1 | 2000ms | 1/249 |
| ✅ | `rest_countries` | 100.0% | 98.8% | 286.3 | 7269.1 | 2500ms | 3/249 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.6% | 234.2 | 2314.9 | 2000ms | 1/249 |
| ✅ | `coingecko_bitcoin` | 100.0% | 100.0% | 100.9 | 252.0 | 1500ms | 0/249 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `catfact_random` | 00:00 | 5139.3 | 50.0% |
| `nasa_apod` | 20:00 | 4096.3 | 58.82% |
| `nasa_apod` | 18:00 | 3896.7 | 70.0% |
| `nasa_apod` | 13:00 | 3734.4 | 57.14% |
| `nasa_apod` | 03:00 | 3704.9 | 80.0% |
| `nasa_apod` | 17:00 | 3623.8 | 50.0% |
| `nasa_apod` | 14:00 | 3601.8 | 42.86% |
| `nasa_apod` | 08:00 | 3100.8 | 50.0% |
| `nasa_apod` | 19:00 | 3078.6 | 46.67% |
| `nasa_apod` | 22:00 | 2961.3 | 46.67% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
