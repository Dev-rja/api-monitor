# API Reliability Monitor — SLA Report

> Last updated: **2026-04-08 21:25 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **4/12** &nbsp;|&nbsp; Avg uptime: **80.7%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 100.0% | 307.2 | 588.9 | 1000ms | 0/159 |
| ❌ | `public_apis_list` | 0.0% | 100.0% | 110.7 | 234.1 | 1500ms | 0/159 |
| ❌ | `nasa_apod` | 83.65% | 72.33% | 1620.7 | 10538.0 | 2000ms | 44/159 |
| ❌ | `ipapi_check` | 93.08% | 100.0% | 154.6 | 252.2 | 2500ms | 0/159 |
| ❌ | `open_meteo_weather` | 94.97% | 95.6% | 965.9 | 14877.1 | 2000ms | 7/159 |
| ❌ | `dog_ceo_random` | 98.74% | 74.84% | 1608.0 | 5586.8 | 2500ms | 40/159 |
| ⚠️ | `useless_fact` | 98.74% | 99.37% | 611.0 | 10229.6 | 2500ms | 1/159 |
| ⚠️ | `catfact_random` | 98.74% | 99.37% | 295.5 | 10070.5 | 3000ms | 1/159 |
| ✅ | `agify_name` | 100.0% | 99.37% | 405.2 | 3237.1 | 2000ms | 1/159 |
| ✅ | `rest_countries` | 100.0% | 98.74% | 294.0 | 7269.1 | 2500ms | 2/159 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.37% | 249.0 | 2314.9 | 2000ms | 1/159 |
| ✅ | `coingecko_bitcoin` | 100.0% | 100.0% | 99.9 | 252.0 | 1500ms | 0/159 |

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
| `nasa_apod` | 22:00 | 2715.0 | 30.0% |
| `open_meteo_weather` | 06:00 | 2675.4 | 16.67% |
| `nasa_apod` | 20:00 | 2672.7 | 36.36% |
| `dog_ceo_random` | 12:00 | 2515.8 | 40.0% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
