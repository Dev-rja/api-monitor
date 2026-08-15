# API Reliability Monitor — SLA Report

> Last updated: **2026-08-15 05:05 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **77.6%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 68.71% | 3265.8 | 10420.1 | 1000ms | 608/1943 |
| ❌ | `public_apis_list` | 0.0% | 99.54% | 136.2 | 5075.4 | 1500ms | 9/1943 |
| ❌ | `ipapi_check` | 60.63% | 99.95% | 146.4 | 4507.0 | 2500ms | 1/1943 |
| ❌ | `nasa_apod` | 77.2% | 53.11% | 3076.6 | 11152.5 | 2000ms | 911/1943 |
| ⚠️ | `dog_ceo_random` | 96.09% | 97.01% | 517.7 | 10244.1 | 2500ms | 58/1943 |
| ⚠️ | `open_meteo_weather` | 98.92% | 97.89% | 687.4 | 14877.1 | 2000ms | 41/1943 |
| ✅ | `rest_countries` | 99.23% | 98.92% | 283.6 | 10221.5 | 2500ms | 21/1943 |
| ✅ | `useless_fact` | 99.74% | 99.64% | 651.1 | 10229.6 | 2500ms | 7/1943 |
| ✅ | `catfact_random` | 99.79% | 99.43% | 259.8 | 10080.2 | 3000ms | 11/1943 |
| ✅ | `coingecko_bitcoin` | 99.79% | 99.95% | 96.3 | 4328.4 | 1500ms | 1/1943 |
| ✅ | `agify_name` | 99.9% | 99.74% | 392.5 | 16112.2 | 2000ms | 5/1943 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.9% | 193.6 | 3882.8 | 2000ms | 2/1943 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `numbers_trivia` | 03:00 | 5135.5 | 51.28% |
| `nasa_apod` | 05:00 | 4468.2 | 61.7% |
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
