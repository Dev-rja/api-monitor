# API Reliability Monitor — SLA Report

> Last updated: **2026-04-08 22:08 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **4/12** &nbsp;|&nbsp; Avg uptime: **80.6%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 100.0% | 308.6 | 588.9 | 1000ms | 0/160 |
| ❌ | `public_apis_list` | 0.0% | 100.0% | 110.3 | 234.1 | 1500ms | 0/160 |
| ❌ | `nasa_apod` | 83.13% | 72.5% | 1613.0 | 10538.0 | 2000ms | 44/160 |
| ❌ | `ipapi_check` | 93.13% | 100.0% | 154.3 | 252.2 | 2500ms | 0/160 |
| ⚠️ | `open_meteo_weather` | 95.0% | 95.63% | 964.0 | 14877.1 | 2000ms | 7/160 |
| ❌ | `dog_ceo_random` | 98.75% | 75.0% | 1600.8 | 5586.8 | 2500ms | 40/160 |
| ⚠️ | `useless_fact` | 98.75% | 99.38% | 612.0 | 10229.6 | 2500ms | 1/160 |
| ⚠️ | `catfact_random` | 98.75% | 99.38% | 294.8 | 10070.5 | 3000ms | 1/160 |
| ✅ | `agify_name` | 100.0% | 99.38% | 406.0 | 3237.1 | 2000ms | 1/160 |
| ✅ | `rest_countries` | 100.0% | 98.75% | 294.2 | 7269.1 | 2500ms | 2/160 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.38% | 248.3 | 2314.9 | 2000ms | 1/160 |
| ✅ | `coingecko_bitcoin` | 100.0% | 100.0% | 99.7 | 252.0 | 1500ms | 0/160 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `catfact_random` | 00:00 | 5139.3 | 50.0% |
| `dog_ceo_random` | 13:00 | 4153.6 | 100.0% |
| `useless_fact` | 03:00 | 3792.8 | 33.33% |
| `open_meteo_weather` | 05:00 | 3474.6 | 20.0% |
| `nasa_apod` | 13:00 | 3279.6 | 50.0% |
| `nasa_apod` | 11:00 | 2978.7 | 45.45% |
| `open_meteo_weather` | 06:00 | 2675.4 | 16.67% |
| `nasa_apod` | 20:00 | 2672.7 | 36.36% |
| `dog_ceo_random` | 12:00 | 2515.8 | 40.0% |
| `nasa_apod` | 22:00 | 2502.9 | 27.27% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
