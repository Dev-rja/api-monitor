# API Reliability Monitor — SLA Report

> Last updated: **2026-04-13 03:47 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **80.1%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 100.0% | 303.0 | 588.9 | 1000ms | 0/256 |
| ❌ | `public_apis_list` | 0.0% | 99.61% | 128.3 | 3806.8 | 1500ms | 1/256 |
| ❌ | `nasa_apod` | 72.27% | 53.13% | 3026.0 | 10538.0 | 2000ms | 120/256 |
| ❌ | `ipapi_check` | 94.92% | 100.0% | 158.4 | 353.0 | 2500ms | 0/256 |
| ⚠️ | `open_meteo_weather` | 96.88% | 95.7% | 858.2 | 14877.1 | 2000ms | 11/256 |
| ⚠️ | `dog_ceo_random` | 99.22% | 83.98% | 1153.1 | 5586.8 | 2500ms | 41/256 |
| ✅ | `useless_fact` | 99.22% | 99.61% | 576.8 | 10229.6 | 2500ms | 1/256 |
| ✅ | `catfact_random` | 99.22% | 99.61% | 266.4 | 10070.5 | 3000ms | 1/256 |
| ✅ | `agify_name` | 100.0% | 99.61% | 389.6 | 3237.1 | 2000ms | 1/256 |
| ✅ | `rest_countries` | 100.0% | 98.83% | 282.4 | 7269.1 | 2500ms | 3/256 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.61% | 238.6 | 2314.9 | 2000ms | 1/256 |
| ✅ | `coingecko_bitcoin` | 100.0% | 100.0% | 100.3 | 252.0 | 1500ms | 0/256 |

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
