# API Reliability Monitor — SLA Report

> Last updated: **2026-04-20 10:18 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **79.4%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 69.62% | 3275.1 | 10206.7 | 1000ms | 120/395 |
| ❌ | `public_apis_list` | 0.0% | 99.75% | 121.2 | 3806.8 | 1500ms | 1/395 |
| ❌ | `nasa_apod` | 63.04% | 39.49% | 4187.9 | 10538.0 | 2000ms | 239/395 |
| ❌ | `ipapi_check` | 93.92% | 100.0% | 159.1 | 353.0 | 2500ms | 0/395 |
| ⚠️ | `open_meteo_weather` | 97.97% | 96.71% | 756.6 | 14877.1 | 2000ms | 13/395 |
| ⚠️ | `dog_ceo_random` | 99.24% | 89.37% | 901.8 | 10244.1 | 2500ms | 42/395 |
| ✅ | `useless_fact` | 99.49% | 98.99% | 588.0 | 10229.6 | 2500ms | 4/395 |
| ✅ | `catfact_random` | 99.49% | 99.75% | 245.2 | 10070.5 | 3000ms | 1/395 |
| ✅ | `agify_name` | 100.0% | 99.75% | 373.1 | 3237.1 | 2000ms | 1/395 |
| ✅ | `rest_countries` | 100.0% | 98.99% | 261.3 | 7269.1 | 2500ms | 4/395 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.75% | 233.4 | 2314.9 | 2000ms | 1/395 |
| ✅ | `coingecko_bitcoin` | 100.0% | 100.0% | 100.6 | 252.0 | 1500ms | 0/395 |

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
| `numbers_trivia` | 10:00 | 4406.3 | 42.11% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
