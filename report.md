# API Reliability Monitor — SLA Report

> Last updated: **2026-04-08 18:19 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **4/12** &nbsp;|&nbsp; Avg uptime: **80.8%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 100.0% | 309.0 | 588.9 | 1000ms | 0/156 |
| ❌ | `public_apis_list` | 0.0% | 100.0% | 110.9 | 234.1 | 1500ms | 0/156 |
| ❌ | `nasa_apod` | 85.26% | 71.79% | 1637.5 | 10538.0 | 2000ms | 44/156 |
| ❌ | `ipapi_check` | 92.95% | 100.0% | 154.6 | 252.2 | 2500ms | 0/156 |
| ❌ | `open_meteo_weather` | 94.87% | 95.51% | 975.2 | 14877.1 | 2000ms | 7/156 |
| ❌ | `dog_ceo_random` | 98.72% | 74.36% | 1633.5 | 5586.8 | 2500ms | 40/156 |
| ⚠️ | `useless_fact` | 98.72% | 99.36% | 615.3 | 10229.6 | 2500ms | 1/156 |
| ⚠️ | `catfact_random` | 98.72% | 99.36% | 297.0 | 10070.5 | 3000ms | 1/156 |
| ✅ | `agify_name` | 100.0% | 99.36% | 408.3 | 3237.1 | 2000ms | 1/156 |
| ✅ | `rest_countries` | 100.0% | 98.72% | 296.7 | 7269.1 | 2500ms | 2/156 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.36% | 250.0 | 2314.9 | 2000ms | 1/156 |
| ✅ | `coingecko_bitcoin` | 100.0% | 100.0% | 100.6 | 252.0 | 1500ms | 0/156 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `catfact_random` | 00:00 | 5139.3 | 50.0% |
| `dog_ceo_random` | 13:00 | 4153.6 | 100.0% |
| `useless_fact` | 03:00 | 3792.8 | 33.33% |
| `open_meteo_weather` | 05:00 | 3474.6 | 20.0% |
| `nasa_apod` | 13:00 | 3279.6 | 50.0% |
| `nasa_apod` | 11:00 | 2978.7 | 45.45% |
| `nasa_apod` | 20:00 | 2829.3 | 40.0% |
| `nasa_apod` | 22:00 | 2715.0 | 30.0% |
| `open_meteo_weather` | 06:00 | 2675.4 | 16.67% |
| `dog_ceo_random` | 12:00 | 2515.8 | 40.0% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
