# API Reliability Monitor — SLA Report

> Last updated: **2026-04-14 23:26 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **79.9%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 95.82% | 709.7 | 10146.1 | 1000ms | 12/287 |
| ❌ | `public_apis_list` | 0.0% | 99.65% | 126.2 | 3806.8 | 1500ms | 1/287 |
| ❌ | `nasa_apod` | 68.99% | 48.08% | 3461.0 | 10538.0 | 2000ms | 149/287 |
| ❌ | `ipapi_check` | 94.43% | 100.0% | 159.3 | 353.0 | 2500ms | 0/287 |
| ⚠️ | `open_meteo_weather` | 97.21% | 96.17% | 820.4 | 14877.1 | 2000ms | 11/287 |
| ⚠️ | `dog_ceo_random` | 99.3% | 85.71% | 1070.5 | 5586.8 | 2500ms | 41/287 |
| ✅ | `useless_fact` | 99.3% | 99.65% | 571.7 | 10229.6 | 2500ms | 1/287 |
| ✅ | `catfact_random` | 99.3% | 99.65% | 260.9 | 10070.5 | 3000ms | 1/287 |
| ✅ | `agify_name` | 100.0% | 99.65% | 386.1 | 3237.1 | 2000ms | 1/287 |
| ✅ | `rest_countries` | 100.0% | 98.95% | 273.0 | 7269.1 | 2500ms | 3/287 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.65% | 239.7 | 2314.9 | 2000ms | 1/287 |
| ✅ | `coingecko_bitcoin` | 100.0% | 100.0% | 100.8 | 252.0 | 1500ms | 0/287 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `nasa_apod` | 03:00 | 5624.1 | 85.71% |
| `nasa_apod` | 18:00 | 4952.5 | 75.0% |
| `nasa_apod` | 20:00 | 4651.7 | 65.0% |
| `nasa_apod` | 14:00 | 4442.8 | 50.0% |
| `nasa_apod` | 17:00 | 3994.7 | 56.25% |
| `nasa_apod` | 08:00 | 3821.0 | 58.33% |
| `nasa_apod` | 11:00 | 3748.3 | 55.56% |
| `nasa_apod` | 13:00 | 3734.4 | 57.14% |
| `nasa_apod` | 22:00 | 3660.8 | 50.0% |
| `catfact_random` | 00:00 | 3471.7 | 33.33% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
