# API Reliability Monitor — SLA Report

> Last updated: **2026-04-12 05:45 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **80.3%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 100.0% | 306.8 | 588.9 | 1000ms | 0/232 |
| ❌ | `public_apis_list` | 0.0% | 99.57% | 126.9 | 3806.8 | 1500ms | 1/232 |
| ❌ | `nasa_apod` | 75.43% | 57.33% | 2591.9 | 10538.0 | 2000ms | 99/232 |
| ❌ | `ipapi_check` | 94.4% | 100.0% | 156.9 | 252.2 | 2500ms | 0/232 |
| ⚠️ | `open_meteo_weather` | 96.55% | 95.69% | 879.2 | 14877.1 | 2000ms | 10/232 |
| ⚠️ | `dog_ceo_random` | 99.14% | 82.33% | 1234.8 | 5586.8 | 2500ms | 41/232 |
| ✅ | `useless_fact` | 99.14% | 99.57% | 586.6 | 10229.6 | 2500ms | 1/232 |
| ✅ | `catfact_random` | 99.14% | 99.57% | 270.0 | 10070.5 | 3000ms | 1/232 |
| ✅ | `agify_name` | 100.0% | 99.57% | 395.1 | 3237.1 | 2000ms | 1/232 |
| ✅ | `rest_countries` | 100.0% | 98.71% | 291.1 | 7269.1 | 2500ms | 3/232 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.57% | 238.0 | 2314.9 | 2000ms | 1/232 |
| ✅ | `coingecko_bitcoin` | 100.0% | 100.0% | 100.5 | 252.0 | 1500ms | 0/232 |

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
