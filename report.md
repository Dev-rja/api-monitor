# API Reliability Monitor — SLA Report

> Last updated: **2026-04-20 00:07 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **79.4%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 70.33% | 3205.5 | 10206.7 | 1000ms | 116/391 |
| ❌ | `public_apis_list` | 0.0% | 99.74% | 121.6 | 3806.8 | 1500ms | 1/391 |
| ❌ | `nasa_apod` | 62.92% | 39.39% | 4195.5 | 10538.0 | 2000ms | 237/391 |
| ❌ | `ipapi_check` | 93.86% | 100.0% | 159.6 | 353.0 | 2500ms | 0/391 |
| ⚠️ | `open_meteo_weather` | 97.95% | 96.93% | 750.7 | 14877.1 | 2000ms | 12/391 |
| ⚠️ | `dog_ceo_random` | 99.23% | 89.26% | 907.3 | 10244.1 | 2500ms | 42/391 |
| ✅ | `useless_fact` | 99.49% | 98.98% | 588.2 | 10229.6 | 2500ms | 4/391 |
| ✅ | `catfact_random` | 99.49% | 99.74% | 246.2 | 10070.5 | 3000ms | 1/391 |
| ✅ | `agify_name` | 100.0% | 99.74% | 372.7 | 3237.1 | 2000ms | 1/391 |
| ✅ | `rest_countries` | 100.0% | 98.98% | 261.4 | 7269.1 | 2500ms | 4/391 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.74% | 234.0 | 2314.9 | 2000ms | 1/391 |
| ✅ | `coingecko_bitcoin` | 100.0% | 100.0% | 100.9 | 252.0 | 1500ms | 0/391 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `numbers_trivia` | 00:00 | 5880.9 | 57.14% |
| `nasa_apod` | 17:00 | 5580.9 | 69.57% |
| `nasa_apod` | 03:00 | 5533.2 | 90.0% |
| `nasa_apod` | 18:00 | 5312.9 | 81.25% |
| `nasa_apod` | 11:00 | 4750.3 | 60.87% |
| `nasa_apod` | 00:00 | 4679.5 | 71.43% |
| `nasa_apod` | 14:00 | 4584.8 | 60.87% |
| `nasa_apod` | 21:00 | 4556.5 | 50.0% |
| `nasa_apod` | 20:00 | 4536.6 | 66.67% |
| `nasa_apod` | 12:00 | 4380.0 | 62.5% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
