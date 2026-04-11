# API Reliability Monitor — SLA Report

> Last updated: **2026-04-11 23:57 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **80.4%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 100.0% | 307.7 | 588.9 | 1000ms | 0/230 |
| ❌ | `public_apis_list` | 0.0% | 99.57% | 127.0 | 3806.8 | 1500ms | 1/230 |
| ❌ | `nasa_apod` | 76.09% | 57.83% | 2523.7 | 10538.0 | 2000ms | 97/230 |
| ❌ | `ipapi_check` | 94.35% | 100.0% | 156.9 | 252.2 | 2500ms | 0/230 |
| ⚠️ | `open_meteo_weather` | 96.52% | 95.65% | 882.7 | 14877.1 | 2000ms | 10/230 |
| ⚠️ | `dog_ceo_random` | 99.13% | 82.17% | 1243.2 | 5586.8 | 2500ms | 41/230 |
| ✅ | `useless_fact` | 99.13% | 99.57% | 586.6 | 10229.6 | 2500ms | 1/230 |
| ✅ | `catfact_random` | 99.13% | 99.57% | 271.7 | 10070.5 | 3000ms | 1/230 |
| ✅ | `agify_name` | 100.0% | 99.57% | 396.1 | 3237.1 | 2000ms | 1/230 |
| ✅ | `rest_countries` | 100.0% | 98.7% | 292.8 | 7269.1 | 2500ms | 3/230 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.57% | 238.8 | 2314.9 | 2000ms | 1/230 |
| ✅ | `coingecko_bitcoin` | 100.0% | 100.0% | 100.8 | 252.0 | 1500ms | 0/230 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `catfact_random` | 00:00 | 5139.3 | 50.0% |
| `nasa_apod` | 13:00 | 4268.1 | 66.67% |
| `nasa_apod` | 18:00 | 4037.8 | 66.67% |
| `nasa_apod` | 20:00 | 3714.0 | 56.25% |
| `nasa_apod` | 17:00 | 3163.1 | 41.67% |
| `nasa_apod` | 19:00 | 3079.8 | 42.86% |
| `nasa_apod` | 11:00 | 3069.2 | 53.33% |
| `useless_fact` | 03:00 | 2972.0 | 25.0% |
| `nasa_apod` | 22:00 | 2961.3 | 46.67% |
| `dog_ceo_random` | 13:00 | 2918.8 | 66.67% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
