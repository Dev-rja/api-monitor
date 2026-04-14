# API Reliability Monitor — SLA Report

> Last updated: **2026-04-14 07:21 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **80.0%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 100.0% | 301.3 | 588.9 | 1000ms | 0/274 |
| ❌ | `public_apis_list` | 0.0% | 99.64% | 126.7 | 3806.8 | 1500ms | 1/274 |
| ❌ | `nasa_apod` | 70.07% | 50.0% | 3317.1 | 10538.0 | 2000ms | 137/274 |
| ❌ | `ipapi_check` | 94.89% | 100.0% | 158.5 | 353.0 | 2500ms | 0/274 |
| ⚠️ | `open_meteo_weather` | 97.08% | 95.99% | 834.8 | 14877.1 | 2000ms | 11/274 |
| ⚠️ | `dog_ceo_random` | 99.27% | 85.04% | 1104.6 | 5586.8 | 2500ms | 41/274 |
| ✅ | `useless_fact` | 99.27% | 99.64% | 577.5 | 10229.6 | 2500ms | 1/274 |
| ✅ | `catfact_random` | 99.27% | 99.64% | 261.4 | 10070.5 | 3000ms | 1/274 |
| ✅ | `agify_name` | 100.0% | 99.64% | 387.6 | 3237.1 | 2000ms | 1/274 |
| ✅ | `rest_countries` | 100.0% | 98.91% | 277.5 | 7269.1 | 2500ms | 3/274 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.64% | 238.9 | 2314.9 | 2000ms | 1/274 |
| ✅ | `coingecko_bitcoin` | 100.0% | 100.0% | 100.6 | 252.0 | 1500ms | 0/274 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `nasa_apod` | 03:00 | 5624.1 | 85.71% |
| `nasa_apod` | 20:00 | 4763.5 | 63.16% |
| `nasa_apod` | 18:00 | 4464.9 | 72.73% |
| `nasa_apod` | 17:00 | 4072.6 | 53.33% |
| `nasa_apod` | 14:00 | 4050.6 | 46.67% |
| `nasa_apod` | 13:00 | 3734.4 | 57.14% |
| `nasa_apod` | 10:00 | 3532.9 | 45.45% |
| `nasa_apod` | 23:00 | 3531.7 | 42.86% |
| `nasa_apod` | 19:00 | 3524.3 | 50.0% |
| `catfact_random` | 00:00 | 3471.7 | 33.33% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
