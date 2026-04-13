# API Reliability Monitor — SLA Report

> Last updated: **2026-04-13 06:07 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **80.1%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 100.0% | 302.3 | 588.9 | 1000ms | 0/257 |
| ❌ | `public_apis_list` | 0.0% | 99.61% | 127.9 | 3806.8 | 1500ms | 1/257 |
| ❌ | `nasa_apod` | 71.98% | 52.92% | 3054.6 | 10538.0 | 2000ms | 121/257 |
| ❌ | `ipapi_check` | 94.94% | 100.0% | 158.3 | 353.0 | 2500ms | 0/257 |
| ⚠️ | `open_meteo_weather` | 96.89% | 95.72% | 856.5 | 14877.1 | 2000ms | 11/257 |
| ⚠️ | `dog_ceo_random` | 99.22% | 84.05% | 1150.0 | 5586.8 | 2500ms | 41/257 |
| ✅ | `useless_fact` | 99.22% | 99.61% | 576.2 | 10229.6 | 2500ms | 1/257 |
| ✅ | `catfact_random` | 99.22% | 99.61% | 265.5 | 10070.5 | 3000ms | 1/257 |
| ✅ | `agify_name` | 100.0% | 99.61% | 389.4 | 3237.1 | 2000ms | 1/257 |
| ✅ | `rest_countries` | 100.0% | 98.83% | 281.9 | 7269.1 | 2500ms | 3/257 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.61% | 238.3 | 2314.9 | 2000ms | 1/257 |
| ✅ | `coingecko_bitcoin` | 100.0% | 100.0% | 100.1 | 252.0 | 1500ms | 0/257 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `catfact_random` | 00:00 | 5139.3 | 50.0% |
| `nasa_apod` | 03:00 | 4838.2 | 83.33% |
| `nasa_apod` | 20:00 | 4450.2 | 61.11% |
| `nasa_apod` | 18:00 | 3896.7 | 70.0% |
| `nasa_apod` | 13:00 | 3734.4 | 57.14% |
| `nasa_apod` | 17:00 | 3623.8 | 50.0% |
| `nasa_apod` | 14:00 | 3601.8 | 42.86% |
| `nasa_apod` | 22:00 | 3427.1 | 50.0% |
| `nasa_apod` | 23:00 | 3190.2 | 40.0% |
| `nasa_apod` | 08:00 | 3100.8 | 50.0% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
