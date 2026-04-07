# API Reliability Monitor — SLA Report

> Last updated: **2026-04-07 22:40 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **5/12** &nbsp;|&nbsp; Avg uptime: **81.3%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 100.0% | 305.8 | 588.9 | 1000ms | 0/142 |
| ❌ | `public_apis_list` | 0.0% | 100.0% | 114.9 | 234.1 | 1500ms | 0/142 |
| ❌ | `nasa_apod` | 91.55% | 69.72% | 1722.4 | 10538.0 | 2000ms | 43/142 |
| ❌ | `ipapi_check` | 92.96% | 100.0% | 156.4 | 252.2 | 2500ms | 0/142 |
| ❌ | `open_meteo_weather` | 94.37% | 95.07% | 1014.7 | 14877.1 | 2000ms | 7/142 |
| ❌ | `dog_ceo_random` | 98.59% | 71.83% | 1755.5 | 5586.8 | 2500ms | 40/142 |
| ⚠️ | `useless_fact` | 98.59% | 99.3% | 627.8 | 10229.6 | 2500ms | 1/142 |
| ✅ | `catfact_random` | 99.3% | 100.0% | 237.7 | 1218.5 | 3000ms | 0/142 |
| ✅ | `agify_name` | 100.0% | 99.3% | 406.3 | 3237.1 | 2000ms | 1/142 |
| ✅ | `rest_countries` | 100.0% | 98.59% | 303.2 | 7269.1 | 2500ms | 2/142 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.3% | 252.1 | 2314.9 | 2000ms | 1/142 |
| ✅ | `coingecko_bitcoin` | 100.0% | 100.0% | 102.3 | 252.0 | 1500ms | 0/142 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `useless_fact` | 03:00 | 5454.5 | 50.0% |
| `open_meteo_weather` | 05:00 | 4216.1 | 25.0% |
| `dog_ceo_random` | 13:00 | 4153.6 | 100.0% |
| `nasa_apod` | 13:00 | 3279.6 | 50.0% |
| `nasa_apod` | 11:00 | 3203.4 | 50.0% |
| `open_meteo_weather` | 06:00 | 3112.1 | 20.0% |
| `dog_ceo_random` | 12:00 | 3057.6 | 50.0% |
| `nasa_apod` | 20:00 | 2829.3 | 40.0% |
| `nasa_apod` | 22:00 | 2715.0 | 30.0% |
| `dog_ceo_random` | 17:00 | 2591.7 | 62.5% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
