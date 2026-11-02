# API Reliability Monitor — SLA Report

> Last updated: **2026-11-02 23:41 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **7/12** &nbsp;|&nbsp; Avg uptime: **76.3%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 73.97% | 2738.2 | 10420.1 | 1000ms | 728/2797 |
| ❌ | `public_apis_list` | 0.0% | 99.36% | 146.6 | 5075.4 | 1500ms | 18/2797 |
| ❌ | `ipapi_check` | 43.37% | 99.96% | 145.0 | 4507.0 | 2500ms | 1/2797 |
| ❌ | `nasa_apod` | 77.65% | 59.1% | 2725.1 | 11152.5 | 2000ms | 1144/2797 |
| ⚠️ | `dog_ceo_random` | 97.25% | 97.82% | 481.7 | 10509.6 | 2500ms | 61/2797 |
| ✅ | `useless_fact` | 99.0% | 99.54% | 670.4 | 10229.6 | 2500ms | 13/2797 |
| ✅ | `open_meteo_weather` | 99.03% | 98.36% | 662.1 | 14877.1 | 2000ms | 46/2797 |
| ✅ | `rest_countries` | 99.46% | 99.18% | 271.2 | 10221.5 | 2500ms | 23/2797 |
| ✅ | `coingecko_bitcoin` | 99.71% | 99.93% | 97.2 | 4328.4 | 1500ms | 2/2797 |
| ✅ | `catfact_random` | 99.82% | 99.5% | 266.3 | 10080.2 | 3000ms | 14/2797 |
| ✅ | `agify_name` | 99.93% | 99.39% | 408.3 | 16112.2 | 2000ms | 17/2797 |
| ✅ | `jsonplaceholder_posts` | 99.96% | 99.86% | 183.1 | 10927.2 | 2000ms | 4/2797 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `numbers_trivia` | 03:00 | 4406.0 | 43.64% |
| `numbers_trivia` | 10:00 | 3294.8 | 31.19% |
| `nasa_apod` | 11:00 | 3200.7 | 43.88% |
| `nasa_apod` | 03:00 | 3157.3 | 45.45% |
| `nasa_apod` | 09:00 | 3117.8 | 44.17% |
| `nasa_apod` | 02:00 | 3117.3 | 41.94% |
| `nasa_apod` | 17:00 | 3102.3 | 39.16% |
| `numbers_trivia` | 14:00 | 3058.4 | 29.37% |
| `nasa_apod` | 18:00 | 3047.8 | 43.57% |
| `nasa_apod` | 05:00 | 3012.8 | 44.09% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
