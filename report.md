# API Reliability Monitor — SLA Report

> Last updated: **2026-04-10 18:31 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **4/12** &nbsp;|&nbsp; Avg uptime: **80.5%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 100.0% | 310.9 | 588.9 | 1000ms | 0/194 |
| ❌ | `public_apis_list` | 0.0% | 100.0% | 111.3 | 429.6 | 1500ms | 0/194 |
| ❌ | `nasa_apod` | 79.38% | 65.98% | 1965.9 | 10538.0 | 2000ms | 66/194 |
| ❌ | `ipapi_check` | 93.3% | 100.0% | 153.9 | 252.2 | 2500ms | 0/194 |
| ⚠️ | `open_meteo_weather` | 95.88% | 95.88% | 917.8 | 14877.1 | 2000ms | 8/194 |
| ❌ | `dog_ceo_random` | 98.97% | 79.38% | 1390.4 | 5586.8 | 2500ms | 40/194 |
| ⚠️ | `useless_fact` | 98.97% | 99.48% | 596.1 | 10229.6 | 2500ms | 1/194 |
| ⚠️ | `catfact_random` | 98.97% | 99.48% | 273.2 | 10070.5 | 3000ms | 1/194 |
| ✅ | `agify_name` | 100.0% | 99.48% | 404.8 | 3237.1 | 2000ms | 1/194 |
| ✅ | `rest_countries` | 100.0% | 98.45% | 303.7 | 7269.1 | 2500ms | 3/194 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.48% | 247.4 | 2314.9 | 2000ms | 1/194 |
| ✅ | `coingecko_bitcoin` | 100.0% | 100.0% | 99.5 | 252.0 | 1500ms | 0/194 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `catfact_random` | 00:00 | 5139.3 | 50.0% |
| `useless_fact` | 03:00 | 3792.8 | 33.33% |
| `dog_ceo_random` | 13:00 | 3433.6 | 80.0% |
| `nasa_apod` | 18:00 | 3228.9 | 62.5% |
| `nasa_apod` | 13:00 | 3087.8 | 60.0% |
| `open_meteo_weather` | 05:00 | 2968.6 | 16.67% |
| `nasa_apod` | 22:00 | 2903.8 | 33.33% |
| `nasa_apod` | 15:00 | 2841.7 | 40.0% |
| `nasa_apod` | 11:00 | 2750.4 | 46.15% |
| `nasa_apod` | 20:00 | 2637.8 | 41.67% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
