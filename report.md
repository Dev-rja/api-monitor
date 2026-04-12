# API Reliability Monitor — SLA Report

> Last updated: **2026-04-12 12:01 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **80.3%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 100.0% | 304.1 | 588.9 | 1000ms | 0/239 |
| ❌ | `public_apis_list` | 0.0% | 99.58% | 128.1 | 3806.8 | 1500ms | 1/239 |
| ❌ | `nasa_apod` | 74.48% | 56.49% | 2708.1 | 10538.0 | 2000ms | 104/239 |
| ❌ | `ipapi_check` | 94.56% | 100.0% | 156.8 | 252.2 | 2500ms | 0/239 |
| ⚠️ | `open_meteo_weather` | 96.65% | 95.82% | 868.1 | 14877.1 | 2000ms | 10/239 |
| ⚠️ | `dog_ceo_random` | 99.16% | 82.85% | 1208.2 | 5586.8 | 2500ms | 41/239 |
| ✅ | `useless_fact` | 99.16% | 99.58% | 581.2 | 10229.6 | 2500ms | 1/239 |
| ✅ | `catfact_random` | 99.16% | 99.58% | 266.3 | 10070.5 | 3000ms | 1/239 |
| ✅ | `agify_name` | 100.0% | 99.58% | 390.3 | 3237.1 | 2000ms | 1/239 |
| ✅ | `rest_countries` | 100.0% | 98.74% | 287.7 | 7269.1 | 2500ms | 3/239 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.58% | 236.0 | 2314.9 | 2000ms | 1/239 |
| ✅ | `coingecko_bitcoin` | 100.0% | 100.0% | 99.7 | 252.0 | 1500ms | 0/239 |

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
