# API Reliability Monitor — SLA Report

> Last updated: **2026-04-20 18:39 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **79.4%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 68.58% | 3376.7 | 10206.7 | 1000ms | 126/401 |
| ❌ | `public_apis_list` | 0.0% | 99.75% | 120.6 | 3806.8 | 1500ms | 1/401 |
| ❌ | `nasa_apod` | 62.84% | 38.9% | 4220.4 | 10538.0 | 2000ms | 245/401 |
| ❌ | `ipapi_check` | 94.01% | 100.0% | 159.3 | 353.0 | 2500ms | 0/401 |
| ⚠️ | `open_meteo_weather` | 98.0% | 96.76% | 753.6 | 14877.1 | 2000ms | 13/401 |
| ⚠️ | `dog_ceo_random` | 99.25% | 89.53% | 893.9 | 10244.1 | 2500ms | 42/401 |
| ✅ | `useless_fact` | 99.5% | 99.0% | 587.5 | 10229.6 | 2500ms | 4/401 |
| ✅ | `catfact_random` | 99.5% | 99.75% | 244.9 | 10070.5 | 3000ms | 1/401 |
| ✅ | `agify_name` | 100.0% | 99.75% | 373.2 | 3237.1 | 2000ms | 1/401 |
| ✅ | `rest_countries` | 100.0% | 99.0% | 260.8 | 7269.1 | 2500ms | 4/401 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.75% | 233.2 | 2314.9 | 2000ms | 1/401 |
| ✅ | `coingecko_bitcoin` | 100.0% | 100.0% | 100.9 | 252.0 | 1500ms | 0/401 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `nasa_apod` | 03:00 | 5952.4 | 90.91% |
| `numbers_trivia` | 00:00 | 5880.9 | 57.14% |
| `nasa_apod` | 17:00 | 5778.8 | 70.83% |
| `nasa_apod` | 18:00 | 5606.7 | 82.35% |
| `nasa_apod` | 11:00 | 4978.5 | 62.5% |
| `nasa_apod` | 00:00 | 4679.5 | 71.43% |
| `nasa_apod` | 21:00 | 4556.5 | 50.0% |
| `nasa_apod` | 20:00 | 4536.6 | 66.67% |
| `nasa_apod` | 14:00 | 4500.5 | 62.5% |
| `numbers_trivia` | 10:00 | 4406.3 | 42.11% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
