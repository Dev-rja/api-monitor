# API Reliability Monitor — SLA Report

> Last updated: **2026-04-08 05:29 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **4/12** &nbsp;|&nbsp; Avg uptime: **81.2%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 100.0% | 306.6 | 588.9 | 1000ms | 0/146 |
| ❌ | `public_apis_list` | 0.0% | 100.0% | 114.7 | 234.1 | 1500ms | 0/146 |
| ❌ | `nasa_apod` | 91.1% | 70.55% | 1689.7 | 10538.0 | 2000ms | 43/146 |
| ❌ | `ipapi_check` | 93.15% | 100.0% | 156.3 | 252.2 | 2500ms | 0/146 |
| ❌ | `open_meteo_weather` | 94.52% | 95.21% | 1001.5 | 14877.1 | 2000ms | 7/146 |
| ❌ | `dog_ceo_random` | 98.63% | 72.6% | 1720.0 | 5586.8 | 2500ms | 40/146 |
| ⚠️ | `useless_fact` | 98.63% | 99.32% | 623.9 | 10229.6 | 2500ms | 1/146 |
| ⚠️ | `catfact_random` | 98.63% | 99.32% | 303.1 | 10070.5 | 3000ms | 1/146 |
| ✅ | `agify_name` | 100.0% | 99.32% | 406.3 | 3237.1 | 2000ms | 1/146 |
| ✅ | `rest_countries` | 100.0% | 98.63% | 299.9 | 7269.1 | 2500ms | 2/146 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.32% | 250.6 | 2314.9 | 2000ms | 1/146 |
| ✅ | `coingecko_bitcoin` | 100.0% | 100.0% | 101.9 | 252.0 | 1500ms | 0/146 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `catfact_random` | 00:00 | 5139.3 | 50.0% |
| `dog_ceo_random` | 13:00 | 4153.6 | 100.0% |
| `useless_fact` | 03:00 | 3792.8 | 33.33% |
| `open_meteo_weather` | 05:00 | 3474.6 | 20.0% |
| `nasa_apod` | 13:00 | 3279.6 | 50.0% |
| `nasa_apod` | 11:00 | 3203.4 | 50.0% |
| `open_meteo_weather` | 06:00 | 3112.1 | 20.0% |
| `dog_ceo_random` | 12:00 | 3057.6 | 50.0% |
| `nasa_apod` | 20:00 | 2829.3 | 40.0% |
| `nasa_apod` | 22:00 | 2715.0 | 30.0% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
