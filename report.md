# API Reliability Monitor — SLA Report

> Last updated: **2026-04-18 20:04 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **79.5%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 76.39% | 2612.7 | 10206.7 | 1000ms | 85/360 |
| ❌ | `public_apis_list` | 0.0% | 99.72% | 123.3 | 3806.8 | 1500ms | 1/360 |
| ❌ | `nasa_apod` | 64.44% | 41.11% | 4031.9 | 10538.0 | 2000ms | 212/360 |
| ❌ | `ipapi_check` | 93.33% | 100.0% | 160.0 | 353.0 | 2500ms | 0/360 |
| ⚠️ | `open_meteo_weather` | 97.78% | 96.67% | 770.4 | 14877.1 | 2000ms | 12/360 |
| ⚠️ | `dog_ceo_random` | 99.17% | 88.33% | 953.8 | 10244.1 | 2500ms | 42/360 |
| ✅ | `useless_fact` | 99.44% | 99.17% | 582.5 | 10229.6 | 2500ms | 3/360 |
| ✅ | `catfact_random` | 99.44% | 99.72% | 248.4 | 10070.5 | 3000ms | 1/360 |
| ✅ | `agify_name` | 100.0% | 99.72% | 376.7 | 3237.1 | 2000ms | 1/360 |
| ✅ | `rest_countries` | 100.0% | 98.89% | 266.9 | 7269.1 | 2500ms | 4/360 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.72% | 237.1 | 2314.9 | 2000ms | 1/360 |
| ✅ | `coingecko_bitcoin` | 100.0% | 100.0% | 101.1 | 252.0 | 1500ms | 0/360 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `nasa_apod` | 03:00 | 5840.5 | 88.89% |
| `nasa_apod` | 17:00 | 5121.2 | 66.67% |
| `nasa_apod` | 18:00 | 4979.5 | 80.0% |
| `nasa_apod` | 20:00 | 4853.9 | 66.67% |
| `nasa_apod` | 11:00 | 4496.8 | 59.09% |
| `nasa_apod` | 21:00 | 4372.0 | 45.0% |
| `numbers_trivia` | 00:00 | 4205.1 | 40.0% |
| `nasa_apod` | 08:00 | 4055.4 | 57.14% |
| `nasa_apod` | 14:00 | 4031.8 | 57.14% |
| `nasa_apod` | 12:00 | 3997.0 | 60.0% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
