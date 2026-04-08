# API Reliability Monitor — SLA Report

> Last updated: **2026-04-08 23:00 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **4/12** &nbsp;|&nbsp; Avg uptime: **80.6%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 100.0% | 308.0 | 588.9 | 1000ms | 0/161 |
| ❌ | `public_apis_list` | 0.0% | 100.0% | 110.9 | 234.1 | 1500ms | 0/161 |
| ❌ | `nasa_apod` | 82.61% | 72.67% | 1608.0 | 10538.0 | 2000ms | 44/161 |
| ❌ | `ipapi_check` | 93.17% | 100.0% | 154.5 | 252.2 | 2500ms | 0/161 |
| ⚠️ | `open_meteo_weather` | 95.03% | 95.65% | 960.8 | 14877.1 | 2000ms | 7/161 |
| ❌ | `dog_ceo_random` | 98.76% | 75.16% | 1594.1 | 5586.8 | 2500ms | 40/161 |
| ⚠️ | `useless_fact` | 98.76% | 99.38% | 611.1 | 10229.6 | 2500ms | 1/161 |
| ⚠️ | `catfact_random` | 98.76% | 99.38% | 295.5 | 10070.5 | 3000ms | 1/161 |
| ✅ | `agify_name` | 100.0% | 99.38% | 404.5 | 3237.1 | 2000ms | 1/161 |
| ✅ | `rest_countries` | 100.0% | 98.76% | 293.4 | 7269.1 | 2500ms | 2/161 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.38% | 248.4 | 2314.9 | 2000ms | 1/161 |
| ✅ | `coingecko_bitcoin` | 100.0% | 100.0% | 99.8 | 252.0 | 1500ms | 0/161 |

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
| `open_meteo_weather` | 06:00 | 2675.4 | 16.67% |
| `nasa_apod` | 20:00 | 2672.7 | 36.36% |
| `dog_ceo_random` | 12:00 | 2515.8 | 40.0% |
| `nasa_apod` | 22:00 | 2502.9 | 27.27% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
