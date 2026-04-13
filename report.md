# API Reliability Monitor — SLA Report

> Last updated: **2026-04-13 11:43 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **80.1%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 100.0% | 301.5 | 588.9 | 1000ms | 0/260 |
| ❌ | `public_apis_list` | 0.0% | 99.62% | 128.2 | 3806.8 | 1500ms | 1/260 |
| ❌ | `nasa_apod` | 71.54% | 52.31% | 3116.1 | 10538.0 | 2000ms | 124/260 |
| ⚠️ | `ipapi_check` | 95.0% | 100.0% | 158.5 | 353.0 | 2500ms | 0/260 |
| ⚠️ | `open_meteo_weather` | 96.92% | 95.77% | 851.4 | 14877.1 | 2000ms | 11/260 |
| ⚠️ | `dog_ceo_random` | 99.23% | 84.23% | 1142.2 | 5586.8 | 2500ms | 41/260 |
| ✅ | `useless_fact` | 99.23% | 99.62% | 580.5 | 10229.6 | 2500ms | 1/260 |
| ✅ | `catfact_random` | 99.23% | 99.62% | 263.9 | 10070.5 | 3000ms | 1/260 |
| ✅ | `agify_name` | 100.0% | 99.62% | 388.6 | 3237.1 | 2000ms | 1/260 |
| ✅ | `rest_countries` | 100.0% | 98.85% | 280.1 | 7269.1 | 2500ms | 3/260 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.62% | 238.2 | 2314.9 | 2000ms | 1/260 |
| ✅ | `coingecko_bitcoin` | 100.0% | 100.0% | 100.1 | 252.0 | 1500ms | 0/260 |

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
| `nasa_apod` | 11:00 | 3354.6 | 52.94% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
