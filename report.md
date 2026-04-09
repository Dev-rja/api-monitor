# API Reliability Monitor — SLA Report

> Last updated: **2026-04-09 14:29 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **4/12** &nbsp;|&nbsp; Avg uptime: **80.6%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 100.0% | 306.6 | 588.9 | 1000ms | 0/171 |
| ❌ | `public_apis_list` | 0.0% | 100.0% | 111.1 | 234.1 | 1500ms | 0/171 |
| ❌ | `nasa_apod` | 81.87% | 74.27% | 1540.1 | 10538.0 | 2000ms | 44/171 |
| ❌ | `ipapi_check` | 92.98% | 100.0% | 154.8 | 252.2 | 2500ms | 0/171 |
| ⚠️ | `open_meteo_weather` | 95.32% | 95.91% | 943.0 | 14877.1 | 2000ms | 7/171 |
| ❌ | `dog_ceo_random` | 98.83% | 76.61% | 1523.4 | 5586.8 | 2500ms | 40/171 |
| ⚠️ | `useless_fact` | 98.83% | 99.42% | 603.5 | 10229.6 | 2500ms | 1/171 |
| ⚠️ | `catfact_random` | 98.83% | 99.42% | 287.8 | 10070.5 | 3000ms | 1/171 |
| ✅ | `agify_name` | 100.0% | 99.42% | 404.1 | 3237.1 | 2000ms | 1/171 |
| ✅ | `rest_countries` | 100.0% | 98.83% | 289.9 | 7269.1 | 2500ms | 2/171 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.42% | 245.0 | 2314.9 | 2000ms | 1/171 |
| ✅ | `coingecko_bitcoin` | 100.0% | 100.0% | 100.9 | 252.0 | 1500ms | 0/171 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `catfact_random` | 00:00 | 5139.3 | 50.0% |
| `dog_ceo_random` | 13:00 | 4153.6 | 100.0% |
| `useless_fact` | 03:00 | 3792.8 | 33.33% |
| `nasa_apod` | 13:00 | 3279.6 | 50.0% |
| `open_meteo_weather` | 05:00 | 2968.6 | 16.67% |
| `nasa_apod` | 11:00 | 2771.9 | 41.67% |
| `open_meteo_weather` | 06:00 | 2675.4 | 16.67% |
| `nasa_apod` | 20:00 | 2672.7 | 36.36% |
| `nasa_apod` | 22:00 | 2502.9 | 27.27% |
| `nasa_apod` | 18:00 | 2207.4 | 50.0% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
