# API Reliability Monitor — SLA Report

> Last updated: **2026-04-11 17:44 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **80.5%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 100.0% | 309.7 | 588.9 | 1000ms | 0/220 |
| ❌ | `public_apis_list` | 0.0% | 100.0% | 112.7 | 429.6 | 1500ms | 0/220 |
| ❌ | `nasa_apod` | 78.64% | 60.0% | 2300.4 | 10538.0 | 2000ms | 88/220 |
| ❌ | `ipapi_check` | 94.09% | 100.0% | 155.5 | 252.2 | 2500ms | 0/220 |
| ⚠️ | `open_meteo_weather` | 96.36% | 96.36% | 873.6 | 14877.1 | 2000ms | 8/220 |
| ⚠️ | `dog_ceo_random` | 99.09% | 81.36% | 1284.1 | 5586.8 | 2500ms | 41/220 |
| ✅ | `useless_fact` | 99.09% | 99.55% | 590.8 | 10229.6 | 2500ms | 1/220 |
| ✅ | `catfact_random` | 99.09% | 99.55% | 271.3 | 10070.5 | 3000ms | 1/220 |
| ✅ | `agify_name` | 100.0% | 99.55% | 399.8 | 3237.1 | 2000ms | 1/220 |
| ✅ | `rest_countries` | 100.0% | 98.64% | 296.6 | 7269.1 | 2500ms | 3/220 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.55% | 241.2 | 2314.9 | 2000ms | 1/220 |
| ✅ | `coingecko_bitcoin` | 100.0% | 100.0% | 100.0 | 252.0 | 1500ms | 0/220 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `catfact_random` | 00:00 | 5139.3 | 50.0% |
| `nasa_apod` | 13:00 | 4268.1 | 66.67% |
| `nasa_apod` | 18:00 | 3228.9 | 62.5% |
| `nasa_apod` | 20:00 | 3176.1 | 50.0% |
| `nasa_apod` | 17:00 | 3163.1 | 41.67% |
| `nasa_apod` | 11:00 | 3069.2 | 53.33% |
| `useless_fact` | 03:00 | 2972.0 | 25.0% |
| `dog_ceo_random` | 13:00 | 2918.8 | 66.67% |
| `nasa_apod` | 22:00 | 2872.5 | 38.46% |
| `nasa_apod` | 15:00 | 2793.9 | 50.0% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
