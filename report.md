# API Reliability Monitor — SLA Report

> Last updated: **2026-04-12 16:22 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **80.2%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 100.0% | 304.3 | 588.9 | 1000ms | 0/244 |
| ❌ | `public_apis_list` | 0.0% | 99.59% | 130.7 | 3806.8 | 1500ms | 1/244 |
| ❌ | `nasa_apod` | 73.77% | 55.74% | 2793.3 | 10538.0 | 2000ms | 108/244 |
| ❌ | `ipapi_check` | 94.67% | 100.0% | 157.6 | 252.2 | 2500ms | 0/244 |
| ⚠️ | `open_meteo_weather` | 96.72% | 95.9% | 861.2 | 14877.1 | 2000ms | 10/244 |
| ⚠️ | `dog_ceo_random` | 99.18% | 83.2% | 1192.9 | 5586.8 | 2500ms | 41/244 |
| ✅ | `useless_fact` | 99.18% | 99.59% | 579.2 | 10229.6 | 2500ms | 1/244 |
| ✅ | `catfact_random` | 99.18% | 99.59% | 268.7 | 10070.5 | 3000ms | 1/244 |
| ✅ | `agify_name` | 100.0% | 99.59% | 389.2 | 3237.1 | 2000ms | 1/244 |
| ✅ | `rest_countries` | 100.0% | 98.77% | 287.2 | 7269.1 | 2500ms | 3/244 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.59% | 235.3 | 2314.9 | 2000ms | 1/244 |
| ✅ | `coingecko_bitcoin` | 100.0% | 100.0% | 100.5 | 252.0 | 1500ms | 0/244 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `catfact_random` | 00:00 | 5139.3 | 50.0% |
| `nasa_apod` | 18:00 | 4037.8 | 66.67% |
| `nasa_apod` | 13:00 | 3734.4 | 57.14% |
| `nasa_apod` | 20:00 | 3714.0 | 56.25% |
| `nasa_apod` | 03:00 | 3704.9 | 80.0% |
| `nasa_apod` | 14:00 | 3601.8 | 42.86% |
| `nasa_apod` | 17:00 | 3163.1 | 41.67% |
| `nasa_apod` | 08:00 | 3100.8 | 50.0% |
| `nasa_apod` | 19:00 | 3079.8 | 42.86% |
| `nasa_apod` | 22:00 | 2961.3 | 46.67% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
