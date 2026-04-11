# API Reliability Monitor — SLA Report

> Last updated: **2026-04-11 21:42 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **80.4%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 100.0% | 308.3 | 588.9 | 1000ms | 0/226 |
| ❌ | `public_apis_list` | 0.0% | 99.56% | 127.7 | 3806.8 | 1500ms | 1/226 |
| ❌ | `nasa_apod` | 76.55% | 58.41% | 2489.8 | 10538.0 | 2000ms | 94/226 |
| ❌ | `ipapi_check` | 94.25% | 100.0% | 156.5 | 252.2 | 2500ms | 0/226 |
| ⚠️ | `open_meteo_weather` | 96.46% | 95.58% | 889.1 | 14877.1 | 2000ms | 10/226 |
| ⚠️ | `dog_ceo_random` | 99.12% | 81.86% | 1260.3 | 5586.8 | 2500ms | 41/226 |
| ✅ | `useless_fact` | 99.12% | 99.56% | 588.0 | 10229.6 | 2500ms | 1/226 |
| ✅ | `catfact_random` | 99.12% | 99.56% | 272.0 | 10070.5 | 3000ms | 1/226 |
| ✅ | `agify_name` | 100.0% | 99.56% | 396.6 | 3237.1 | 2000ms | 1/226 |
| ✅ | `rest_countries` | 100.0% | 98.67% | 294.4 | 7269.1 | 2500ms | 3/226 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.56% | 240.0 | 2314.9 | 2000ms | 1/226 |
| ✅ | `coingecko_bitcoin` | 100.0% | 100.0% | 100.6 | 252.0 | 1500ms | 0/226 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `catfact_random` | 00:00 | 5139.3 | 50.0% |
| `nasa_apod` | 13:00 | 4268.1 | 66.67% |
| `nasa_apod` | 18:00 | 4037.8 | 66.67% |
| `nasa_apod` | 20:00 | 3714.0 | 56.25% |
| `nasa_apod` | 17:00 | 3163.1 | 41.67% |
| `nasa_apod` | 19:00 | 3079.8 | 42.86% |
| `nasa_apod` | 11:00 | 3069.2 | 53.33% |
| `useless_fact` | 03:00 | 2972.0 | 25.0% |
| `dog_ceo_random` | 13:00 | 2918.8 | 66.67% |
| `nasa_apod` | 22:00 | 2872.5 | 38.46% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
