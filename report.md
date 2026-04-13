# API Reliability Monitor — SLA Report

> Last updated: **2026-04-13 20:40 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **80.0%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 100.0% | 302.6 | 588.9 | 1000ms | 0/267 |
| ❌ | `public_apis_list` | 0.0% | 99.63% | 126.7 | 3806.8 | 1500ms | 1/267 |
| ❌ | `nasa_apod` | 70.04% | 50.94% | 3274.8 | 10538.0 | 2000ms | 131/267 |
| ❌ | `ipapi_check` | 94.76% | 100.0% | 158.1 | 353.0 | 2500ms | 0/267 |
| ⚠️ | `open_meteo_weather` | 97.0% | 95.88% | 843.9 | 14877.1 | 2000ms | 11/267 |
| ⚠️ | `dog_ceo_random` | 99.25% | 84.64% | 1123.0 | 5586.8 | 2500ms | 41/267 |
| ✅ | `useless_fact` | 99.25% | 99.63% | 580.1 | 10229.6 | 2500ms | 1/267 |
| ✅ | `catfact_random` | 99.25% | 99.63% | 263.2 | 10070.5 | 3000ms | 1/267 |
| ✅ | `agify_name` | 100.0% | 99.63% | 389.7 | 3237.1 | 2000ms | 1/267 |
| ✅ | `rest_countries` | 100.0% | 98.88% | 280.0 | 7269.1 | 2500ms | 3/267 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.63% | 239.2 | 2314.9 | 2000ms | 1/267 |
| ✅ | `coingecko_bitcoin` | 100.0% | 100.0% | 100.2 | 252.0 | 1500ms | 0/267 |

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
| `nasa_apod` | 22:00 | 3427.1 | 50.0% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
