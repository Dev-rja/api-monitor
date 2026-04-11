# API Reliability Monitor — SLA Report

> Last updated: **2026-04-11 20:57 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **80.4%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 100.0% | 308.2 | 588.9 | 1000ms | 0/225 |
| ❌ | `public_apis_list` | 0.0% | 99.56% | 127.9 | 3806.8 | 1500ms | 1/225 |
| ❌ | `nasa_apod` | 76.89% | 58.67% | 2454.9 | 10538.0 | 2000ms | 93/225 |
| ❌ | `ipapi_check` | 94.22% | 100.0% | 156.2 | 252.2 | 2500ms | 0/225 |
| ⚠️ | `open_meteo_weather` | 96.44% | 95.56% | 890.2 | 14877.1 | 2000ms | 10/225 |
| ⚠️ | `dog_ceo_random` | 99.11% | 81.78% | 1264.2 | 5586.8 | 2500ms | 41/225 |
| ✅ | `useless_fact` | 99.11% | 99.56% | 588.1 | 10229.6 | 2500ms | 1/225 |
| ✅ | `catfact_random` | 99.11% | 99.56% | 271.8 | 10070.5 | 3000ms | 1/225 |
| ✅ | `agify_name` | 100.0% | 99.56% | 396.8 | 3237.1 | 2000ms | 1/225 |
| ✅ | `rest_countries` | 100.0% | 98.67% | 294.6 | 7269.1 | 2500ms | 3/225 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.56% | 240.3 | 2314.9 | 2000ms | 1/225 |
| ✅ | `coingecko_bitcoin` | 100.0% | 100.0% | 100.3 | 252.0 | 1500ms | 0/225 |

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
