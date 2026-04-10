# API Reliability Monitor — SLA Report

> Last updated: **2026-04-10 09:23 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **4/12** &nbsp;|&nbsp; Avg uptime: **80.5%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 100.0% | 309.9 | 588.9 | 1000ms | 0/185 |
| ❌ | `public_apis_list` | 0.0% | 100.0% | 111.8 | 429.6 | 1500ms | 0/185 |
| ❌ | `nasa_apod` | 80.0% | 69.19% | 1824.8 | 10538.0 | 2000ms | 57/185 |
| ❌ | `ipapi_check` | 92.97% | 100.0% | 154.1 | 252.2 | 2500ms | 0/185 |
| ⚠️ | `open_meteo_weather` | 95.68% | 96.22% | 914.5 | 14877.1 | 2000ms | 7/185 |
| ❌ | `dog_ceo_random` | 98.92% | 78.38% | 1439.5 | 5586.8 | 2500ms | 40/185 |
| ⚠️ | `useless_fact` | 98.92% | 99.46% | 599.0 | 10229.6 | 2500ms | 1/185 |
| ⚠️ | `catfact_random` | 98.92% | 99.46% | 279.8 | 10070.5 | 3000ms | 1/185 |
| ✅ | `agify_name` | 100.0% | 99.46% | 403.7 | 3237.1 | 2000ms | 1/185 |
| ✅ | `rest_countries` | 100.0% | 98.92% | 284.3 | 7269.1 | 2500ms | 2/185 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.46% | 250.4 | 2314.9 | 2000ms | 1/185 |
| ✅ | `coingecko_bitcoin` | 100.0% | 100.0% | 100.0 | 252.0 | 1500ms | 0/185 |

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
