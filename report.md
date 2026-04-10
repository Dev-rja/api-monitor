# API Reliability Monitor — SLA Report

> Last updated: **2026-04-10 23:48 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **80.5%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 100.0% | 312.5 | 588.9 | 1000ms | 0/201 |
| ❌ | `public_apis_list` | 0.0% | 100.0% | 111.4 | 429.6 | 1500ms | 0/201 |
| ❌ | `nasa_apod` | 79.1% | 64.18% | 2083.1 | 10538.0 | 2000ms | 72/201 |
| ❌ | `ipapi_check` | 93.53% | 100.0% | 155.6 | 252.2 | 2500ms | 0/201 |
| ⚠️ | `open_meteo_weather` | 96.02% | 96.02% | 906.8 | 14877.1 | 2000ms | 8/201 |
| ⚠️ | `dog_ceo_random` | 99.0% | 80.1% | 1354.4 | 5586.8 | 2500ms | 40/201 |
| ✅ | `useless_fact` | 99.0% | 99.5% | 599.7 | 10229.6 | 2500ms | 1/201 |
| ✅ | `catfact_random` | 99.0% | 99.5% | 274.8 | 10070.5 | 3000ms | 1/201 |
| ✅ | `agify_name` | 100.0% | 99.5% | 404.5 | 3237.1 | 2000ms | 1/201 |
| ✅ | `rest_countries` | 100.0% | 98.51% | 301.9 | 7269.1 | 2500ms | 3/201 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.5% | 246.3 | 2314.9 | 2000ms | 1/201 |
| ✅ | `coingecko_bitcoin` | 100.0% | 100.0% | 100.6 | 252.0 | 1500ms | 0/201 |

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
