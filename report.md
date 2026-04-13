# API Reliability Monitor — SLA Report

> Last updated: **2026-04-13 19:45 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **80.0%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 100.0% | 303.2 | 588.9 | 1000ms | 0/266 |
| ❌ | `public_apis_list` | 0.0% | 99.62% | 127.0 | 3806.8 | 1500ms | 1/266 |
| ❌ | `nasa_apod` | 70.3% | 51.13% | 3248.0 | 10538.0 | 2000ms | 130/266 |
| ❌ | `ipapi_check` | 94.74% | 100.0% | 158.0 | 353.0 | 2500ms | 0/266 |
| ⚠️ | `open_meteo_weather` | 96.99% | 95.86% | 845.5 | 14877.1 | 2000ms | 11/266 |
| ⚠️ | `dog_ceo_random` | 99.25% | 84.59% | 1126.1 | 5586.8 | 2500ms | 41/266 |
| ✅ | `useless_fact` | 99.25% | 99.62% | 580.6 | 10229.6 | 2500ms | 1/266 |
| ✅ | `catfact_random` | 99.25% | 99.62% | 262.6 | 10070.5 | 3000ms | 1/266 |
| ✅ | `agify_name` | 100.0% | 99.62% | 390.5 | 3237.1 | 2000ms | 1/266 |
| ✅ | `rest_countries` | 100.0% | 98.87% | 280.5 | 7269.1 | 2500ms | 3/266 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.62% | 236.2 | 2314.9 | 2000ms | 1/266 |
| ✅ | `coingecko_bitcoin` | 100.0% | 100.0% | 100.2 | 252.0 | 1500ms | 0/266 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `catfact_random` | 00:00 | 5139.3 | 50.0% |
| `nasa_apod` | 03:00 | 4838.2 | 83.33% |
| `nasa_apod` | 18:00 | 4464.9 | 72.73% |
| `nasa_apod` | 20:00 | 4450.2 | 61.11% |
| `nasa_apod` | 17:00 | 4072.6 | 53.33% |
| `nasa_apod` | 14:00 | 4050.6 | 46.67% |
| `nasa_apod` | 13:00 | 3734.4 | 57.14% |
| `nasa_apod` | 10:00 | 3532.9 | 45.45% |
| `nasa_apod` | 19:00 | 3524.3 | 50.0% |
| `nasa_apod` | 22:00 | 3427.1 | 50.0% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
