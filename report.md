# API Reliability Monitor — SLA Report

> Last updated: **2026-04-12 10:52 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **80.2%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 100.0% | 305.0 | 588.9 | 1000ms | 0/237 |
| ❌ | `public_apis_list` | 0.0% | 99.58% | 128.1 | 3806.8 | 1500ms | 1/237 |
| ❌ | `nasa_apod` | 74.26% | 56.54% | 2707.6 | 10538.0 | 2000ms | 103/237 |
| ❌ | `ipapi_check` | 94.51% | 100.0% | 156.7 | 252.2 | 2500ms | 0/237 |
| ⚠️ | `open_meteo_weather` | 96.62% | 95.78% | 870.1 | 14877.1 | 2000ms | 10/237 |
| ⚠️ | `dog_ceo_random` | 99.16% | 82.7% | 1214.7 | 5586.8 | 2500ms | 41/237 |
| ✅ | `useless_fact` | 99.16% | 99.58% | 582.0 | 10229.6 | 2500ms | 1/237 |
| ✅ | `catfact_random` | 99.16% | 99.58% | 267.2 | 10070.5 | 3000ms | 1/237 |
| ✅ | `agify_name` | 100.0% | 99.58% | 391.8 | 3237.1 | 2000ms | 1/237 |
| ✅ | `rest_countries` | 100.0% | 98.73% | 288.3 | 7269.1 | 2500ms | 3/237 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.58% | 236.6 | 2314.9 | 2000ms | 1/237 |
| ✅ | `coingecko_bitcoin` | 100.0% | 100.0% | 99.6 | 252.0 | 1500ms | 0/237 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `catfact_random` | 00:00 | 5139.3 | 50.0% |
| `nasa_apod` | 13:00 | 4268.1 | 66.67% |
| `nasa_apod` | 18:00 | 4037.8 | 66.67% |
| `nasa_apod` | 20:00 | 3714.0 | 56.25% |
| `nasa_apod` | 03:00 | 3704.9 | 80.0% |
| `nasa_apod` | 17:00 | 3163.1 | 41.67% |
| `nasa_apod` | 08:00 | 3100.8 | 50.0% |
| `nasa_apod` | 19:00 | 3079.8 | 42.86% |
| `nasa_apod` | 11:00 | 3069.2 | 53.33% |
| `nasa_apod` | 22:00 | 2961.3 | 46.67% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
