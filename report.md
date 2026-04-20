# API Reliability Monitor — SLA Report

> Last updated: **2026-04-20 14:55 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **79.4%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 69.1% | 3326.1 | 10206.7 | 1000ms | 123/398 |
| ❌ | `public_apis_list` | 0.0% | 99.75% | 121.1 | 3806.8 | 1500ms | 1/398 |
| ❌ | `nasa_apod` | 63.07% | 39.2% | 4194.5 | 10538.0 | 2000ms | 242/398 |
| ❌ | `ipapi_check` | 93.97% | 100.0% | 159.5 | 353.0 | 2500ms | 0/398 |
| ⚠️ | `open_meteo_weather` | 97.99% | 96.73% | 754.9 | 14877.1 | 2000ms | 13/398 |
| ⚠️ | `dog_ceo_random` | 99.25% | 89.45% | 898.2 | 10244.1 | 2500ms | 42/398 |
| ✅ | `useless_fact` | 99.5% | 98.99% | 587.6 | 10229.6 | 2500ms | 4/398 |
| ✅ | `catfact_random` | 99.5% | 99.75% | 245.7 | 10070.5 | 3000ms | 1/398 |
| ✅ | `agify_name` | 100.0% | 99.75% | 373.2 | 3237.1 | 2000ms | 1/398 |
| ✅ | `rest_countries` | 100.0% | 98.99% | 260.9 | 7269.1 | 2500ms | 4/398 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.75% | 233.5 | 2314.9 | 2000ms | 1/398 |
| ✅ | `coingecko_bitcoin` | 100.0% | 100.0% | 101.0 | 252.0 | 1500ms | 0/398 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `nasa_apod` | 03:00 | 5952.4 | 90.91% |
| `numbers_trivia` | 00:00 | 5880.9 | 57.14% |
| `nasa_apod` | 17:00 | 5580.9 | 69.57% |
| `nasa_apod` | 18:00 | 5312.9 | 81.25% |
| `nasa_apod` | 11:00 | 4978.5 | 62.5% |
| `nasa_apod` | 00:00 | 4679.5 | 71.43% |
| `nasa_apod` | 21:00 | 4556.5 | 50.0% |
| `nasa_apod` | 20:00 | 4536.6 | 66.67% |
| `nasa_apod` | 14:00 | 4500.5 | 62.5% |
| `numbers_trivia` | 10:00 | 4406.3 | 42.11% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
