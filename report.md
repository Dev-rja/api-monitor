# API Reliability Monitor — SLA Report

> Last updated: **2026-08-14 23:13 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **77.6%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 68.99% | 3237.7 | 10420.1 | 1000ms | 600/1935 |
| ❌ | `public_apis_list` | 0.0% | 99.53% | 136.1 | 5075.4 | 1500ms | 9/1935 |
| ❌ | `ipapi_check` | 60.88% | 99.95% | 146.6 | 4507.0 | 2500ms | 1/1935 |
| ❌ | `nasa_apod` | 77.11% | 53.02% | 3084.3 | 11152.5 | 2000ms | 909/1935 |
| ⚠️ | `dog_ceo_random` | 96.07% | 97.0% | 518.4 | 10244.1 | 2500ms | 58/1935 |
| ⚠️ | `open_meteo_weather` | 98.97% | 97.88% | 687.3 | 14877.1 | 2000ms | 41/1935 |
| ✅ | `rest_countries` | 99.22% | 98.91% | 284.2 | 10221.5 | 2500ms | 21/1935 |
| ✅ | `useless_fact` | 99.74% | 99.64% | 650.7 | 10229.6 | 2500ms | 7/1935 |
| ✅ | `coingecko_bitcoin` | 99.79% | 99.95% | 96.4 | 4328.4 | 1500ms | 1/1935 |
| ✅ | `catfact_random` | 99.84% | 99.48% | 255.2 | 10080.2 | 3000ms | 10/1935 |
| ✅ | `agify_name` | 99.9% | 99.74% | 392.0 | 16112.2 | 2000ms | 5/1935 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.9% | 193.8 | 3882.8 | 2000ms | 2/1935 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `numbers_trivia` | 03:00 | 5004.5 | 50.0% |
| `nasa_apod` | 05:00 | 4561.4 | 63.04% |
| `nasa_apod` | 02:00 | 4524.3 | 66.67% |
| `numbers_trivia` | 10:00 | 4165.2 | 39.73% |
| `nasa_apod` | 03:00 | 4010.5 | 60.53% |
| `numbers_trivia` | 14:00 | 3905.2 | 37.93% |
| `nasa_apod` | 09:00 | 3794.5 | 53.75% |
| `nasa_apod` | 11:00 | 3735.5 | 51.43% |
| `nasa_apod` | 17:00 | 3658.9 | 48.48% |
| `numbers_trivia` | 02:00 | 3607.4 | 33.33% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
