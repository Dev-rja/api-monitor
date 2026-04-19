# API Reliability Monitor — SLA Report

> Last updated: **2026-04-19 23:36 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **79.4%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 70.51% | 3187.9 | 10206.7 | 1000ms | 115/390 |
| ❌ | `public_apis_list` | 0.0% | 99.74% | 121.7 | 3806.8 | 1500ms | 1/390 |
| ❌ | `nasa_apod` | 63.08% | 39.49% | 4179.8 | 10538.0 | 2000ms | 236/390 |
| ❌ | `ipapi_check` | 93.85% | 100.0% | 159.3 | 353.0 | 2500ms | 0/390 |
| ⚠️ | `open_meteo_weather` | 97.95% | 96.92% | 751.1 | 14877.1 | 2000ms | 12/390 |
| ⚠️ | `dog_ceo_random` | 99.23% | 89.23% | 908.6 | 10244.1 | 2500ms | 42/390 |
| ✅ | `useless_fact` | 99.49% | 98.97% | 588.0 | 10229.6 | 2500ms | 4/390 |
| ✅ | `catfact_random` | 99.49% | 99.74% | 246.0 | 10070.5 | 3000ms | 1/390 |
| ✅ | `agify_name` | 100.0% | 99.74% | 371.9 | 3237.1 | 2000ms | 1/390 |
| ✅ | `rest_countries` | 100.0% | 98.97% | 261.3 | 7269.1 | 2500ms | 4/390 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.74% | 234.1 | 2314.9 | 2000ms | 1/390 |
| ✅ | `coingecko_bitcoin` | 100.0% | 100.0% | 100.7 | 252.0 | 1500ms | 0/390 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `nasa_apod` | 17:00 | 5580.9 | 69.57% |
| `nasa_apod` | 03:00 | 5533.2 | 90.0% |
| `nasa_apod` | 18:00 | 5312.9 | 81.25% |
| `numbers_trivia` | 00:00 | 5183.1 | 50.0% |
| `nasa_apod` | 11:00 | 4750.3 | 60.87% |
| `nasa_apod` | 14:00 | 4584.8 | 60.87% |
| `nasa_apod` | 21:00 | 4556.5 | 50.0% |
| `nasa_apod` | 20:00 | 4536.6 | 66.67% |
| `nasa_apod` | 12:00 | 4380.0 | 62.5% |
| `nasa_apod` | 13:00 | 4333.9 | 66.67% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
