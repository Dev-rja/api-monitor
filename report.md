# API Reliability Monitor — SLA Report

> Last updated: **2026-04-11 10:47 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **80.5%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 100.0% | 312.6 | 588.9 | 1000ms | 0/210 |
| ❌ | `public_apis_list` | 0.0% | 100.0% | 112.2 | 429.6 | 1500ms | 0/210 |
| ❌ | `nasa_apod` | 79.05% | 62.86% | 2151.5 | 10538.0 | 2000ms | 78/210 |
| ❌ | `ipapi_check` | 93.81% | 100.0% | 155.8 | 252.2 | 2500ms | 0/210 |
| ⚠️ | `open_meteo_weather` | 96.19% | 96.19% | 891.6 | 14877.1 | 2000ms | 8/210 |
| ⚠️ | `dog_ceo_random` | 99.05% | 80.95% | 1312.5 | 5586.8 | 2500ms | 40/210 |
| ✅ | `useless_fact` | 99.05% | 99.52% | 596.7 | 10229.6 | 2500ms | 1/210 |
| ✅ | `catfact_random` | 99.05% | 99.52% | 275.0 | 10070.5 | 3000ms | 1/210 |
| ✅ | `agify_name` | 100.0% | 99.52% | 405.1 | 3237.1 | 2000ms | 1/210 |
| ✅ | `rest_countries` | 100.0% | 98.57% | 298.8 | 7269.1 | 2500ms | 3/210 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.52% | 244.9 | 2314.9 | 2000ms | 1/210 |
| ✅ | `coingecko_bitcoin` | 100.0% | 100.0% | 100.7 | 252.0 | 1500ms | 0/210 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `catfact_random` | 00:00 | 5139.3 | 50.0% |
| `dog_ceo_random` | 13:00 | 3433.6 | 80.0% |
| `nasa_apod` | 18:00 | 3228.9 | 62.5% |
| `nasa_apod` | 20:00 | 3176.1 | 50.0% |
| `nasa_apod` | 13:00 | 3087.8 | 60.0% |
| `useless_fact` | 03:00 | 2972.0 | 25.0% |
| `nasa_apod` | 22:00 | 2872.5 | 38.46% |
| `nasa_apod` | 15:00 | 2841.7 | 40.0% |
| `nasa_apod` | 11:00 | 2750.4 | 46.15% |
| `open_meteo_weather` | 05:00 | 2637.8 | 14.29% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
