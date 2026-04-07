# API Reliability Monitor — SLA Report

> Last updated: **2026-04-07 23:24 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **5/12** &nbsp;|&nbsp; Avg uptime: **81.3%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 100.0% | 307.3 | 588.9 | 1000ms | 0/143 |
| ❌ | `public_apis_list` | 0.0% | 100.0% | 115.0 | 234.1 | 1500ms | 0/143 |
| ❌ | `nasa_apod` | 91.61% | 69.93% | 1712.0 | 10538.0 | 2000ms | 43/143 |
| ❌ | `ipapi_check` | 93.01% | 100.0% | 155.9 | 252.2 | 2500ms | 0/143 |
| ❌ | `open_meteo_weather` | 94.41% | 95.1% | 1012.2 | 14877.1 | 2000ms | 7/143 |
| ❌ | `dog_ceo_random` | 98.6% | 72.03% | 1747.2 | 5586.8 | 2500ms | 40/143 |
| ⚠️ | `useless_fact` | 98.6% | 99.3% | 628.2 | 10229.6 | 2500ms | 1/143 |
| ✅ | `catfact_random` | 99.3% | 100.0% | 237.1 | 1218.5 | 3000ms | 0/143 |
| ✅ | `agify_name` | 100.0% | 99.3% | 406.8 | 3237.1 | 2000ms | 1/143 |
| ✅ | `rest_countries` | 100.0% | 98.6% | 303.0 | 7269.1 | 2500ms | 2/143 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.3% | 252.3 | 2314.9 | 2000ms | 1/143 |
| ✅ | `coingecko_bitcoin` | 100.0% | 100.0% | 101.9 | 252.0 | 1500ms | 0/143 |

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
