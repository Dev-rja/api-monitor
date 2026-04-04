# API Reliability Monitor — SLA Report

> Last updated: **2026-04-04 15:19 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **82.8%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 100.0% | 307.8 | 517.6 | 1000ms | 0/61 |
| ❌ | `public_apis_list` | 0.0% | 100.0% | 115.1 | 234.1 | 1500ms | 0/61 |
| ⚠️ | `open_meteo_weather` | 96.72% | 100.0% | 576.7 | 1426.6 | 2000ms | 0/61 |
| ❌ | `nasa_apod` | 98.36% | 70.49% | 1201.4 | 10538.0 | 2000ms | 18/61 |
| ⚠️ | `ipapi_check` | 98.36% | 100.0% | 153.9 | 248.6 | 2500ms | 0/61 |
| ❌ | `dog_ceo_random` | 100.0% | 77.05% | 1595.0 | 4785.5 | 2500ms | 14/61 |
| ✅ | `useless_fact` | 100.0% | 100.0% | 586.7 | 1705.0 | 2500ms | 0/61 |
| ✅ | `agify_name` | 100.0% | 98.36% | 463.5 | 3237.1 | 2000ms | 1/61 |
| ✅ | `catfact_random` | 100.0% | 100.0% | 257.7 | 1218.5 | 3000ms | 0/61 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 100.0% | 235.4 | 1556.1 | 2000ms | 0/61 |
| ✅ | `rest_countries` | 100.0% | 100.0% | 209.6 | 363.3 | 2500ms | 0/61 |
| ✅ | `coingecko_bitcoin` | 100.0% | 100.0% | 101.8 | 252.0 | 1500ms | 0/61 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `nasa_apod` | 10:00 | 3753.5 | 33.33% |
| `dog_ceo_random` | 17:00 | 3075.1 | 66.67% |
| `dog_ceo_random` | 14:00 | 3011.8 | 75.0% |
| `dog_ceo_random` | 13:00 | 2942.8 | 100.0% |
| `nasa_apod` | 18:00 | 2476.7 | 100.0% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
