# API Reliability Monitor — SLA Report

> Last updated: **2026-04-11 09:57 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **80.5%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 100.0% | 312.8 | 588.9 | 1000ms | 0/209 |
| ❌ | `public_apis_list` | 0.0% | 100.0% | 111.9 | 429.6 | 1500ms | 0/209 |
| ❌ | `nasa_apod` | 78.95% | 63.16% | 2149.5 | 10538.0 | 2000ms | 77/209 |
| ❌ | `ipapi_check` | 93.78% | 100.0% | 155.8 | 252.2 | 2500ms | 0/209 |
| ⚠️ | `open_meteo_weather` | 96.17% | 96.17% | 893.4 | 14877.1 | 2000ms | 8/209 |
| ⚠️ | `dog_ceo_random` | 99.04% | 80.86% | 1317.0 | 5586.8 | 2500ms | 40/209 |
| ✅ | `useless_fact` | 99.04% | 99.52% | 597.1 | 10229.6 | 2500ms | 1/209 |
| ✅ | `catfact_random` | 99.04% | 99.52% | 274.9 | 10070.5 | 3000ms | 1/209 |
| ✅ | `agify_name` | 100.0% | 99.52% | 405.7 | 3237.1 | 2000ms | 1/209 |
| ✅ | `rest_countries` | 100.0% | 98.56% | 299.0 | 7269.1 | 2500ms | 3/209 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.52% | 244.5 | 2314.9 | 2000ms | 1/209 |
| ✅ | `coingecko_bitcoin` | 100.0% | 100.0% | 100.5 | 252.0 | 1500ms | 0/209 |

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
