# API Reliability Monitor — SLA Report

> Last updated: **2026-04-13 21:33 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **80.0%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 100.0% | 302.0 | 588.9 | 1000ms | 0/268 |
| ❌ | `public_apis_list` | 0.0% | 99.63% | 126.3 | 3806.8 | 1500ms | 1/268 |
| ❌ | `nasa_apod` | 70.15% | 50.75% | 3272.3 | 10538.0 | 2000ms | 132/268 |
| ❌ | `ipapi_check` | 94.78% | 100.0% | 158.1 | 353.0 | 2500ms | 0/268 |
| ⚠️ | `open_meteo_weather` | 97.01% | 95.9% | 842.3 | 14877.1 | 2000ms | 11/268 |
| ⚠️ | `dog_ceo_random` | 99.25% | 84.7% | 1119.6 | 5586.8 | 2500ms | 41/268 |
| ✅ | `useless_fact` | 99.25% | 99.63% | 579.9 | 10229.6 | 2500ms | 1/268 |
| ✅ | `catfact_random` | 99.25% | 99.63% | 262.5 | 10070.5 | 3000ms | 1/268 |
| ✅ | `agify_name` | 100.0% | 99.63% | 388.9 | 3237.1 | 2000ms | 1/268 |
| ✅ | `rest_countries` | 100.0% | 98.88% | 279.6 | 7269.1 | 2500ms | 3/268 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.63% | 238.8 | 2314.9 | 2000ms | 1/268 |
| ✅ | `coingecko_bitcoin` | 100.0% | 100.0% | 100.0 | 252.0 | 1500ms | 0/268 |

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
