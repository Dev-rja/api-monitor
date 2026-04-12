# API Reliability Monitor — SLA Report

> Last updated: **2026-04-12 23:21 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **80.2%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 100.0% | 303.8 | 588.9 | 1000ms | 0/254 |
| ❌ | `public_apis_list` | 0.0% | 99.61% | 128.9 | 3806.8 | 1500ms | 1/254 |
| ❌ | `nasa_apod` | 72.83% | 53.54% | 2967.2 | 10538.0 | 2000ms | 118/254 |
| ❌ | `ipapi_check` | 94.88% | 100.0% | 158.2 | 353.0 | 2500ms | 0/254 |
| ⚠️ | `open_meteo_weather` | 96.85% | 95.67% | 861.6 | 14877.1 | 2000ms | 11/254 |
| ⚠️ | `dog_ceo_random` | 99.21% | 83.86% | 1160.2 | 5586.8 | 2500ms | 41/254 |
| ✅ | `useless_fact` | 99.21% | 99.61% | 578.3 | 10229.6 | 2500ms | 1/254 |
| ✅ | `catfact_random` | 99.21% | 99.61% | 266.9 | 10070.5 | 3000ms | 1/254 |
| ✅ | `agify_name` | 100.0% | 99.61% | 390.0 | 3237.1 | 2000ms | 1/254 |
| ✅ | `rest_countries` | 100.0% | 98.82% | 283.6 | 7269.1 | 2500ms | 3/254 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.61% | 239.4 | 2314.9 | 2000ms | 1/254 |
| ✅ | `coingecko_bitcoin` | 100.0% | 100.0% | 100.6 | 252.0 | 1500ms | 0/254 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `catfact_random` | 00:00 | 5139.3 | 50.0% |
| `nasa_apod` | 20:00 | 4450.2 | 61.11% |
| `nasa_apod` | 18:00 | 3896.7 | 70.0% |
| `nasa_apod` | 13:00 | 3734.4 | 57.14% |
| `nasa_apod` | 03:00 | 3704.9 | 80.0% |
| `nasa_apod` | 17:00 | 3623.8 | 50.0% |
| `nasa_apod` | 14:00 | 3601.8 | 42.86% |
| `nasa_apod` | 22:00 | 3427.1 | 50.0% |
| `nasa_apod` | 08:00 | 3100.8 | 50.0% |
| `nasa_apod` | 19:00 | 3078.6 | 46.67% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
