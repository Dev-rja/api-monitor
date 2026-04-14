# API Reliability Monitor — SLA Report

> Last updated: **2026-04-14 14:29 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **79.9%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 98.57% | 441.2 | 10117.1 | 1000ms | 4/279 |
| ❌ | `public_apis_list` | 0.0% | 99.64% | 127.1 | 3806.8 | 1500ms | 1/279 |
| ❌ | `nasa_apod` | 69.53% | 49.1% | 3387.8 | 10538.0 | 2000ms | 142/279 |
| ❌ | `ipapi_check` | 94.27% | 100.0% | 158.6 | 353.0 | 2500ms | 0/279 |
| ⚠️ | `open_meteo_weather` | 97.13% | 96.06% | 828.7 | 14877.1 | 2000ms | 11/279 |
| ⚠️ | `dog_ceo_random` | 99.28% | 85.3% | 1089.5 | 5586.8 | 2500ms | 41/279 |
| ✅ | `useless_fact` | 99.28% | 99.64% | 575.5 | 10229.6 | 2500ms | 1/279 |
| ✅ | `catfact_random` | 99.28% | 99.64% | 260.4 | 10070.5 | 3000ms | 1/279 |
| ✅ | `agify_name` | 100.0% | 99.64% | 387.5 | 3237.1 | 2000ms | 1/279 |
| ✅ | `rest_countries` | 100.0% | 98.92% | 275.4 | 7269.1 | 2500ms | 3/279 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.64% | 239.0 | 2314.9 | 2000ms | 1/279 |
| ✅ | `coingecko_bitcoin` | 100.0% | 100.0% | 100.8 | 252.0 | 1500ms | 0/279 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `nasa_apod` | 03:00 | 5624.1 | 85.71% |
| `nasa_apod` | 20:00 | 4763.5 | 63.16% |
| `nasa_apod` | 18:00 | 4464.9 | 72.73% |
| `nasa_apod` | 14:00 | 4442.8 | 50.0% |
| `nasa_apod` | 17:00 | 4072.6 | 53.33% |
| `nasa_apod` | 08:00 | 3821.0 | 58.33% |
| `nasa_apod` | 11:00 | 3748.3 | 55.56% |
| `nasa_apod` | 13:00 | 3734.4 | 57.14% |
| `nasa_apod` | 23:00 | 3531.7 | 42.86% |
| `nasa_apod` | 19:00 | 3524.3 | 50.0% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
