# API Reliability Monitor — SLA Report

> Last updated: **2026-04-19 05:51 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **79.5%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 74.73% | 2775.4 | 10206.7 | 1000ms | 93/368 |
| ❌ | `public_apis_list` | 0.0% | 99.73% | 122.9 | 3806.8 | 1500ms | 1/368 |
| ❌ | `nasa_apod` | 64.67% | 41.03% | 4016.0 | 10538.0 | 2000ms | 217/368 |
| ❌ | `ipapi_check` | 93.48% | 100.0% | 159.9 | 353.0 | 2500ms | 0/368 |
| ⚠️ | `open_meteo_weather` | 97.83% | 96.74% | 764.7 | 14877.1 | 2000ms | 12/368 |
| ⚠️ | `dog_ceo_random` | 99.18% | 88.59% | 940.6 | 10244.1 | 2500ms | 42/368 |
| ✅ | `useless_fact` | 99.46% | 98.91% | 592.4 | 10229.6 | 2500ms | 4/368 |
| ✅ | `catfact_random` | 99.46% | 99.73% | 245.6 | 10070.5 | 3000ms | 1/368 |
| ✅ | `agify_name` | 100.0% | 99.73% | 375.2 | 3237.1 | 2000ms | 1/368 |
| ✅ | `rest_countries` | 100.0% | 98.91% | 265.4 | 7269.1 | 2500ms | 4/368 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.73% | 235.9 | 2314.9 | 2000ms | 1/368 |
| ✅ | `coingecko_bitcoin` | 100.0% | 100.0% | 101.4 | 252.0 | 1500ms | 0/368 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `nasa_apod` | 03:00 | 5533.2 | 90.0% |
| `numbers_trivia` | 00:00 | 5183.1 | 50.0% |
| `nasa_apod` | 17:00 | 5121.2 | 66.67% |
| `nasa_apod` | 18:00 | 4979.5 | 80.0% |
| `nasa_apod` | 20:00 | 4677.6 | 64.0% |
| `nasa_apod` | 11:00 | 4496.8 | 59.09% |
| `nasa_apod` | 21:00 | 4275.9 | 47.62% |
| `nasa_apod` | 23:00 | 4115.2 | 51.85% |
| `nasa_apod` | 05:00 | 4071.7 | 71.43% |
| `nasa_apod` | 08:00 | 4055.4 | 57.14% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
