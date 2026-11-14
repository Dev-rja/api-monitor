# API Reliability Monitor — SLA Report

> Last updated: **2026-11-14 20:59 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **7/12** &nbsp;|&nbsp; Avg uptime: **76.2%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 74.4% | 2695.6 | 10420.1 | 1000ms | 728/2844 |
| ❌ | `public_apis_list` | 0.0% | 99.37% | 146.0 | 5075.4 | 1500ms | 18/2844 |
| ❌ | `ipapi_check` | 42.76% | 99.96% | 145.1 | 4507.0 | 2500ms | 1/2844 |
| ❌ | `nasa_apod` | 77.14% | 59.14% | 2714.2 | 11152.5 | 2000ms | 1162/2844 |
| ⚠️ | `dog_ceo_random` | 97.29% | 97.86% | 480.6 | 10509.6 | 2500ms | 61/2844 |
| ✅ | `useless_fact` | 99.02% | 99.54% | 670.3 | 10229.6 | 2500ms | 13/2844 |
| ✅ | `open_meteo_weather` | 99.02% | 98.35% | 661.1 | 14877.1 | 2000ms | 47/2844 |
| ✅ | `rest_countries` | 99.47% | 99.19% | 270.5 | 10221.5 | 2500ms | 23/2844 |
| ✅ | `coingecko_bitcoin` | 99.72% | 99.93% | 97.2 | 4328.4 | 1500ms | 2/2844 |
| ✅ | `catfact_random` | 99.82% | 99.51% | 267.0 | 10080.2 | 3000ms | 14/2844 |
| ✅ | `agify_name` | 99.93% | 99.4% | 408.0 | 16112.2 | 2000ms | 17/2844 |
| ✅ | `jsonplaceholder_posts` | 99.96% | 99.86% | 181.9 | 10927.2 | 2000ms | 4/2844 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `numbers_trivia` | 03:00 | 4187.4 | 41.38% |
| `nasa_apod` | 11:00 | 3217.2 | 43.97% |
| `numbers_trivia` | 10:00 | 3182.9 | 30.09% |
| `nasa_apod` | 09:00 | 3117.8 | 44.17% |
| `nasa_apod` | 17:00 | 3083.2 | 38.89% |
| `nasa_apod` | 03:00 | 3067.0 | 44.83% |
| `nasa_apod` | 18:00 | 3039.7 | 44.44% |
| `numbers_trivia` | 14:00 | 3013.2 | 28.91% |
| `nasa_apod` | 05:00 | 3012.8 | 44.09% |
| `nasa_apod` | 02:00 | 2959.5 | 39.39% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
