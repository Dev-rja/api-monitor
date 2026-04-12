# API Reliability Monitor — SLA Report

> Last updated: **2026-04-12 09:04 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **80.3%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 100.0% | 305.9 | 588.9 | 1000ms | 0/235 |
| ❌ | `public_apis_list` | 0.0% | 99.57% | 127.9 | 3806.8 | 1500ms | 1/235 |
| ❌ | `nasa_apod` | 74.89% | 57.02% | 2648.7 | 10538.0 | 2000ms | 101/235 |
| ❌ | `ipapi_check` | 94.47% | 100.0% | 156.7 | 252.2 | 2500ms | 0/235 |
| ⚠️ | `open_meteo_weather` | 96.6% | 95.74% | 873.8 | 14877.1 | 2000ms | 10/235 |
| ⚠️ | `dog_ceo_random` | 99.15% | 82.55% | 1222.5 | 5586.8 | 2500ms | 41/235 |
| ✅ | `useless_fact` | 99.15% | 99.57% | 584.0 | 10229.6 | 2500ms | 1/235 |
| ✅ | `catfact_random` | 99.15% | 99.57% | 268.9 | 10070.5 | 3000ms | 1/235 |
| ✅ | `agify_name` | 100.0% | 99.57% | 392.9 | 3237.1 | 2000ms | 1/235 |
| ✅ | `rest_countries` | 100.0% | 98.72% | 289.8 | 7269.1 | 2500ms | 3/235 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.57% | 236.8 | 2314.9 | 2000ms | 1/235 |
| ✅ | `coingecko_bitcoin` | 100.0% | 100.0% | 100.0 | 252.0 | 1500ms | 0/235 |

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
