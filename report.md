# API Reliability Monitor — SLA Report

> Last updated: **2026-04-19 17:07 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **79.5%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 72.18% | 3024.5 | 10206.7 | 1000ms | 106/381 |
| ❌ | `public_apis_list` | 0.0% | 99.74% | 122.6 | 3806.8 | 1500ms | 1/381 |
| ❌ | `nasa_apod` | 64.04% | 40.42% | 4073.7 | 10538.0 | 2000ms | 227/381 |
| ❌ | `ipapi_check` | 93.7% | 100.0% | 159.9 | 353.0 | 2500ms | 0/381 |
| ⚠️ | `open_meteo_weather` | 97.9% | 96.85% | 756.5 | 14877.1 | 2000ms | 12/381 |
| ⚠️ | `dog_ceo_random` | 99.21% | 88.98% | 921.6 | 10244.1 | 2500ms | 42/381 |
| ✅ | `useless_fact` | 99.48% | 98.95% | 590.4 | 10229.6 | 2500ms | 4/381 |
| ✅ | `catfact_random` | 99.48% | 99.74% | 245.4 | 10070.5 | 3000ms | 1/381 |
| ✅ | `agify_name` | 100.0% | 99.74% | 373.1 | 3237.1 | 2000ms | 1/381 |
| ✅ | `rest_countries` | 100.0% | 98.95% | 263.0 | 7269.1 | 2500ms | 4/381 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.74% | 235.0 | 2314.9 | 2000ms | 1/381 |
| ✅ | `coingecko_bitcoin` | 100.0% | 100.0% | 101.4 | 252.0 | 1500ms | 0/381 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `nasa_apod` | 03:00 | 5533.2 | 90.0% |
| `nasa_apod` | 17:00 | 5363.4 | 68.18% |
| `numbers_trivia` | 00:00 | 5183.1 | 50.0% |
| `nasa_apod` | 18:00 | 4979.5 | 80.0% |
| `nasa_apod` | 11:00 | 4750.3 | 60.87% |
| `nasa_apod` | 20:00 | 4677.6 | 64.0% |
| `nasa_apod` | 14:00 | 4584.8 | 60.87% |
| `nasa_apod` | 12:00 | 4380.0 | 62.5% |
| `nasa_apod` | 13:00 | 4333.9 | 66.67% |
| `nasa_apod` | 21:00 | 4275.9 | 47.62% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
