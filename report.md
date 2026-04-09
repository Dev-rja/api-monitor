# API Reliability Monitor — SLA Report

> Last updated: **2026-04-09 23:51 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **4/12** &nbsp;|&nbsp; Avg uptime: **80.4%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 100.0% | 309.2 | 588.9 | 1000ms | 0/180 |
| ❌ | `public_apis_list` | 0.0% | 100.0% | 111.2 | 429.6 | 1500ms | 0/180 |
| ❌ | `nasa_apod` | 79.44% | 70.56% | 1817.0 | 10538.0 | 2000ms | 53/180 |
| ❌ | `ipapi_check` | 93.33% | 100.0% | 154.8 | 252.2 | 2500ms | 0/180 |
| ⚠️ | `open_meteo_weather` | 95.56% | 96.11% | 924.7 | 14877.1 | 2000ms | 7/180 |
| ❌ | `dog_ceo_random` | 98.89% | 77.78% | 1468.2 | 5586.8 | 2500ms | 40/180 |
| ⚠️ | `useless_fact` | 98.89% | 99.44% | 600.2 | 10229.6 | 2500ms | 1/180 |
| ⚠️ | `catfact_random` | 98.89% | 99.44% | 284.2 | 10070.5 | 3000ms | 1/180 |
| ✅ | `agify_name` | 100.0% | 99.44% | 403.6 | 3237.1 | 2000ms | 1/180 |
| ✅ | `rest_countries` | 100.0% | 98.89% | 287.2 | 7269.1 | 2500ms | 2/180 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.44% | 245.2 | 2314.9 | 2000ms | 1/180 |
| ✅ | `coingecko_bitcoin` | 100.0% | 100.0% | 100.3 | 252.0 | 1500ms | 0/180 |

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
| `open_meteo_weather` | 06:00 | 2675.4 | 16.67% |
| `nasa_apod` | 20:00 | 2637.8 | 41.67% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
