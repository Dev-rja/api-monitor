# API Reliability Monitor — SLA Report

> Last updated: **2026-04-12 23:59 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **80.2%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 100.0% | 303.4 | 588.9 | 1000ms | 0/255 |
| ❌ | `public_apis_list` | 0.0% | 99.61% | 128.6 | 3806.8 | 1500ms | 1/255 |
| ❌ | `nasa_apod` | 72.55% | 53.33% | 2996.6 | 10538.0 | 2000ms | 119/255 |
| ❌ | `ipapi_check` | 94.9% | 100.0% | 158.4 | 353.0 | 2500ms | 0/255 |
| ⚠️ | `open_meteo_weather` | 96.86% | 95.69% | 859.9 | 14877.1 | 2000ms | 11/255 |
| ⚠️ | `dog_ceo_random` | 99.22% | 83.92% | 1157.0 | 5586.8 | 2500ms | 41/255 |
| ✅ | `useless_fact` | 99.22% | 99.61% | 577.4 | 10229.6 | 2500ms | 1/255 |
| ✅ | `catfact_random` | 99.22% | 99.61% | 267.1 | 10070.5 | 3000ms | 1/255 |
| ✅ | `agify_name` | 100.0% | 99.61% | 389.8 | 3237.1 | 2000ms | 1/255 |
| ✅ | `rest_countries` | 100.0% | 98.82% | 282.8 | 7269.1 | 2500ms | 3/255 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.61% | 239.0 | 2314.9 | 2000ms | 1/255 |
| ✅ | `coingecko_bitcoin` | 100.0% | 100.0% | 100.5 | 252.0 | 1500ms | 0/255 |

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
| `nasa_apod` | 22:00 | 3427.1 | 50.0% |
| `nasa_apod` | 23:00 | 3190.2 | 40.0% |
| `nasa_apod` | 08:00 | 3100.8 | 50.0% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
