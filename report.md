# API Reliability Monitor — SLA Report

> Last updated: **2026-04-11 20:21 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **80.4%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 100.0% | 308.9 | 588.9 | 1000ms | 0/224 |
| ❌ | `public_apis_list` | 0.0% | 99.55% | 128.3 | 3806.8 | 1500ms | 1/224 |
| ❌ | `nasa_apod` | 77.23% | 58.93% | 2445.6 | 10538.0 | 2000ms | 92/224 |
| ❌ | `ipapi_check` | 94.2% | 100.0% | 156.1 | 252.2 | 2500ms | 0/224 |
| ⚠️ | `open_meteo_weather` | 96.43% | 95.54% | 891.9 | 14877.1 | 2000ms | 10/224 |
| ⚠️ | `dog_ceo_random` | 99.11% | 81.7% | 1268.6 | 5586.8 | 2500ms | 41/224 |
| ✅ | `useless_fact` | 99.11% | 99.55% | 588.7 | 10229.6 | 2500ms | 1/224 |
| ✅ | `catfact_random` | 99.11% | 99.55% | 271.0 | 10070.5 | 3000ms | 1/224 |
| ✅ | `agify_name` | 100.0% | 99.55% | 397.7 | 3237.1 | 2000ms | 1/224 |
| ✅ | `rest_countries` | 100.0% | 98.66% | 295.2 | 7269.1 | 2500ms | 3/224 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.55% | 240.4 | 2314.9 | 2000ms | 1/224 |
| ✅ | `coingecko_bitcoin` | 100.0% | 100.0% | 100.3 | 252.0 | 1500ms | 0/224 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `catfact_random` | 00:00 | 5139.3 | 50.0% |
| `nasa_apod` | 13:00 | 4268.1 | 66.67% |
| `nasa_apod` | 18:00 | 4037.8 | 66.67% |
| `nasa_apod` | 20:00 | 3659.8 | 53.33% |
| `nasa_apod` | 17:00 | 3163.1 | 41.67% |
| `nasa_apod` | 19:00 | 3079.8 | 42.86% |
| `nasa_apod` | 11:00 | 3069.2 | 53.33% |
| `useless_fact` | 03:00 | 2972.0 | 25.0% |
| `dog_ceo_random` | 13:00 | 2918.8 | 66.67% |
| `nasa_apod` | 22:00 | 2872.5 | 38.46% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
