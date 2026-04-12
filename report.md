# API Reliability Monitor — SLA Report

> Last updated: **2026-04-12 21:23 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **80.2%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 100.0% | 304.8 | 588.9 | 1000ms | 0/251 |
| ❌ | `public_apis_list` | 0.0% | 99.6% | 129.0 | 3806.8 | 1500ms | 1/251 |
| ❌ | `nasa_apod` | 73.31% | 54.18% | 2908.5 | 10538.0 | 2000ms | 115/251 |
| ❌ | `ipapi_check` | 94.82% | 100.0% | 158.4 | 353.0 | 2500ms | 0/251 |
| ⚠️ | `open_meteo_weather` | 96.81% | 95.62% | 866.4 | 14877.1 | 2000ms | 11/251 |
| ⚠️ | `dog_ceo_random` | 99.2% | 83.67% | 1169.9 | 5586.8 | 2500ms | 41/251 |
| ✅ | `useless_fact` | 99.2% | 99.6% | 579.1 | 10229.6 | 2500ms | 1/251 |
| ✅ | `catfact_random` | 99.2% | 99.6% | 267.3 | 10070.5 | 3000ms | 1/251 |
| ✅ | `agify_name` | 100.0% | 99.6% | 390.7 | 3237.1 | 2000ms | 1/251 |
| ✅ | `rest_countries` | 100.0% | 98.8% | 284.8 | 7269.1 | 2500ms | 3/251 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.6% | 235.5 | 2314.9 | 2000ms | 1/251 |
| ✅ | `coingecko_bitcoin` | 100.0% | 100.0% | 100.9 | 252.0 | 1500ms | 0/251 |

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
