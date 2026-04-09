# API Reliability Monitor — SLA Report

> Last updated: **2026-04-09 21:31 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **4/12** &nbsp;|&nbsp; Avg uptime: **80.5%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 100.0% | 309.3 | 588.9 | 1000ms | 0/177 |
| ❌ | `public_apis_list` | 0.0% | 100.0% | 109.1 | 234.1 | 1500ms | 0/177 |
| ❌ | `nasa_apod` | 80.23% | 71.75% | 1689.0 | 10538.0 | 2000ms | 50/177 |
| ❌ | `ipapi_check` | 93.22% | 100.0% | 154.0 | 252.2 | 2500ms | 0/177 |
| ⚠️ | `open_meteo_weather` | 95.48% | 96.05% | 931.1 | 14877.1 | 2000ms | 7/177 |
| ❌ | `dog_ceo_random` | 98.87% | 77.4% | 1486.1 | 5586.8 | 2500ms | 40/177 |
| ⚠️ | `useless_fact` | 98.87% | 99.44% | 601.1 | 10229.6 | 2500ms | 1/177 |
| ⚠️ | `catfact_random` | 98.87% | 99.44% | 285.5 | 10070.5 | 3000ms | 1/177 |
| ✅ | `agify_name` | 100.0% | 99.44% | 403.9 | 3237.1 | 2000ms | 1/177 |
| ✅ | `rest_countries` | 100.0% | 98.87% | 288.7 | 7269.1 | 2500ms | 2/177 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.44% | 246.1 | 2314.9 | 2000ms | 1/177 |
| ✅ | `coingecko_bitcoin` | 100.0% | 100.0% | 100.3 | 252.0 | 1500ms | 0/177 |

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
| `nasa_apod` | 11:00 | 2771.9 | 41.67% |
| `open_meteo_weather` | 06:00 | 2675.4 | 16.67% |
| `nasa_apod` | 20:00 | 2637.8 | 41.67% |
| `nasa_apod` | 22:00 | 2502.9 | 27.27% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
