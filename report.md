# API Reliability Monitor — SLA Report

> Last updated: **2026-10-17 16:53 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **7/12** &nbsp;|&nbsp; Avg uptime: **76.5%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 73.1% | 2825.6 | 10420.1 | 1000ms | 728/2706 |
| ❌ | `public_apis_list` | 0.0% | 99.41% | 143.9 | 5075.4 | 1500ms | 16/2706 |
| ❌ | `ipapi_check` | 44.64% | 99.96% | 145.1 | 4507.0 | 2500ms | 1/2706 |
| ❌ | `nasa_apod` | 79.34% | 59.39% | 2691.6 | 11152.5 | 2000ms | 1099/2706 |
| ⚠️ | `dog_ceo_random` | 97.15% | 97.78% | 480.6 | 10509.6 | 2500ms | 60/2706 |
| ✅ | `open_meteo_weather` | 99.0% | 98.3% | 669.3 | 14877.1 | 2000ms | 46/2706 |
| ✅ | `useless_fact` | 99.11% | 99.52% | 669.8 | 10229.6 | 2500ms | 13/2706 |
| ✅ | `rest_countries` | 99.45% | 99.15% | 271.5 | 10221.5 | 2500ms | 23/2706 |
| ✅ | `coingecko_bitcoin` | 99.7% | 99.93% | 97.3 | 4328.4 | 1500ms | 2/2706 |
| ✅ | `catfact_random` | 99.82% | 99.52% | 262.8 | 10080.2 | 3000ms | 13/2706 |
| ✅ | `agify_name` | 99.93% | 99.48% | 404.9 | 16112.2 | 2000ms | 14/2706 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.89% | 181.1 | 3882.8 | 2000ms | 3/2706 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `numbers_trivia` | 03:00 | 4483.7 | 44.44% |
| `numbers_trivia` | 10:00 | 3415.4 | 32.38% |
| `nasa_apod` | 03:00 | 3208.5 | 46.3% |
| `nasa_apod` | 09:00 | 3163.4 | 44.92% |
| `numbers_trivia` | 14:00 | 3129.4 | 30.08% |
| `nasa_apod` | 11:00 | 3115.1 | 43.38% |
| `nasa_apod` | 17:00 | 3094.5 | 38.41% |
| `numbers_trivia` | 17:00 | 3050.8 | 30.22% |
| `nasa_apod` | 05:00 | 3032.8 | 44.83% |
| `nasa_apod` | 02:00 | 3024.0 | 40.0% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
