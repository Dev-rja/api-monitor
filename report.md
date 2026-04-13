# API Reliability Monitor — SLA Report

> Last updated: **2026-04-13 10:12 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **80.1%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 100.0% | 301.9 | 588.9 | 1000ms | 0/259 |
| ❌ | `public_apis_list` | 0.0% | 99.61% | 128.5 | 3806.8 | 1500ms | 1/259 |
| ❌ | `nasa_apod` | 71.81% | 52.51% | 3088.3 | 10538.0 | 2000ms | 123/259 |
| ❌ | `ipapi_check` | 94.98% | 100.0% | 158.5 | 353.0 | 2500ms | 0/259 |
| ⚠️ | `open_meteo_weather` | 96.91% | 95.75% | 853.1 | 14877.1 | 2000ms | 11/259 |
| ⚠️ | `dog_ceo_random` | 99.23% | 84.17% | 1145.6 | 5586.8 | 2500ms | 41/259 |
| ✅ | `useless_fact` | 99.23% | 99.61% | 580.9 | 10229.6 | 2500ms | 1/259 |
| ✅ | `catfact_random` | 99.23% | 99.61% | 264.6 | 10070.5 | 3000ms | 1/259 |
| ✅ | `agify_name` | 100.0% | 99.61% | 388.9 | 3237.1 | 2000ms | 1/259 |
| ✅ | `rest_countries` | 100.0% | 98.84% | 280.8 | 7269.1 | 2500ms | 3/259 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.61% | 238.4 | 2314.9 | 2000ms | 1/259 |
| ✅ | `coingecko_bitcoin` | 100.0% | 100.0% | 100.3 | 252.0 | 1500ms | 0/259 |

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
| `nasa_apod` | 10:00 | 3532.9 | 45.45% |
| `nasa_apod` | 22:00 | 3427.1 | 50.0% |
| `nasa_apod` | 08:00 | 3226.7 | 54.55% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
