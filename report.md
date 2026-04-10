# API Reliability Monitor — SLA Report

> Last updated: **2026-04-10 23:01 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **80.5%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 100.0% | 312.1 | 588.9 | 1000ms | 0/200 |
| ❌ | `public_apis_list` | 0.0% | 100.0% | 110.9 | 429.6 | 1500ms | 0/200 |
| ❌ | `nasa_apod` | 79.0% | 64.5% | 2081.0 | 10538.0 | 2000ms | 71/200 |
| ❌ | `ipapi_check` | 93.5% | 100.0% | 155.2 | 252.2 | 2500ms | 0/200 |
| ⚠️ | `open_meteo_weather` | 96.0% | 96.0% | 908.1 | 14877.1 | 2000ms | 8/200 |
| ⚠️ | `dog_ceo_random` | 99.0% | 80.0% | 1359.3 | 5586.8 | 2500ms | 40/200 |
| ✅ | `useless_fact` | 99.0% | 99.5% | 600.1 | 10229.6 | 2500ms | 1/200 |
| ✅ | `catfact_random` | 99.0% | 99.5% | 275.2 | 10070.5 | 3000ms | 1/200 |
| ✅ | `agify_name` | 100.0% | 99.5% | 404.6 | 3237.1 | 2000ms | 1/200 |
| ✅ | `rest_countries` | 100.0% | 98.5% | 302.1 | 7269.1 | 2500ms | 3/200 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.5% | 246.0 | 2314.9 | 2000ms | 1/200 |
| ✅ | `coingecko_bitcoin` | 100.0% | 100.0% | 100.2 | 252.0 | 1500ms | 0/200 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `catfact_random` | 00:00 | 5139.3 | 50.0% |
| `useless_fact` | 03:00 | 3792.8 | 33.33% |
| `dog_ceo_random` | 13:00 | 3433.6 | 80.0% |
| `nasa_apod` | 18:00 | 3228.9 | 62.5% |
| `nasa_apod` | 20:00 | 3176.1 | 50.0% |
| `nasa_apod` | 13:00 | 3087.8 | 60.0% |
| `open_meteo_weather` | 05:00 | 2968.6 | 16.67% |
| `nasa_apod` | 22:00 | 2872.5 | 38.46% |
| `nasa_apod` | 15:00 | 2841.7 | 40.0% |
| `nasa_apod` | 11:00 | 2750.4 | 46.15% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
