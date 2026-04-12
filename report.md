# API Reliability Monitor — SLA Report

> Last updated: **2026-04-12 19:26 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **80.2%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 100.0% | 305.1 | 588.9 | 1000ms | 0/248 |
| ❌ | `public_apis_list` | 0.0% | 99.6% | 129.4 | 3806.8 | 1500ms | 1/248 |
| ❌ | `nasa_apod` | 73.79% | 54.84% | 2822.7 | 10538.0 | 2000ms | 112/248 |
| ❌ | `ipapi_check` | 94.76% | 100.0% | 158.2 | 353.0 | 2500ms | 0/248 |
| ⚠️ | `open_meteo_weather` | 96.77% | 95.97% | 856.8 | 14877.1 | 2000ms | 10/248 |
| ⚠️ | `dog_ceo_random` | 99.19% | 83.47% | 1179.7 | 5586.8 | 2500ms | 41/248 |
| ✅ | `useless_fact` | 99.19% | 99.6% | 580.6 | 10229.6 | 2500ms | 1/248 |
| ✅ | `catfact_random` | 99.19% | 99.6% | 268.6 | 10070.5 | 3000ms | 1/248 |
| ✅ | `agify_name` | 100.0% | 99.6% | 389.4 | 3237.1 | 2000ms | 1/248 |
| ✅ | `rest_countries` | 100.0% | 98.79% | 286.4 | 7269.1 | 2500ms | 3/248 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.6% | 234.5 | 2314.9 | 2000ms | 1/248 |
| ✅ | `coingecko_bitcoin` | 100.0% | 100.0% | 100.7 | 252.0 | 1500ms | 0/248 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `catfact_random` | 00:00 | 5139.3 | 50.0% |
| `nasa_apod` | 18:00 | 3896.7 | 70.0% |
| `nasa_apod` | 13:00 | 3734.4 | 57.14% |
| `nasa_apod` | 20:00 | 3714.0 | 56.25% |
| `nasa_apod` | 03:00 | 3704.9 | 80.0% |
| `nasa_apod` | 17:00 | 3623.8 | 50.0% |
| `nasa_apod` | 14:00 | 3601.8 | 42.86% |
| `nasa_apod` | 08:00 | 3100.8 | 50.0% |
| `nasa_apod` | 19:00 | 3078.6 | 46.67% |
| `nasa_apod` | 22:00 | 2961.3 | 46.67% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
