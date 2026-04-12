# API Reliability Monitor — SLA Report

> Last updated: **2026-04-12 11:31 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **80.3%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 100.0% | 304.5 | 588.9 | 1000ms | 0/238 |
| ❌ | `public_apis_list` | 0.0% | 99.58% | 128.4 | 3806.8 | 1500ms | 1/238 |
| ❌ | `nasa_apod` | 74.37% | 56.72% | 2699.1 | 10538.0 | 2000ms | 103/238 |
| ❌ | `ipapi_check` | 94.54% | 100.0% | 156.8 | 252.2 | 2500ms | 0/238 |
| ⚠️ | `open_meteo_weather` | 96.64% | 95.8% | 868.3 | 14877.1 | 2000ms | 10/238 |
| ⚠️ | `dog_ceo_random` | 99.16% | 82.77% | 1211.6 | 5586.8 | 2500ms | 41/238 |
| ✅ | `useless_fact` | 99.16% | 99.58% | 581.4 | 10229.6 | 2500ms | 1/238 |
| ✅ | `catfact_random` | 99.16% | 99.58% | 266.9 | 10070.5 | 3000ms | 1/238 |
| ✅ | `agify_name` | 100.0% | 99.58% | 390.9 | 3237.1 | 2000ms | 1/238 |
| ✅ | `rest_countries` | 100.0% | 98.74% | 287.7 | 7269.1 | 2500ms | 3/238 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.58% | 236.5 | 2314.9 | 2000ms | 1/238 |
| ✅ | `coingecko_bitcoin` | 100.0% | 100.0% | 99.5 | 252.0 | 1500ms | 0/238 |

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
| `nasa_apod` | 22:00 | 2961.3 | 46.67% |
| `nasa_apod` | 11:00 | 2919.7 | 50.0% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
