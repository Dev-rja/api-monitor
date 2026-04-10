# API Reliability Monitor — SLA Report

> Last updated: **2026-04-10 21:40 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **4/12** &nbsp;|&nbsp; Avg uptime: **80.4%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 100.0% | 311.1 | 588.9 | 1000ms | 0/198 |
| ❌ | `public_apis_list` | 0.0% | 100.0% | 110.5 | 429.6 | 1500ms | 0/198 |
| ❌ | `nasa_apod` | 78.79% | 65.15% | 2045.5 | 10538.0 | 2000ms | 69/198 |
| ❌ | `ipapi_check` | 93.43% | 100.0% | 154.6 | 252.2 | 2500ms | 0/198 |
| ⚠️ | `open_meteo_weather` | 95.96% | 95.96% | 910.7 | 14877.1 | 2000ms | 8/198 |
| ❌ | `dog_ceo_random` | 98.99% | 79.8% | 1368.6 | 5586.8 | 2500ms | 40/198 |
| ⚠️ | `useless_fact` | 98.99% | 99.49% | 596.5 | 10229.6 | 2500ms | 1/198 |
| ⚠️ | `catfact_random` | 98.99% | 99.49% | 273.6 | 10070.5 | 3000ms | 1/198 |
| ✅ | `agify_name` | 100.0% | 99.49% | 403.3 | 3237.1 | 2000ms | 1/198 |
| ✅ | `rest_countries` | 100.0% | 98.48% | 302.3 | 7269.1 | 2500ms | 3/198 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.49% | 246.3 | 2314.9 | 2000ms | 1/198 |
| ✅ | `coingecko_bitcoin` | 100.0% | 100.0% | 99.9 | 252.0 | 1500ms | 0/198 |

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
| `nasa_apod` | 22:00 | 2903.8 | 33.33% |
| `nasa_apod` | 15:00 | 2841.7 | 40.0% |
| `nasa_apod` | 11:00 | 2750.4 | 46.15% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
