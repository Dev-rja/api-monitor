# API Reliability Monitor — SLA Report

> Last updated: **2026-06-08 11:52 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **79.1%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 74.3% | 2762.3 | 10206.7 | 1000ms | 266/1035 |
| ❌ | `public_apis_list` | 0.0% | 99.61% | 125.5 | 4595.4 | 1500ms | 4/1035 |
| ❌ | `ipapi_check` | 76.14% | 99.9% | 156.7 | 4507.0 | 2500ms | 1/1035 |
| ❌ | `nasa_apod` | 76.71% | 55.65% | 3029.5 | 10565.8 | 2000ms | 459/1035 |
| ⚠️ | `rest_countries` | 98.55% | 98.26% | 351.5 | 10221.5 | 2500ms | 18/1035 |
| ⚠️ | `open_meteo_weather` | 98.94% | 97.0% | 701.2 | 14877.1 | 2000ms | 31/1035 |
| ✅ | `dog_ceo_random` | 99.52% | 95.94% | 574.5 | 10244.1 | 2500ms | 42/1035 |
| ✅ | `catfact_random` | 99.71% | 99.13% | 268.1 | 10080.2 | 3000ms | 9/1035 |
| ✅ | `coingecko_bitcoin` | 99.71% | 100.0% | 96.6 | 253.3 | 1500ms | 0/1035 |
| ✅ | `useless_fact` | 99.81% | 99.61% | 623.0 | 10229.6 | 2500ms | 4/1035 |
| ✅ | `agify_name` | 99.9% | 99.71% | 380.2 | 16112.2 | 2000ms | 3/1035 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.81% | 222.0 | 3882.8 | 2000ms | 2/1035 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `nasa_apod` | 03:00 | 4611.9 | 78.95% |
| `nasa_apod` | 02:00 | 4606.1 | 62.5% |
| `numbers_trivia` | 03:00 | 4408.7 | 42.11% |
| `nasa_apod` | 17:00 | 4070.4 | 51.72% |
| `nasa_apod` | 09:00 | 3820.6 | 50.0% |
| `nasa_apod` | 11:00 | 3771.4 | 48.28% |
| `nasa_apod` | 05:00 | 3766.2 | 62.96% |
| `numbers_trivia` | 05:00 | 3541.5 | 33.33% |
| `nasa_apod` | 12:00 | 3363.9 | 47.83% |
| `numbers_trivia` | 07:00 | 3340.4 | 31.25% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
