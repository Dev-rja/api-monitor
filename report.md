# API Reliability Monitor — SLA Report

> Last updated: **2026-04-10 04:34 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **4/12** &nbsp;|&nbsp; Avg uptime: **80.4%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 100.0% | 309.8 | 588.9 | 1000ms | 0/182 |
| ❌ | `public_apis_list` | 0.0% | 100.0% | 111.3 | 429.6 | 1500ms | 0/182 |
| ❌ | `nasa_apod` | 79.67% | 69.78% | 1824.8 | 10538.0 | 2000ms | 55/182 |
| ❌ | `ipapi_check` | 92.86% | 100.0% | 154.4 | 252.2 | 2500ms | 0/182 |
| ⚠️ | `open_meteo_weather` | 95.6% | 96.15% | 920.6 | 14877.1 | 2000ms | 7/182 |
| ❌ | `dog_ceo_random` | 98.9% | 78.02% | 1458.4 | 5586.8 | 2500ms | 40/182 |
| ⚠️ | `useless_fact` | 98.9% | 99.45% | 599.4 | 10229.6 | 2500ms | 1/182 |
| ⚠️ | `catfact_random` | 98.9% | 99.45% | 282.2 | 10070.5 | 3000ms | 1/182 |
| ✅ | `agify_name` | 100.0% | 99.45% | 404.3 | 3237.1 | 2000ms | 1/182 |
| ✅ | `rest_countries` | 100.0% | 98.9% | 286.1 | 7269.1 | 2500ms | 2/182 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.45% | 244.9 | 2314.9 | 2000ms | 1/182 |
| ✅ | `coingecko_bitcoin` | 100.0% | 100.0% | 100.4 | 252.0 | 1500ms | 0/182 |

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
