# API Reliability Monitor — SLA Report

> Last updated: **2026-04-13 14:25 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **80.0%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 100.0% | 301.3 | 588.9 | 1000ms | 0/262 |
| ❌ | `public_apis_list` | 0.0% | 99.62% | 128.2 | 3806.8 | 1500ms | 1/262 |
| ❌ | `nasa_apod` | 70.99% | 51.91% | 3171.6 | 10538.0 | 2000ms | 126/262 |
| ❌ | `ipapi_check` | 94.66% | 100.0% | 158.7 | 353.0 | 2500ms | 0/262 |
| ⚠️ | `open_meteo_weather` | 96.95% | 95.8% | 848.9 | 14877.1 | 2000ms | 11/262 |
| ⚠️ | `dog_ceo_random` | 99.24% | 84.35% | 1136.1 | 5586.8 | 2500ms | 41/262 |
| ✅ | `useless_fact` | 99.24% | 99.62% | 579.6 | 10229.6 | 2500ms | 1/262 |
| ✅ | `catfact_random` | 99.24% | 99.62% | 262.9 | 10070.5 | 3000ms | 1/262 |
| ✅ | `agify_name` | 100.0% | 99.62% | 388.4 | 3237.1 | 2000ms | 1/262 |
| ✅ | `rest_countries` | 100.0% | 98.85% | 280.3 | 7269.1 | 2500ms | 3/262 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.62% | 237.6 | 2314.9 | 2000ms | 1/262 |
| ✅ | `coingecko_bitcoin` | 100.0% | 100.0% | 100.3 | 252.0 | 1500ms | 0/262 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `catfact_random` | 00:00 | 5139.3 | 50.0% |
| `nasa_apod` | 03:00 | 4838.2 | 83.33% |
| `nasa_apod` | 20:00 | 4450.2 | 61.11% |
| `nasa_apod` | 14:00 | 4050.6 | 46.67% |
| `nasa_apod` | 18:00 | 3896.7 | 70.0% |
| `nasa_apod` | 13:00 | 3734.4 | 57.14% |
| `nasa_apod` | 17:00 | 3623.8 | 50.0% |
| `nasa_apod` | 10:00 | 3532.9 | 45.45% |
| `nasa_apod` | 22:00 | 3427.1 | 50.0% |
| `nasa_apod` | 11:00 | 3354.6 | 52.94% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
