# API Reliability Monitor — SLA Report

> Last updated: **2026-10-30 00:02 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **7/12** &nbsp;|&nbsp; Avg uptime: **76.3%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 73.8% | 2755.1 | 10420.1 | 1000ms | 728/2779 |
| ❌ | `public_apis_list` | 0.0% | 99.35% | 146.6 | 5075.4 | 1500ms | 18/2779 |
| ❌ | `ipapi_check` | 43.65% | 99.96% | 145.0 | 4507.0 | 2500ms | 1/2779 |
| ❌ | `nasa_apod` | 77.94% | 59.19% | 2713.8 | 11152.5 | 2000ms | 1134/2779 |
| ⚠️ | `dog_ceo_random` | 97.23% | 97.8% | 482.4 | 10509.6 | 2500ms | 61/2779 |
| ✅ | `open_meteo_weather` | 99.03% | 98.34% | 663.6 | 14877.1 | 2000ms | 46/2779 |
| ✅ | `useless_fact` | 99.06% | 99.53% | 670.2 | 10229.6 | 2500ms | 13/2779 |
| ✅ | `rest_countries` | 99.46% | 99.17% | 271.5 | 10221.5 | 2500ms | 23/2779 |
| ✅ | `coingecko_bitcoin` | 99.71% | 99.93% | 97.3 | 4328.4 | 1500ms | 2/2779 |
| ✅ | `catfact_random` | 99.82% | 99.5% | 266.0 | 10080.2 | 3000ms | 14/2779 |
| ✅ | `agify_name` | 99.93% | 99.39% | 408.4 | 16112.2 | 2000ms | 17/2779 |
| ✅ | `jsonplaceholder_posts` | 99.96% | 99.86% | 183.5 | 10927.2 | 2000ms | 4/2779 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `numbers_trivia` | 03:00 | 4483.7 | 44.44% |
| `numbers_trivia` | 10:00 | 3324.8 | 31.48% |
| `nasa_apod` | 03:00 | 3208.5 | 46.3% |
| `nasa_apod` | 11:00 | 3149.5 | 43.48% |
| `nasa_apod` | 09:00 | 3117.8 | 44.17% |
| `nasa_apod` | 02:00 | 3117.3 | 41.94% |
| `nasa_apod` | 17:00 | 3069.3 | 39.01% |
| `numbers_trivia` | 14:00 | 3058.4 | 29.37% |
| `nasa_apod` | 18:00 | 3047.8 | 43.57% |
| `nasa_apod` | 05:00 | 3036.1 | 44.57% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
