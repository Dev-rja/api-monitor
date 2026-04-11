# API Reliability Monitor — SLA Report

> Last updated: **2026-04-11 11:19 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **80.5%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 100.0% | 313.1 | 588.9 | 1000ms | 0/211 |
| ❌ | `public_apis_list` | 0.0% | 100.0% | 112.6 | 429.6 | 1500ms | 0/211 |
| ❌ | `nasa_apod` | 79.15% | 62.56% | 2177.8 | 10538.0 | 2000ms | 79/211 |
| ❌ | `ipapi_check` | 93.84% | 100.0% | 155.8 | 252.2 | 2500ms | 0/211 |
| ⚠️ | `open_meteo_weather` | 96.21% | 96.21% | 890.2 | 14877.1 | 2000ms | 8/211 |
| ⚠️ | `dog_ceo_random` | 99.05% | 80.57% | 1325.4 | 5586.8 | 2500ms | 41/211 |
| ✅ | `useless_fact` | 99.05% | 99.53% | 596.2 | 10229.6 | 2500ms | 1/211 |
| ✅ | `catfact_random` | 99.05% | 99.53% | 274.5 | 10070.5 | 3000ms | 1/211 |
| ✅ | `agify_name` | 100.0% | 99.53% | 405.3 | 3237.1 | 2000ms | 1/211 |
| ✅ | `rest_countries` | 100.0% | 98.58% | 298.6 | 7269.1 | 2500ms | 3/211 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.53% | 244.5 | 2314.9 | 2000ms | 1/211 |
| ✅ | `coingecko_bitcoin` | 100.0% | 100.0% | 100.5 | 252.0 | 1500ms | 0/211 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `catfact_random` | 00:00 | 5139.3 | 50.0% |
| `dog_ceo_random` | 13:00 | 3433.6 | 80.0% |
| `nasa_apod` | 18:00 | 3228.9 | 62.5% |
| `nasa_apod` | 20:00 | 3176.1 | 50.0% |
| `nasa_apod` | 11:00 | 3103.0 | 50.0% |
| `nasa_apod` | 13:00 | 3087.8 | 60.0% |
| `useless_fact` | 03:00 | 2972.0 | 25.0% |
| `nasa_apod` | 22:00 | 2872.5 | 38.46% |
| `nasa_apod` | 15:00 | 2841.7 | 40.0% |
| `open_meteo_weather` | 05:00 | 2637.8 | 14.29% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
