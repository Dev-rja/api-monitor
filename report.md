# API Reliability Monitor — SLA Report

> Last updated: **2026-04-12 03:38 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **80.3%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 100.0% | 307.1 | 588.9 | 1000ms | 0/231 |
| ❌ | `public_apis_list` | 0.0% | 99.57% | 126.6 | 3806.8 | 1500ms | 1/231 |
| ❌ | `nasa_apod` | 75.76% | 57.58% | 2558.0 | 10538.0 | 2000ms | 98/231 |
| ❌ | `ipapi_check` | 94.37% | 100.0% | 156.9 | 252.2 | 2500ms | 0/231 |
| ⚠️ | `open_meteo_weather` | 96.54% | 95.67% | 880.9 | 14877.1 | 2000ms | 10/231 |
| ⚠️ | `dog_ceo_random` | 99.13% | 82.25% | 1238.4 | 5586.8 | 2500ms | 41/231 |
| ✅ | `useless_fact` | 99.13% | 99.57% | 587.2 | 10229.6 | 2500ms | 1/231 |
| ✅ | `catfact_random` | 99.13% | 99.57% | 270.8 | 10070.5 | 3000ms | 1/231 |
| ✅ | `agify_name` | 100.0% | 99.57% | 395.6 | 3237.1 | 2000ms | 1/231 |
| ✅ | `rest_countries` | 100.0% | 98.7% | 292.1 | 7269.1 | 2500ms | 3/231 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.57% | 238.5 | 2314.9 | 2000ms | 1/231 |
| ✅ | `coingecko_bitcoin` | 100.0% | 100.0% | 100.7 | 252.0 | 1500ms | 0/231 |

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
| `nasa_apod` | 19:00 | 3079.8 | 42.86% |
| `nasa_apod` | 11:00 | 3069.2 | 53.33% |
| `nasa_apod` | 22:00 | 2961.3 | 46.67% |
| `dog_ceo_random` | 13:00 | 2918.8 | 66.67% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
