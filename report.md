# API Reliability Monitor — SLA Report

> Last updated: **2026-10-19 07:10 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **7/12** &nbsp;|&nbsp; Avg uptime: **76.5%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 73.23% | 2812.8 | 10420.1 | 1000ms | 728/2719 |
| ❌ | `public_apis_list` | 0.0% | 99.37% | 145.3 | 5075.4 | 1500ms | 17/2719 |
| ❌ | `ipapi_check` | 44.43% | 99.96% | 145.1 | 4507.0 | 2500ms | 1/2719 |
| ❌ | `nasa_apod` | 79.15% | 59.4% | 2696.7 | 11152.5 | 2000ms | 1104/2719 |
| ⚠️ | `dog_ceo_random` | 97.17% | 97.79% | 480.5 | 10509.6 | 2500ms | 60/2719 |
| ✅ | `open_meteo_weather` | 99.01% | 98.31% | 668.5 | 14877.1 | 2000ms | 46/2719 |
| ✅ | `useless_fact` | 99.12% | 99.52% | 670.1 | 10229.6 | 2500ms | 13/2719 |
| ✅ | `rest_countries` | 99.45% | 99.15% | 271.9 | 10221.5 | 2500ms | 23/2719 |
| ✅ | `coingecko_bitcoin` | 99.71% | 99.93% | 97.3 | 4328.4 | 1500ms | 2/2719 |
| ✅ | `catfact_random` | 99.82% | 99.52% | 263.2 | 10080.2 | 3000ms | 13/2719 |
| ✅ | `agify_name` | 99.93% | 99.45% | 406.4 | 16112.2 | 2000ms | 15/2719 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.89% | 180.8 | 3882.8 | 2000ms | 3/2719 |

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
