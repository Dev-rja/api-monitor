# API Reliability Monitor — SLA Report

> Last updated: **2026-06-09 17:34 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **79.0%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 74.57% | 2735.5 | 10206.7 | 1000ms | 266/1046 |
| ❌ | `public_apis_list` | 0.0% | 99.62% | 125.3 | 4595.4 | 1500ms | 4/1046 |
| ❌ | `ipapi_check` | 76.1% | 99.9% | 156.5 | 4507.0 | 2500ms | 1/1046 |
| ❌ | `nasa_apod` | 76.29% | 55.16% | 3074.3 | 10565.8 | 2000ms | 469/1046 |
| ⚠️ | `rest_countries` | 98.57% | 98.28% | 349.9 | 10221.5 | 2500ms | 18/1046 |
| ⚠️ | `open_meteo_weather` | 98.95% | 96.94% | 704.1 | 14877.1 | 2000ms | 32/1046 |
| ✅ | `dog_ceo_random` | 99.52% | 95.98% | 571.5 | 10244.1 | 2500ms | 42/1046 |
| ✅ | `catfact_random` | 99.71% | 99.14% | 266.9 | 10080.2 | 3000ms | 9/1046 |
| ✅ | `coingecko_bitcoin` | 99.71% | 100.0% | 96.6 | 253.3 | 1500ms | 0/1046 |
| ✅ | `useless_fact` | 99.81% | 99.62% | 623.0 | 10229.6 | 2500ms | 4/1046 |
| ✅ | `agify_name` | 99.9% | 99.71% | 380.4 | 16112.2 | 2000ms | 3/1046 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.81% | 221.6 | 3882.8 | 2000ms | 2/1046 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `nasa_apod` | 03:00 | 4611.9 | 78.95% |
| `nasa_apod` | 02:00 | 4606.1 | 62.5% |
| `numbers_trivia` | 03:00 | 4408.7 | 42.11% |
| `nasa_apod` | 17:00 | 4039.6 | 52.54% |
| `nasa_apod` | 05:00 | 3993.8 | 64.29% |
| `nasa_apod` | 09:00 | 3820.6 | 50.0% |
| `nasa_apod` | 11:00 | 3771.4 | 48.28% |
| `nasa_apod` | 01:00 | 3603.5 | 45.45% |
| `nasa_apod` | 12:00 | 3508.4 | 48.94% |
| `numbers_trivia` | 05:00 | 3427.1 | 32.14% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
