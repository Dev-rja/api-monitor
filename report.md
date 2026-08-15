# API Reliability Monitor — SLA Report

> Last updated: **2026-08-15 02:39 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **77.6%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 68.85% | 3251.7 | 10420.1 | 1000ms | 604/1939 |
| ❌ | `public_apis_list` | 0.0% | 99.54% | 136.1 | 5075.4 | 1500ms | 9/1939 |
| ❌ | `ipapi_check` | 60.75% | 99.95% | 146.5 | 4507.0 | 2500ms | 1/1939 |
| ❌ | `nasa_apod` | 77.15% | 53.02% | 3082.0 | 11152.5 | 2000ms | 911/1939 |
| ⚠️ | `dog_ceo_random` | 96.08% | 97.01% | 518.0 | 10244.1 | 2500ms | 58/1939 |
| ⚠️ | `open_meteo_weather` | 98.92% | 97.89% | 687.6 | 14877.1 | 2000ms | 41/1939 |
| ✅ | `rest_countries` | 99.23% | 98.92% | 283.9 | 10221.5 | 2500ms | 21/1939 |
| ✅ | `useless_fact` | 99.74% | 99.64% | 651.1 | 10229.6 | 2500ms | 7/1939 |
| ✅ | `catfact_random` | 99.79% | 99.43% | 260.1 | 10080.2 | 3000ms | 11/1939 |
| ✅ | `coingecko_bitcoin` | 99.79% | 99.95% | 96.4 | 4328.4 | 1500ms | 1/1939 |
| ✅ | `agify_name` | 99.9% | 99.74% | 392.5 | 16112.2 | 2000ms | 5/1939 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.9% | 193.7 | 3882.8 | 2000ms | 2/1939 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `numbers_trivia` | 03:00 | 5004.5 | 50.0% |
| `nasa_apod` | 05:00 | 4561.4 | 63.04% |
| `nasa_apod` | 02:00 | 4198.8 | 61.54% |
| `numbers_trivia` | 10:00 | 4165.2 | 39.73% |
| `numbers_trivia` | 02:00 | 4103.1 | 38.46% |
| `nasa_apod` | 03:00 | 4010.5 | 60.53% |
| `numbers_trivia` | 14:00 | 3905.2 | 37.93% |
| `nasa_apod` | 09:00 | 3794.5 | 53.75% |
| `nasa_apod` | 11:00 | 3735.5 | 51.43% |
| `nasa_apod` | 17:00 | 3658.9 | 48.48% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
