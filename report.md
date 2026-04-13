# API Reliability Monitor — SLA Report

> Last updated: **2026-04-13 22:27 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **80.0%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 100.0% | 301.9 | 588.9 | 1000ms | 0/269 |
| ❌ | `public_apis_list` | 0.0% | 99.63% | 126.6 | 3806.8 | 1500ms | 1/269 |
| ❌ | `nasa_apod` | 70.26% | 50.93% | 3262.6 | 10538.0 | 2000ms | 132/269 |
| ❌ | `ipapi_check` | 94.8% | 100.0% | 158.1 | 353.0 | 2500ms | 0/269 |
| ⚠️ | `open_meteo_weather` | 97.03% | 95.91% | 840.6 | 14877.1 | 2000ms | 11/269 |
| ⚠️ | `dog_ceo_random` | 99.26% | 84.76% | 1117.0 | 5586.8 | 2500ms | 41/269 |
| ✅ | `useless_fact` | 99.26% | 99.63% | 579.4 | 10229.6 | 2500ms | 1/269 |
| ✅ | `catfact_random` | 99.26% | 99.63% | 262.6 | 10070.5 | 3000ms | 1/269 |
| ✅ | `agify_name` | 100.0% | 99.63% | 388.1 | 3237.1 | 2000ms | 1/269 |
| ✅ | `rest_countries` | 100.0% | 98.88% | 279.3 | 7269.1 | 2500ms | 3/269 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.63% | 238.8 | 2314.9 | 2000ms | 1/269 |
| ✅ | `coingecko_bitcoin` | 100.0% | 100.0% | 100.0 | 252.0 | 1500ms | 0/269 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `catfact_random` | 00:00 | 5139.3 | 50.0% |
| `nasa_apod` | 03:00 | 4838.2 | 83.33% |
| `nasa_apod` | 20:00 | 4763.5 | 63.16% |
| `nasa_apod` | 18:00 | 4464.9 | 72.73% |
| `nasa_apod` | 17:00 | 4072.6 | 53.33% |
| `nasa_apod` | 14:00 | 4050.6 | 46.67% |
| `nasa_apod` | 13:00 | 3734.4 | 57.14% |
| `nasa_apod` | 10:00 | 3532.9 | 45.45% |
| `nasa_apod` | 19:00 | 3524.3 | 50.0% |
| `nasa_apod` | 11:00 | 3354.6 | 52.94% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
