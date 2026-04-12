# API Reliability Monitor — SLA Report

> Last updated: **2026-04-12 17:50 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **80.2%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 100.0% | 304.2 | 588.9 | 1000ms | 0/246 |
| ❌ | `public_apis_list` | 0.0% | 99.59% | 130.0 | 3806.8 | 1500ms | 1/246 |
| ❌ | `nasa_apod` | 73.58% | 55.28% | 2822.6 | 10538.0 | 2000ms | 110/246 |
| ❌ | `ipapi_check` | 94.72% | 100.0% | 157.6 | 252.2 | 2500ms | 0/246 |
| ⚠️ | `open_meteo_weather` | 96.75% | 95.93% | 858.7 | 14877.1 | 2000ms | 10/246 |
| ⚠️ | `dog_ceo_random` | 99.19% | 83.33% | 1186.2 | 5586.8 | 2500ms | 41/246 |
| ✅ | `useless_fact` | 99.19% | 99.59% | 579.5 | 10229.6 | 2500ms | 1/246 |
| ✅ | `catfact_random` | 99.19% | 99.59% | 267.6 | 10070.5 | 3000ms | 1/246 |
| ✅ | `agify_name` | 100.0% | 99.59% | 388.4 | 3237.1 | 2000ms | 1/246 |
| ✅ | `rest_countries` | 100.0% | 98.78% | 286.5 | 7269.1 | 2500ms | 3/246 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.59% | 234.6 | 2314.9 | 2000ms | 1/246 |
| ✅ | `coingecko_bitcoin` | 100.0% | 100.0% | 100.7 | 252.0 | 1500ms | 0/246 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `catfact_random` | 00:00 | 5139.3 | 50.0% |
| `nasa_apod` | 18:00 | 4037.8 | 66.67% |
| `nasa_apod` | 13:00 | 3734.4 | 57.14% |
| `nasa_apod` | 20:00 | 3714.0 | 56.25% |
| `nasa_apod` | 03:00 | 3704.9 | 80.0% |
| `nasa_apod` | 17:00 | 3623.8 | 50.0% |
| `nasa_apod` | 14:00 | 3601.8 | 42.86% |
| `nasa_apod` | 08:00 | 3100.8 | 50.0% |
| `nasa_apod` | 19:00 | 3079.8 | 42.86% |
| `nasa_apod` | 22:00 | 2961.3 | 46.67% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
