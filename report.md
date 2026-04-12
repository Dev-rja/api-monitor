# API Reliability Monitor — SLA Report

> Last updated: **2026-04-12 13:22 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **80.3%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 100.0% | 304.3 | 588.9 | 1000ms | 0/240 |
| ❌ | `public_apis_list` | 0.0% | 99.58% | 127.8 | 3806.8 | 1500ms | 1/240 |
| ❌ | `nasa_apod` | 74.58% | 56.67% | 2699.1 | 10538.0 | 2000ms | 104/240 |
| ❌ | `ipapi_check` | 94.58% | 100.0% | 157.1 | 252.2 | 2500ms | 0/240 |
| ⚠️ | `open_meteo_weather` | 96.67% | 95.83% | 866.8 | 14877.1 | 2000ms | 10/240 |
| ⚠️ | `dog_ceo_random` | 99.17% | 82.92% | 1205.0 | 5586.8 | 2500ms | 41/240 |
| ✅ | `useless_fact` | 99.17% | 99.58% | 580.5 | 10229.6 | 2500ms | 1/240 |
| ✅ | `catfact_random` | 99.17% | 99.58% | 266.5 | 10070.5 | 3000ms | 1/240 |
| ✅ | `agify_name` | 100.0% | 99.58% | 390.4 | 3237.1 | 2000ms | 1/240 |
| ✅ | `rest_countries` | 100.0% | 98.75% | 287.7 | 7269.1 | 2500ms | 3/240 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.58% | 235.9 | 2314.9 | 2000ms | 1/240 |
| ✅ | `coingecko_bitcoin` | 100.0% | 100.0% | 99.9 | 252.0 | 1500ms | 0/240 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `catfact_random` | 00:00 | 5139.3 | 50.0% |
| `nasa_apod` | 18:00 | 4037.8 | 66.67% |
| `nasa_apod` | 13:00 | 3734.4 | 57.14% |
| `nasa_apod` | 20:00 | 3714.0 | 56.25% |
| `nasa_apod` | 03:00 | 3704.9 | 80.0% |
| `nasa_apod` | 17:00 | 3163.1 | 41.67% |
| `nasa_apod` | 08:00 | 3100.8 | 50.0% |
| `nasa_apod` | 19:00 | 3079.8 | 42.86% |
| `nasa_apod` | 22:00 | 2961.3 | 46.67% |
| `nasa_apod` | 11:00 | 2919.7 | 50.0% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
