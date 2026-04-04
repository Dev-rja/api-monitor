# API Reliability Monitor — SLA Report

> Last updated: **2026-04-04 17:47 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **82.8%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 100.0% | 308.6 | 517.6 | 1000ms | 0/65 |
| ❌ | `public_apis_list` | 0.0% | 100.0% | 114.5 | 234.1 | 1500ms | 0/65 |
| ⚠️ | `open_meteo_weather` | 96.92% | 100.0% | 574.7 | 1426.6 | 2000ms | 0/65 |
| ❌ | `nasa_apod` | 98.46% | 70.77% | 1186.4 | 10538.0 | 2000ms | 19/65 |
| ⚠️ | `ipapi_check` | 98.46% | 100.0% | 152.5 | 248.6 | 2500ms | 0/65 |
| ❌ | `dog_ceo_random` | 100.0% | 73.85% | 1679.1 | 4785.5 | 2500ms | 17/65 |
| ✅ | `useless_fact` | 100.0% | 100.0% | 584.6 | 1705.0 | 2500ms | 0/65 |
| ✅ | `agify_name` | 100.0% | 98.46% | 458.0 | 3237.1 | 2000ms | 1/65 |
| ✅ | `catfact_random` | 100.0% | 100.0% | 251.2 | 1218.5 | 3000ms | 0/65 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 100.0% | 242.3 | 1556.1 | 2000ms | 0/65 |
| ✅ | `rest_countries` | 100.0% | 100.0% | 209.5 | 363.3 | 2500ms | 0/65 |
| ✅ | `coingecko_bitcoin` | 100.0% | 100.0% | 99.6 | 252.0 | 1500ms | 0/65 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `nasa_apod` | 10:00 | 3753.5 | 33.33% |
| `dog_ceo_random` | 17:00 | 3292.2 | 80.0% |
| `dog_ceo_random` | 14:00 | 3011.8 | 75.0% |
| `dog_ceo_random` | 13:00 | 2942.8 | 100.0% |
| `nasa_apod` | 18:00 | 2476.7 | 100.0% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
