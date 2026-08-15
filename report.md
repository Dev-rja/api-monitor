# API Reliability Monitor — SLA Report

> Last updated: **2026-08-15 03:23 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **77.6%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 68.81% | 3255.3 | 10420.1 | 1000ms | 605/1940 |
| ❌ | `public_apis_list` | 0.0% | 99.54% | 136.2 | 5075.4 | 1500ms | 9/1940 |
| ❌ | `ipapi_check` | 60.72% | 99.95% | 146.5 | 4507.0 | 2500ms | 1/1940 |
| ❌ | `nasa_apod` | 77.16% | 53.04% | 3080.7 | 11152.5 | 2000ms | 911/1940 |
| ⚠️ | `dog_ceo_random` | 96.08% | 97.01% | 517.9 | 10244.1 | 2500ms | 58/1940 |
| ⚠️ | `open_meteo_weather` | 98.92% | 97.89% | 687.4 | 14877.1 | 2000ms | 41/1940 |
| ✅ | `rest_countries` | 99.23% | 98.92% | 283.8 | 10221.5 | 2500ms | 21/1940 |
| ✅ | `useless_fact` | 99.74% | 99.64% | 651.0 | 10229.6 | 2500ms | 7/1940 |
| ✅ | `catfact_random` | 99.79% | 99.43% | 260.0 | 10080.2 | 3000ms | 11/1940 |
| ✅ | `coingecko_bitcoin` | 99.79% | 99.95% | 96.4 | 4328.4 | 1500ms | 1/1940 |
| ✅ | `agify_name` | 99.9% | 99.74% | 392.4 | 16112.2 | 2000ms | 5/1940 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.9% | 193.7 | 3882.8 | 2000ms | 2/1940 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `numbers_trivia` | 03:00 | 5135.5 | 51.28% |
| `nasa_apod` | 05:00 | 4561.4 | 63.04% |
| `nasa_apod` | 02:00 | 4198.8 | 61.54% |
| `numbers_trivia` | 10:00 | 4165.2 | 39.73% |
| `numbers_trivia` | 02:00 | 4103.1 | 38.46% |
| `nasa_apod` | 03:00 | 3922.3 | 58.97% |
| `numbers_trivia` | 14:00 | 3905.2 | 37.93% |
| `nasa_apod` | 09:00 | 3794.5 | 53.75% |
| `nasa_apod` | 11:00 | 3735.5 | 51.43% |
| `nasa_apod` | 17:00 | 3658.9 | 48.48% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
