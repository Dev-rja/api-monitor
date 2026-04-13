# API Reliability Monitor — SLA Report

> Last updated: **2026-04-13 17:14 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **80.0%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 100.0% | 301.9 | 588.9 | 1000ms | 0/264 |
| ❌ | `public_apis_list` | 0.0% | 99.62% | 127.6 | 3806.8 | 1500ms | 1/264 |
| ❌ | `nasa_apod` | 70.83% | 51.52% | 3195.5 | 10538.0 | 2000ms | 128/264 |
| ❌ | `ipapi_check` | 94.7% | 100.0% | 158.4 | 353.0 | 2500ms | 0/264 |
| ⚠️ | `open_meteo_weather` | 96.97% | 95.83% | 847.0 | 14877.1 | 2000ms | 11/264 |
| ⚠️ | `dog_ceo_random` | 99.24% | 84.47% | 1130.2 | 5586.8 | 2500ms | 41/264 |
| ✅ | `useless_fact` | 99.24% | 99.62% | 580.4 | 10229.6 | 2500ms | 1/264 |
| ✅ | `catfact_random` | 99.24% | 99.62% | 263.3 | 10070.5 | 3000ms | 1/264 |
| ✅ | `agify_name` | 100.0% | 99.62% | 388.4 | 3237.1 | 2000ms | 1/264 |
| ✅ | `rest_countries` | 100.0% | 98.86% | 280.2 | 7269.1 | 2500ms | 3/264 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.62% | 236.8 | 2314.9 | 2000ms | 1/264 |
| ✅ | `coingecko_bitcoin` | 100.0% | 100.0% | 100.3 | 252.0 | 1500ms | 0/264 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `catfact_random` | 00:00 | 5139.3 | 50.0% |
| `nasa_apod` | 03:00 | 4838.2 | 83.33% |
| `nasa_apod` | 20:00 | 4450.2 | 61.11% |
| `nasa_apod` | 17:00 | 4072.6 | 53.33% |
| `nasa_apod` | 14:00 | 4050.6 | 46.67% |
| `nasa_apod` | 18:00 | 3896.7 | 70.0% |
| `nasa_apod` | 13:00 | 3734.4 | 57.14% |
| `nasa_apod` | 10:00 | 3532.9 | 45.45% |
| `nasa_apod` | 22:00 | 3427.1 | 50.0% |
| `nasa_apod` | 11:00 | 3354.6 | 52.94% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
