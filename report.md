# API Reliability Monitor — SLA Report

> Last updated: **2026-04-11 19:50 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **80.5%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 100.0% | 309.4 | 588.9 | 1000ms | 0/223 |
| ❌ | `public_apis_list` | 0.0% | 99.55% | 128.7 | 3806.8 | 1500ms | 1/223 |
| ❌ | `nasa_apod` | 77.58% | 59.19% | 2409.8 | 10538.0 | 2000ms | 91/223 |
| ❌ | `ipapi_check` | 94.17% | 100.0% | 156.0 | 252.2 | 2500ms | 0/223 |
| ⚠️ | `open_meteo_weather` | 96.41% | 95.52% | 893.7 | 14877.1 | 2000ms | 10/223 |
| ⚠️ | `dog_ceo_random` | 99.1% | 81.61% | 1271.8 | 5586.8 | 2500ms | 41/223 |
| ✅ | `useless_fact` | 99.1% | 99.55% | 589.5 | 10229.6 | 2500ms | 1/223 |
| ✅ | `catfact_random` | 99.1% | 99.55% | 271.4 | 10070.5 | 3000ms | 1/223 |
| ✅ | `agify_name` | 100.0% | 99.55% | 398.7 | 3237.1 | 2000ms | 1/223 |
| ✅ | `rest_countries` | 100.0% | 98.65% | 295.7 | 7269.1 | 2500ms | 3/223 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.55% | 240.9 | 2314.9 | 2000ms | 1/223 |
| ✅ | `coingecko_bitcoin` | 100.0% | 100.0% | 100.1 | 252.0 | 1500ms | 0/223 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `catfact_random` | 00:00 | 5139.3 | 50.0% |
| `nasa_apod` | 13:00 | 4268.1 | 66.67% |
| `nasa_apod` | 18:00 | 4037.8 | 66.67% |
| `nasa_apod` | 20:00 | 3176.1 | 50.0% |
| `nasa_apod` | 17:00 | 3163.1 | 41.67% |
| `nasa_apod` | 19:00 | 3079.8 | 42.86% |
| `nasa_apod` | 11:00 | 3069.2 | 53.33% |
| `useless_fact` | 03:00 | 2972.0 | 25.0% |
| `dog_ceo_random` | 13:00 | 2918.8 | 66.67% |
| `nasa_apod` | 22:00 | 2872.5 | 38.46% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
