# API Reliability Monitor — SLA Report

> Last updated: **2026-04-14 12:45 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **79.9%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 98.92% | 406.5 | 10117.1 | 1000ms | 3/278 |
| ❌ | `public_apis_list` | 0.0% | 99.64% | 127.3 | 3806.8 | 1500ms | 1/278 |
| ❌ | `nasa_apod` | 69.78% | 49.28% | 3362.9 | 10538.0 | 2000ms | 141/278 |
| ❌ | `ipapi_check` | 94.24% | 100.0% | 158.0 | 353.0 | 2500ms | 0/278 |
| ⚠️ | `open_meteo_weather` | 97.12% | 96.04% | 829.6 | 14877.1 | 2000ms | 11/278 |
| ⚠️ | `dog_ceo_random` | 99.28% | 85.25% | 1092.2 | 5586.8 | 2500ms | 41/278 |
| ✅ | `useless_fact` | 99.28% | 99.64% | 575.5 | 10229.6 | 2500ms | 1/278 |
| ✅ | `catfact_random` | 99.28% | 99.64% | 260.7 | 10070.5 | 3000ms | 1/278 |
| ✅ | `agify_name` | 100.0% | 99.64% | 387.6 | 3237.1 | 2000ms | 1/278 |
| ✅ | `rest_countries` | 100.0% | 98.92% | 275.2 | 7269.1 | 2500ms | 3/278 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.64% | 238.1 | 2314.9 | 2000ms | 1/278 |
| ✅ | `coingecko_bitcoin` | 100.0% | 100.0% | 100.7 | 252.0 | 1500ms | 0/278 |

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
