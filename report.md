# API Reliability Monitor — SLA Report

> Last updated: **2026-04-14 11:37 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **79.9%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 99.28% | 371.7 | 10117.1 | 1000ms | 2/277 |
| ❌ | `public_apis_list` | 0.0% | 99.64% | 127.0 | 3806.8 | 1500ms | 1/277 |
| ❌ | `nasa_apod` | 69.68% | 49.46% | 3365.7 | 10538.0 | 2000ms | 140/277 |
| ❌ | `ipapi_check` | 94.58% | 100.0% | 158.4 | 353.0 | 2500ms | 0/277 |
| ⚠️ | `open_meteo_weather` | 97.11% | 96.03% | 831.1 | 14877.1 | 2000ms | 11/277 |
| ⚠️ | `dog_ceo_random` | 99.28% | 85.2% | 1095.6 | 5586.8 | 2500ms | 41/277 |
| ✅ | `useless_fact` | 99.28% | 99.64% | 576.4 | 10229.6 | 2500ms | 1/277 |
| ✅ | `catfact_random` | 99.28% | 99.64% | 261.4 | 10070.5 | 3000ms | 1/277 |
| ✅ | `agify_name` | 100.0% | 99.64% | 386.1 | 3237.1 | 2000ms | 1/277 |
| ✅ | `rest_countries` | 100.0% | 98.92% | 275.9 | 7269.1 | 2500ms | 3/277 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.64% | 238.1 | 2314.9 | 2000ms | 1/277 |
| ✅ | `coingecko_bitcoin` | 100.0% | 100.0% | 100.9 | 252.0 | 1500ms | 0/277 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `nasa_apod` | 03:00 | 5624.1 | 85.71% |
| `nasa_apod` | 20:00 | 4763.5 | 63.16% |
| `nasa_apod` | 18:00 | 4464.9 | 72.73% |
| `nasa_apod` | 17:00 | 4072.6 | 53.33% |
| `nasa_apod` | 14:00 | 4050.6 | 46.67% |
| `nasa_apod` | 08:00 | 3821.0 | 58.33% |
| `nasa_apod` | 11:00 | 3748.3 | 55.56% |
| `nasa_apod` | 13:00 | 3734.4 | 57.14% |
| `nasa_apod` | 23:00 | 3531.7 | 42.86% |
| `nasa_apod` | 19:00 | 3524.3 | 50.0% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
