# API Reliability Monitor — SLA Report

> Last updated: **2026-04-09 12:42 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **4/12** &nbsp;|&nbsp; Avg uptime: **80.5%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 100.0% | 306.3 | 588.9 | 1000ms | 0/170 |
| ❌ | `public_apis_list` | 0.0% | 100.0% | 111.3 | 234.1 | 1500ms | 0/170 |
| ❌ | `nasa_apod` | 81.76% | 74.12% | 1546.6 | 10538.0 | 2000ms | 44/170 |
| ❌ | `ipapi_check` | 92.94% | 100.0% | 154.3 | 252.2 | 2500ms | 0/170 |
| ⚠️ | `open_meteo_weather` | 95.29% | 95.88% | 944.6 | 14877.1 | 2000ms | 7/170 |
| ❌ | `dog_ceo_random` | 98.82% | 76.47% | 1529.8 | 5586.8 | 2500ms | 40/170 |
| ⚠️ | `useless_fact` | 98.82% | 99.41% | 604.5 | 10229.6 | 2500ms | 1/170 |
| ⚠️ | `catfact_random` | 98.82% | 99.41% | 287.7 | 10070.5 | 3000ms | 1/170 |
| ✅ | `agify_name` | 100.0% | 99.41% | 404.4 | 3237.1 | 2000ms | 1/170 |
| ✅ | `rest_countries` | 100.0% | 98.82% | 290.1 | 7269.1 | 2500ms | 2/170 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.41% | 245.3 | 2314.9 | 2000ms | 1/170 |
| ✅ | `coingecko_bitcoin` | 100.0% | 100.0% | 100.2 | 252.0 | 1500ms | 0/170 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `catfact_random` | 00:00 | 5139.3 | 50.0% |
| `dog_ceo_random` | 13:00 | 4153.6 | 100.0% |
| `useless_fact` | 03:00 | 3792.8 | 33.33% |
| `nasa_apod` | 13:00 | 3279.6 | 50.0% |
| `open_meteo_weather` | 05:00 | 2968.6 | 16.67% |
| `nasa_apod` | 11:00 | 2771.9 | 41.67% |
| `open_meteo_weather` | 06:00 | 2675.4 | 16.67% |
| `nasa_apod` | 20:00 | 2672.7 | 36.36% |
| `nasa_apod` | 22:00 | 2502.9 | 27.27% |
| `nasa_apod` | 18:00 | 2207.4 | 50.0% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
