# API Reliability Monitor — SLA Report

> Last updated: **2026-04-15 16:45 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **79.7%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 92.28% | 1056.0 | 10176.4 | 1000ms | 23/298 |
| ❌ | `public_apis_list` | 0.0% | 99.66% | 125.8 | 3806.8 | 1500ms | 1/298 |
| ❌ | `nasa_apod` | 67.45% | 46.64% | 3612.7 | 10538.0 | 2000ms | 159/298 |
| ❌ | `ipapi_check` | 93.62% | 100.0% | 159.3 | 353.0 | 2500ms | 0/298 |
| ⚠️ | `open_meteo_weather` | 97.32% | 96.31% | 810.9 | 14877.1 | 2000ms | 11/298 |
| ⚠️ | `dog_ceo_random` | 99.33% | 86.24% | 1047.7 | 5586.8 | 2500ms | 41/298 |
| ✅ | `useless_fact` | 99.33% | 99.66% | 570.3 | 10229.6 | 2500ms | 1/298 |
| ✅ | `catfact_random` | 99.33% | 99.66% | 257.5 | 10070.5 | 3000ms | 1/298 |
| ✅ | `agify_name` | 100.0% | 99.66% | 386.1 | 3237.1 | 2000ms | 1/298 |
| ✅ | `rest_countries` | 100.0% | 98.66% | 282.0 | 7269.1 | 2500ms | 4/298 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.66% | 241.1 | 2314.9 | 2000ms | 1/298 |
| ✅ | `coingecko_bitcoin` | 100.0% | 100.0% | 101.1 | 252.0 | 1500ms | 0/298 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `nasa_apod` | 03:00 | 5273.5 | 87.5% |
| `nasa_apod` | 18:00 | 4952.5 | 75.0% |
| `nasa_apod` | 20:00 | 4651.7 | 65.0% |
| `nasa_apod` | 14:00 | 4321.9 | 52.94% |
| `nasa_apod` | 11:00 | 4098.4 | 57.89% |
| `nasa_apod` | 17:00 | 3994.7 | 56.25% |
| `nasa_apod` | 10:00 | 3989.3 | 53.85% |
| `nasa_apod` | 08:00 | 3821.0 | 58.33% |
| `nasa_apod` | 13:00 | 3734.4 | 57.14% |
| `nasa_apod` | 15:00 | 3689.4 | 62.5% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
