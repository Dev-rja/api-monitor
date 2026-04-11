# API Reliability Monitor — SLA Report

> Last updated: **2026-04-11 14:22 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **80.5%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 100.0% | 311.8 | 588.9 | 1000ms | 0/215 |
| ❌ | `public_apis_list` | 0.0% | 100.0% | 112.1 | 429.6 | 1500ms | 0/215 |
| ❌ | `nasa_apod` | 78.6% | 61.4% | 2257.3 | 10538.0 | 2000ms | 83/215 |
| ❌ | `ipapi_check` | 93.95% | 100.0% | 155.6 | 252.2 | 2500ms | 0/215 |
| ⚠️ | `open_meteo_weather` | 96.28% | 96.28% | 883.5 | 14877.1 | 2000ms | 8/215 |
| ⚠️ | `dog_ceo_random` | 99.07% | 80.93% | 1306.9 | 5586.8 | 2500ms | 41/215 |
| ✅ | `useless_fact` | 99.07% | 99.53% | 593.6 | 10229.6 | 2500ms | 1/215 |
| ✅ | `catfact_random` | 99.07% | 99.53% | 272.2 | 10070.5 | 3000ms | 1/215 |
| ✅ | `agify_name` | 100.0% | 99.53% | 404.0 | 3237.1 | 2000ms | 1/215 |
| ✅ | `rest_countries` | 100.0% | 98.6% | 296.7 | 7269.1 | 2500ms | 3/215 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.53% | 242.7 | 2314.9 | 2000ms | 1/215 |
| ✅ | `coingecko_bitcoin` | 100.0% | 100.0% | 100.4 | 252.0 | 1500ms | 0/215 |

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
| `nasa_apod` | 15:00 | 2841.7 | 40.0% |
| `open_meteo_weather` | 05:00 | 2637.8 | 14.29% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
