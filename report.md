# API Reliability Monitor — SLA Report

> Last updated: **2026-04-12 20:50 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **80.2%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 100.0% | 305.1 | 588.9 | 1000ms | 0/250 |
| ❌ | `public_apis_list` | 0.0% | 99.6% | 128.8 | 3806.8 | 1500ms | 1/250 |
| ❌ | `nasa_apod` | 73.2% | 54.4% | 2882.9 | 10538.0 | 2000ms | 114/250 |
| ❌ | `ipapi_check` | 94.8% | 100.0% | 158.4 | 353.0 | 2500ms | 0/250 |
| ⚠️ | `open_meteo_weather` | 96.8% | 95.6% | 868.2 | 14877.1 | 2000ms | 11/250 |
| ⚠️ | `dog_ceo_random` | 99.2% | 83.6% | 1173.0 | 5586.8 | 2500ms | 41/250 |
| ✅ | `useless_fact` | 99.2% | 99.6% | 579.9 | 10229.6 | 2500ms | 1/250 |
| ✅ | `catfact_random` | 99.2% | 99.6% | 268.0 | 10070.5 | 3000ms | 1/250 |
| ✅ | `agify_name` | 100.0% | 99.6% | 390.3 | 3237.1 | 2000ms | 1/250 |
| ✅ | `rest_countries` | 100.0% | 98.8% | 285.6 | 7269.1 | 2500ms | 3/250 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.6% | 235.7 | 2314.9 | 2000ms | 1/250 |
| ✅ | `coingecko_bitcoin` | 100.0% | 100.0% | 101.1 | 252.0 | 1500ms | 0/250 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `catfact_random` | 00:00 | 5139.3 | 50.0% |
| `nasa_apod` | 20:00 | 4450.2 | 61.11% |
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
