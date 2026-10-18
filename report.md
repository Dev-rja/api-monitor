# API Reliability Monitor — SLA Report

> Last updated: **2026-10-18 21:50 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **7/12** &nbsp;|&nbsp; Avg uptime: **76.5%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 73.2% | 2815.8 | 10420.1 | 1000ms | 728/2716 |
| ❌ | `public_apis_list` | 0.0% | 99.37% | 145.3 | 5075.4 | 1500ms | 17/2716 |
| ❌ | `ipapi_check` | 44.48% | 99.96% | 145.1 | 4507.0 | 2500ms | 1/2716 |
| ❌ | `nasa_apod` | 79.23% | 59.39% | 2695.5 | 11152.5 | 2000ms | 1103/2716 |
| ⚠️ | `dog_ceo_random` | 97.16% | 97.79% | 480.4 | 10509.6 | 2500ms | 60/2716 |
| ✅ | `open_meteo_weather` | 99.01% | 98.31% | 668.8 | 14877.1 | 2000ms | 46/2716 |
| ✅ | `useless_fact` | 99.12% | 99.52% | 669.9 | 10229.6 | 2500ms | 13/2716 |
| ✅ | `rest_countries` | 99.45% | 99.15% | 272.0 | 10221.5 | 2500ms | 23/2716 |
| ✅ | `coingecko_bitcoin` | 99.71% | 99.93% | 97.4 | 4328.4 | 1500ms | 2/2716 |
| ✅ | `catfact_random` | 99.82% | 99.52% | 263.3 | 10080.2 | 3000ms | 13/2716 |
| ✅ | `agify_name` | 99.93% | 99.45% | 406.3 | 16112.2 | 2000ms | 15/2716 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.89% | 180.9 | 3882.8 | 2000ms | 3/2716 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `numbers_trivia` | 03:00 | 4483.7 | 44.44% |
| `numbers_trivia` | 10:00 | 3384.6 | 32.08% |
| `nasa_apod` | 03:00 | 3208.5 | 46.3% |
| `nasa_apod` | 09:00 | 3163.4 | 44.92% |
| `nasa_apod` | 11:00 | 3115.1 | 43.38% |
| `numbers_trivia` | 14:00 | 3105.5 | 29.84% |
| `nasa_apod` | 17:00 | 3076.2 | 38.13% |
| `nasa_apod` | 05:00 | 3032.8 | 44.83% |
| `numbers_trivia` | 17:00 | 3030.1 | 30.0% |
| `nasa_apod` | 02:00 | 3024.0 | 40.0% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
