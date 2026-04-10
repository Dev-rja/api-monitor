# API Reliability Monitor — SLA Report

> Last updated: **2026-04-10 06:20 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **4/12** &nbsp;|&nbsp; Avg uptime: **80.4%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 100.0% | 309.4 | 588.9 | 1000ms | 0/183 |
| ❌ | `public_apis_list` | 0.0% | 100.0% | 110.9 | 429.6 | 1500ms | 0/183 |
| ❌ | `nasa_apod` | 79.78% | 69.4% | 1829.8 | 10538.0 | 2000ms | 56/183 |
| ❌ | `ipapi_check` | 92.9% | 100.0% | 154.4 | 252.2 | 2500ms | 0/183 |
| ⚠️ | `open_meteo_weather` | 95.63% | 96.17% | 917.9 | 14877.1 | 2000ms | 7/183 |
| ❌ | `dog_ceo_random` | 98.91% | 78.14% | 1451.2 | 5586.8 | 2500ms | 40/183 |
| ⚠️ | `useless_fact` | 98.91% | 99.45% | 598.5 | 10229.6 | 2500ms | 1/183 |
| ⚠️ | `catfact_random` | 98.91% | 99.45% | 281.1 | 10070.5 | 3000ms | 1/183 |
| ✅ | `agify_name` | 100.0% | 99.45% | 403.0 | 3237.1 | 2000ms | 1/183 |
| ✅ | `rest_countries` | 100.0% | 98.91% | 285.0 | 7269.1 | 2500ms | 2/183 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.45% | 244.8 | 2314.9 | 2000ms | 1/183 |
| ✅ | `coingecko_bitcoin` | 100.0% | 100.0% | 100.1 | 252.0 | 1500ms | 0/183 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `catfact_random` | 00:00 | 5139.3 | 50.0% |
| `dog_ceo_random` | 13:00 | 4153.6 | 100.0% |
| `useless_fact` | 03:00 | 3792.8 | 33.33% |
| `nasa_apod` | 18:00 | 3358.5 | 57.14% |
| `nasa_apod` | 13:00 | 3279.6 | 50.0% |
| `open_meteo_weather` | 05:00 | 2968.6 | 16.67% |
| `nasa_apod` | 22:00 | 2903.8 | 33.33% |
| `nasa_apod` | 11:00 | 2771.9 | 41.67% |
| `nasa_apod` | 20:00 | 2637.8 | 41.67% |
| `open_meteo_weather` | 06:00 | 2352.6 | 14.29% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
