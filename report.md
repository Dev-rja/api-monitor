# API Reliability Monitor — SLA Report

> Last updated: **2026-04-11 17:00 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **80.6%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 100.0% | 310.3 | 588.9 | 1000ms | 0/219 |
| ❌ | `public_apis_list` | 0.0% | 100.0% | 112.5 | 429.6 | 1500ms | 0/219 |
| ❌ | `nasa_apod` | 79.0% | 60.27% | 2263.3 | 10538.0 | 2000ms | 87/219 |
| ❌ | `ipapi_check` | 94.06% | 100.0% | 155.5 | 252.2 | 2500ms | 0/219 |
| ⚠️ | `open_meteo_weather` | 96.35% | 96.35% | 875.7 | 14877.1 | 2000ms | 8/219 |
| ⚠️ | `dog_ceo_random` | 99.09% | 81.28% | 1288.2 | 5586.8 | 2500ms | 41/219 |
| ✅ | `useless_fact` | 99.09% | 99.54% | 591.5 | 10229.6 | 2500ms | 1/219 |
| ✅ | `catfact_random` | 99.09% | 99.54% | 272.1 | 10070.5 | 3000ms | 1/219 |
| ✅ | `agify_name` | 100.0% | 99.54% | 400.9 | 3237.1 | 2000ms | 1/219 |
| ✅ | `rest_countries` | 100.0% | 98.63% | 294.7 | 7269.1 | 2500ms | 3/219 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.54% | 241.3 | 2314.9 | 2000ms | 1/219 |
| ✅ | `coingecko_bitcoin` | 100.0% | 100.0% | 100.1 | 252.0 | 1500ms | 0/219 |

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
| `nasa_apod` | 15:00 | 2793.9 | 50.0% |
| `open_meteo_weather` | 05:00 | 2637.8 | 14.29% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
