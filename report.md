# API Reliability Monitor — SLA Report

> Last updated: **2026-04-11 15:01 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **80.5%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 100.0% | 311.4 | 588.9 | 1000ms | 0/216 |
| ❌ | `public_apis_list` | 0.0% | 100.0% | 112.5 | 429.6 | 1500ms | 0/216 |
| ❌ | `nasa_apod` | 78.7% | 61.11% | 2258.9 | 10538.0 | 2000ms | 84/216 |
| ❌ | `ipapi_check` | 93.98% | 100.0% | 155.7 | 252.2 | 2500ms | 0/216 |
| ⚠️ | `open_meteo_weather` | 96.3% | 96.3% | 881.3 | 14877.1 | 2000ms | 8/216 |
| ⚠️ | `dog_ceo_random` | 99.07% | 81.02% | 1302.1 | 5586.8 | 2500ms | 41/216 |
| ✅ | `useless_fact` | 99.07% | 99.54% | 594.0 | 10229.6 | 2500ms | 1/216 |
| ✅ | `catfact_random` | 99.07% | 99.54% | 271.5 | 10070.5 | 3000ms | 1/216 |
| ✅ | `agify_name` | 100.0% | 99.54% | 403.1 | 3237.1 | 2000ms | 1/216 |
| ✅ | `rest_countries` | 100.0% | 98.61% | 296.1 | 7269.1 | 2500ms | 3/216 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.54% | 242.6 | 2314.9 | 2000ms | 1/216 |
| ✅ | `coingecko_bitcoin` | 100.0% | 100.0% | 100.6 | 252.0 | 1500ms | 0/216 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `catfact_random` | 00:00 | 5139.3 | 50.0% |
| `nasa_apod` | 13:00 | 4268.1 | 66.67% |
| `nasa_apod` | 18:00 | 3228.9 | 62.5% |
| `nasa_apod` | 20:00 | 3176.1 | 50.0% |
| `nasa_apod` | 11:00 | 3069.2 | 53.33% |
| `useless_fact` | 03:00 | 2972.0 | 25.0% |
| `dog_ceo_random` | 13:00 | 2918.8 | 66.67% |
| `nasa_apod` | 22:00 | 2872.5 | 38.46% |
| `nasa_apod` | 15:00 | 2819.6 | 45.45% |
| `open_meteo_weather` | 05:00 | 2637.8 | 14.29% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
