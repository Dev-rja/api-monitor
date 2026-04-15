# API Reliability Monitor — SLA Report

> Last updated: **2026-04-15 10:25 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **79.8%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 93.86% | 901.8 | 10146.1 | 1000ms | 18/293 |
| ❌ | `public_apis_list` | 0.0% | 99.66% | 126.7 | 3806.8 | 1500ms | 1/293 |
| ❌ | `nasa_apod` | 67.92% | 47.1% | 3561.0 | 10538.0 | 2000ms | 155/293 |
| ❌ | `ipapi_check` | 93.86% | 100.0% | 159.7 | 353.0 | 2500ms | 0/293 |
| ⚠️ | `open_meteo_weather` | 97.27% | 96.25% | 815.4 | 14877.1 | 2000ms | 11/293 |
| ⚠️ | `dog_ceo_random` | 99.32% | 86.01% | 1059.4 | 5586.8 | 2500ms | 41/293 |
| ✅ | `useless_fact` | 99.32% | 99.66% | 570.6 | 10229.6 | 2500ms | 1/293 |
| ✅ | `catfact_random` | 99.32% | 99.66% | 259.3 | 10070.5 | 3000ms | 1/293 |
| ✅ | `agify_name` | 100.0% | 99.66% | 386.6 | 3237.1 | 2000ms | 1/293 |
| ✅ | `rest_countries` | 100.0% | 98.98% | 271.7 | 7269.1 | 2500ms | 3/293 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.66% | 239.7 | 2314.9 | 2000ms | 1/293 |
| ✅ | `coingecko_bitcoin` | 100.0% | 100.0% | 101.4 | 252.0 | 1500ms | 0/293 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `nasa_apod` | 03:00 | 5273.5 | 87.5% |
| `nasa_apod` | 18:00 | 4952.5 | 75.0% |
| `nasa_apod` | 20:00 | 4651.7 | 65.0% |
| `nasa_apod` | 14:00 | 4442.8 | 50.0% |
| `nasa_apod` | 17:00 | 3994.7 | 56.25% |
| `nasa_apod` | 10:00 | 3989.3 | 53.85% |
| `nasa_apod` | 08:00 | 3821.0 | 58.33% |
| `nasa_apod` | 11:00 | 3748.3 | 55.56% |
| `nasa_apod` | 13:00 | 3734.4 | 57.14% |
| `nasa_apod` | 22:00 | 3660.8 | 50.0% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
