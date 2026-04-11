# API Reliability Monitor — SLA Report

> Last updated: **2026-04-11 12:30 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **80.6%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 100.0% | 311.3 | 588.9 | 1000ms | 0/213 |
| ❌ | `public_apis_list` | 0.0% | 100.0% | 112.6 | 429.6 | 1500ms | 0/213 |
| ❌ | `nasa_apod` | 79.34% | 61.97% | 2182.2 | 10538.0 | 2000ms | 81/213 |
| ❌ | `ipapi_check` | 93.9% | 100.0% | 155.7 | 252.2 | 2500ms | 0/213 |
| ⚠️ | `open_meteo_weather` | 96.24% | 96.24% | 885.9 | 14877.1 | 2000ms | 8/213 |
| ⚠️ | `dog_ceo_random` | 99.06% | 80.75% | 1316.0 | 5586.8 | 2500ms | 41/213 |
| ✅ | `useless_fact` | 99.06% | 99.53% | 594.4 | 10229.6 | 2500ms | 1/213 |
| ✅ | `catfact_random` | 99.06% | 99.53% | 272.7 | 10070.5 | 3000ms | 1/213 |
| ✅ | `agify_name` | 100.0% | 99.53% | 403.8 | 3237.1 | 2000ms | 1/213 |
| ✅ | `rest_countries` | 100.0% | 98.59% | 296.5 | 7269.1 | 2500ms | 3/213 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.53% | 243.5 | 2314.9 | 2000ms | 1/213 |
| ✅ | `coingecko_bitcoin` | 100.0% | 100.0% | 100.4 | 252.0 | 1500ms | 0/213 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `catfact_random` | 00:00 | 5139.3 | 50.0% |
| `dog_ceo_random` | 13:00 | 3433.6 | 80.0% |
| `nasa_apod` | 18:00 | 3228.9 | 62.5% |
| `nasa_apod` | 20:00 | 3176.1 | 50.0% |
| `nasa_apod` | 13:00 | 3087.8 | 60.0% |
| `nasa_apod` | 11:00 | 3069.2 | 53.33% |
| `useless_fact` | 03:00 | 2972.0 | 25.0% |
| `nasa_apod` | 22:00 | 2872.5 | 38.46% |
| `nasa_apod` | 15:00 | 2841.7 | 40.0% |
| `open_meteo_weather` | 05:00 | 2637.8 | 14.29% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
