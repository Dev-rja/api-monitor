# API Reliability Monitor — SLA Report

> Last updated: **2026-04-11 01:03 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **80.5%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 100.0% | 311.6 | 588.9 | 1000ms | 0/202 |
| ❌ | `public_apis_list` | 0.0% | 100.0% | 111.0 | 429.6 | 1500ms | 0/202 |
| ❌ | `nasa_apod` | 79.21% | 64.36% | 2076.5 | 10538.0 | 2000ms | 72/202 |
| ❌ | `ipapi_check` | 93.56% | 100.0% | 155.6 | 252.2 | 2500ms | 0/202 |
| ⚠️ | `open_meteo_weather` | 96.04% | 96.04% | 904.5 | 14877.1 | 2000ms | 8/202 |
| ⚠️ | `dog_ceo_random` | 99.01% | 80.2% | 1348.8 | 5586.8 | 2500ms | 40/202 |
| ✅ | `useless_fact` | 99.01% | 99.5% | 598.5 | 10229.6 | 2500ms | 1/202 |
| ✅ | `catfact_random` | 99.01% | 99.5% | 275.8 | 10070.5 | 3000ms | 1/202 |
| ✅ | `agify_name` | 100.0% | 99.5% | 403.8 | 3237.1 | 2000ms | 1/202 |
| ✅ | `rest_countries` | 100.0% | 98.51% | 300.8 | 7269.1 | 2500ms | 3/202 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.5% | 245.6 | 2314.9 | 2000ms | 1/202 |
| ✅ | `coingecko_bitcoin` | 100.0% | 100.0% | 100.5 | 252.0 | 1500ms | 0/202 |

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
