# API Reliability Monitor — SLA Report

> Last updated: **2026-04-20 08:28 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **79.4%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 69.8% | 3257.9 | 10206.7 | 1000ms | 119/394 |
| ❌ | `public_apis_list` | 0.0% | 99.75% | 121.0 | 3806.8 | 1500ms | 1/394 |
| ❌ | `nasa_apod` | 62.94% | 39.34% | 4197.6 | 10538.0 | 2000ms | 239/394 |
| ❌ | `ipapi_check` | 93.91% | 100.0% | 159.2 | 353.0 | 2500ms | 0/394 |
| ⚠️ | `open_meteo_weather` | 97.97% | 96.7% | 757.1 | 14877.1 | 2000ms | 13/394 |
| ⚠️ | `dog_ceo_random` | 99.24% | 89.34% | 902.7 | 10244.1 | 2500ms | 42/394 |
| ✅ | `useless_fact` | 99.49% | 98.98% | 588.3 | 10229.6 | 2500ms | 4/394 |
| ✅ | `catfact_random` | 99.49% | 99.75% | 245.2 | 10070.5 | 3000ms | 1/394 |
| ✅ | `agify_name` | 100.0% | 99.75% | 373.0 | 3237.1 | 2000ms | 1/394 |
| ✅ | `rest_countries` | 100.0% | 98.98% | 261.3 | 7269.1 | 2500ms | 4/394 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.75% | 233.6 | 2314.9 | 2000ms | 1/394 |
| ✅ | `coingecko_bitcoin` | 100.0% | 100.0% | 100.6 | 252.0 | 1500ms | 0/394 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `nasa_apod` | 03:00 | 5952.4 | 90.91% |
| `numbers_trivia` | 00:00 | 5880.9 | 57.14% |
| `nasa_apod` | 17:00 | 5580.9 | 69.57% |
| `nasa_apod` | 18:00 | 5312.9 | 81.25% |
| `nasa_apod` | 11:00 | 4750.3 | 60.87% |
| `nasa_apod` | 00:00 | 4679.5 | 71.43% |
| `nasa_apod` | 14:00 | 4584.8 | 60.87% |
| `nasa_apod` | 21:00 | 4556.5 | 50.0% |
| `nasa_apod` | 20:00 | 4536.6 | 66.67% |
| `nasa_apod` | 12:00 | 4380.0 | 62.5% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
