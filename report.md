# API Reliability Monitor — SLA Report

> Last updated: **2026-08-18 07:10 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **77.4%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 65.77% | 3553.2 | 10420.1 | 1000ms | 712/2080 |
| ❌ | `public_apis_list` | 0.0% | 99.57% | 136.1 | 5075.4 | 1500ms | 9/2080 |
| ❌ | `ipapi_check` | 57.02% | 99.95% | 145.4 | 4507.0 | 2500ms | 1/2080 |
| ❌ | `nasa_apod` | 78.32% | 54.52% | 2970.7 | 11152.5 | 2000ms | 946/2080 |
| ⚠️ | `dog_ceo_random` | 96.35% | 97.21% | 503.7 | 10244.1 | 2500ms | 58/2080 |
| ⚠️ | `open_meteo_weather` | 98.94% | 97.93% | 688.9 | 14877.1 | 2000ms | 43/2080 |
| ✅ | `rest_countries` | 99.28% | 98.99% | 277.6 | 10221.5 | 2500ms | 21/2080 |
| ✅ | `useless_fact` | 99.76% | 99.66% | 651.5 | 10229.6 | 2500ms | 7/2080 |
| ✅ | `catfact_random` | 99.76% | 99.42% | 264.7 | 10080.2 | 3000ms | 12/2080 |
| ✅ | `coingecko_bitcoin` | 99.81% | 99.9% | 96.9 | 4328.4 | 1500ms | 2/2080 |
| ✅ | `agify_name` | 99.9% | 99.76% | 391.2 | 16112.2 | 2000ms | 5/2080 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.9% | 190.3 | 3882.8 | 2000ms | 2/2080 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `numbers_trivia` | 03:00 | 5132.1 | 51.16% |
| `numbers_trivia` | 02:00 | 4598.2 | 43.75% |
| `numbers_trivia` | 10:00 | 4544.4 | 43.59% |
| `numbers_trivia` | 14:00 | 4090.2 | 39.78% |
| `numbers_trivia` | 05:00 | 4051.3 | 40.0% |
| `nasa_apod` | 05:00 | 3992.2 | 58.18% |
| `numbers_trivia` | 09:00 | 3988.1 | 38.64% |
| `numbers_trivia` | 07:00 | 3748.1 | 35.48% |
| `numbers_trivia` | 17:00 | 3731.6 | 37.38% |
| `numbers_trivia` | 00:00 | 3712.5 | 35.59% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
