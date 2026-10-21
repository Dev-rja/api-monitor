# API Reliability Monitor — SLA Report

> Last updated: **2026-10-21 09:33 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **7/12** &nbsp;|&nbsp; Avg uptime: **76.5%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 73.33% | 2802.0 | 10420.1 | 1000ms | 728/2730 |
| ❌ | `public_apis_list` | 0.0% | 99.34% | 146.8 | 5075.4 | 1500ms | 18/2730 |
| ❌ | `ipapi_check` | 44.29% | 99.96% | 145.0 | 4507.0 | 2500ms | 1/2730 |
| ❌ | `nasa_apod` | 78.97% | 59.27% | 2707.3 | 11152.5 | 2000ms | 1112/2730 |
| ⚠️ | `dog_ceo_random` | 97.18% | 97.8% | 479.9 | 10509.6 | 2500ms | 60/2730 |
| ✅ | `open_meteo_weather` | 99.01% | 98.32% | 667.6 | 14877.1 | 2000ms | 46/2730 |
| ✅ | `useless_fact` | 99.12% | 99.52% | 669.9 | 10229.6 | 2500ms | 13/2730 |
| ✅ | `rest_countries` | 99.45% | 99.16% | 271.7 | 10221.5 | 2500ms | 23/2730 |
| ✅ | `coingecko_bitcoin` | 99.71% | 99.93% | 97.3 | 4328.4 | 1500ms | 2/2730 |
| ✅ | `catfact_random` | 99.82% | 99.49% | 264.4 | 10080.2 | 3000ms | 14/2730 |
| ✅ | `agify_name` | 99.93% | 99.38% | 409.4 | 16112.2 | 2000ms | 17/2730 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.89% | 180.5 | 3882.8 | 2000ms | 3/2730 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `numbers_trivia` | 03:00 | 4483.7 | 44.44% |
| `numbers_trivia` | 10:00 | 3384.6 | 32.08% |
| `nasa_apod` | 03:00 | 3208.5 | 46.3% |
| `nasa_apod` | 09:00 | 3139.6 | 44.54% |
| `nasa_apod` | 02:00 | 3117.3 | 41.94% |
| `nasa_apod` | 11:00 | 3115.1 | 43.38% |
| `numbers_trivia` | 14:00 | 3081.8 | 29.6% |
| `nasa_apod` | 17:00 | 3071.4 | 38.57% |
| `nasa_apod` | 05:00 | 3032.8 | 44.83% |
| `numbers_trivia` | 11:00 | 3021.4 | 28.47% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
